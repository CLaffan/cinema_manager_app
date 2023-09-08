"""
    Movie Class

    Handles all of the movie related information
    
    Changelog:
        28NOV2022 - Initial release
"""


class Movie:

    # https://www.nfi.edu/movie-genres/
    _GENRE = {
        "not set": "Not Set",
        "Horror": "Dark places and unexplained things like forests, graveyards, castles, abandoned structures or buildings, locked doors to remove rooms, blood, gore, or killing instruments.",
        "Sci-Fi": "Outer space or futuristic items like spaceships or laser guns",
        "Sport": "Sports arenas, teams, athletes, and sports equipment",
        "Western": "Cattle, stage coaches, saloons, ten-gallon hats, the frontier, or revolvers",
        "Comedy": "Slapstick humor, witty dialogue, rites of passage, gross-out humor, fish-out-of-water, cross-dressing, mistaken identity",
        "Crime": "Restricted to persons 15 Years and over",
        "Action": "Chase sequences, extended fight scenes, guns, races against time",
        "Musical": "different stages of 'falling in love' with a subsequent break-up and reconciliation, true love, fairy tales, forbidden love",
        "Drama": "a self-sacrificial maternal figure",
    }

    # Private Methods and Variables
    _RATINGS = {
        "not set": "Not Set",
        "G": "Suitable for General Audiences",
        "PG": "Parental Guidance Recommended for Younger Viewers",
        "M": "Suitable for Mature Audiences 16 and over",
        "R13": "Restricted to persons 13 Years and over",
        "RP13": "Restricted to persons 13 Years and over unless accompanied by a Parent/Guardian",
        "R15": "Restricted to persons 15 Years and over",
        "R16": "Restricted to persons 16 Years and over",
        "RP16": "Restricted to persons 16 Years and over unless accompanied by a Parent/Guardian",
        "R18": "Restricted to persons 18 Years and over",
    }

    # Constructor
    def __init__(self, name="", minutes=-1, rating="not set", genre="not set"):
        self._name = name
        self._minutes = minutes
        self._rating = rating
        self._genre = genre

    # Public Class methods
    @classmethod
    def get_ratings(cls):
        return cls._RATINGS

    @classmethod
    def valid_rating(cls, rating):
        if not rating or not cls._RATINGS[rating]:
            return False
        return True

    @classmethod
    def getRatingText(cls, rating):
        if not cls.valid_rating(rating):
            raise ValueError
        return cls._RATINGS[rating]

    @classmethod
    def get_genres(cls):
        return cls._GENRE

    @classmethod
    def genre_list(cls):
        return list(cls._GENRE.keys())

    @classmethod
    def valid_genre(cls, genre):
        if not genre or not cls._GENRE[genre]:
            return False
        return True

    @classmethod
    def getGenreText(cls, genre):
        if not cls.valid_genre(genre):
            raise ValueError
        return cls._GENRE[genre]

    # Property Public Instance Methods
    @property
    def genre(self):
        return str(self._genre)

    @genre.setter
    def genre(self, genre):
        if not Movie.valid_genre(genre):
            raise ValueError
        # Only set if it has not been set before
        if self._genre == "not set":
            self._genre = genre
        else:
            raise ValueError("Cannot set genre twice")
        return self

# instances attributes and methods
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError
        self._name = name
        return self

    @property
    def minutes(self):
        return self._minutes

    @minutes.setter
    def minutes(self, minutes):
        try:
            minutes = int(minutes)
        except:
            raise ValueError
        if not minutes or minutes <= 0 or minutes > 300:
            raise ValueError
        self._minutes = minutes
        return self

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, rating):
        if not Movie.valid_rating(rating):
            raise ValueError
        # Only set if it has not been set before
        if self._rating == "not set":
            self._rating = rating
        else:
            raise ValueError("Cannot set rating twice")
        return self

    # aliases to match assignment spec
    audienceRating = rating

    # Can't alias setters (https://stackoverflow.com/questions/51047956/error-str-object-is-not-callable-when-using-property-setter)
    def setAudienceRating(self, rating):
        self.rating = rating

    def setMinutes(self, minutes):
        self.minutes = minutes

    def setGenre(self, genre):
        self.genre = genre

    # Other Public Instance methods
    def setNameAndMinutes(self, name, minutes):
        self.name = name
        self.minutes = minutes
        return self

    def populate(self, name, minutes, rating, genre):
        self.name = name
        self.minutes = minutes
        self.rating = rating
        self.genre = genre
        return self

    def show(self):
        return "\n".join([f"Movie: {self._name}",
                          f"Run Time: {self._minutes}mins",
                          f"Audience Rating: {self._rating}",
                          f"Genre: {self._genre}"])

    def __str__(self):
        return self.show()


