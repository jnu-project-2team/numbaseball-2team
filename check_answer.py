def check_answer(user_ans, sol):
    strike_count = 0
    ball_count = 0
    i = 0

    while i < len(user_ans):
        if user_ans[i] == sol[i]:
            strike_count += 1
            i += 1

    return strike_count, ball_count




