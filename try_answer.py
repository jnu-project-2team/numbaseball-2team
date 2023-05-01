from is_available import *
from check_answer import *

def try_answer(sol_ans):
    sol_len = len(sol_ans)
    count = 0

    while True:
        count += 1

        print(f"#{count:02} : ", end='')

        # 사용자입력
        error_code = -1
        while error_code != 0:
            user_ans = input()
            error_code = is_available(user_ans, sol_len)

            # 유효성 검사
            if error_code == 0:
                pass
            elif error_code == 1:
                print(f"{sol_len} 길이의 숫자를 입력하세요.")
            elif error_code == 2:
                print("입력에 중복된 숫자가 포함되어 있습니다.")
            elif error_code == 3:
                print("입력에 숫자가 아닌 문자가 포함되어 있습니다.")
            else:
                print("유효성 검사 에러 발생")
                exit()

        # 결과 계산
        s, b = check_answer(user_ans, sol_ans)
        
        # 결과 출력
        if s == sol_len:
            print("정답입니다.")
            break
        else:
            print(f"  {s}S {b}B")
            
    return
