def merge_alternately(word_1,word_2):
    string=""
    a=len(word_1)
    b=len(word_2)
    c=min(a,b)
    for i in range(c):
        string=string+word_1[i]+word_2[i]
    if a>b:
        string+=word_1[c:]
        return string
    elif b>a:
        string+=word_2[c:]
        return string
    else:
        return string
