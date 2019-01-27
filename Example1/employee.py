#! python
#
# Python SQLite Tutorial: Complete Oververview - Creating a Database, Table and
# Running [YouTube video]
# Corey Schafer [YouTube channel]
# I do not claim this work as my own so much as what I did while following
# along with the video I watched (see reference above).  This recreation is for
# my own reference purposes and may contain slight variations not depicted in
# the original video.


class Employee:
    # A sample Employee class

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last,
                                                   self.pay)
