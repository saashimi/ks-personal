class MyTime:
    """
    """

    def __init__(self, hrs=0, mins=0, secs=0):
        """ Create a new MyTime object initialized to hrs, mins, secs.
           The values of mins and secs may be outside the range 0-59,
           but the resulting MyTime object will be normalized.
        """

        # Calculate total seconds to represent
        totalsecs = hrs*3600 + mins*60 + secs
        self.hours = totalsecs // 3600        # Split in h, m, s
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60

    def __str__(self):
        return "{h}:{m}:{s}".format(h=self.hours, m=self.minutes, s=self.seconds)

    def __add__(self, other):
        return MyTime(0, 0, self.to_seconds() + other.to_seconds())

    def __iadd__(self, other):
        return MyTime(0, 0, self.to_seconds() + other.to_seconds())
    
    def __le__(self, other):
        return MyTime(0, 0, self.to_seconds() <= other.to_seconds())

    def __lt__(self, other):
        return MyTime(0, 0, self.to_seconds() < other.to_seconds())

    def to_seconds(self):
        """ Return the number of seconds represented
            by this instance
        """
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def after(self, t1, t2):
        if t1 <= self < t2:
            print("True")
            return True
        else:
            print("False")
            return False

t1 = MyTime(1, 0, 0)
t2 = MyTime(3, 0, 0)
t3 = MyTime(2, 30, 0)


if __name__ == "__main__":
    t1 = MyTime(1, 0, 0)
    t2 = MyTime(3, 0, 0)
    t3 = MyTime(2, 30, 0)




