from customer import Customer
from movie import Movie

"""
    Booking Class

    Handles customers booking for a particular movie

    Changelog:
        28NOV2022 - Initial release

"""


class Booking:

    # Constructor
    def __init__(self):
        self._customer = None
        self._session = -1
        self._movie = None

    @property
    def bookingid(self):
        return self._customer.contact

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        if not customer:
            raise ValueError
        self._customer = customer
        return self

    @property
    def movie(self):
        return self._movie

    @movie.setter
    def movie(self, movie):
        if not movie:
            raise ValueError
        self._movie = movie
        return self

    @property
    def session(self):
        return self._session

    @session.setter
    def session(self, session):
        if not session or session <= 0 or session > 6:
            raise ValueError
        self._session = session
        return self

    # Public methods
    def customer_name(self):
        return self._customer.name

    def movie_name(self):
        return self._movie.name

    def populate(self, customer, session, movie):
        self.customer = customer
        self.movie = movie
        self.session = session
        return self

    def show(self):
        return "\n".join([f"Customer: {self._customer.name}",
                          f"Session: {self._session}",
                          f"Movie: {self._movie.name}", ])

    def __str__(self):
        return self.show()


# End of class, tests below
if __name__ == "__main__":
    print("Start Tests")


    print("End Tests")
