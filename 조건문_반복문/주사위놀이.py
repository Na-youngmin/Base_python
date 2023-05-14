print('20183217 나영민(데이터사이언스학부)')

print('''1. random 모듈 import
2. 주사위 변수 생성 및 random함수를 통해 임의의 값 할당
3. 주사위 값을 맞출때까지 반복하는 반복문 생성
4. user 변수 생성 및 키보드를 통해 값 할당
5. user와 주사위 변수 값이 같으면 반복문 종료
6. 그렇지 않은 경우 2가지 경우로 나뉩니다.
6-1. user 값이 1 ~ 6사이로 입력받은 경우 반복문 초기로 돌아갑니다.
6-2. user 값이 1~6 사이 값이 아닌 경우 에러메세지를 보내며 반복문을 종료합니다.''')

print('='*65)

import random
dice = random.randint(1,6)

while (True):
    user = int(input('\n주사위의 숫자를 맞춰보세요! (1~6사이의 값을 입력해주세요.)'))
    if user == dice:
        print('정답~!!')
        print('게임을 종료합니다.')
        break
    else:
        if (user >= 1) and (user <=6):
            print('아쉬워요~')
            continue
        else:
            print('범위 외 값을 입력하셨으므로 게임을 종료합니다.')
            break
        
