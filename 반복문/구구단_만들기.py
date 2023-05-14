multi = int(input('몇단을 출력할까요? (종료:0)'))

if (multi == 0):
        print('구구단 종료')
        
while (multi != 0):

    print('{}단 시작!'.format(multi))
    for i in range(1,10):
        print(multi,'x',i,'=',multi*i)
        if (i == 9):
            print('{}단 종료!\n'.format(multi))
    multi = int(input('몇단을 출력할까요? (종료:0)'))
    
    if (multi == 0):
        print('구구단 종료')
    else:
        continue
