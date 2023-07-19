from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from main.auth import login_required
from main.auth import get_db


bp = Blueprint('admin',__name__)

@bp.route('/')
def index():
    db = get_db()
    menus = db.execute('SELECT category FROM menu ORDER BY category ASC').fetchall()
    items = db.execute(
        'SELECT i.id, category, code, dish, price, author_id'
        ' FROM item i JOIN user u ON i.author_id = u.id'
        ' ORDER BY code ASC'
    ).fetchall()
    return render_template('index.html', items=items, menus=menus)

@bp.route('/create', methods=('GET','POST'))
@login_required
def create():
    db = get_db()
    # this is to populate the 'categories' drop down menu
    menus = db.execute(
        'SELECT * FROM menu ORDER BY category ASC'
    ).fetchall()
    items = db.execute(
        'SELECT * FROM item'
    ).fetchall()
      
    if request.method == 'POST':
        if request.form.get('create'):

            category  = (request.form['category']) or (request.form['existing_category'])
            code = request.form['code']
            dish = request.form['dish']
            price = request.form['price']
            error = None

            if not category:
                error = 'Category is required.'
            if not code:
                error = 'Code is required.'
            if not dish:
                error = 'Name is required.'
            if not price:
                error = 'Price is required.'

            if error is not None:
                flash(error)
            else:
                # this is to check if the 'category' input is already in the
                # db, if not we add it
                query = db.execute(
                    'SELECT * FROM menu WHERE category = ?', (category,)
                ).fetchone()
                if query is None:
                    db.execute(
                    'INSERT INTO menu (category) VALUES (?)',
                    (category,),
                ) 

                # this is to record the values for the new entry
                db.execute(
                    'INSERT INTO item (category, code, dish, price, author_id)'
                    ' VALUES (?, ?, ?, ?, ?)',
                    (category, code, dish, price, g.user['id']),
                )
                db.commit()
                return redirect(url_for('index'))
            
        if request.form.getlist('items_to_delete'):
            
            items_to_delete = request.form.getlist('items_to_delete')
            
            for item_id in items_to_delete:
                db.execute(
                    'DELETE FROM item WHERE id = ?', (item_id,)
                )
            db.commit()
            
            return redirect(url_for('index'))
        


    return render_template('menu/create.html', menus=menus, items=items)
