# Write a Python function to find the Max of three numbers

def maximum(a,b,c):
    if a>b and a>c :
        print('Biggest Number=',a)
    elif b>a and b>c:
        print('Biggest Number=',b)
    elif a==b:
        print('a=b') 
    elif a==c: 
         print('a=c')
    elif b==c:
        print('b=c')
    else:
        print('Biggest Number=',c)   