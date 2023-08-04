from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from main.auth import login_required
from main.auth import get_db

import csv
import os

bp = Blueprint('admin',__name__)

def import_CSV(db, file):
    with open(file, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            menu = row[0]
            code = row[1]
            dish = row[2]
            price = row[3]
            notes = row[4]
            spicy = row[5]
            db.execute()

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

def save_item(db, form, category, user_id):
    spicy = True if form.get('spicy') else False
    db.execute(
        'INSERT INTO item (category, code, dish, price, notes, special, spicy, author_id)'
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
            
            return redirect(url_for('index'))
        


    return render_template('menu/create.html', menus=menus, items=items)
