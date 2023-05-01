def is_available(number, length):
    error_code = 0

    # 길이검사
    if len(number) != length:
        error_code = 1

    # 중복검사
    elif len(number) != len(set(number)):
        error_code = 2

    # 숫자검사
    else:
        for i in range(len(number)):
            if not ('0' <= number[i] <= '9'):
                error_code = 3
                break

    return error_code
