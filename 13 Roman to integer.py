def roman(string):
    result=0
    values={"I":1,"V":5,"X":10,"L":50,
            "C":100,"D":500,"M":1000}
    for i in range(len(string)):
        if i+1<len(string) and values[string[i]]<values[string[i-1]]:
            result-=values[string[i]]
        else:
            result+=values[string[i]]
    return result
z=roman("VVX")
print(z)