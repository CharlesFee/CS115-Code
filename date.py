'''
Created on 11/25/18
@author:   Charles Fee
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 12 - Date class
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False

    def copy(self):
        '''Returns a new object with the same month, day, year
        as the calling object (self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
        '''Decides if self and d2 represent the same calendar date,
        whether or not they are the in the same place in memory.'''
        return self.year == d2.year and self.month == d2.month and \
            self.day == d2.day
    def tomorrow(self):
        '''finds out if the year or month needs to be adjusted
        Otherwise adds 1 to the former date'''
        if self.isLeapYear() == True and self.month == 2 and self.day == 28:
            self.day = 29
        elif self.day < DAYS_IN_MONTH[self.month]:
            self.day += 1
        else:
            if self.month != 12:
                self.month += 1
                self.day = 1
            else:
                self.month = 1
                self.day = 1
                self.year += 1

    def yesterday(self):
        '''finds out if the year or month needs to be adjusted
        Otherwise subtracts 1 from the former date'''
        if self.day > 1:
            self.day -= 1
        else:
            if self.isLeapYear() == True and self.month == 3:
                self.month = 2
                self.day = 29
            elif self.month != 1:
                self.month -= 1
                self.day = DAYS_IN_MONTH[self.month]
            else:
                self.month = 12
                self.day = DAYS_IN_MONTH[self.month]
                self.year -= 1
    def addNDays(self, N):
        '''changes the date to tomorrow's date N times'''
        print(self)
        for x in range(N):
            self.tomorrow()
            print(self)

    def subNDays(self, N):
        '''changes the date to yesterday's date N times'''
        print(self)
        for x in range(N):
            self.yesterday()
            print(self)
            
    def isBefore(self, d2):
        '''first checks year then month then day and makes sure that
        they are all before the date given or it will say it is not before'''
        if self.year < d2.year:
            return True
        elif self.year > d2.year:
            return False
        else:
            if self.month < d2.month:
                return True
            elif self.month > d2.month:
                return False
            else:
                if self.day < d2.day:
                    return True
                else:
                    return False

    def isAfter(self, d2):
        '''first checks year then month then day and makes sure that
        they are all after the date given or it will say it is not after'''
        if self.year < d2.year:
            return False
        elif self.year > d2.year:
            return True
        else:
            if self.month < d2.month:
                return False
            elif self.month > d2.month:
                return True
            else:
                if self.day > d2.day:
                    return True
                else:
                    return False
    def diff(self, d2):
        '''makes a copy of d2 and then manipulates that
        while counting to get the days in between self and d2'''
        counter = 0
        d = d2.copy()
        while d.isAfter(self):
            counter-=1
            d.yesterday()
        while d.isBefore(self):
            counter+=1
            d.tomorrow()
        return counter

    def dow(self):
        '''First checks if the difference is going back in time or in
        the future then wil the remainder after dividing by 7 it can
        calculate the day of the week all based off of that 11/25/2018
        was a sunday'''
        d = Date(11, 25, 2018)
        differ = self.diff(d)
        if differ > 0:
            if differ%7 == 0:
                return 'Sunday'
            elif differ%7 == 6:
                return 'Saturday'
            elif differ%7 == 5:
                return 'Friday'
            elif differ%7 == 4:
                return 'Thursday'
            elif differ%7 == 3:
                return 'Wednesday'
            elif differ%7 == 2:
                return 'Tuesday'
            elif differ%7 == 1:
                return 'Monday'
        else:
            differ = abs(differ)
            if differ%7 == 0:
                return 'Sunday'
            elif differ%7 == 1:
                return 'Saturday'
            elif differ%7 == 2:
                return 'Friday'
            elif differ%7 == 3:
                return 'Thursday'
            elif differ%7 == 4:
                return 'Wednesday'
            elif differ%7 == 5:
                return 'Tuesday'
            elif differ%7 == 6:
                return 'Monday'
