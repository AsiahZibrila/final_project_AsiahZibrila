#from crypt import methods
from lib2to3.pgen2 import driver
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

bp = Blueprint("trips", __name__)


@bp.route("/trips", methods=['GET', 'POST'])
def index():
    """Show all trips"""
    conn = get_db()
    cur = conn.cursor()
    cur.execute('''
                SELECT trip.id, trip.origin, trip.destination, trip.departure_date, trip.comment
                FROM trip ORDER BY trip.departure_date;
    ''')
    trips = cur.fetchall()

    #for trip in trips:
    #    id_num = trucks[0]

    return render_template("trips/triplist.html", 
                            trips=trips,
                            #id_num=id_num
                            )

def get_drivers():
    """Get all drivers.
    """
    conn = get_db()
    cur = conn.cursor()
    cur.execute('''
        SELECT person.username 
        FROM person;
        ''')
    drivers = cur.fetchall()

    if drivers is None:
        abort(404, f"There is no driver.")

    return drivers


def get_driver_id(uname):
    """Get a driver's id.
    """
    conn = get_db()
    cur = conn.cursor()
    cur.execute('''
        SELECT person.id 
        FROM person WHERE person.username=%s
        ''', (uname,),
        )
    driver_id = cur.fetchone()

    if driver_id is None:
        abort(404, f"This driver doesn't exist.")

    return driver_id


def get_driver_uname(driver_id):
    """Get a driver's username.
    """
    conn = get_db()
    cur = conn.cursor()
    cur.execute('''
        SELECT person.username 
        FROM person WHERE person.id=%s
        ''', (driver_id,),
        )
    driver_uname = cur.fetchone()

    if driver_uname is None:
        abort(404, f"This driver doesn't exist.")

    return driver_uname

def get_trucks():
    """Get all trucks.
    """
    conn = get_db()
    cur = conn.cursor()
    cur.execute('''
                SELECT truck.id_num
                FROM truck;
    ''')
    trucks = cur.fetchall()

    if trucks is None:
        abort(404, f"There is no truck.")

    return trucks

def get_truck_id(truck_num):
    """Get a truck's id.
    """
    conn = get_db()
    cur = conn.cursor()
    cur.execute('''
        SELECT truck.id 
        FROM truck WHERE truck.id_num=%s
        ''', (truck_num,),
        )
    truck_id = cur.fetchone()

    if truck_id is None:
        abort(404, f"This truck doesn't exist.")

    return truck_id

# Edit
def get_truck_num(truck_id):
    """Get a truck's num.
    """
    conn = get_db()
    cur = conn.cursor()
    cur.execute('''
        SELECT truck.id_num 
        FROM truck WHERE truck.id=%s
        ''', (truck_id,),
        )
    id_num = cur.fetchone()

    if id_num is None:
        abort(404, f"This truck doesn't exist.")

    return id_num

@bp.route("/newtrip", methods=['GET', 'POST'])
def addtrip():
    """Adds a new trip and assigns to driver and truck"""
    drivers = get_drivers()
    trucks = get_trucks()
    conn = get_db()
    cur = conn.cursor()
    if request.method == 'POST':
        origin = request.form['origin']
        dest = request.form['dest']
        #depdate = str(request.form['depdate'])
        depdate = str(request.form.get('depdate'))
        comment = request.form['comment']
        driver = request.form['driver']
        truck = request.form['truck']
        driver_id = get_driver_id(driver)
        truck_id = get_truck_id(truck)
        error = None
        if not origin:
            error = "Enter origin"
        if not dest:
            error = "Enter destination"
        if not depdate:
            error = "Select depature date"
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
                    INSERT INTO trip (origin, destination, departure_date, comment, person_id, truck_id) VALUES (%s, %s, %s, %s, %s, %s)''',
                    (origin, dest, depdate, comment, driver_id, truck_id),
                    )
            conn.commit()
            cur.close()
            return redirect(url_for('trips.index'))
    return render_template("trips/addtrip.html", drivers=drivers, trucks=trucks)


@bp.route("/<id>/trip-details", methods=['GET', 'POST'])
#@login_required
def trip_detail(id):
    """Get details of specific trip.
    """
    error = None
    conn = get_db()
    cur = conn.cursor()
    cur.execute('''
        SELECT trip.id, trip.origin, trip.destination, trip.departure_date, 
        trip.person_id, trip.truck_id, trip.comment, trip.route
        FROM trip WHERE trip.id=%s
        ''', (id,),
        )
    trip = cur.fetchone()
    if trip is None:
        error = "This trip doesn't exist."
    if error is not None:
        flash(error)
    driver_id = trip[4]
    driver_uname = get_driver_uname(driver_id)
    truck_id = trip[5]
    truck_num = get_truck_num(truck_id)

    return render_template("trips/detail.html",
                            trip=trip,
                            driver_uname=driver_uname, 
                            truck_num=truck_num
                            )


@bp.route('/trip/route/<start>/<end>')
def trip_route(start, end):
    start=start
    end=end
    return render_template("trips/triproute.html", start=start, end=end) 
