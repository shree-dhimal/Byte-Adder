
#Decimal to binary conversion for list

def dectobin(num):
    l=[]
    for i in range(1,9,1):
        if num%2==0:
            l.append(0)
        else:
            l.append(1)
        num=num//2
        i=i+1
    l2=[]
    for i in range(len(l)-1,-1,-1):
        l2.append(l[i])
    return l2
    


#Decimal to binary conversion for actual binary number

def conv(decimalno):
    bit=[]
    actualbinary=[]
    actualbinarynum=""
    while decimalno!=0:
        remainder=decimalno%2
        bit.append(remainder)
        decimalno=decimalno//2
    for i in range (len(bit)-1,-1,-1):
        actualbinarynum=actualbinarynum+str(bit[i])
    return actualbinarynum

#binary to decimal

def bintodec(l):
    val = 0 
    init = 1 
    for i in range(len(l)-1,-1,-1) :
        val = val + init*l[i] 
        init = init*2
    return val








    
