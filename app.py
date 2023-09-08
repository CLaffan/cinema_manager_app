"""
    Online Booking sub-system

    Handles customers booking for a particular movie over the Internet

    Changelog:
        28NOV2022 - Initial release

    This requires the Flask module
    pip install flask
"""

import os
import sqlite3
from sqlite3 import Error
from flask import (Flask, redirect,render_template, request)
from flask.helpers import flash, url_for
import cinemadb
             
app = Flask(__name__)
app.config["SECRET_KEY"] = "secret key"

@app.route("/")
def main():
    """ 
    Route for home/index.html
    :param:
    :return:
    """
    return render_template("index.html")

@app.route('/book', methods=["GET", "POST"])
def create_booking():
    """ 
    Route for making a booking /book
    :param:
    :return:
    """
    conn = sqlite3.connect("cinema.db")
    cur = conn.cursor()        
    cur.execute("SELECT id,name FROM customers;")
    customers = cur.fetchall()    
    cur.execute("SELECT id,name FROM movies;")    
    movies = cur.fetchall()

    if request.method.upper() == "POST":
        customer = request.form.get("customer")
        movie = request.form.get("movie")
        session = request.form.get("session")

        if session== None or customer == None or movie == None or session.strip() == "" or customer.strip() == "" or movie.strip() == "":
            flash("Please fill in all of the fields")
            return render_template("book.html", movies=movies, customers=customers)

        SQL = "INSERT INTO bookings (customerID,session,movieID) VALUES(?,?,?)"
        cur.execute(SQL, (customer, session,movie))            
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for("display_bookings")) 

    cur.close()
    conn.close()
    return render_template("book.html", movies=movies, customers=customers)

@app.route("/bookings/<int:booking_id>/edit", methods=["POST", "GET"])
def edit_booking(booking_id):
    """ 
    Route for editing a single booking /booking/#/edit
    :param:
    :return:
    """

    conn = sqlite3.connect("cinema.db")
    cur = conn.cursor()        
    cur.execute("SELECT id,name FROM customers;")
    customers = cur.fetchall()    
    cur.execute("SELECT id,name FROM movies;")    
    movies = cur.fetchall()
    booking = cur.execute("SELECT id,session,customerID,movieID FROM bookings WHERE id = ?",(str(booking_id))).fetchone()

    if request.method.upper() == "POST":
        customer = request.form.get("customer")
        movie = request.form.get("movie")
        session = request.form.get("session")

        if session== None or customer == None or movie == None or session.strip() == ""  or customer.strip() == "" or movie.strip() == "":
            flash("Please fill in all of the fields")
            return render_template("edit.html", booking=booking, movies=movies, customers=customers)

        SQL = "UPDATE bookings SET customerID = ?, movieID = ?, session = ? WHERE id = ?"
        cur.execute(SQL, (customer, movie, session, booking_id))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for("display_bookings"))
    cur.close()
    conn.close()
    return render_template("edit.html", booking=booking, movies=movies, customers=customers)


@app.route("/bookings/<int:booking_id>/delete")
def delete_booking(booking_id):
    """ 
    Route for removing a single booking /booking/#/delete
    :param:
    :return:
    """

    conn = sqlite3.connect("cinema.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM bookings WHERE bookings.id = ?", (str(booking_id)))
    conn.commit()
    cur.close()
    conn.close()

    return redirect(url_for("display_bookings"))


@app.route("/bookings/<int:booking_id>")
def display_booking(booking_id):
    """ 
    Route for showing the details of a single booking /booking/#
    :param:
    :return:
    """

    conn = sqlite3.connect("cinema.db")
    cur = conn.cursor()
    SQL = """
        SELECT bookings.id, session, customers.name, movies.name
        FROM bookings,movies,customers 
        WHERE bookings.customerID = customers.id AND bookings.movieID = movies.id
              AND bookings.id=?;
    """
    booking = cur.execute(SQL,(str(booking_id))).fetchone()

    return render_template("booking.html", booking=booking, booking_id=booking_id)


@app.route("/bookings")
def display_bookings():
    """ 
    Route for listing all of the bookings /bookings
    :param:
    :return:
    """
 
    conn = sqlite3.connect("cinema.db")
    cur = conn.cursor()
    SQL = """
        SELECT bookings.id, session, customers.name, movies.name
        FROM bookings,movies,customers 
        WHERE bookings.customerID = customers.id AND bookings.movieID = movies.id;
    """
    cur.execute(SQL)
    bookings = cur.fetchall()
    cur.close()
    conn.close()

    return render_template("bookings.html", bookings=bookings)

# driver code for the flask application
if __name__ == "__main__":
    conn = None
    db = os.getcwd()+"\cinema.db"
    if "cinema.db" not in os.listdir():    
        conn = cinemadb.dbconnect(db)
        if conn:
            cinemadb.prepareDB(conn)
            cinemadb.importData(conn)
    if conn:
        conn.close()
    app.run(debug=True)