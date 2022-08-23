"""
Write and run your program on vscode, ensure that your program is running effectively before pushing to github. Share the link on citrone for grading.

• Create a class called “Group_leader” that inherits from the class “Students” that we created in the practical session today. (Initialize the class and let it&nbsp; take an argument of the list of students under the group leader. Let the parent class take care of the other arguments)
• Define a method that adds students to the list of student under the group leader.
• Define a method that removes students from the list of students under the group leader.
• Define a method that prints out the full names of students in the list of students under group leader.
"""
from module3 import Students


class GroupLeader(Students):
    
    def __init__(self, first, last, students = None):
        super().__init__(first, last)
        if students is None:
            students = []
        self.students = students

    def add_students(self, student):
        return self.students.append(student)

    def remove_students(self, student):
        return self.students.remove(student)

    def print_fullname(self):
        for student in self.students:
            print(student)

stud_1 = Students("Bukola", "Dare")
stud_2 = Students("Temitope", "Balogun")

# Create 3 more instances of the parent class we defined in the practical session.
stud_3 = Students("John", "Doe")
stud_4 = Students("Jane", "Smith")
stud_5 = Students("Judith", "Lee")

# Create 2 instances of the sub class you created.
group_leader_1 = GroupLeader("Jane", "Doe")
group_leader_2 = GroupLeader("Judith", "Smith", ["Bukola Dare", "Judith Lee"])

# Add 2 students each to the list of students under the instances of your subclass.
group_leader_1.add_students("Janet Doe")
group_leader_1.add_students("Leo Chu")
# print(group_leader_1.students)

group_leader_2.add_students("Jane Smith")
group_leader_2.add_students("John Doe")
# print(group_leader_2.students)

# Remove 1 student each from the list of students under the instances of your subclass
group_leader_1.remove_students("Leo Chu")
# print(group_leader_1.students)

group_leader_2.remove_students("John Doe")
# print(group_leader_2.students)

# Print the fullname of the students in the list of students under the instances of your subclass.
group_leader_1.print_fullname()
group_leader_2.print_fullname()

# Print the email of the instances of your subclass.
print(group_leader_1.email)
print(group_leader_2.email)
