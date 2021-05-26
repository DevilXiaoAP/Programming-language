class SimpleGradebook(object):
    def __init__(self):
        self._grade = {}

    def add_student(self,name):
        self._grade[name] = []

    def report_grade(self, name, score):
        self._grade[name].append(score)

    def average_grade(self, name):
        grades = self._grade[name]
        print(grades)
        print(sum(grades))
        return sum(grades) / len(grades)


book = SimpleGradebook()
book.add_student('Isaac Newton')
book.report_grade('Isaac Newton', 90)
book.report_grade('Isaac Newton', 100)
print(book.average_grade('Isaac Newton'))
