'''
use the following to remove the _pycache folders in the project folder
pip3 install pyclean
pyclean .
'''
import pathlib

from booking import Booking
from cinema import Cinema
from customer import Customer
from guizero import (App, Box, Combo, ListBox, Picture, PushButton, Text,
                     TextBox, TitleBox, Window)
from movie import Movie

# https://lawsie.github.io/guizero/

"""
Cinema management system

    Known limitations:
    - Test coverage is limited. 
    - Error handling could be better. 
    - Main program logic is messy. 
    - Booking administration is broken
    - Customer administration could handled better
    - Code commentary is sparse
    - Not all class functionality is exposed in the GUI.

    - Cinema data is NOT persistent - changes are not recorded to storage

    colors: https://wiki.tcl-lang.org/page/Color+Names%2C+running%2C+all+screens

    Changelog:
        28NOV2022 - Initial release

"""

############# public declarations ##############
pwd = pathlib.Path().absolute()  # current working folder


cinema = Cinema()
app = App(title="Cinema Administration",
          width=800, height=600, bg="palegreen4")
app.text_color = "black"
main_box = Box(app, height="fill", width="fill", align="left", border=False)
heading_box = Box(main_box, width="fill", align="top", border=False)
# source: https://www.pexels.com/photo/clapper-board-in-green-surface-5662857/
Picture(heading_box, image=f"{pwd}/images/logo.png", align="left")
heading_text = Text(heading_box, size=32, text="Cinema Movie Manager")


RATINGS = Movie.get_ratings()
GENRES = Movie.get_genres()


def evtNull(value=None):
    # null event placeholder
    pass


def refreshLists():
    movieList.clear()
    movie_select.clear()
    custList.clear()
    bookList.clear()
    for m in cinema.getMovieNames():
        movieList.append(m)
        movie_select.append(m)
        bookList.append(m)

    for c in cinema.customers():
        custList.append(c)


############# Customer maintenance  ##############

## -----local events for customer maintenance ------------ ##

_customername = ""


def evtCustHide():
    frmCustomer.hide()


def displayCustomer(value):
    global _customername
    b = cinema.findCustomer(value)
    if b != None:
        edName.value = b.customer.name
        edContact.value = b.customer.contact
        edEmail.value = b.customer.email
        _customername = value


def evtDeleteCustomer():
    global _customername
    c = cinema.findCustomer(_customername)
    if c != None:
        cinema.removeBooking(c.bookingid)
        edName.value = ""
        edContact.value = ""
        edEmail.value = ""
        _customername = ""
        refreshLists()


def evtUpdateCustomer():
    global _customername
    b = cinema.findCustomer(_customername)
    if b != None:
        c = Customer(edName.value, edContact.value, edEmail.value)
        b.customer = c
        edName.value = ""
        edContact.value = ""
        edEmail.value = ""
        _customername = ""
        refreshLists()


def evtAddCustomer():
    global _customername
    c = cinema.findCustomer(_customername)
    if c == None:  # make sure it does not exist
        c = Customer(edName.value, edContact.value, edEmail.value)
        m = Movie()
        b = Booking()
        b.populate(c, 1, m)
        edName.value = ""
        edContact.value = ""
        edEmail.value = ""
        _customername = ""
        refreshLists()


## ----- Customer form/window ------------ ##
frmCustomer = Window(app, title="Customer Maintenance", width=400,
                     height=400, layout="auto", bg="palegreen4")
frmCustomer.hide()
Text(frmCustomer, size=24, text="Customer Manager")

custbox = Box(frmCustomer, width="fill", align="top",
              border=True, layout="auto")
_customers = []
custList = ListBox(custbox, items=_customers, height='fill', width='fill',
                   multiselect=False, command=displayCustomer, scrollbar=True)
custList.bg = "cornsilk2"
custbox = Box(frmCustomer, width="fill", align="top",
              border=True, layout="grid")
Text(custbox, text="Name:", grid=[0, 0])
Text(custbox, text="Contact:", grid=[0, 1])
Text(custbox, text="Email:", grid=[0, 2])

edName = TextBox(custbox, text="", width=25, align="left", grid=[1, 0])
edContact = TextBox(custbox, text="", width=25, align="left",  grid=[1, 1])
Text(custbox, text="(this impacts bookings)",
     align="right", size=12, grid=[1, 1])
edEmail = TextBox(custbox, text="", width=50, align="left",  grid=[1, 2])
edName.bg = "cornsilk2"
edContact.bg = "cornsilk2"
edEmail.bg = "cornsilk2"

btnbox = Box(frmCustomer, width="fill", align="top",
             border=True, layout="auto")
