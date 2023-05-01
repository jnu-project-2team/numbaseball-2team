def is_available(number, length):

    error_code = 0

    # 길이검사
    if len(number) != length:
        error_code = 1

    # 중복검사
    if len(number) != len(set(number)):
        error_code = 2

    return error_code
