"""5. N을 입력 받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오(format 활용)

예시
<입력>
출력할 단을 입력해주세요 : 5

<출력>
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45

"""
print('<입력>')
dan = int(input('출력할 단을 입력해주세요 : '))

print()

print('<출력>')
for i in range(9) :
    print('{} * {} = {}'.format(dan, i+1, dan*(i+1)))