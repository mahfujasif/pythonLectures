class Employee:

    def __init__(self, ini_years):
        self.__years = ini_years

    def getHours(self):
        return 40

    def getSalary(self):
        return 40000

    def getVacationDay(self):
        return 10 + 2 * self.__years

    def getVacationForm(self):
        return "yellow"

    def printInfo(self, empl):
        print("salary: ", empl.getSalary())
        print("v.days: ", empl.getVacationDay())
        print("v.form: ", empl.getVacationForm())
        print()

class Secretary(Employee):
    def takeDictaion(self, s):
        print("Taking dictation of", s)


class Lawyer(Employee):
    def getVacationDay(self):
        return super(Lawyer, self).getVacationDay() + 5

    def getVacationForm(self):
        return "pinku"

    def getCanSue(self):
        return True


class Marketer(Employee):
    def getSalary(self):
        return super(Marketer, self).getSalary() + 10000

    def getAdvertise(self, s):
        print(s, "is awesome")


class LegalSecretary(Secretary):
    def fileLegal(self):
        print("I could file all day")

    def getSalary(self):
        return super(LegalSecretary, self).getSalary() + 50000


lisa = Lawyer(2)
steve = Secretary(3)

lisa.printInfo(lisa)
steve.printInfo(steve)