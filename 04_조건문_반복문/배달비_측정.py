print('20183217 나영민(데이터사이언스학부)\n')
print('''1. 금액(price)을 변수로 선언했습니다.
2. 호수(address)를 키보드로 입력받습니다.
3. 호수의 글자수를 통해 층수를 구분합니다.
3-1. 만약 address가 4글자 이하면 첫번째 문자를 층수 변수에 할당합니다. 
3-2. 그렇지 않은 경우는 두번째 문자까지를 층수 변수에 할당합니다.
    ex. 101호 -> 4글자 이므로 1을 할당, 1101호 5글자 이므로 11을 할당
4. 층에 따른 금액 계산
4-1. 1~5층인 경우는 기본 금액을 출력
4-2. 6~10층인 경우는 기본 금액의 10% 추가요금을 적용한 금액 출력
4-3. 11~15층인 경우는 기본 금액의 20% 추가요금을 적용한 금액 출력
4-4. 16~20층인 경우는 기본 금액의 30% 추가요금을 적용한 금액 출력
4-5. 그 외는 주문을 받지 않는다는 문구 출력''')

print('='*65)

price = 4000
address = (input('\n호수를 입력해주세요: (ex. 105호): '))

if len(address) <= 4:
    floor = int(address[:1])
    print('고객님은',floor,'층으로 배달을 시켰습니다.')
else:
    floor = int(address[:2])
    print('고객님은',floor,'층으로 배달을 시켰습니다.')
    
print('\n층 수에 따른 금액을 안내드립니다.')

if (floor >= 1) and (floor <= 5):
    print(price,'원 입니다.')
elif (floor >= 6) and (floor <= 10):
    print(int(price*1.1), '원 입니다.')
elif (floor >= 11) and (floor <= 15):
    print(int(price*1.2),'원 입니다.')
elif (floor >= 16) and (floor <= 20):
    print(int(price*1.3),'원 입니다.')
else:
    print('주문을 받지 않습니다.')
