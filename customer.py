"""
    Customer Class

    Handles customers booking for a particular movie

    Changelog:
        28NOV2022 - Initial release

"""


class Customer:
    # Constructor
    def __init__(self, name="", contact="", email=""):
        self._name = name
        self._contact = contact
        self._email = email

    # Public methods
    def get_customer(self):
        return self.name

    @property
    def name(self):
        return str(self._name)

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError
        self._name = name
        return self

    @property
    def email(self):
        return str(self._email)

    @email.setter
    def email(self, email):
        if not email:
            raise ValueError
        self._email = email
        return self

    @property
    def contact(self):
        return str(self._contact)

    @contact.setter
    def contact(self, contact):
        if not contact:
            raise ValueError
        self._contact = contact
        return self

    def show(self):
        return "\n".join([f"Customer: {self._name}",
                          f"Contact: {self._contact}",
                          f"Email: {self._email}", ])

    def __str__(self):
        return self.show()


# End of class, tests below
if __name__ == "__main__":
    print("Start Tests")

    print("End Tests")
