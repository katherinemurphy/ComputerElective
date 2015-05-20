name = raw_input("what's your best friend name?")
age = input("how old are you?")

namebf = raw_input("what's your best friend name?")
agebf = input("how old are you?")

if age == agebf:
    print name, "and", namebf, "are both", age, "years old"
elif age > agebf:
    print name, "is older than" , namebf
    print name, "is", age, "and", namebf, "is", agebf
elif age < agebf"
    print name, "is younger than" , namebf
    print name, "is", age, "and", namebf, "is", agebf
