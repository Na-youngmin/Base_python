
import random

# 게임 규칙 설명
print(''' 숫자 맞추기 게임에 대해서 설명드리겠습니다.
1. 게임 진행 횟수를 입력합니다.
2. 사용자는 컴퓨터가 지정한 1 ~ 100 사이의 값을 맞춥니다.
3. 맞출 수 있는 기회는 5번이며, 5번 이내에 숫자를 맞출 시 점수를 얻게 됩니다.
4. 1 ~ 100 사이가 아닌 값을 입력해도 기회는 차감되니 신중하게 숫자를 입력해주셔야 합니다.
5. 사용자 입력 숫자와 컴퓨터가 지정한 숫자의 차이가 5 이하이면 조금 작아요/커요 를 출력합니다.''')

#게임 수 설정
game = int(input('몇 판을 진행할건가요?'))
chance = 5 # 맞출 수 있는 기회
user = 0 # 사용자 점수

print('\n{}판의 숫자 맞추기 게임을 시작합니다.'.format(game))

#게임 실행 코드
for i in range(game):
    print(i+1,'라운드 시작!\n')
    number = random.randint(1,101)
    for j in range(chance):
        print(j+1,'번째 시도 입니다.')
        answer = int(input('1부터 100까지 숫자를 맞춰보세요(기회는 5번): '))
        if ((answer >= 1) and (answer <= 100)):
            if (answer == number):
                print('정답~!\n')
                user = user + 1
                print('현재 점수는 {}점 입니다.\n'.format(user))
                break
            elif (answer < number):
                if (number - answer <= 5):
                    print('조금 작아요~\n')
                else:
                    print('너무 작아요~\n')
            else: 
                if (answer - number <= 5):
                    print('조금 커요~\n')
                else:
                    print('너무 커요~\n')
        else:
            print('1부터 100까지 숫자를 입력해주세요!')
            print('기회가 차감됩니다.')

#점수계산
com = game - user
print('최종 점수를 발표합니다.')
print('사용자 {}점, 컴퓨터 {}점 입니다.'.format(user, com)) 

#결과출력
if user > com:
    print('축하합니다! 승리하셨습니다!')
elif user < com:
    print('아쉬워요.. 이번에는 컴퓨터가 이겼어요')
else:
    print('이번에는 비겼네요..한번 더 하시는건 어떨까요?')
