#creating the function
def num_valid():
    #expectinal handling inside while loop
    while True:
        try:
            num1=int(input("Enter the first Number:"))
            num2=int(input("Enter the second Number:"))
                #checking if entered number is between 0-256
            if (num1>0 and num1<256) and (num2>0 and num2<256):
                break
            else:
                print("Please enter numbers between 0-256")
                continue
        except ValueError:
            print("Please enter numbers only")
            continue
        else:
            break
    return num1,num2


