class Human:
    mail_pref = ''

    def __init__(self, email):
        if self.__class__.is_valid_email(email):
            self.email = email
        else:
            self.email = 'booo'


    @classmethod
    def is_valid_email(cls, email: str) -> bool:
        return email.startswith(cls.mail_pref)

    def _privet(self):
        print('hi from human')


class User(Human):
    mail_pref = 'user_'


class Admin(Human):
    mail_pref = 'admin_'

    def privet2(self):
        return self._privet()