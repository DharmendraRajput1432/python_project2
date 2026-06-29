print("\n________Welcome to the Pattern Generator and Number Analyzer!________\n")
while True:
    
    print("\nSelect an option:\n")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice=int(input("Enetr your choice : "))

    if choice==1:
        n=int(input("Enter number of Rows : "))
        for i in range(n+1):
            for j in range(1,i+1):
                print("*",end=" ")
            print(" ")
            

    elif choice==2:
        start=int(input("Enter start range : "))
        end=int(input("Enter end range : "))
        sum=0
        print(" ")
        for i in range(start,end+1):
            if i%2==0:
                print("Number ",i,"is Even")
            else:
                print("Number ",i,"is Odd")
            sum=sum+i
        print("\nThe sum of all number from ",start,"to",end,"is :",sum)

    elif choice ==3:
        print("Exiting the program GoodBye! ")
        break

    else:
        print("\nInvalid choice! try again ")
        continue