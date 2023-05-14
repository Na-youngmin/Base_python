to_do_list = [] #빈 리스트 만들기
make_list = 0 #변수 선언

#해야할 일 리스트에 넣기
while (make_list != 'N'):
    make_list = input('해야할 일을 넣어주세요(다 넣었으면 N을 적어주세요) ')
    if (make_list != 'N'):
        to_do_list.append(make_list)
    elif (make_list == 'N'):
        break

# 스케쥴표 작성 코드
while (len(to_do_list) != 0):
    print('\n현재 해야할 일 입니다.\n',to_do_list,'\n')
    do = input('해야할 일이 있습니까?(Y/N) ')
    if (do == 'Y'):
        do_list = input('어떤 일을 해야합니까? ')
        to_do_list.append(do_list)
    elif (do == 'N'):
        done = input('완료한 일이 있습니까?(Y/N) ')
        if (done == 'Y'):
            done_list = input('어떤 일을 완료했습니까? ')
            if (done_list in to_do_list):
                to_do_list.remove(done_list)
            else:
                print('목록에 없어요 ')
        elif (done == 'N'):
            print('할 일이 많으니 서둘러주세요! ')
        else:
            print('Y 또는 N으로만 답해주세요! ')
    else:
        print('Y 또는 N으로만 답해주세요! ')

# 휴가 메세지 코드
print('\n모든 일을 다 하셨습니다~!, 휴가를 즐기세요~!')
