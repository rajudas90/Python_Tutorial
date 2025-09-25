class Person:
    name= "Rohan"
    occupation = "Software Developer"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
b = Person()
c = Person()
a.name = "Raju"
a.occupation = "Accountant"

b.name = "Kiran"
b.occupation = "Data Analyst"
# print(a.name, a.occupation) # Output is Raju Accountant
a.info()
b.info()
c.info()
# If I do not change a.name = "Raju" & a.occupation = "Accountant" then print only default value
# As we have not mentioned any information of c, so it will take default value