print('20183217 나영민(데이터사이언스학부)\n')
print('''1. str_list에 키보드로 문자열을 입력받습니다.
2. str_list를 집합으로 만들어 중복을 제거해줍니다.
3. result를 딕셔너리로 할당합니다.
4. 반복문을 통해 str_list에 있는 문자열들의 중복값들을 세준 뒤, result에 저장합니다.
5. 결과를 출력합니다.''')

print('='*65)

str_list = input('\n문자열을 입력해주세요')
print('입력받은 문자열을 출력합니다.')
print(str_list,'\n')

groupby=list(set(str_list))
result=dict()
for i in groupby:
    result[i]=str_list.count(i)

print('결과를 출력합니다.')
print(result)
