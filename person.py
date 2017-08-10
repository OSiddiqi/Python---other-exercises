class Person():
    
    def __init__(self):
        self.firstName = ""
        self.lastName = ""
        self.dateOfBirth = ""
        self.personList = []
        self.isMember = True

    def addDetails(self):
        """creating a new person"""

        self.firstName = input("Enter first name: ")
        self.lastName = input("Enter last name: ")
        self.dateOfBirth = input("Enter date of birth (dd/mm/yyyy): ")
        self.isMember = input("Are you staff (s) or a member (m)?: ")
            
    def updateDetails(self):
        """Updating a person"""
        
        self.firstName = input("Update first name: ")
        self.lastName = input("Update last name: ")
        self.dateOfBirth = input("Update date of birth (dd/mm/yyyy): ")

class Member(Person):

    def __init__(self):
        Person.__init__(self, firstName, lastName, dateOfBirth, True)
        self.numberOfItemsBorrowed

    def addDetails(self):
         """creating a new person"""

        self.firstName = input("Enter first name: ")
        self.lastName = input("Enter last name: ")
        self.dateOfBirth = input("Enter date of birth (dd/mm/yyyy): ")
        self.isMember = input("Are you staff (s) or a member (m)?: ")

m1 = Member()
m1.addDetails()
memberList =[]
memberList.append(p1)
if m1 in memberList:
    print(len(memberList))