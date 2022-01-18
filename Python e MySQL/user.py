class User:
    def __init__(self, name, email, password, date, acess=0):
        self._name = name
        self._email = email
        self._password = password
        self._date = date
        self._acess = acess

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    @property
    def acess(self):
        return self._acess

    @acess.setter
    def acess(self, acess):
        self._acess = acess
    

