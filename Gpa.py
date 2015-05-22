def GetName():
   name = raw_input("Enter the student's name  ")
   grade1 = raw_input("Enter a grade:  ")
   grade2 = raw_input("Enter a grade:  ")
   grade3 = raw_input("Enter a grade:  ")
   grade4 = raw_input("Enter a grade:  ")
   return name, grade1, grade2, grade3, grade4

grademap = { 'A': 4.00, 'B': 3.00, 'C': 2.00, 'D': 1.00 }

def grade2int(x):
   try:
       return grademap[x.upper()]
   except KeyError:
       raise Exception('invalid grade: ' + x)

def GetGrades(grades):
   return map(grade2int, grades)

def CalcGPA(grades):
   return sum(grades)/len(grades)

def main(name, GPA):
   print "The GPA for", name, "is", GPA
   return 0

if __name__ == '__main__':
   name, grade1, grade2, grade3, grade4 = GetName()
   grades = GetGrades([grade1, grade2, grade3, grade4])
   GPA = CalcGPA(grades)
   main(name, GPA)
