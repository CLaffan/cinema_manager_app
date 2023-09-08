from booking import Booking
from customer import Customer
from movie import Movie

"""

    Movies are stored in a private dict _movies, keyed by name
    Bookings are stored in a private dict _bookings, keyed by customer contact
    
    Changelog:
        28NOV2022 - Initial release

"""


def group_by(seqs, idx=0, merge=True):
    d = dict()
    for seq in seqs:
        k = seq[idx]
        v = d.get(k, tuple()) + (seq[:idx]+seq[idx+1:]
                                 if merge else (seq[:idx]+seq[idx+1:],))
        d.update({k: v})
    return d


class Cinema:

    # Public Methods
    def __init__(self):
        self._movies = {}
        self._bookings = {}

# movie methods
    def movies(self):
        return list(self._movies.values())

    def add(self, movie):
        if not movie:
            raise ValueError
        if not isinstance(movie, Movie):
            raise TypeError

        self._movies[movie.name] = movie
        return self

    def getMovieNames(self):
        return sorted(list(self._movies.keys()))

    def remove(self, name):
        if not name or not self._movies[name]:
            raise ValueError
        del self._movies[name]
        return self

    def findMovieItem(self, name):
        if not name or not self._movies[name]:
            raise ValueError
        return self._movies[name]

    def findRatedMoviesNames(self, rating):
        if not rating or not Movie.valid_rating(rating):
            raise ValueError
        return sorted(map(lambda m: m.name, filter(lambda m: m.rating == rating, self.movies())))

    def getTotalMinutes(self):
        return reduce((lambda x, y: x + y), map(lambda m: m.minutes, self.movies()))

# cinema customer methods
    def customers(self):
        bookings = list(self._bookings.values())
        return [b.customer.name for b in bookings]

    def findCustomer(self, name):
        if not name:
            raise ValueError
        for b in list(self._bookings.values()):
            if b.customer.name == name:
                return b
        return None

# cinema booking methods
    def bookings(self):
        return list(self._bookings.values())

    def bySessions(self, movie):
        lst = [(b.session,  b.bookingid)
               for b in list(self._bookings.values()) if movie == b.movie.name]
        gb = group_by(lst)
        res = {key: val for key, val in sorted(
            gb.items(), key=lambda ele: ele[0])}
        return res

    def addBooking(self, customer, session, movie):
        if not customer:
            raise ValueError
        if not session:
            raise ValueError
        if not movie:
            raise ValueError

        if not isinstance(customer, Customer):
            raise TypeError
        if not isinstance(movie, Movie):
            raise TypeError
        if not isinstance(session, int):
            raise TypeError

        b = Booking()
        b.populate(customer, session, movie)
        self._bookings[b.bookingid] = b
        return self

    def updBooking(self, booking, session, movie):
        if not booking:
            raise ValueError
        b = self.findBooking(booking)
        if not session:
            session = b.session
        if not movie or not isinstance(movie, Movie):
            movie = b.movie
        del self._bookings[booking]
        self.addBooking(b.customer, session, movie)
        return booking

    def removeBooking(self, booking):
        if not booking:
            raise ValueError
        b = self.findBooking(booking)
        del self._bookings[booking]

    def getBookings(self, session=0):
        if session > 0:
            return sorted(map(lambda b: b.bookingid, filter(lambda b: b.session == session, self.bookings())))
        else:
            return sorted(list(self._bookings.keys()))

    def showBookings(self):
        s = ""
        for b in list(self._bookings.values()):
            name = b.customer_name()
            movie = b.movie_name()
            session = b.session
            s += "\n".join([f"Customer: {name}",
                            f"Movie: {movie}",
                            f"Session: {session}\n", ])
        return s

    def findBooking(self, booking):
        if not booking or not self._bookings[booking]:
            raise ValueError
        return self._bookings[booking]

    def show(self):
        s = ""
        for m in list(self._movies.values()):
            s += "\n".join([f"Movie: {m.name}",
                            f"Run Time: {m.minutes}mins",
                            f"Audience Rating: {m.rating}",
                            f"Genre: {m.genre}\n", ])
        return s

    def __str__(self):
        return self.show()


# End of class, tests below
if __name__ == "__main__":
    import pprint

    pp = pprint.PrettyPrinter(indent=4)
    print("Start Tests")
    print("--- Testing Movies ---")
    TEST_DATA = [
        ["The Shawshank Redemption", 142, "RP16", "Drama"],
        ["The Godfather", 175, "R16", "Action"],
        ["The Dark Knight", 152, "M", "Sci-Fi"],
        ["12 Angry Men", 96, "G", "not set"],
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
        ["Poltergeist", 114, "PG", "not set"],
        ["Full Metal Jacket", 116, "RP13", "not set"],
        ["The Exorcist", 122, "R15", "not set"],
        ["Apocalypse Now", 147, "R16", "not set"],
    ]

    cinema = Cinema()
# movie testing
    for mv in TEST_DATA:
        m = Movie()
        m.populate(*mv)
        print(m.show())
        cinema.add(m)

    pp.pprint(cinema)
    names = cinema.getMovieNames()
    for n in names:
        print(n)

    mins = cinema.getTotalMinutes()
    print(f"Total Minutes: {mins}")

    cinema.remove("Platoon")
    mins = cinema.getTotalMinutes()
    print(f"Total Minutes: {mins}")

    for r in ("G", "PG", "M", "R13", "RP13", "R15", "R16", "RP16", "R18"):
        print(f"Movies rated {r}")
        rnames = cinema.findRatedMoviesNames(r)
        for n in rnames:
            print(f"\t{n}")

    ex = cinema.findMovieItem("The Exorcist")
    print(ex.show())

# booking testing
    print("--- Testing Bookings ---")

    m = cinema.findMovieItem("The Shawshank Redemption")
    c = Customer("Joe Bloggs", "021-123-1234", "joe.bloggs@mail.com")
    cinema.addBooking(c, 1, m)

    m = cinema.findMovieItem("The Exorcist")
    c = Customer("Jane Doe", "021-456-4567", "jane.doe@mail.com")
    cinema.addBooking(c, 2, m)

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

    print(cinema.customers())

    print(cinema.getBookings())
    print(cinema.showBookings())
    b = cinema.findBooking("021-123-1234")
    print(b)
    assert b.bookingid == "021-123-1234", "Public Methods"

    m = cinema.findMovieItem("Poltergeist")
    cinema.updBooking("021-456-4567", None, m)
    print(cinema.showBookings())
    print(cinema.getBookings(1))

    cinema.removeBooking("021-456-4567")
    print(cinema.showBookings())
    print(cinema.bySessions("Cars"))

    print("End Tests")
