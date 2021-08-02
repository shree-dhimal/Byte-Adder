#main module
import exceptionhandling as t
import conversion as c
import calculation as cal

def main_method():
    m=True
    while m==True:
        print(("\n"))
        actualbinarynum=""
        num1,num2=t.num_valid()
        binary_1=c.conv(num1)
        binary_2=c.conv(num2)
        l1=c.dectobin(num1)
        l3=c.dectobin(num2)
        a=l1
        b=l3
        actual_result=cal.calculate_result(b,a)
        Result=actual_result
        Result.reverse()
        actual=actual_result
        l=c.bintodec(actual_result)
        for i in range (len(actual)-1,-1,-1):
            actualbinarynum = actualbinarynum+str(actual[i])
        a.reverse()
        b.reverse()
        print(("\n"))
        print("The first Number you entered is:",num1)
        print("The conversion of first number in list is:",a)
        print("The binary conversion of the first number is:",binary_1)
        print(("\n"))
        print("The second number you entered is:",num2)
        print("The conversion of second number in list is:",b)
        print("The binary conversion of the second number is:",binary_2)
        print(("\n"))
        print("The sum of numbers in binary in list is:",Result)
        print("The sum of the number in binary  is:",actualbinarynum)
        print("The final result in Decimal is:",l)
        print(("\n"))
        cont=input("Do you wish to continue ?(Y/N)")
        if cont.upper()=="Y":
            m= True
        elif cont.upper()=="N":
            
            m= False
        
if __name__=='__main__':
    main_method()

