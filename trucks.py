
from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort
from auth import login_required
from dbvars import get_db
from app import db

bp = Blueprint("trucks", __name__)


@bp.route("/trucks", methods=['GET', 'POST'])
def index():
    """Show all trucks"""
    conn = get_db()
    cur = conn.cursor()
    cur.execute('''
                SELECT truck.id_num
                FROM truck ORDER BY truck.id_num ASC;
    ''')
    trucks = cur.fetchall()

    for truck in trucks:
        id_num = trucks[0]

    return render_template("trucks/trucklist.html", 
                            trucks=trucks,
                            #id_num=id_num
                            )

@bp.route("/newtruck", methods=['GET', 'POST'])
def addtruck():
    """Adds a new truck ID"""
    conn = get_db()
    cur = conn.cursor()
    if request.method == 'POST':
        truck_id = request.form['comments']
        error = None
        if not truck_id:
            error = "Enter truck ID"
        if g.person is None:
            return redirect(url_for('auth.login'))
        #if g.person[0] in reviewed_users:
        #   error = """You have already submitted a review for this book. 
        #                Multiple Reviews for the same book are not permitted"""
        if error is not None:
            flash(error)
        else:
            conn = get_db()
            cur = conn.cursor()
            cur.execute('''
                    INSERT INTO truck (id_num) VALUES (%s)''',
                    (truck_id,)
                    )
            conn.commit()
            cur.close()
            return redirect(url_for('trucks.index'))
    return render_template("trucks/addtruck.html",)