btn = PushButton(btnbox, text="New", command=evtAddCustomer,
                 align="left")
btn.bg = "palegreen3"
btn = PushButton(btnbox, text="Update",
                 command=evtUpdateCustomer, align="left")
btn.bg = "palegreen3"
btn = PushButton(btnbox, text="Delete",
                 command=evtDeleteCustomer, align="left")
btn.bg = "palegreen3"
btn = PushButton(btnbox, text="Cancel",
                 command=evtCustHide, align="left")
btn.bg = "palegreen3"

############# Movie maintenance  ##############

## -----local events for movie maintenance ------------ ##

_moviename = ""


def evtMovieHide():
    frmMovies.hide()


def evtSetRate(rating):
    edRating.value = rating


def displayMovies(value):
    global _moviename
    m = cinema.findMovieItem(value)
    if m != None:
        edMoviName.value = m.name
        edDuration.value = m.minutes
        edRating.value = m.rating
        edGenre.value = m.genre
        _moviename = value


def evtDeleteMovie():
    global _moviename
    m = cinema.findMovieItem(_moviename)
    if m != None:
        cinema.remove(_moviename)
        edMoviName.value = ""
        edDuration.value = ""
        edRating.value = ""
        edGenre.value = "not set"
        refreshLists()


def evtUpdateMovie():
    global _moviename
    m = cinema.findMovieItem(_moviename)
    if m != None:
        cinema.remove(_moviename)
        m = Movie()
        m.name = edMoviName.value
        m.minutes = edDuration.value
        m.rating = edRating.value
        m.genre = edGenre.value
        edMoviName.value = ""
        edDuration.value = ""
        edRating.value = ""
        edGenre.value = "not set"
        cinema.add(m)
        _moviename = ""
        refreshLists()


def evtAddMovie():
    global _moviename
    m = cinema.findMovieItem(_moviename)
    if m == None:  # make sure it does nto exist
        m = Movie()
        m.name = edMoviName.value
        m.minutes = edDuration.value
        m.rating = edRating.value
        m.genre = edGenre.value
        edMoviName.value = ""
        edDuration.value = ""
        edRating.value = ""
        edGenre.value = "not set"
        cinema.add(m)
        _moviename = ""


## ----- Movie form/window ------------ ##
frmMovies = Window(app, title="Movie Maintenance", width=450,
                   height=400, layout="auto", bg="palegreen4")
frmMovies.hide()
Text(frmMovies, size=24, text="Movie Manager")

movbox0 = Box(frmMovies, width="fill", align="top",
              border=True, layout="auto")
_movies = []
movieList = ListBox(movbox0, items=_movies, height='fill', width='fill',
                    multiselect=False, command=displayMovies, scrollbar=True)
movieList.bg = "cornsilk2"
movbox1 = Box(frmMovies, width="fill", align="top",
              border=True, layout="grid")
Text(movbox1, text="Name:", grid=[0, 0])
Text(movbox1, text="Duration:", grid=[0, 1])
Text(movbox1, text="Rating:", grid=[0, 2])
Text(movbox1, text="Genre:", grid=[0, 3])


edMoviName = TextBox(movbox1, text="", width=25, align="left", grid=[1, 0])
edDuration = TextBox(movbox1, text="", width=25, align="left",  grid=[1, 1])
edRating = TextBox(movbox1, text="", width=5, align="left",  grid=[1, 2])
edGenre = Combo(movbox1, options=Movie.genre_list(), align="left", grid=[1, 3])

edMoviName.bg = "cornsilk2"
edDuration.bg = "cornsilk2"
edRating.bg = "cornsilk2"
edGenre.bg = "palegreen3"

btnbox0 = Box(frmMovies, width="fill", align="top",
              border=True, layout="grid")
BtnRatings = {}
col = 0
for rating in RATINGS:
    # want to make sure we dont use an unset rating
    if rating == "not set":
        continue
    image_location = f"{pwd}/images/{rating.lower()}.png"
    BtnRatings[rating] = PushButton(btnbox0, image=image_location, grid=[col, 0],
                                    command=evtSetRate, args={rating}, padx=5, pady=5)
    col = col + 1

btnbox1 = Box(frmMovies, width="fill", align="top",
              border=True, layout="auto")
btn = PushButton(btnbox1, text="New", command=evtAddMovie,
                 align="left")
btn.bg = "palegreen3"
btn = PushButton(btnbox1, text="Update",
                 command=evtUpdateMovie,  align="left")
btn.bg = "palegreen3"
btn = PushButton(btnbox1, text="Delete",
                 command=evtDeleteMovie,  align="left")
