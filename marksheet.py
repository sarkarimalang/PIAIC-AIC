#marksheet
print ("************ ~@ MarkSheet @~ ************")
print ("-----------------------------------------")
#totalsub is to count the number of entries
totalsub = 0
physics = int(input("Numbers of Physics? "))
totalsub += 1
statistics = int(input("Numbers of Statistics? "))
totalsub += 1
math = int(input("Numbers of Math? "))
totalsub += 1
chemistry = int(input("Numbers of Chemistry? "))
totalsub += 1
total = physics + statistics + math + chemistry
print ("-----------------------------------------")
# \t is used for spacing
print("|\tPhysics: \t\t", physics, "/ 100")
print("|\tChemistry: \t\t", chemistry, "/ 100")
print("|\tMath: \t\t\t", math, "/ 100")
print("|\tStatistics: \t\t", statistics, "/ 100")
print ("-----------------------------------------")
print ("Total Obtained Marks Are : ", total)
print ("-----------------------------------------")
print ("You have secured percentage : ", total/totalsub, " %")
print ("-----------------------------------------")
#the below is to get pass or fail
passfatfail = total/totalsub
if passfatfail>=72:
    number1result = 'Pass'
    print ("You are -",number1result, "- in this semester.")
    print("You will be moved to next semester")
else:
    number1result = 'Fail'
    print ("You are -",number1result, "- in this semester.")
    print("You will not be moved to next semester")
#below grading
percentage = total/totalsub
if percentage >= 81:
    grade = "A+"
elif percentage >= 71 and percentage <= 80:
    grade = "A "
elif percentage >= 61 and percentage <= 70:
    grade = "B "
elif percentage >= 51 and percentage <= 60:
    grade = "C "
elif percentage >=41 and percentage <=50:
    grade = "D"
elif percentage >=31 and percentage <=40:
    grade = "E"
else:
    grade = "F"
print ("You Secured -",grade, "- in this semester.")
print ("-----------------------------------------")