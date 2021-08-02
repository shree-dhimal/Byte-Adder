def and_Gate(Upper_bit,Lower_bit):
    if Upper_bit==1 and Lower_bit==1:
        return 1
    else:
        return 0
def or_Gate(Upper_bit,Lower_bit):
    if Upper_bit==1:
        return 1
    elif Lower_bit==1:
        return 1
    else:
        return 0
def compliment_gate(bit):
    if bit==0:
        return 1
    elif bit==1:
        return 0

def xor_Gate(Upper_bit,Lower_bit):
    a=and_Gate(compliment_gate(Upper_bit),Lower_bit)
    b=and_Gate(Upper_bit,compliment_gate(Lower_bit))
    c=or_Gate(a,b)
    return int(c)
def to_carry(Upper_bit,Lower_bit,carry):
    a1=xor_Gate(Upper_bit,Lower_bit)
    b1=and_Gate(Upper_bit,Lower_bit)
    c1=and_Gate(carry,a1)
    d1=or_Gate(c1,b1)
    return int(d1)
def calculate_result(Upper_bit,Lower_bit):
    result=[]
    carry=0
    Upper_bit.reverse()
    Lower_bit.reverse()
    for i in range(len(Upper_bit)):
        sum1=xor_Gate(Upper_bit[i],Lower_bit[i])
        result.append(xor_Gate(sum1,carry))
        carry=to_carry(Upper_bit[i],Lower_bit[i],carry)
        i+=1
    result.append(carry)
    return result


