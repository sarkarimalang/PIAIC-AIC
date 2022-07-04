#marksheet
print ("-----------------------------------------------------------------------------")
print ("\t\t************ ~@ MarkSheet @~ ************")
print ("-----------------------------------------------------------------------------")
#totalsub is to count the number of entries
passingmarks = 33 #passing marks variable
totalsub = 0 #this is to get the total number of subjects
physics = int(input("Numbers of Physics? "))
totalsub += 1
chemistry = int(input("Numbers of Chemistry? "))
totalsub += 1
math = int(input("Numbers of Math? "))
totalsub += 1
statistics = int(input("Numbers of Statistics? "))
totalsub += 1
total = physics + statistics + math + chemistry
#subject-grade #subject-grade #subject-grade #subject-grade #subject-grade
#subject-grade #subject-grade #subject-grade #subject-grade #subject-grade
subdefaultmarks = 100 #default marks
failingsub = 0

subjects = [physics, statistics, math, chemistry]
for x in subjects:
    if x >= 81: # here it should read all the subjects and get separated result of all subjects
        subgrader = "A+"
    elif x >= 71 and x <=80:
        subgrader = "A"
    elif x >= 61 and x <=70:
        subgrader = "B"
    elif x >= 51 and x <=60:
        subgrader = "C"
    elif x >= 41 and x <=50:
        subgrader = "D"
    elif x >= 31 and x:
        subgrader = "E"
    else:
        subgrader = "F"
    print (subgrader)

if physics >= 81:
    phsubgrade = "A+"
elif physics >= 71 and physics <=80:
    phsubgrade = "A"
elif physics >= 61 and physics <=70:
    phsubgrade = "B"
elif physics >= 51 and physics <=60:
    phsubgrade = "C"
elif physics >= 41 and physics <=50:
    phsubgrade = "D"
elif physics >= 31 and physics:
    phsubgrade = "E"
else:
    failingsub += 1
    phsubgrade = "F"

if chemistry >= 81:
    chsubgrade = "A+"
elif chemistry >= 71 and chemistry <=80:
    chsubgrade = "A"
elif chemistry >= 61 and chemistry <=70:
    chsubgrade = "B"
elif chemistry >= 51 and chemistry <=60:
    chsubgrade = "C"
elif chemistry >= 41 and chemistry <=50:
    chsubgrade = "D"
elif chemistry >= 31 and chemistry <=40:
    chsubgrade = "E"
else:
    failingsub += 1
    chsubgrade = "F"

if math >= 81:
    masubgrade = "A+"
elif math >= 71 and math <= 80:
    masubgrade = "A"
elif math >= 61 and math <= 70:
    masubgrade = "B"
elif math >= 51 and math <= 60:
    masubgrade = "C"
elif math >= 41 and math <= 50:
    masubgrade = "D"
elif math >= 31 and math <= 40:
    masubgrade = "E"
else:
    failingsub += 1
    masubgrade = "F"

if statistics >= 81:
    stsubgrade = "A+"
elif statistics >= 71 and statistics <= 80:
    stsubgrade = "A"
elif statistics >= 61 and statistics <= 70:
    stsubgrade = "B"
elif statistics >= 51 and statistics <= 60:
    stsubgrade = "C"
elif statistics >= 41 and statistics <= 50:
    stsubgrade = "D"
elif statistics >= 31 and statistics <= 40:
    stsubgrade = "E"
else:
    failingsub += 1
    stsubgrade = "F"
#subject-grade #subject-grade #subject-grade #subject-grade #subject-grade
#subject-grade #subject-grade #subject-grade #subject-grade #subject-grade

#pass fail #pass fail #pass fail #pass fail #pass fail #pass fail 
if physics>passingmarks:
    physicsmsg = "Pass"
    phpname = ""
else:
    physicsmsg = "Fail"
    phpname = "Physics, "
#pass fail #pass fail #pass fail #pass fail #pass fail #pass fail 
if chemistry>passingmarks:
    chemistrysmsg = "Pass"
    chename = ""
else:
    chemistrysmsg = "Fail"
    chename = "Chemistry, "
#pass fail #pass fail #pass fail #pass fail #pass fail #pass fail 
if math>passingmarks:
    mathsmsg = "Pass"
else:
    mathsmsg = "Fail"
    mathname = "Math, "
#pass fail #pass fail #pass fail #pass fail #pass fail #pass fail 
if statistics>passingmarks:
    statisticsmsg = "Pass"
    stsname = ""
else:
    statisticsmsg = "Fail"
    stsname = "Statistics, "
#pass fail #pass fail #pass fail #pass fail #pass fail #pass fail 
print ("-----------------------------------------------------------------------------")
# \t is used for spacing
print("|\tSubject: \t", "Marks", "\t\t", "Result \t", "Grade")
print("|\tPhysics: \t", physics, "/ 100", "\t", physicsmsg, "\t\t", phsubgrade)
print("|\tChemistry: \t", chemistry, "/ 100", "\t",chemistrysmsg, "\t\t", chsubgrade)
print("|\tMath: \t\t", math, "/ 100", "\t", mathsmsg, "\t\t", masubgrade)
print("|\tStatistics: \t", statistics, "/ 100", "\t", statisticsmsg, "\t\t", stsubgrade)
print ("-----------------------------------------------------------------------------")
print ("Total Obtained Marks Are : ", total, "Out Of", totalsub*100)
print ("-----------------------------------------------------------------------------")
#print ("You have secured percentage : ", total/totalsub, " %")
#print ("-----------------------------------------------------------------------------")
#below grading
percentage = total/totalsub
if percentage >= 81:
    grade = "A+"
elif percentage >= 71 and percentage <= 80:
    grade = "A"
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
print ("You Secured (",grade,") grade and got (", total/totalsub, "% ) percentage in this semester.")
print ("-----------------------------------------------------------------------------")
#the below is to get pass or fail
passfatfail = total/totalsub
if percentage>=63:
    number1result = 'Passed'
    print ("You have (",number1result, ") this semester. You will be promoted to next semester")
    print ("-----------------------------------------------------------------------------")
else:
    number1result = 'Failed'
    print ("You are -",number1result, "- in (",failingsub,") subjects (",phpname,chename,mathname,stsname,") in this semester.")
    print ("-----------------------------------------------------------------------------")
    print ("You will not be promoted to next semester")
    print ("-----------------------------------------------------------------------------")
