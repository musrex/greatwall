from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, current_app
)
from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename

from main.auth import login_required
from main.auth import get_db

import csv
import os

bp = Blueprint('admin',__name__)

def import_CSV(db, file_path):
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            menu = row[0]
            code = row[2]
            dish = row[3]
            price = row[4]
            notes = row[5]
            spicy = bool(row[6])
            try:
                if not db.execute('SELECT * FROM menu WHERE category = ?', (menu,)).fetchone():
                    special = True if request.form.get('special') else False
                    db.execute('INSERT INTO menu (category, special) VALUES (?,?)', (menu, special))
                    db.commit()
                db.execute('INSERT INTO item (category, code, dish, price, notes, spicy, author_id) VALUES (?, ?, ?, ?, ?, ?, ?)', 
                           (menu, code, dish, price, notes, spicy, g.user['id']))
            except:
                flash('Error, something went wrong.')

        db.commit()

def get_all_menus(db):
    return db.execute('SELECT * FROM menu ORDER BY category ASC').fetchall()

def get_all_items(db):
    return db.execute('SELECT * FROM item').fetchall()

def validate_form_data(form):
    fields = ['category', 'code', 'dish', 'price']
    errors = {field: f'{field.capitalize()} is required.' for field in fields if not form.get(field)}
    return ', '.join(errors.values()) if errors else None

def save_data(db, form, user_id):
    category = form.get('category') or form.get('existing_category')
    save_menu_category(db, category)
    save_item(db, form, category, user_id)

def save_menu_category(db, form, category):
    if not db.execute('SELECT * FROM menu WHERE category = ?', (category,)).fetchone():
        special = True if form.get('special') else False
        db.execute('INSERT INTO menu (category, special) VALUES (?,?)', (category, special))
        db.commit()

def save_item(db, form, category, user_id):
    spicy = True if form.get('spicy') else False
    db.execute(
        'INSERT INTO item (category, code, dish, price, notes, spicy, author_id)'
        ' VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
        (category, form.get('code'), form.get('dish'), form.get('price'), form.get('notes'), spicy, form.get('spicy'), user_id)
    )
    db.commit()

def delete_items(db, items_to_delete):
    for item_id in items_to_delete:
        db.execute('DELETE FROM item WHERE id = ?', (item_id),)
    db.commit()

@bp.route('/')
def index():
    db = get_db()
    menus = get_all_menus(db)
    items = get_all_items(db)
    return render_template('index.html', items=items, menus=menus)


@bp.route('/create', methods=('GET','POST'))
@login_required
def create():
    db = get_db()
    # this is to populate the 'categories' drop down menu
    menus = get_all_menus(db)
    items = get_all_items(db)

    if request.method == 'POST':

        if request.form.get('create_item'):    
            error = validate_form_data(request.form)
            if error:
                flash(error)
            else:
                save_data(db, request.form, g.user['id'])
        
        elif request.form.get('delete_items'):
            delete_items(db, request.form.get('items_to_delete'))
        
        elif request.form.get('import_csv'):
            file_object = request.files['file']
            if file_object.filename == '':
                flash('No file selected')
            else:
                file_name = secure_filename(file_object.filename)
                file_path = os.path.join(current_app.config['UPLOAD_PATH'], file_name)
                file_object.save(file_path)
                import_CSV(db, file_path)
                return redirect(url_for('index'))
            
        return redirect(url_for('index'))
        


    return render_template('menu/create.html', menus=menus, items=items)