btn.bg = "palegreen3"
btn = PushButton(btnbox1, text="Cancel",
                 command=evtMovieHide, align="left")
btn.bg = "palegreen3"

############# Booking maintenance  ##############

## -----local events for booking maintenance ------------ ##


def evtBookHide():
    frmBooking.hide()


def displayBooking(value):
    b = cinema.findCustomer(value)
    if b != None:
        cbCustomer.value = ""
        cbSession.value = ""
        cbMovies.value = ""


## ----- Booking form/window ------------ ##
frmBooking = Window(app, title="Booking Maintenance", width=400,
                    height=400, layout="auto", bg="palegreen4")
frmBooking.hide()
Text(frmBooking, size=24, text="Customer Manager")

bookbox = Box(frmBooking, width="fill", align="top",
              border=True, layout="auto")
_customers = []
bookList = ListBox(bookbox, items=_customers, height='fill', width='fill',
                   multiselect=False, command=displayBooking, scrollbar=True)
bookList.bg = "cornsilk2"
bookbox = Box(frmBooking, width="fill", align="top",
              border=True, layout="grid")
Text(bookbox, text="Customer:", grid=[0, 0])
Text(bookbox, text="Session:", grid=[0, 1])
Text(bookbox, text="Movies:", grid=[0, 2])
sess = range(1, 7)
cbCustomer = Combo(bookbox, options=cinema.getMovieNames(),
                   align="left", grid=[1, 0])
cbSession = Combo(bookbox, options=sess, align="left", grid=[1, 1])
cbMovies = Combo(bookbox, options=cinema.getMovieNames(),
                 align="left", grid=[1, 2])
cbCustomer.bg = "palegreen3"
cbSession.bg = "palegreen3"
cbMovies.bg = "palegreen3"

btnbox = Box(frmBooking, width="fill", align="top",
             border=True, layout="auto")
btn = PushButton(btnbox, text="New", command=evtNull,
                 align="left")
btn.bg = "palegreen3"
btn = PushButton(btnbox, text="Update",
                 command=evtNull, align="left")
btn.bg = "palegreen3"
btn = PushButton(btnbox, text="Delete",
                 command=evtNull, align="left")
btn.bg = "palegreen3"
btn = PushButton(btnbox, text="Cancel",
                 command=evtBookHide, align="left")
btn.bg = "palegreen3"

############# Main application window ##############
## -----local events for main window ------------ ##


def evtUpdateDetails(value):
    edTheMovie.value = value
    totc = int(len(cinema.bookings()))
    edTotBooking.value = f"Total Bookings: {totc}"
    sess = cinema.bySessions(value)
    c = len(sess)
    edSession.value = f"Sessions: {c}"
    edBooking.clear()
    book = f"Session:Bookings\n"
    for d in sess:
        c = len(sess[d])
        book += f"{d}: {c}\n"
    edBooking.value = book


def evtFilterRating(rating=None):
    movie_select.clear()
    movie_names = cinema.findRatedMoviesNames(
        rating) if rating else cinema.getMovieNames()
    for m in movie_names:
        movie_select.append(m)


movie_names = []
movies_box = Box(main_box, width="fill", border=3, layout="grid")
Text(movies_box, size=24, text="Movies", grid=[0, 0])
Text(movies_box, size=24, text="Session Details", align="left", grid=[1, 0])
edTheMovie = Text(movies_box, size=16, text="-", align="left", grid=[1, 1])
edTheMovie.text_color = "gold"
edTotBooking = Text(movies_box, size=16, text="Total Bookings: 0",
                    align="left", grid=[1, 2])
edSession = Text(movies_box, size=16, text="Sessions: 0",
                 align="left", grid=[1, 3])
edBooking = Text(movies_box, size=16, text="Bookings: ",
                 align="left", grid=[1, 4])
movie_select = ListBox(movies_box, items=movie_names, width=300, height=300,
                       multiselect=False, command=evtUpdateDetails, scrollbar=True, grid=[0, 1, 1, 4])
movie_select.bg = "cornsilk2"

filter_box = TitleBox(main_box, text="Filter Movies",
                      layout="grid", width="fill", border=3)
col = 0
for rating in RATINGS:
    # if rating == "not set":
    #    continue
    image_location = f"{pwd}/images/{rating.lower()}.png"
    PushButton(filter_box, image=image_location, grid=[col, 0],
               command=evtFilterRating, args={rating}, padx=5, pady=5)
    col = col + 1
bratings = PushButton(filter_box, text='All Ratings', grid=[col, 0],
                      command=evtFilterRating, args={None}, padx=5, pady=5)
bratings.bg = "palegreen3"


