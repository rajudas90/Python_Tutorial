class person:
    name= "Rohan"
    occupation = "Software Developer"
    networth = 10

a = person()
a.name = "Raju"
a.occupation = "Accountant"
print(a.name, a.occupation) # Output is Raju Accountant

# If I do not change a.name = "Raju" & a.occupation = "Accountant" then print only "Rohan Software Developer"
