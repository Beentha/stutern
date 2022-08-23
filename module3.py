class Students:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + "@stutern.com"

    def fullname(self):
        return "{} {}".format(self.first, self.last)

stud_1 = Students("Bukola", "Dare")
stud_2 = Students("Temitope", "Balogun")

# print(stud_1.first)
# print(stud_2.last)

# print(stud_1.email)
# print(stud_2.first)

# print(stud_1.fullname())
# print(stud_2.fullname())
