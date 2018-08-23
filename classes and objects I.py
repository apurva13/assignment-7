#Q.1- Create a user defined dictionary and get keys corresponding to the value using for loop.
def dict():
    n=int(input("Enter no. of Keys:"))
    dic={}
    for i in range(n):
        key=int(input("Enter Key :"))
        value=input("Enter Value :")
        dic[key]=value          
    print('Dictionary :',dic)
    val=input('Enter value:')
    for k,v in dic.items():
        if(v==val):
            print("KEY FOR",val,"IS",k)
dict()


'''
Q.2- Create a dictionary and store student names and create nested dictionary to store the subject wise marks of every student.
Print the marks of a given student from that dictionary for every subject. Hint: Use nested dictionary to store subjects marks.
'''
def dict():
    n=int(input("Enter no. of Keys:"))
    dic={}
    for x in range(n):
        name=input("Enter name: ")
        marks={}
        m1=int(input("Enter marks in Python: "))
        m2=int(input("Enter marks in ADBMS: "))
        m3=int(input("Enter marks in DS: "))
        marks['Python']=m1
        marks['ADBMS']=m2
        marks['DS']=m3
        dic[name]=marks
    print('Dictionary :',dic)
    student=input("Enter name of student:")
    print('Marks:',dic[student])
dict()
