print('20183217 나영민(데이터사이언스학부)\n')
print('''1. 원하는 숫자(num)를 입력받습니다.
2. 빈 리스트(num_list)를 생성합니다.
3. 리스트들의 총합 값을 할당할 변수(sum)를 설정합니다. (초기값 0)
4. 반복문을 통해 빈 리스트에 1부터 num까지 추가해줍니다.
5. 반복문을 통해 num_list에 있는 값들의 합을 계산해줍니다.
6. 최종결과(sum)를 출력해줍니다.\n''')

print('='*65)

num = int(input('\n원하는 숫자를 입력해주세요'))
num_list = []
sum = 0

for i in range(1,num+1):
    print('num_list {}값을 추가합니다.'.format(i))
    num_list.append(i)
print('모든 값을 다 넣었습니다.')
print('\n현재 num_list에 들어있는 값을 출력합니다.\n',num_list)

print('\nnum_list 값들의 합을 구합니다.\n')
for i in range(len(num_list)):
    print('num_list의',num_list[i],'을 더합니다.')
    sum += num_list[i]
print('모든 값을 다 더했습니다.\n')
print('num_list의 총합은 {}입니다.'.format(sum))