# End of class, tests below
if __name__ == "__main__":
    print("Start Tests")
    m1 = Movie()
    m1.name = "The Shawshank Redemption"
    m1.rating = "RP16"
    m1.minutes = 142
    m1.genre = "Drama"
    print(m1)
    assert str(m1) == "Movie: The Shawshank Redemption\nRun Time: 142mins\nAudience Rating: RP16\nGenre: Drama", \
        "Basic Setters and show"

    assert m1.show() == "Movie: The Shawshank Redemption\nRun Time: 142mins\nAudience Rating: RP16\nGenre: Drama", \
        "Basic Setters and show"

    try:
        m1.rating = "R18"
    except ValueError as e:
        assert str(e) == "Cannot set rating twice", "Correct exception raised"
    except:
        raise

    try:
        m1.genre = "Comedy"
    except ValueError as e:
        assert str(e) == "Cannot set genre twice", "Correct exception raised"
    except:
        raise

    m2 = Movie()
    m2.setNameAndMinutes("12 Angry Men", 96)
    m2.setAudienceRating("G")
    m2.setGenre("Comedy")
    assert m2.show() == "Movie: 12 Angry Men\nRun Time: 96mins\nAudience Rating: G\nGenre: Comedy", \
        "Aliased setters and show"

    m3 = Movie()
    m3.setNameAndMinutes("Halloween", 91)
    m3.audienceRating = "R16"
    assert m3.show() == "Movie: Halloween\nRun Time: 91mins\nAudience Rating: R16\nGenre: not set", \
        "Aliased setters and show"

    m4 = Movie()
    m4.name = "Cars"
    m4.setMinutes(117)
    assert m4.show() == "Movie: Cars\nRun Time: 117mins\nAudience Rating: not set\nGenre: not set", \
        "Aliased setters and show"
    m4.rating = "G"
    assert m4.rating == "G", "rating getter"
    assert m4.name == "Cars", "name getter"
    assert m4.minutes == 117, "minutes getter"

    try:
        m4.setMinutes(0)
    except ValueError:
        pass
    except:
        raise

    try:
        m4.setMinutes(400)
    except ValueError:
        pass
    except:
        raise

    m5 = Movie()
    m5.populate("Apocalypse Now", 147, "R16", "Sci-Fi")
    assert m5.show() == "Movie: Apocalypse Now\nRun Time: 147mins\nAudience Rating: R16\nGenre: Sci-Fi", \
        "populate"

    # FIXME: Tests for class methods

    print("End Tests")

    """The Shawshank Redemption, 142, RP16
    The Godfather, 175, R16, Action
    The Dark Knight, 152, M, Sci-Fi
    12 Angry Men, 96, G
    Schindler's List, 195, RP13, Drama
    The Lord of the Rings: The Return of the King, 201, M
    One Flew Over the Cuckoo's Nest, 133, R18
    The Lord of the Rings: The Fellowship of the Ring, 178, PG, Sci-Fi
    Saving Private Ryan, 169, R15
    Blade Runner 2049, 164, R13, SciFi
    Halloween, 91, R16, Horro
    Beverly Hills Cop, 105, RP16
    Platoon, 120, RP16
    Total Recall, 113, RP16
    Back to the Future, 116, G
    The Lion King, 88, G
    Cars, 117, G
    The Wizard of Oz, 102, G
    The Wolf of Wall Street, 180, R18
    Harry Potter and the Philosopher's Stone, 152, PG
    Poltergeist, 114, PG
    Full Metal Jacket, 116, RP13
    The Exorcist, 122, R15, Horror
    Apocalypse Now, 147, R16, Horror
    """
