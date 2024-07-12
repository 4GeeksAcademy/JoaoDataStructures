
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self.id = 1

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 10)

    def add_member(self, member):
        member.last_name = self.last_name
        # member.id = self._generateId()
        member.id = self.id
        self.id=self.id + 1
        self._members.append(member)

    def delete_member(self, id):
        for member in self._members:
            print(member.id)
            if(member.id == id):
                self._members.remove(member)
            else: return print("ID not found")

    def get_member(self, id):
        for member in self._members:
            if(member.id == id):
                
                return member
            else: return print("ID not found" + member.id)

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members

class FamilyMember:
    last_name = None
    def __init__(self, id, firstName, age, luckyNumbers):
        self.id = id
        self.firstName = firstName
        self.age = age
        self.luckyNumbers = luckyNumbers
        
    def __str__(self):
        return f"{self.id}{self.firstName} {self.age} {self.last_name}"