############# Event handlers##############
def evtExit():
    """ Confirm quit on exit or close button  """
    # if app.yesno("Close", "Are you sure you want to exit?"):
    exit()


def evtBooking():
    bookList.clear()
    for c in cinema.getMovieNames():
        bookList.append(c)
    frmBooking.show(wait=True)


def evtCustomers():
    custList.clear()
    for c in cinema.customers():
        custList.append(c)
    frmCustomer.show(wait=True)


def evtMovies():
    movieList.clear()
    for m in cinema.getMovieNames():
        movieList.append(m)
    frmMovies.show(wait=True)


def evtLoadDemoData():
    TEST_DATA = [
        ["The Shawshank Redemption", 142, "RP16", "Drama"],
        ["The Godfather", 175, "R16", "Action"],
        ["The Dark Knight", 152, "M", "Sci-Fi"],
        ["12 Angry Men", 96, "G", "Action"],
        ["Schindler's List", 195, "RP13", "not set"],
        ["The Lord of the Rings: The Return of the King", 201, "M", "not set"],
        ["One Flew Over the Cuckoo's Nest", 133, "R18", "not set"],
        ["The Lord of the Rings: The Fellowship of the Ring", 178, "PG", "not set"],
        ["Saving Private Ryan", 169, "R15", "not set"],
        ["Blade Runner 2049", 164, "R13", "not set"],
        ["Halloween", 91, "R16", "not set"],
        ["Beverly Hills Cop", 105, "RP16", "not set"],
        ["Platoon", 120, "RP16", "not set"],
        ["Total Recall", 113, "RP16", "not set"],
        ["Back to the Future", 116, "G", "not set"],
        ["The Lion King", 88, "G", "not set"],
        ["Cars", 117, "G", "not set"],
        ["The Wizard of Oz", 102, "G", "not set"],
        ["The Wolf of Wall Street", 180, "R18", "not set"],
        ["Harry Potter and the Philosopher's Stone", 152, "PG", "not set"],
        ["Poltergeist", 114, "not set", "not set"],
        ["Full Metal Jacket", 116, "RP13", "not set"],
        ["The Exorcist", 122, "R15", "not set"],
        ["Apocalypse Now", 147, "R16", "not set"],
    ]
    for mv in TEST_DATA:
        m = Movie()
        m.populate(*mv)
        cinema.add(m)
    movieList.clear()
    movie_select.clear()
    for m in cinema.getMovieNames():
        movieList.append(m)
        movie_select.append(m)

    m = cinema.findMovieItem("The Shawshank Redemption")
    c = Customer("Joe Bloggs", "021-123-1234", "joe.bloggs@mail.com")
    cinema.addBooking(m, 1, c)

    m = cinema.findMovieItem("The Exorcist")
    c = Customer("Jane Doe", "021-456-4567", "jane.doe@mail.com")
    cinema.addBooking(c, 2, m)

    m = cinema.findMovieItem("Cars")
    c = Customer("King Kong", "021-123-4567", "king.kong@mail.com")
    cinema.addBooking(c, 1, m)

    m = cinema.findMovieItem("Cars")
    c = Customer("King Kong", "021-123-4567", "king.kong@mail.com")
    cinema.addBooking(c, 2, m)

    m = cinema.findMovieItem("Cars")
    c = Customer("ABC", "022-123-1234", "ABC@mail.com")
    cinema.addBooking(c, 1, m)

    m = cinema.findMovieItem("Cars")
    c = Customer("DEF", "022-456-4567", "DEF@mail.com")
    cinema.addBooking(c, 2, m)

    m = cinema.findMovieItem("Cars")
    c = Customer("HIJ", "024-123-4567", "HIJ@mail.com")
    cinema.addBooking(c, 2, m)


app.when_closed = evtExit  # confirm exit on X button

btn_box = TitleBox(main_box, text="Other", width="fill",
                   border=3, layout="grid")
btn = PushButton(btn_box, text="Customer Admin",
                 grid=[0, 0], command=evtCustomers)
btn.bg = "palegreen3"
btn = PushButton(btn_box, text="Movie Admin",
                 grid=[1, 0], command=evtMovies)
btn.bg = "palegreen3"
btn = PushButton(btn_box, text="Booking Admin",
                 grid=[2, 0], command=evtBooking)
btn.bg = "palegreen3"
btn = PushButton(btn_box, text="Reload Demo Data",
                 grid=[4, 0], command=evtLoadDemoData)
btn.bg = "palegreen3"
btn = PushButton(btn_box, text="Quit", grid=[5, 0], command=evtExit)
btn.bg = "palegreen3"

evtLoadDemoData()

app.display()
