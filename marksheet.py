#marksheet
#totalsub is to count the number of entries
passingmarks = 33 #passing marks variable
subdefaultmarks = 100 #default marks
failingsub = 0
totalsub = 0 #this is to get the total number of subjects
rollnumber = int(input("Enter Your Roll Number? "))
yourname = input("Enter Your Name? ")
#Physics
try:
    physics = int(input("Numbers of Physics? "))
except ValueError:
    print('PLease input a value for Physics')
    physics = int(input("Numbers of Physics? "))
totalsub += 1
#Chemistry
try:
    chemistry = int(input("Numbers of Chemistry? "))
except ValueError:
    print('PLease input a value for Chemistry')
    chemistry = int(input("Numbers of Chemistry? "))
totalsub += 1
#Math
try:
    math = int(input("Numbers of Math? "))
except ValueError:
    print('PLease input a value for Math')
    math = int(input("Numbers of Math? "))
totalsub += 1
#Statistics
try:
    statistics = int(input("Numbers of Statistics? "))
except ValueError:
    print('PLease input a value for Statistics')
    statistics = int(input("Numbers of Statistics? "))
totalsub += 1

total = physics + statistics + math + chemistry
#subject-grade #subject-grade #subject-grade #subject-grade #subject-grade
#subject-grade #subject-grade #subject-grade #subject-grade #subject-grade

subjects = [physics, statistics, math, chemistry]
for x in subjects:
    if x >= 81: # here it should read all the subjects and get separated result of all subjects
        if x == physics:
            subgraderp = "A+"
            physicsmsg = "Pass"
            phpname = ""
        if x == chemistry:
            subgraderc = "A+"
            chemistrysmsg = "Pass"
            chename = ""
        if x == math:
            subgraderm = "A+"
            mathsmsg = "Pass"
            mathname = ""
        if x == statistics:
            subgraderst = "A+"
            statisticsmsg = "Pass"
            stsname = ""
    elif x >= 71 and x <=80:
        if x == physics:
            subgraderp = "A"
            physicsmsg = "Pass"
            phpname = ""
        if x == chemistry:
            subgraderc = "A"
            chemistrysmsg = "Pass"
            chename = ""
        if x == math:
            subgraderm = "A"
            mathsmsg = "Pass"
            mathname = ""
        if x == statistics:
            subgraderst = "A"
            statisticsmsg = "Pass"
            stsname = ""
    elif x >= 61 and x <=70:
        if x == physics:
            subgraderp = "B"
            physicsmsg = "Pass"
            phpname = ""
        if x == chemistry:
            subgraderc = "B"
            chemistrysmsg = "Pass"
            chename = ""
        if x == math:
            subgraderm = "B"
            mathsmsg = "Pass"
            mathname = ""
        if x == statistics:
            subgraderst = "B"
            statisticsmsg = "Pass"
            stsname = ""
    elif x >= 51 and x <=60:
        if x == physics:
            subgraderp = "C"
            physicsmsg = "Pass"
            phpname = ""
        if x == chemistry:
            subgraderc = "C"
            chemistrysmsg = "Pass"
            chename = ""
        if x == math:
            subgraderm = "C"
            mathsmsg = "Pass"
            mathname = ""
        if x == statistics:
            subgraderst = "C"
            statisticsmsg = "Pass"
            stsname = ""
    elif x >= 41 and x <=50:
        if x == physics:
            subgraderp = "D"
            physicsmsg = "Pass"
            phpname = ""
        if x == chemistry:
            subgraderc = "D"
            chemistrysmsg = "Pass"
            chename = ""
        if x == math:
            subgraderm = "D"
            mathsmsg = "Pass"
            mathname = ""
        if x == statistics:
            subgraderst = "D"
            statisticsmsg = "Pass"
            stsname = ""
    elif x >= 31 and x:
        if x == physics:
            subgraderp = "E"
            physicsmsg = "Pass"
            phpname = ""
        if x == chemistry:
            subgraderc = "E"
            chemistrysmsg = "Pass"
            chename = ""
        if x == math:
            subgraderm = "E"
            mathsmsg = "Pass"
            mathname = ""
        if x == statistics:
            subgraderst = "E"
            statisticsmsg = "Pass"
            stsname = ""
    else:
        if x == physics:
            subgraderp = "F"
            physicsmsg = "Fail" #pass fail
            phpname = "Physics, " #pass fail
        if x == chemistry:
            subgraderc = "F"
            chemistrysmsg = "Fail"
            chename = "Chemistry, "
        if x == math:
            subgraderm = "F"
            mathsmsg = "Fail"
            mathname = "Math, "
        if x == statistics:
            subgraderst = "F"
            statisticsmsg = "Fail"
            stsname = "Statistics, "
        failingsub += 1
#subject-grade #subject-grade #subject-grade #subject-grade #subject-grade
#subject-grade #subject-grade #subject-grade #subject-grade #subject-grade

print ("-----------------------------------------------------------------------------")
print ("\t\t************ ~@ MarkSheet @~ ************")
print ("-----------------------------------------------------------------------------")
print ("|\t~Roll Number~ (",rollnumber,")")
print ("-----------------------------------------------------------------------------")
print ("|\t~Name~ (",yourname,")")
print ("-----------------------------------------------------------------------------")
# \t is used for spacing
print("|\tSubject: \t|", "Marks", "\t|", "Result \t|", "Grade")
print ("-----------------------------------------------------------------------------")
print("|\tPhysics: \t|", physics, "/ 100", "\t|", physicsmsg, "\t\t|", subgraderp)
print("|\tChemistry: \t|", chemistry, "/ 100", "\t|",chemistrysmsg, "\t\t|", subgraderc)
print("|\tMath: \t\t|", math, "/ 100", "\t|", mathsmsg, "\t\t|", subgraderm)
print("|\tStatistics: \t|", statistics, "/ 100", "\t|", statisticsmsg, "\t\t|", subgraderst)
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
if percentage>=63 and physics >= 33 and chemistry>=33 and math>=33 and statistics>=33:
    number1result = 'Passed'
    print ("You have (",number1result, ") this semester. You will be promoted to next semester")
    print ("-----------------------------------------------------------------------------")
else:
    number1result = 'Fail'
    print ("You are -",number1result, "- in (",failingsub,") subjects (",phpname,chename,mathname,stsname,") in this semester.")
    print ("-----------------------------------------------------------------------------")
    print ("You will not be promoted to next semester")
    print ("-----------------------------------------------------------------------------")
