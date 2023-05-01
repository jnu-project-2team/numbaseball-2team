from get_rand_num import *
from try_answer import *

print("숫자게임을 시작합니다."
      "진행할 숫자의 길이를 입력하세요. (1~9)"
      "입력 : ", end='')

length = 0
while True:
    length = int(input())
    digit = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    if length not in digit:
        print("다시 입력하세요."
              "입력 : ", end='')
    else:
        break

sol_ans = get_rand_num(length)

try_answer(sol_ans)
