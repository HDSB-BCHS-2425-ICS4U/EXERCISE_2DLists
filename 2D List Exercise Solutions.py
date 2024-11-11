from random import randint

#2D List Exercise Solutions

#Create a user defined 2D list and 
print("Let's create a student list: ")
rows = int(input("How many students do you have: "))
columns = int(input("How many assignments do these students have: "))
students = []
titles = []
titles.append("Student Id")
for i in range(0,columns):
    assignment = input("Please enter name of assignment: ")
    titles.append(assignment)

students.append(titles)
for i in range(0,rows):
    student = []
    for k in range(len(titles)):
        value = int(input("Please enter value for column "+str(titles[k])))
        student.append(value)
    students.append(student)

#Sum a row of their choice
row = int(input("Please enter the id of the student you want to get grade sum of: "))
for i in range(0,len(students)):
    if students[i][0]==row:
        st_sum = 0
        for k in range(1,columns+1):
            st_sum+=students[i][k]
        print(st_sum)

#Sum a column of their choice 
assignment = input("Please enter the name of the assignment you want to get the sum of: ")
for i in range(0,len(titles)):
    if assignment == titles[i]:
        assign_sum = 0
        for k in range(1,rows+1):
            assign_sum += students[k][i]
        print(assign_sum)



#New user defined list (random values)
rows = int(input("Please enter the number of rows: "))
columns = int(input("Please enter the number of columns: "))
rand_list = []
for i in range(0,rows):
    row = []
    for k in range(0,columns):
        value = randint(0,1000)
        row.append(value)
    print(row)
    rand_list.append(row)

#find smallest prime
smallest_prime = 0
for i in range(0,rows):
    for k in range(0,columns):
        val = rand_list[i][k]
        is_prime = True
        for j in range(2,val//2+1):
            if val%j==0:
                is_prime = False
        if is_prime and (val<smallest_prime or smallest_prime==0):
            smallest_prime=val
print(smallest_prime) 

#find largest prime
largest_prime = 0
for i in range(0,rows):
    for k in range(0,columns):
        val = rand_list[i][k]
        is_prime = True
        for j in range(2,val//2+1):
            if val%j==0:
                is_prime = False
        if is_prime and (val>largest_prime or largest_prime==0):
            largest_prime=val
print(largest_prime) 

#find the largest column by sum
largest_col = -1
largest_sum = 0
for i in range(0,columns):
    sum = 0
    for k in range(0,rows):
        sum+=rand_list[k][i]
    if sum>largest_sum:
        largest_col = i
        largest_sum = sum

#find the smallest column by sum
smallest_col = -1
smallest_sum = -1
for i in range(0,columns):
    sum = 0
    for k in range(0,rows):
        sum+=rand_list[k][i]
    if sum<smallest_sum or smallest_sum==-1:
        smallest_sum = sum
        smallest_col = i