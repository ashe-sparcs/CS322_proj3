eng_kor_map = {'1':'ㄱ', '2':'ㄴ', '3':'ㅏ', 'q':'ㄹ', 'w':'ㅁ', 'e':'ㅗ', 'a':'ㅅ', 's':'ㅇ', 'd':'ㅣ', 'z':'.', 'x':'ㅡ', 'c':'='}
state_transition_dict = {'q19': {'3': 'q5', 'd': 'q6', 'x': 'q8', 'z': 'q23', 'e': 'q7'}, 'q22': {'2': 'q2', 'a': 'q2', 'w': 'q2', '1': 'q1', 'd': 'q6', 'x': 'q8', 's': 'q4', '3': 'q5', 'c': 'q3', 'q': 'q3', 'z': 'q18', 'e': 'q7'}, 'q9': {'2': 'q2', 'a': 'q17', 'w': 'q2', '1': 'q1', 'd': 'q6', 'x': 'q8', 's': 'q4', '3': 'q5', 'c': 'q18', 'q': 'q3', 'z': 'q18', 'e': 'q7'}, 'q17': {'q': 'q3', '2': 'q2', 'a': 'q2', 'w': 'q2', '1': 'q1', '3': 'q5', 'd': 'q6', 'x': 'q8', 's': 'q4', 'z': 'q1', 'e': 'q7'}, 'q14': {'q': 'q3', '2': 'q2', 'a': 'q2', 'w': 'q2', '1': 'q1', '3': 'q5', 'd': 'q6', 'x': 'q8', 's': 'q4', 'z': 'q18', 'e': 'q7'}
, 'q20': {'3': 'q5', 'd': 'q6', 'x': 'q8', 'z': 'q18', 'e': 'q7'}, 'q1': {'c': 'q3', '3': 'q5', 'd': 'q6', 'x': 'q8', 'z': 'q3', 'e': 'q7'}, 'q8': {'1': 'q9', '2': 'q10', 'a': 'q12', 'w': 'q15', 'q': 'q13', 'd': 'q6', 's': 'q14'}, 'q4': {'3': 'q5', 'd': 'q6', 'x': 'q8', 'z': 'q3', 'e': 'q7'}, 'q23': {'2'
: 'q2', 'a': 'q2', 'w': 'q2', '1': 'q1', 'd': 'q6', 'x': 'q8', 's': 'q4', '3': 'q5', 'c': 'q3', 'q': 'q3', 'z': 'q3', 'e': 'q7'}, 'q24': {'3': 'q5', 'd': 'q6', 'x': 'q8', 'z': 'q28', 'e': 'q7'}, 'q5': {'q': 'q13', '2': 'q10', 'a': 'q12', 'w': 'q15', '1': 'q9', '3': 'q11', 'd': 'q6', 's': 'q14', 'z': 'q8'
}, 'q27': {'3': 'q8'}, 'q16': {'q': 'q13', '2': 'q10', 'a': 'q12', 'w': 'q15', '1': 'q9', '3': 'q27', 'd': 'q6', 's': 'q14', 'z': 'q6'}, 'q3': {'3': 'q5', 'd': 'q6', 'x': 'q8', 'e': 'q7'}, 'q7': {'q': 'q13', '2': 'q10', 'a': 'q12', 'w': 'q15', '1': 'q9', '3': 'q8', 'd': 'q6', 's': 'q14', 'z': 'q6', 'e':
'q16'}, 'q10': {'q': 'q3', '2': 'q2', 'a': 'q19', 'w': 'q2', '1': 'q1', '3': 'q5', 'd': 'q6', 'x': 'q8', 's': 'q20', 'z': 'q21', 'e': 'q7'}, 'q12': {'2': 'q2', 'a': 'q2', 'w': 'q2', '1': 'q1', 'd': 'q6', 'x': 'q8', 's': 'q4', '3': 'q5', 'c': 'q0', 'q': 'q3', 'z': 'q22', 'e': 'q7'}, 'q18': {'q': 'q3', '2'
: 'q2', 'a': 'q2', 'w': 'q2', '1': 'q1', '3': 'q5', 'd': 'q6', 'x': 'q8', 's': 'q4', 'e': 'q7'}, 'q2': {'3': 'q5', 'd': 'q6', 'x': 'q8', 'z': 'q1', 'e': 'q7'}, 'q25': {'q': 'q3', '2': 'q2', 'a': 'q2', 'w': 'q2', '1': 'q1', '3': 'q5', 'd': 'q6', 'x': 'q8', 's': 'q4', 'z': 'q22', 'e': 'q7'}, 'q6': {'1': 'q9', '2': 'q10', 'a': 'q12', 'w': 'q15', 'q': 'q13', 's': 'q14'}, 'q13': {'q': 'q3', '2': 'q24', 'a': 'q17', 'w': 'q25', '1': 'q23', '3': 'q5', 'd': 'q6', 'x': 'q8', 's': 'q20', 'e': 'q7'}, 'q28': {'c': 'q3', '3': 'q5', 'd': 'q6', 'x': 'q8', 'z': 'q18', 'e': 'q7'}, 'q0': {'1': 'q1', '2': 'q2', 'a': 'q2',
'w': 'q2', 'q': 'q3', 's': 'q4'}, 'q15': {'q': 'q3', '2': 'q2', 'a': 'q2', 'w': 'q2', '1': 'q1', '3': 'q5', 'd': 'q6', 'x': 'q8', 's': 'q4', 'z': 'q26', 'e': 'q7'}, 'q26': {'2': 'q2', 'a': 'q17', 'w': 'q2', '1': 'q1', 'd': 'q6', 'x': 'q8', 's': 'q4', '3': 'q5', 'c': 'q3', 'q': 'q3', 'z': 'q18', 'e': 'q7'
}, 'q21': {'2': 'q2', 'a': 'q2', 'w': 'q2', '1': 'q1', 'd': 'q6', 'x': 'q8', 's': 'q4', '3': 'q5', 'c': 'q18', 'q': 'q3', 'z': 'q18', 'e': 'q7'}, 'q11': {'1': 'q9', '2': 'q10', 'a': 'q12', 'w': 'q15', 'q': 'q13', 'd': 'q6', 's': 'q14', 'z': 'q8'}}
key_consonant = ['1', '2', 'q', 'w', 'a', 's']
key_vowel = ['3', 'e', 'd', 'x']
key_special = ['z', 'c']
state = ['q0']
result = []
batchim = True
incomplete = []


