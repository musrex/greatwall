from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename

from main.auth import login_required
from main.auth import get_db

import csv
import os
import logging

logging.basicConfig(filename='logfile.log', level=logging.DEBUG)


bp = Blueprint('admin',__name__)

def import_CSV(db, file_path):
    logging.debug("import_CSV was called.")  # Debugging line
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            menu = row[0]
            code = row[1]
            dish = row[2]
            price = int(row[3])
            notes = row[4]
            spicy = bool(row[5])

            # Debugging lines
            logging.debug(f"Attempting to insert menu: {menu}, code: {code}, dish: {dish}, price: {price}, notes: {notes}, spicy: {spicy}")

            try:
                db.execute('INSERT INTO menu (category) VALUES (?)', (menu,))
                db.execute('INSERT INTO item (category, code, dish, price, notes, spicy, author_id) VALUES (?, ?, ?, ?, ?, ?, ?)', 
                           (menu, code, dish, price, notes, spicy, g.user['id']))
            except Exception as e:
                logging.error(f"Failed to insert data into database. Exception: {e}")

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
        error = validate_form_data(request.form)

        if error:
            flash(error)
        else:
            if request.form.get('save'):
                save_data(db, request.form, g.user['id'])
            elif request.form.get('items_to_delete'):
                delete_items(db, request.form.get('items_to_delete'))
            elif request.form.get('import_csv'):
                file = request.files['csv_file']
                if file.filename == '':
                    flash('No file selected')
                else:
                    file_path = os.path.join('uploads', file)
                    file.save(file_path)
                    import_CSV(db, file_path)
                    return redirect(url_for('index'))
                
            return redirect(url_for('index'))
        


    return render_template('menu/create.html', menus=menus, items=items)
