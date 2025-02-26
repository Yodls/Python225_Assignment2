class Date:  # defines the Date class to represent a date
    def __init__(self, year, month, day):  # initializes a new Date object with year, month, and day
        self.year = year    # assigns the year to the year attribute
        self.month = month  # assigns the month to the month attribute
        self.day = day      # assigns the day to the day attribute

    def __str__(self):  # defines a method to return a string of the Date object
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d}"  # formats the date

    def to_tuple(self):  # defines a method to return the date as a tuple (year, month, day)
        return (self.year, self.month, self.day)  # returns the tuple for comparison

    def is_after(self, other):  # defines a method to determine if the date comes after another Date object
        return self.to_tuple() > other.to_tuple()  # compare the tuples


# tests

date1 = Date(1933, 6, 22)  # date1 is June 22, 1933
print(date1)              # Print date1; should display "1933-06-22"

date2 = Date(1933, 9, 17)  # date2 is September 17, 1933
print(date2)              # Print date2; should display "1933-09-17"

# checks if date1 comes after date2; expected output is False because June 22 is before September 17
print(date1.is_after(date2))

# checks if date2 comes after date1; expected output is True
print(date2.is_after(date1))

