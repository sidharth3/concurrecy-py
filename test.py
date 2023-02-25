

def gcd(a, b):
    
    if (a == 0):
        return b;
    
    print("a is not 0")
    return gcd(b % a, a);


def Student(cls, input1, input2):
    if len(input2) < 1:
        return 0
    
    res = input2[0]
    print("get")
    for i in input2:
        res = gcd(res, i)
        if res == 1:
            return 1
    return res
    
def Student2(cls, input1, input2):
    if len(input2) < 1:
        return 0

    res = input2[0]
    print("get")
    for i in input2:
        res = gcd(res, i)
        if res == 1:
            return 1
    return res


