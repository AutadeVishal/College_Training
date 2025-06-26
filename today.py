emp=[('Aditya',19,33,20),('Deep',18,48,16),('Anisha',19,56,42),('Ganesh',17,50,42)]
#1)list out all emp 
#2)who is younger
#3 top performer
#4)top task assigned
#5)max task done by employee

while True:
    print(
    "Enter Choice : \n"
    "1: Show all Employees \n"
    "2: Show Youngest Employee \n" \
    "3: Show Top Performer \n" \
    "4: Show Top Task Assigned \n" \
    "5: Show Max Task Done by Employee \n" \
    "0: Quit \n"
    )
    
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Employees List: \n")
        print(list(map(lambda x : x[0],emp)))

    elif choice == 2:
        print("Youngest Employee is : ")
        print(min(emp, key=lambda x: x[1])[0])

    elif choice == 3:
        print("Top Performer is: ")
        print(max(emp,key=lambda x:x[2])[0])
    elif choice==4:
        print("Top Task Assigned :")
        print(max(emp,key=lambda x:x[3])[0])
    elif choice==5:
        print("Max Tax is done by:")
        print(max(emp,key=lambda x:x[2])[0])
    elif choice==0:
        break
    