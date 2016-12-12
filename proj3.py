eng_kor_map = {'1':'ㄱ', '2':'ㄴ', '3':'ㅏ', 'q':'ㄹ', 'w':'ㅁ', 'e':'ㅗ', 'a':'ㅅ', 's':'ㅇ', 'd':'ㅣ', 'z':'.', 'x':'ㅡ', 'c':'='}
state_transition_list = [{'1':'q1', '2':'q2', 'a':'q2', 'q':'q3', 's':'q4', 'w':'q2'}, {'3':'q5', 'c':'q3', 'd':'q6', 'e':'q7', 'x':'q8', 'z':'q3'},  {},  {},  {},  {},  {},  {},  {},  {},  {},  {},  {},  {},  {},  {},  {},  {},  {},  {},  {},  {},  {},  {},  {},  {},  {},  {},  {}]
def state_transition_func(q, sigma):
    if state_transition_dict[q]

    return next_state