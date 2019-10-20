import math
import random

#-------------FUNCTION DECLARATION----------
def generate_birthday():
    return(int(random.uniform(1,365)))

def generate_class_birthdays(numSt):
    return([generate_birthday() for j in range(numSt)])

def check_class_bdays(bday_list, num_st_matches):
    act_match = max([bday_list.count(entry) for entry in bday_list])
    if act_match >= num_st_matches:
           return (True)
    else:
           return (False)
        
def generate_school_class(nclases, nsclass):
    daclases = [None]*nclases
    for e in range(nclases):
        daclases[e] = generate_class_birthdays(nsclass)
        
    return ([generate_class_bdays(nsclass) for j in range(nclases)])
def check_school_birthdays(shclass, clmatch, stmatch):
    stud_matcher = 0
    return([check_class_bdays(shclass, stmatch) for j in shclass].count(True) >= clmatch)
    
def generate_district_birthdays(nschools, nclass, nbdays):
    allschools = [None]*nschools
    for i in range(len(allschools)):
        allschools[i] = generate_school_class(nclass, nbdays)
    return allschools

def check_district_birthdays(dslist, nshmatch, nclmatches, nstmatch):
    st_matcher = 0
    for g in range(len(dslist)):
        ch = check_school_birthdays(dslist[g], nclmatches, nstmatch)
        if ch == True:
            st_matcher = st_matcher + 1
    if st_matcher >= nshmatch:
        return True
    else:
        return False

###-----------------------MAIN FUNCTION -------------

#USER PROMPT
user_prompt = input("Would you like to create only a class, school, or district? ")
while user_prompt !="class" and user_prompt != "school" and user_prompt!= "district":
    user_prompt= input("Please, only enter class, school, or district ")

    #CLASS CASE
if user_prompt == "class":
    attempts = int(input("How many times will you run the simulation? "))
    answer = [None]*attempts
    ma = int(input("How many matches would you like to find?"))
    s_number = int(input("How many students in the class? "))
    lists = [None]*s_number
    for l in range(len(answer)):
        lists = generate_class_birthdays(s_number)
      
        answer[l] = check_class_bdays(lists, ma)
        
        #SCHOOL CASE
elif user_prompt == "school":
    attempts = int(input("How many times will you run the simulation? "))
    class_number = int(input("How many classes are there? "))
    s_number = int(input("How many students per class? "))
    cmat_num = int(input("How many class matches would you like to find? "))
    smat_num = int(input("How many student matches would you like to find? "))
    answer = [None]*attempts
    for k in range(len(answer)):
        lists = generate_school_class(class_number, s_number)
        answer[k] = check_school_birthdays(lists, cmat_num, smat_num)
        
    #DISTRICT CASE
elif user_prompt == "district":
    attempts = int(input("How many times will you run the simulation? "))
    school_number = int(input("How many schools are there? "))
    class_number = int(input("How many classes are there? "))
    stud_number = int(input("How many students are there?"))
    scmat_num = int(input("How many school matches would you like to find?: "))
    cmat_num = int(input("How many class matches would you like to find? "))
    smat_num = int(input("How many student matches would you like to find? "))
    answer = [None]*attempts
    for m in range(len(answer)):
        lists = generate_district_birthdays(school_number,class_number,stud_number)
        answer[m] = check_district_birthdays(lists, scmat_num,cmat_num, smat_num)
        
# CALCULATING PROBABILITY
counter = answer.count(True)
print("The probability is: {0}".format(counter/attempts))
