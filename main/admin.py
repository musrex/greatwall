from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from main.auth import login_required
from main.auth import get_db

bp = Blueprint('admin',__name__)

@bp.