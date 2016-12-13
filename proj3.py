# coding=utf-8
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
cho = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
cho_key = ['1', '1c', '2', '2z', '2zc', 'q', 'w', 'wz', 'wzc', 'a', 'ac', 's', 'az', 'azc', 'azz', '1z', '2zz', 'wzz', 'sz']
jung = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅗㅏ', 'ㅗㅐ', 'ㅗㅣ', 'ㅛ', 'ㅜ', 'ㅜㅓ', 'ㅜㅔ', 'ㅜㅣ', 'ㅠ', 'ㅡ', 'ㅡㅣ', 'ㅣ']
jung_key = ['3', '3d', '3z', '3zd', '33', '33d', '33z', '33zd', 'e', 'e3', 'e3d', 'ed', 'ez', 'ee', 'ee33', 'ee33d', 'eed', 'eez', 'x', 'xd', 'd']
jong = ['', 'ㄱ', 'ㄲ', 'ㄱㅅ', 'ㄴ', 'ㄴㅈ', 'ㄴㅎ', 'ㄷ', 'ㄹ', 'ㄹㄱ', 'ㄹㅁ', 'ㄹㅂ', 'ㄹㅅ', 'ㄹㅌ', 'ㄹㅍ', 'ㄹㅎ', 'ㅁ', 'ㅂ', 'ㅂㅅ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
jong_key = ['', '1', '1c', '1a', '2', '2az', '2sz', '2z', 'q', 'q1', 'qw', 'qwz', 'qa', 'q2zz', 'qwzz', 'qsz', 'w', 'wz', 'wza', 'a', 'ac', 's', 'az', 'azz', '1z', '2zz', 'wzz', 'sz']
jong_double = ['1a', '2az', '2sz', 'q1', 'qw', 'qwz', 'qa', 'q2zz', 'qwzz', 'qsz', 'wza']
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
        elif sigma in key_consonant:
            result.append([sigma, '', ''])
        elif sigma in key_vowel:
            result.append([result[-1][2], sigma, ''])
            result[-2][2] = ''
        else:
            return None
    # ㄱ + ㅏ + ㄴ + sigma
    elif q == 'q10':
        if sigma in ['a', 'z']:
            result[-1][2] += sigma
        elif sigma in key_consonant:
            if result[-1][2]+sigma in jong_double:
                result[-1][2] += sigma
            else:
                result.append([sigma, '', ''])
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
        elif sigma in key_consonant:
            result.append([sigma, '', ''])
        elif sigma in key_vowel:
            result.append([result[-1][2], sigma, ''])
            result[-2][2] = ''
        else:
            return None
    # ㄱ + ㅏ + ㄹ + sigma
    elif q == 'q13':
        if sigma in ['1', 'a', 'w']:
            result[-1][2] += sigma
        elif sigma in key_consonant:
            result.append([sigma, '', ''])
        elif sigma in key_vowel:
            result.append([result[-1][2], sigma, ''])
            result[-2][2] = ''
        else:
            return None
    # ㄱ + ㅏ + ㅇ + sigma
    elif q == 'q14':
        if sigma in ['z']:
            result[-1][2] += sigma
        elif sigma in key_consonant:
            result.append([sigma, '', ''])
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
        elif sigma in key_consonant:
            result.append([sigma, '', ''])
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
        elif sigma == '3':
            result.append(['', sigma, ''])
        else:
            return None
    # ㄱ + ㅏ + ㄱ + ㅅ + sigma, 그 외에 두가지 경우가 더 있다.
    elif q == 'q17':
        if sigma in key_consonant:
            result.append([sigma, '', ''])
        elif sigma in key_vowel:
            # 만약 두번째 받침이 획추가나 쌍자음이 된 상태라면?
            result.append([result[-1][2][-1], sigma, ''])
            result[-2][2] = result[-2][2][:-1]
        elif sigma == 'z':
            # 획추가한 결과가 겹받침으로 유효하면?
            if (result[-1][2] + sigma) in jong_double:
                result[-1][2] += sigma
            # 그렇지 않으면?
            else:
                result.append([result[-1][2][-1] + sigma, '', ''])
                result[-2][2] = result[-2][2][:-1]
        elif sigma == 'c':
            result.append([result[-1][2][-1]+sigma, '', ''])
            result[-2][2] = result[-2][2][:-1]
    # ㄱ + ㅏ + ㄱ + 쌍 + sigma == ㄱ + ㅏ + ㄲ + sigma
    elif q == 'q18':
        if result[-1][1] == '' and result[-1][2] == '':
            if sigma in key_vowel:
                result[-1][1] = sigma
            else:
                return None
        else:
            if sigma in key_consonant:
                result.append([sigma, '', ''])
            elif sigma in key_vowel:
                result.append([result[-1][2], sigma, ''])
                result[-2][2] = ''
            else:
                return None
    # ㄱ + ㅏ + ㄴ + ㅅ + sigma
    elif q == 'q19':
        if sigma in key_vowel:
            result[-1][1] = sigma
        elif sigma == 'z':
            result[-2][2] += result[-1][0]+sigma
            result.pop()
        elif sigma == 'c':
            result[-1][0] += sigma
        else:
            return None
    # ㄱ + ㅏ + ㄴ + ㅇ + sigma
    elif q == 'q20':
        if sigma in key_vowel:
            result[-1][1] = sigma
        elif sigma == 'z':
            result[-2][2] += result[-1][0]+sigma
            result.pop()
        else:
            return None
    # ㄱ + ㅏ + ㄴ + 획 + sigma == ㄱ + ㅏ + ㄷ + sigma
    elif q == 'q21':
        if sigma in key_consonant:
            result.append([sigma, '', ''])
        elif sigma in key_vowel:
            result.append([result[-1][2], sigma, ''])
            result[-2][2] = ''
        elif sigma == 'z':
            result[-1][2] += sigma
        elif sigma == 'c':
            result.append([result[-1][2] + sigma, '', ''])
            result[-2][2] = ''
        else:
            return None
    # ㄱ + ㅏ + ㅅ + 획 + sigma == ㄱ + ㅏ + ㅈ + sigma , 21인 경우와 합쳐도 될 거 같다. 만약 여기에 추가할 분기가 없다면
    elif q == 'q22':
        if sigma in key_consonant:
            result.append([sigma, '', ''])
        elif sigma in key_vowel:
            result.append([result[-1][2], sigma, ''])
            result[-2][2] = ''
        elif sigma == 'z':
            result[-1][0] += sigma
        elif sigma == 'c':
            result.append([result[-1][2]+sigma, '', ''])
            result[-2][2] = ''
        else:
            return None
    # ㄱ + ㅏ + ㄹ + ㄱ + sigma == ㄱ + ㅏ + ㄺ + sigma
    elif q == 'q23':
        if sigma in key_consonant:
            result.append([sigma, '', ''])
        elif sigma in key_vowel:
            # 이거랑 비슷한 부분에 코멘트 해놓은 거랑 같은 문제가 발생?
            result.append([result[-1][2][-1], sigma, ''])
            result[-2][2] = result[-2][2][:-1]
        elif sigma in key_special:
            result.append([result[-1][2][-1]+sigma, '', ''])
            result[-2][2] = result[-2][2][:-1]
        else:
            return None
    # ㄱ + ㅏ + ㄹ + ㄴ + sigma
    elif q == 'q24':
        if sigma in key_vowel:
            result[-1][1] = sigma
        elif sigma == 'z':
            result[-2][2] += result[-1][0]+sigma
            result.pop()
        else:
            return None
    # ㄱ + ㅏ + ㄹ + ㅁ + sigma == ㄱ + ㅏ + ㄻ + sigma
    elif q == 'q25':
        if sigma in key_consonant:
            result.append([sigma, '', ''])
        elif sigma in key_vowel:
            # 이거랑 비슷한 부분에 코멘트 해놓은 거랑 같은 문제가 발생?
            result.append([result[-1][2][-1], sigma, ''])
            result[-2][2] = result[-2][2][:-1]
        elif sigma == 'z':
            result[-1][2] += sigma
        elif sigma == 'c':
            result.append([result[-1][2] + sigma, '', ''])
            result[-2][2] = result[-2][2][:-1]
        else:
            return None
    # ㄱ + ㅏ + ㅁ + 획 + sigma == 갑 + sigma
    elif q == 'q26':
        if sigma in key_consonant:
            if sigma == 'a':
                result[-1][2] += sigma
            else:
                result.append([sigma, '', ''])
        elif sigma in key_vowel:
            result.append([result[-1][2], sigma, ''])
            result[-2][2] = ''
        elif sigma == 'z':
            result[-1][2] += sigma
        elif sigma == 'c':
            result.append([result[-1][2]+sigma, '', ''])
            result[-2][2] = ''
        else:
            return None
    # ㄱ + ㅗ + ㅗ + ㅏ + sigma == 구 + ㅏ + sigma, else가 무조건 none이 아니고 그냥 이상한 형태지만 입력이 될 수도 있을 것이다.
    elif q == 'q27':
        if sigma == '3':
            result[-2][1] += result[-1][1]+sigma
            result.pop()
        else:
            return None
    # ㄱ + ㅏ + ㄹ + ㄴ + 획 + sigma == 갈+ㄷ+sigma
    elif q == 'q28':
        if sigma in key_vowel:
            result[-1][1] = sigma
        elif sigma == 'z':
            result[-2][2] += result[-1][0]+sigma
            result.pop()
        elif sigma == 'c':
            result[-1][0] += sigma
        else:
            return None
    # Success
    return 0


def convert_to_kor(nara_char):
    kor_char = []
    if nara_char[0] == '' and nara_char[2] == '':
        kor_char = ['', jung[jung_key.index(nara_char[1])], '']
    elif nara_char[1] == '' and nara_char[2] == '':
        kor_char = [cho[cho_key.index(nara_char[0])], '', '']
    elif not nara_char[0] == '' and not nara_char[1] == '':
        kor_char.append(cho[cho_key.index(nara_char[0])])
        kor_char.append(jung[jung_key.index(nara_char[1])])
        kor_char.append(jong[jong_key.index(nara_char[2])])
    else:
        print('convert error')
    return kor_char


while True:
    print('Type hangul to get right result. Type invalid hangul or ; to exit')
    eng_in = input()

    eng_in_temp = []

    for i in range(len(eng_in)):
        eng_in_temp = eng_in[:i+1]
        current_state = 'q0'
        for letter in eng_in_temp:
            print(current_state, end=', ')
            action_func(current_state, letter)
            current_state = state_transition_func(current_state, letter)
        print('')
        print([convert_to_kor(x) for x in result])
        for geulja in result:
            if geulja[1] == '' and geulja[2] == '':
                pass
                print(cho[cho_key.index(geulja[0])], end='')
            elif geulja[0] == '' and geulja[2] == '':
                print(jung[jung_key.index(geulja[1])], end='')
            else:
                print(chr(44032 + 588 * cho_key.index(geulja[0]) + 28 * jung_key.index(geulja[1]) + jong_key.index(geulja[2])), end=''),
        print('')
        result = []
        incomplete = []
    # print('exit')
    # break
