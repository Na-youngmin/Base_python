 #90 ~ 100 : A
 #70 ~   89 : B
 #40 ~   69 : C
 #0 ~   39 : D
 
n = int(input())
 
if n >= 90 and n <= 100:
    print('A')
else:
    if n >= 70 and n <= 89:
        print('B')
    else:
        if n >= 40 and n <= 69:
            print('C')
        else:
            print('D')
