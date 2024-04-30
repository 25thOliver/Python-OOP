# Python OOP Assignment
class Person:
    def introduce(self):
        print("These are the person's details:")
    def person_info(self, name, age, gender):
        print("Name: ", name)
        print("Age: ", age)
        print("Gender: ", gender)
        
person1 = Person()
person2 = Person()

person1.introduce()
person1.person_info("Bill Owino", 11, "Male")
print("")

person2.introduce()
person2.person_info('Shamim Night', 24, 'Female')