def state_transition_func(q, sigma):
    # returns None if not found
    return state_transition_dict[q].get(sigma)


def action_func(q, sigma):
    # Initial state
    if q == 'q0':
        if sigma in key_consonant:
            result.append([sigma, '', ''])
        else:
            return None
    # 초성 ㄱ, ㄴ, ㅁ, ㅅ
    elif q in ['q1', 'q2']:
        if sigma in key_vowel:
            result[-1][1] = sigma
        elif sigma in key_special:
            result[-1][0] += sigma
        else:
            return None
    # 초성 ㄹ
    elif q == 'q3':
        if sigma in key_vowel:
            result[-1][1] = sigma
        else:
            return None
    # 초성 ㅇ
    elif q == 'q4':
        if sigma in key_vowel:
            result[-1][1] = sigma
        elif sigma == 'z':
            result[-1][0] += sigma
        else:
            return None
    # ㄱ + ㅏ + sigma
    elif q == 'q5':
        if sigma in key_consonant:
            result[-1][2] = sigma
        elif sigma in ['3', 'd', 'z']:
            result[-1][1] += sigma
        else:
            return None
    # ㄱ + ㅣ + sigma
    elif q == 'q6':
        if sigma in key_consonant:
            result[-1][2] = sigma
        else:
            return None
    # ㄱ + ㅗ + sigma
    elif q == 'q7':
        if sigma in key_consonant:
            result[-1][2] = sigma
        elif sigma in ['3', 'e', 'd', 'z']:
            result[-1][1] += sigma
        else:
            return None
    # ㄱ + ㅡ + sigma
    elif q == 'q8':
        if sigma in key_consonant:
            result[-1][2] = sigma
        elif sigma == 'd':
            result[-1][1] += sigma
        else:
            return None
    # ㄱ + ㅏ + ㄱ + sigma
    elif q == 'q9':
        if sigma in ['a', 'z', 'c']:
            result[-1][2] += sigma
        elif sigma in key_vowel:
            result.append([result[-1][2], sigma, ''])
            result[-2][2] = ''
        else:
            return None
    # ㄱ + ㅏ + ㄴ + sigma
    elif q == 'q10':
        if sigma in ['a', 'z']:
            result[-1][2] += sigma
        elif sigma in key_vowel:
            result.append([result[-1][2], sigma, ''])
            result[-2][2] = ''
        else:
            return None
    # ㄱ + ㅏ + ㅏ + sigma == ㄱ + ㅓ + sigma
    elif q == 'q11':
        if sigma in key_consonant:
            result[-1][2] = sigma
        elif sigma in ['d', 'z']:
            result[-1][1] += sigma
        else:
            return None
    # ㄱ + ㅏ + ㅅ + sigma
    elif q == 'q12':
        if sigma in ['z', 'c']:
            result[-1][2] += sigma
        elif sigma in key_vowel:
            result.append([result[-1][2], sigma, ''])
            result[-2][2] = ''
        else:
            return None
    # ㄱ + ㅏ + ㄹ + sigma
    elif q == 'q13':
        if sigma in ['1', 'a', 'w']:
            result[-1][2] += sigma
        elif sigma in key_vowel:
            result.append([result[-1][2], sigma, ''])
            result[-2][2] = ''
        else:
            return None
    # ㄱ + ㅏ + ㅇ + sigma
    elif q == 'q14':
        if sigma in ['z']:
            result[-1][2] += sigma
        elif sigma in key_vowel:
            result.append([result[-1][2], sigma, ''])
            result[-2][2] = ''
        else:
            return None
    # ㄱ + ㅏ + ㅁ + sigma
    elif q == 'q15':
        if sigma in key_vowel:
            result.append([result[-1][2], sigma, ''])
            result[-2][2] = ''
        elif sigma in ['z']:
            result[-1][2] += sigma
        else:
            return None
    # ㄱ + ㅗ + ㅗ + sigma == ㄱ + ㅜ + sigma
    elif q == 'q16':
        if sigma in key_consonant:
            result[-1][2] = sigma
        elif sigma in ['d', 'z']:
            result[-1][1] += sigma
        else:
            return None
    
    elif q == 'q17':

    # None이 아닌 무언가를 리턴해야 한다?

