def is_available(number, length):

    error_code = 0

    # 길이검사
    if len(number) != length:
        error_code = 1

    return error_code
