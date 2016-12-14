# coding=utf-8
import traceback
state_transition_dict = ({
    'q19': {'c': 'q3', '3': 'q5', 'd': 'q6', 'x': 'q8', 'z': 'q23', 'e': 'q7'},
    'q22': {'2': 'q2', 'a': 'q2', 'w': 'q2', '1': 'q1', 'd': 'q6', 'x': 'q8', 's': 'q4', '3': 'q5', 'c': 'q3', 'q': 'q3', 'z': 'q18', 'e': 'q7'},
    'q9': {'2': 'q2', 'a': 'q17', 'w': 'q2', '1': 'q1', 'd': 'q6', 'x': 'q8', 's': 'q4', '3': 'q5', 'c': 'q18', 'q': 'q3', 'z': 'q18', 'e': 'q7'},
    'q17': {'c': 'q3', 'q': 'q3', '2': 'q2', 'a': 'q2', 'w': 'q2', '1': 'q1', '3': 'q5', 'd': 'q6', 'x': 'q8', 's': 'q4', 'z': 'q1', 'e': 'q7'},
    'q14': {'q': 'q3', '2': 'q2', 'a': 'q2', 'w': 'q2', '1': 'q1', '3': 'q5', 'd': 'q6', 'x': 'q8', 's': 'q4', 'z': 'q18', 'e': 'q7'},
    'q20': {'3': 'q5', 'd': 'q6', 'x': 'q8', 'z': 'q18', 'e': 'q7'},
    'q1': {'c': 'q3', '3': 'q5', 'd': 'q6', 'x': 'q8', 'z': 'q3', 'e': 'q7'},
    'q8': {'1': 'q9', '2': 'q10', 'a': 'q12', 'w': 'q15', 'q': 'q13', 'd': 'q6', 's': 'q14'},
    'q4': {'3': 'q5', 'd': 'q6', 'x': 'q8', 'z': 'q3', 'e': 'q7'},
    'q23': {'2': 'q2', 'a': 'q2', 'w': 'q2', '1': 'q1', 'd': 'q6', 'x': 'q8', 's': 'q4', '3': 'q5', 'c': 'q3', 'q': 'q3', 'z': 'q3', 'e': 'q7'},
    'q24': {'3': 'q5', 'd': 'q6', 'x': 'q8', 'z': 'q28', 'e': 'q7'},
    'q5': {'q': 'q13', '2': 'q10', 'a': 'q12', 'w': 'q15', '1': 'q9', '3': 'q11', 'd': 'q6', 's': 'q14', 'z': 'q8'},
    'q27': {'3': 'q8'},
    'q16': {'q': 'q13', '2': 'q10', 'a': 'q12', 'w': 'q15', '1': 'q9', '3': 'q27', 'd': 'q6', 's': 'q14', 'z': 'q6'},
    'q3': {'3': 'q5', 'd': 'q6', 'x': 'q8', 'e': 'q7'},
    'q7': {'q': 'q13', '2': 'q10', 'a': 'q12', 'w': 'q15', '1': 'q9', '3': 'q8', 'd': 'q6', 's': 'q14', 'z': 'q6', 'e':'q16'},
    'q10': {'q': 'q3', '2': 'q2', 'a': 'q19', 'w': 'q2', '1': 'q1', '3': 'q5', 'd': 'q6', 'x': 'q8', 's': 'q20', 'z': 'q21', 'e': 'q7'},
    'q12': {'2': 'q2', 'a': 'q2', 'w': 'q2', '1': 'q1', 'd': 'q6', 'x': 'q8', 's': 'q4', '3': 'q5', 'c': 'q18', 'q': 'q3', 'z': 'q22', 'e': 'q7'},
    'q18': {'q': 'q3', '2': 'q2', 'a': 'q2', 'w': 'q2', '1': 'q1', '3': 'q5', 'd': 'q6', 'x': 'q8', 's': 'q4', 'e': 'q7'},
    'q2': {'c': 'q3', '3': 'q5', 'd': 'q6', 'x': 'q8', 'z': 'q1', 'e': 'q7'},
    'q25': {'q': 'q3', '2': 'q2', 'a': 'q2', 'w': 'q2', '1': 'q1', '3': 'q5', 'd': 'q6', 'x': 'q8', 's': 'q4', 'z': 'q22', 'e': 'q7'},
    'q6': {'1': 'q9', '2': 'q10', 'a': 'q12', 'w': 'q15', 'q': 'q13', 's': 'q14'},
    'q13': {'q': 'q3', '2': 'q24', 'a': 'q17', 'w': 'q25', '1': 'q23', '3': 'q5', 'd': 'q6', 'x': 'q8', 's': 'q20', 'e': 'q7'},
    'q28': {'c': 'q3', '3': 'q5', 'd': 'q6', 'x': 'q8', 'z': 'q18', 'e': 'q7'},
    'q0': {'1': 'q1', '2': 'q2', 'a': 'q2','w': 'q2', 'q': 'q3', 's': 'q4'},
    'q15': {'q': 'q3', '2': 'q2', 'a': 'q2', 'w': 'q2', '1': 'q1', '3': 'q5', 'd': 'q6', 'x': 'q8', 's': 'q4', 'z': 'q26', 'e': 'q7'},
    'q26': {'2': 'q2', 'a': 'q17', 'w': 'q2', '1': 'q1', 'd': 'q6', 'x': 'q8', 's': 'q4', '3': 'q5', 'c': 'q3', 'q': 'q3', 'z': 'q18', 'e': 'q7'},
    'q21': {'2': 'q2', 'a': 'q2', 'w': 'q2', '1': 'q1', 'd': 'q6', 'x': 'q8', 's': 'q4', '3': 'q5', 'c': 'q18', 'q': 'q3', 'z': 'q18', 'e': 'q7'},
    'q11': {'1': 'q9', '2': 'q10', 'a': 'q12', 'w': 'q15', 'q': 'q13', 'd': 'q6', 's': 'q14', 'z': 'q8'}
})
key_consonant = ['1', '2', 'q', 'w', 'a', 's']
key_vowel = ['3', 'e', 'd', 'x']
key_special = ['z', 'c']
cho = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
cho_key = ['1', '1c', '2', '2z', '2zc', 'q', 'w', 'wz', 'wzc', 'a', 'ac', 's', 'az', 'azc', 'azz', '1z', '2zz', 'wzz', 'sz']

jung = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅗㅏ', 'ㅗㅐ', 'ㅗㅣ', 'ㅛ', 'ㅜ', 'ㅜㅓ', 'ㅜㅔ', 'ㅜㅣ', 'ㅠ', 'ㅡ', 'ㅡㅣ', 'ㅣ']
jung_key = ['3', '3d', '3z', '3zd', '33', '33d', '33z', '33zd', 'e', 'e3', 'e3d', 'ed', 'ez', 'ee', 'ee33', 'ee33d', 'eed', 'eez', 'x', 'xd', 'd']
jung_double = ['3d', '3zd', '33d', '33zd', 'e3', 'ed', 'ee33', 'eed', 'xd']
jung_double_first = ['3', '3z', '33', '33z', 'e', 'e', 'ee', 'ee', 'x']
jung_double_second = ['d', 'd', 'd', 'd', '3', 'd', '33', 'd', 'd']
jung_triple = ['e3d', 'ee33d']
jung_triple_first = ['e', 'ee']
jung_triple_second = ['3', '33']
jung_triple_third = ['d', 'd']

jong = ['', 'ㄱ', 'ㄲ', 'ㄱㅅ', 'ㄴ', 'ㄴㅈ', 'ㄴㅎ', 'ㄷ', 'ㄹ', 'ㄹㄱ', 'ㄹㅁ', 'ㄹㅂ', 'ㄹㅅ', 'ㄹㅌ', 'ㄹㅍ', 'ㄹㅎ', 'ㅁ', 'ㅂ', 'ㅂㅅ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
jong_key = ['', '1', '1c', '1a', '2', '2az', '2sz', '2z', 'q', 'q1', 'qw', 'qwz', 'qa', 'q2zz', 'qwzz', 'qsz', 'w', 'wz', 'wza', 'a', 'ac', 's', 'az', 'azz', '1z', '2zz', 'wzz', 'sz']
jong_double = ['1a', '2az', '2sz', 'q1', 'qw', 'qwz', 'qa', 'q2zz', 'qwzz', 'qsz', 'wza']
jong_double_first = ['1', '2', '2', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'wz']
jong_double_second = ['a', 'az', 'sz', '1', 'w', 'wz', 'a', '2zz', 'wzz', 'sz', 'a']
batchim_double = ['1a', '2az', '2sz', 'q1', 'qw', 'qwz', 'qa', 'q2zz', 'qwzz', 'qsz', 'wza', '1c', 'ac']
batchim_double_first = ['1', '2', '2', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'wz', '1', 'a']
batchim_double_second = ['a', 'az', 'sz', '1', 'w', 'wz', 'a', '2zz', 'wzz', 'sz', 'a', '1', 'a']

state = ['q0']
result = []
erased = 0
batchim = False
#batchim = True


def state_transition_func(q, sigma):
    global state, erased
    if sigma == '<':
        for k in range(erased):
            state.pop()
        return state[-1]
    else:
        # returns None if not found
        next_state = state_transition_dict[q].get(sigma)
        state.append(next_state)
        return next_state


# 받침우선
def action_func(q, sigma):
    global erased
    if sigma == '<':
        erased = 0
        # Initial state
        if q == 'q0':
            return None
        # 초성 ㄱ, ㄴ, ㅁ, ㅅ, ㄹ, ㅇ
        # ㄱ + ㅏ + ㄴ + ㅅ + sigma
        # ㄱ + ㅏ + ㄴ + ㅇ + sigma
        # ㄱ + ㅏ + ㄹ + ㄴ + sigma
        # ㄱ + ㅗ + ㅗ + ㅏ + sigma == 구 + ㅏ + sigma, else가 무조건 none이 아니고 그냥 이상한 형태지만 입력이 될 수도 있을 것이다.
        # ㄱ + ㅏ + ㄹ + ㄴ + 획 + sigma == 갈+ㄷ+sigma
        elif q in ['q1', 'q2', 'q3', 'q4', 'q19', 'q20', 'q24', 'q27', 'q28']:
            if 'c' in result[-1][0]:
                erased = 1
                result[-1][0] = result[-1][0][:-1]
            else:
                erased = len(result[-1][0])
                result.pop()
        # ㄱ + ㅏ + sigma
        # ㄱ + ㅣ + sigma
        # ㄱ + ㅗ + sigma
        # ㄱ + ㅡ + sigma
        # ㄱ + ㅏ + ㅏ + sigma == ㄱ + ㅓ + sigma
        # ㄱ + ㅗ + ㅗ + sigma == ㄱ + ㅜ + sigma
        elif q in ['q5', 'q6', 'q7', 'q8', 'q11', 'q16']:
            if result[-1][1] in jung_double:
                jung_first = jung_double_first[jung_double.index(result[-1][1])]
                jung_second = jung_double_second[jung_double.index(result[-1][1])]
                erased = len(jung_second)
                result[-1][1] = jung_first
            elif result[-1][1] in jung_triple:
                jung_first = jung_triple_first[jung_triple.index(result[-1][1])]
                jung_second = jung_triple_second[jung_triple.index(result[-1][1])]
                jung_third = jung_triple_third[jung_triple.index(result[-1][1])]
                erased = len(jung_third)
                result[-1][1] = jung_first + jung_second
            elif result[-1][1] in jung_key:
                erased = len(result[-1][1])
                result[-1][1] = ''
                if len(result) == 1:
                    pass
                elif result[-2][2]+result[-1][0] in jong_key:
                    result[-2][2] += result[-1][0]
                    result.pop()
        # 단일 받침
        # ㄱ + ㅏ + ㄱ + sigma
        # ㄱ + ㅏ + ㄴ + sigma
        # ㄱ + ㅏ + ㅅ + sigma
        # ㄱ + ㅏ + ㄹ + sigma
        # ㄱ + ㅏ + ㅇ + sigma
        # ㄱ + ㅏ + ㅁ + sigma
        # ㄱ + ㅏ + ㄴ + 획 + sigma == ㄱ + ㅏ + ㄷ + sigma
        # ㄱ + ㅏ + ㅁ + 획 + sigma == 갑 + sigma
        elif q in ['q9', 'q10', 'q12', 'q13', 'q14', 'q15', 'q21', 'q26']:
            erased = len(result[-1][2])
            result[-1][2] = ''

        # ㄱ + ㅏ + ㄱ + ㅅ + sigma, 그 외에 두가지 경우가 더 있다.
        # ㄱ + ㅏ + ㄹ + ㄱ + sigma == ㄱ + ㅏ + ㄺ + sigma
        # ㄱ + ㅏ + ㄹ + ㅁ + sigma == ㄱ + ㅏ + ㄻ + sigma
        elif q in ['q17', 'q23', 'q25']:
            batchim_first = batchim_double_first[batchim_double.index(result[-1][2])]
            batchim_second = batchim_double_second[batchim_double.index(result[-1][2])]
            erased = len(batchim_second)
            result[-1][2] = batchim_first
        # ㄱ + ㅏ + ㄱ + 쌍 + sigma == ㄱ + ㅏ + ㄲ + sigma
        elif q == 'q18':
            if result[-1][1] == '' and result[-1][2] == '':
                erased = 1
                result.pop()
            # 쌍자음 받침
            elif result[-1][2] in ['1c', 'ac']:
                batchim_first = batchim_double_first[batchim_double.index(result[-1][2])]
                batchim_second = batchim_double_second[batchim_double.index(result[-1][2])]
                erased = len(batchim_second)
                result[-1][2] = batchim_first
            # 겹받침
            elif result[-1][2] in jong_double:
                batchim_first = batchim_double_first[batchim_double.index(result[-1][2])]
                batchim_second = batchim_double_second[batchim_double.index(result[-1][2])]
                erased = len(batchim_second)
                result[-1][2] = batchim_first
            # 마지막 글자의 종성이 겹받침도 아니고 쌍자음도 아니다.
            elif result[-1][2] in jong_key:
                erased = len(result[-1][2])
                result[-1][2] = ''
            else:
                return None
        # ㄱ + ㅏ + ㅅ + 획 + sigma == ㄱ + ㅏ + ㅈ + sigma , 21인 경우와 합쳐도 될 거 같다. 만약 여기에 추가할 분기가 없다면. % 있어~
        elif q == 'q22':
            if result[-1][2] in jong_double:
                batchim_first = batchim_double_first[batchim_double.index(result[-1][2])]
                batchim_second = batchim_double_second[batchim_double.index(result[-1][2])]
                erased = len(batchim_second)
                result[-1][2] = batchim_first
            elif result[-1][2] in jong_key:
                erased = len(result[-1][2])
                result[-1][2] = ''
            else:
                return None
        # Success
        return 0
    else:
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
            if sigma in key_special:
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
                jong_first = jong_double_first[jong_double.index(result[-1][2])]
                jong_second = jong_double_second[jong_double.index(result[-1][2])]
                result.append([jong_second, sigma, ''])
                result[-2][2] = jong_first
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
            # 쌍자음 받침
            elif result[-1][2] in ['1c', 'ac']:
                if sigma in key_consonant:
                    result.append([sigma, '', ''])
                elif sigma in key_vowel:
                    result.append([result[-1][2], sigma, ''])
                    result[-2][2] = ''
                else:
                    return None
            # 겹받침
            elif result[-1][2] in jong_double:
                jong_double_idx = jong_double.index(result[-1][2])
                jong_first = jong_double_first[jong_double_idx]
                jong_second = jong_double_second[jong_double_idx]
                if sigma in key_consonant:
                    result.append([sigma, '', ''])
                elif sigma in key_vowel:
                    result.append([jong_second, sigma, ''])
                    result[-2][2] = jong_first
                elif sigma == 'z':
                    if result[-1][2]+sigma in jong_double:
                        result[-1][2] += sigma
                    elif jong_second+sigma in cho_key:
                        result.append([jong_second+sigma, '', ''])
                        result[-2][2] = jong_first
                    else:
                        return None
                # sigma is c(쌍자음)
                else:
                    if jong_second+sigma in cho_key:
                        result.append([jong_second + sigma, '', ''])
                        result[-2][2] = jong_first
                    else:
                        return None
            # 마지막 글자의 종성이 겹받침도 아니고 쌍자음도 아니다.
            elif result[-1][2] in jong_key:
                if sigma in key_vowel:
                    result.append([result[-1][2], sigma, ''])
                    result[-2][2] = ''
                elif sigma in key_consonant:
                    result.append([sigma, '', ''])
                elif sigma in key_special:
                    if result[-1][2]+sigma in jong_key:
                        result[-1][2] += sigma
                    else:
                        result.append([result[-1][2]+sigma, '', ''])
                        result[-2][2] = ''
                else:
                    return None
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
        # ㄱ + ㅏ + ㅅ + 획 + sigma == ㄱ + ㅏ + ㅈ + sigma , 21인 경우와 합쳐도 될 거 같다. 만약 여기에 추가할 분기가 없다면. % 있어~
        elif q == 'q22':
            if result[-1][2] in jong_double:
                jong_first = jong_double_first[jong_double.index(result[-1][2])]
                jong_second = jong_double_second[jong_double.index(result[-1][2])]
                if sigma in key_consonant:
                    result.append([sigma, '', ''])
                elif sigma in key_vowel:
                    result.append([jong_second, sigma, ''])
                    result[-2][2] = jong_first
                elif sigma == 'z':
                    result[-1][0] += sigma
                elif sigma == 'c':
                    result.append([jong_second + sigma, '', ''])
                    result[-2][2] = jong_first
                else:
                    return None
            elif result[-1][2] in jong_key:
                if sigma in key_consonant:
                    result.append([sigma, '', ''])
                elif sigma in key_vowel:
                    result.append([result[-1][2], sigma, ''])
                    result[-2][2] = ''
                elif sigma == 'z':
                    result[-1][0] += sigma
                elif sigma == 'c':
                    result.append([result[-1][2] + sigma, '', ''])
                    result[-2][2] = ''
                else:
                    return None
            else:
                return None
        # ㄱ + ㅏ + ㄹ + ㄱ + sigma == ㄱ + ㅏ + ㄺ + sigma
        elif q == 'q23':
            jong_first = jong_double_first[jong_double.index(result[-1][2])]
            jong_second = jong_double_second[jong_double.index(result[-1][2])]
            if sigma in key_consonant:
                result.append([sigma, '', ''])
            elif sigma in key_vowel:
                # 이거랑 비슷한 부분에 코멘트 해놓은 거랑 같은 문제가 발생?
                result.append([jong_second, sigma, ''])
                result[-2][2] = jong_first
            elif sigma in key_special:
                result.append([jong_second+sigma, '', ''])
                result[-2][2] = jong_first
            else:
                return None
        # ㄱ + ㅏ + ㄹ + ㄴ + sigma
        elif q == 'q24':
            if sigma in key_vowel:
                result[-1][1] = sigma
            elif sigma == 'z':
                result[-1][0] += sigma
            else:
                return None
        # ㄱ + ㅏ + ㄹ + ㅁ + sigma == ㄱ + ㅏ + ㄻ + sigma
        elif q == 'q25':
            if sigma in key_consonant:
                result.append([sigma, '', ''])
            elif sigma in key_vowel:
                # 이거랑 비슷한 부분에 코멘트 해놓은 거랑 같은 문제가 발생?
                jong_first = jong_double_first[jong_double.index(result[-1][2])]
                jong_second = jong_double_second[jong_double.index(result[-1][2])]
                result.append([jong_second, sigma, ''])
                result[-2][2] = jong_first
            elif sigma == 'z':
                result[-1][2] += sigma
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


def action_func_chosung(q, sigma):
    global erased
    if sigma == '<':
        erased = 0
        # Initial state
        if q == 'q0':
            return None
        # 초성 ㄱ, ㄴ, ㅁ, ㅅ, ㄹ, ㅇ
        # ㄱ + ㅏ + ㄴ + ㅅ + sigma
        # ㄱ + ㅏ + ㄴ + ㅇ + sigma
        # ㄱ + ㅏ + ㄹ + ㄴ + sigma
        # ㄱ + ㅗ + ㅗ + ㅏ + sigma == 구 + ㅏ + sigma, else가 무조건 none이 아니고 그냥 이상한 형태지만 입력이 될 수도 있을 것이다.
        # ㄱ + ㅏ + ㄹ + ㄴ + 획 + sigma == 갈+ㄷ+sigma
        elif q in ['q1', 'q2', 'q3', 'q4', 'q19', 'q20', 'q24', 'q27', 'q28']:
            if 'c' in result[-1][0]:
                erased = 1
                result[-1][0] = result[-1][0][:-1]
            else:
                erased = len(result[-1][0])
                result.pop()
                if result == []:
                    pass
                elif result[-1][2] in jong_double:
                    jong_first = jong_double_first[jong_double.index(result[-1][2])]
                    jong_second = jong_double_second[jong_double.index(result[-1][2])]
                    result[-1][2] = jong_first
                    result.append([jong_second, '', ''])
                elif result[-1][2] in jong_key:
                    result.append([result[-1][2], '', ''])
                    result[-2][2] = ''
                else:
                    return None

        # ㄱ + ㅏ + sigma
        # ㄱ + ㅣ + sigma
        # ㄱ + ㅗ + sigma
        # ㄱ + ㅡ + sigma
        # ㄱ + ㅏ + ㅏ + sigma == ㄱ + ㅓ + sigma
        # ㄱ + ㅗ + ㅗ + sigma == ㄱ + ㅜ + sigma
        elif q in ['q5', 'q6', 'q7', 'q8', 'q11', 'q16']:
            if result[-1][1] in jung_double:
                jung_first = jung_double_first[jung_double.index(result[-1][1])]
                jung_second = jung_double_second[jung_double.index(result[-1][1])]
                erased = len(jung_second)
                result[-1][1] = jung_first
            elif result[-1][1] in jung_triple:
                jung_first = jung_triple_first[jung_triple.index(result[-1][1])]
                jung_second = jung_triple_second[jung_triple.index(result[-1][1])]
                jung_third = jung_triple_third[jung_triple.index(result[-1][1])]
                erased = len(jung_third)
                result[-1][1] = jung_first + jung_second
            elif result[-1][1] in jung_key:
                erased = len(result[-1][1])
                result[-1][1] = ''
        # 단일 받침
        # ㄱ + ㅏ + ㄱ + sigma
        # ㄱ + ㅏ + ㄴ + sigma
        # ㄱ + ㅏ + ㅅ + sigma
        # ㄱ + ㅏ + ㄹ + sigma
        # ㄱ + ㅏ + ㅇ + sigma
        # ㄱ + ㅏ + ㅁ + sigma
        # ㄱ + ㅏ + ㄴ + 획 + sigma == ㄱ + ㅏ + ㄷ + sigma
        # ㄱ + ㅏ + ㅁ + 획 + sigma == 갑 + sigma
        elif q in ['q9', 'q10', 'q12', 'q13', 'q14', 'q15', 'q21', 'q26']:
            if 'c' in result[-1][0]:
                erased = 1
                result[-1][0] = result[-1][0][:-1]
            else:
                erased = len(result[-1][0])
                result.pop()

        # ㄱ + ㅏ + ㄱ + ㅅ + sigma, 그 외에 두가지 경우가 더 있다.
        # ㄱ + ㅏ + ㄹ + ㄱ + sigma == ㄱ + ㅏ + ㄺ + sigma
        # ㄱ + ㅏ + ㄹ + ㅁ + sigma == ㄱ + ㅏ + ㄻ + sigma
        elif q in ['q17', 'q23', 'q25']:
            if 'c' in result[-1][0]:
                erased = 1
                result[-1][0] = result[-1][0][:-1]
            else:
                erased = len(result[-1][0])
                result[-1][0] = result[-2][2]
                result[-2][2] = ''
        # ㄱ + ㅏ + ㄱ + 쌍 + sigma == ㄱ + ㅏ + ㄲ + sigma
        # ㄱ + ㅏ + ㅅ + 획 + sigma == ㄱ + ㅏ + ㅈ + sigma , 21인 경우와 합쳐도 될 거 같다. 만약 여기에 추가할 분기가 없다면. % 있어~
        elif q in ['q18', 'q22']:
            if 'c' in result[-1][0]:
                erased = 1
                result[-1][0] = result[-1][0][:-1]
            elif result[-2][2] == '':
                erased = len(result[-1][0])
                result.pop()
            elif result[-2][2] in jong_double:
                jong_first = jong_double_first[jong_double.index(result[-2][2])]
                jong_second = jong_double_second[jong_double.index(result[-2][2])]
                erased = len(result[-1][0])
                result[-2][2] = jong_first
                result[-1][0] = jong_second
            elif result[-2][2] in jong_key:
                erased = len(result[-1][0])
                result[-1][0] = result[-2][2]
                result[-2][2] = ''
            else:
                return None
    else:
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
                result.append([sigma, '', ''])
            elif sigma in ['3', 'd', 'z']:
                result[-1][1] += sigma
            else:
                return None
        # ㄱ + ㅣ + sigma
        elif q == 'q6':
            if sigma in key_consonant:
                result.append([sigma, '', ''])
            else:
                return None
        # ㄱ + ㅗ + sigma
        elif q == 'q7':
            if sigma in key_consonant:
                result.append([sigma, '', ''])
            elif sigma in ['3', 'e', 'd', 'z']:
                result[-1][1] += sigma
            else:
                return None
        # ㄱ + ㅡ + sigma
        elif q == 'q8':
            if sigma in key_consonant:
                result.append([sigma, '', ''])
            elif sigma == 'd':
                result[-1][1] += sigma
            else:
                return None
        # ㄱ + ㅏ + ㄱ + sigma
        elif q == 'q9':
            if sigma == 'a':
                result[-2][2] = result[-1][0]
                result[-1][0] = sigma
            elif sigma in key_consonant:
                result[-2][2] = result[-1][0]
                result[-1][0] = sigma
            elif sigma in ['z', 'c']:
                result[-1][0] += sigma
            elif sigma in key_vowel:
                result[-1][1] = sigma
            else:
                return None
        # ㄱ + ㅏ + ㄴ + sigma
        elif q == 'q10':
            if sigma in key_special:
                result[-1][0] += sigma
            elif sigma in key_consonant:
                result[-2][2] = result[-1][0]
                result[-1][0] = sigma
            elif sigma in key_vowel:
                result[-1][1] = sigma
            else:
                return None
        # ㄱ + ㅏ + ㅏ + sigma == ㄱ + ㅓ + sigma
        elif q == 'q11':
            if sigma in key_consonant:
                result.append([sigma, '', ''])
            elif sigma in ['d', 'z']:
                result[-1][1] += sigma
            else:
                return None
        # ㄱ + ㅏ + ㅅ + sigma
        elif q == 'q12':
            if sigma in ['z', 'c']:
                result[-1][0] += sigma
            elif sigma in key_consonant:
                result[-2][2] = result[-1][0]
                result[-1][0] = sigma
            elif sigma in key_vowel:
                result[-1][1] = sigma
            else:
                return None
        # ㄱ + ㅏ + ㄹ + sigma
        elif q == 'q13':
            if sigma in ['1', 'a', 'w']:
                result[-2][2] = result[-1][0]
                result[-1][0] = sigma
            elif sigma in key_consonant:
                result[-2][2] = result[-1][0]
                result[-1][0] = sigma
            elif sigma in key_vowel:
                result[-1][1] = sigma
            else:
                return None
        # ㄱ + ㅏ + ㅇ + sigma
        elif q == 'q14':
            if sigma in ['z']:
                result[-1][0] += sigma
            elif sigma in key_consonant:
                result[-2][2] = result[-1][0]
                result[-1][0] = sigma
            elif sigma in key_vowel:
                result[-1][1] = sigma
            else:
                return None
        # ㄱ + ㅏ + ㅁ + sigma
        elif q == 'q15':
            if sigma in key_vowel:
                result[-1][1] = sigma
            elif sigma in key_consonant:
                result[-2][2] = result[-1][0]
                result[-1][0] = sigma
            elif sigma in ['z']:
                result[-1][0] += sigma
            else:
                return None
        # ㄱ + ㅗ + ㅗ + sigma == ㄱ + ㅜ + sigma
        elif q == 'q16':
            if sigma in key_consonant:
                result.append([sigma, '', ''])
            elif sigma in ['d', 'z']:
                result[-1][1] += sigma
            elif sigma == '3':
                result.append(['', sigma, ''])
            else:
                return None
        # ㄱ + ㅏ + ㄱ + ㅅ + sigma, 그 외에 두가지 경우가 더 있다.
        elif q == 'q17':
            if sigma in key_consonant:
                result[-2][2] += result[-1][0]
                result[-1][0] = sigma
            elif sigma in key_vowel:
                result[-1][1] = sigma
            elif sigma in ['z', 'c']:
                result[-1][0] += sigma
        # ㄱ + ㅏ + ㄱ + 쌍 + sigma == ㄱ + ㅏ + ㄲ + sigma
        elif q == 'q18':
            # 쌍자음 안받침
            if result[-1][1] == '' and result[-1][2] == '' and not result[-1][0] in jong_key:
                if sigma in key_vowel:
                    result[-1][1] = sigma
                else:
                    return None
            # 쌍자음 받침
            elif result[-1][2] in ['1c', 'ac']:
                if sigma in key_consonant:
                    result[-2][2] = result[-1][0]
                    result[-1][0] = sigma
                elif sigma in key_vowel:
                    result[-1][1] = sigma
                else:
                    return None
            # 겹받침
            elif result[-2][2]+result[-1][0] in jong_double:
                if sigma in key_consonant:
                    result[-2][2] += result[-1][0]
                    result[-1][0] = sigma
                elif sigma in key_vowel:
                    result[-1][1] = sigma
                # sigma is special key
                elif sigma in key_special:
                    result[-1][0] += sigma
                else:
                    return None
            # 마지막 글자의 종성이 겹받침도 아니고 쌍자음도 아니다.
            elif result[-1][0] in jong_key:
                if sigma in key_vowel:
                    result[-1][1] = sigma
                elif sigma in key_consonant:
                    result[-2][2] = result[-1][0]
                    result[-1][0] = sigma
                elif sigma in key_special:
                    result[-1][0] += sigma
                else:
                    return None
            else:
                return None
        # ㄱ + ㅏ + ㄴ + ㅅ + sigma
        elif q == 'q19':
            if sigma in key_vowel:
                result[-1][1] = sigma
            elif sigma in key_special:
                result[-1][0] += sigma
            else:
                return None
        # ㄱ + ㅏ + ㄴ + ㅇ + sigma
        elif q == 'q20':
            if sigma in key_vowel:
                result[-1][1] = sigma
            elif sigma == 'z':
                result[-1][0] += sigma
            else:
                return None
        # ㄱ + ㅏ + ㄴ + 획 + sigma == ㄱ + ㅏ + ㄷ + sigma
        elif q == 'q21':
            if sigma in key_consonant:
                result[-2][2] = result[-1][0]
                result[-1][0] = sigma
            elif sigma in key_vowel:
                result[-1][1] = sigma
            elif sigma in key_special:
                result[-1][0] += sigma
            else:
                return None
        # ㄱ + ㅏ + ㅅ + 획 + sigma == ㄱ + ㅏ + ㅈ + sigma , 21인 경우와 합쳐도 될 거 같다. 만약 여기에 추가할 분기가 없다면. % 있어~
        elif q == 'q22':
            if result[-2][2]+result[-1][0] in jong_double:
                if sigma in key_consonant:
                    result[-2][2] += result[-1][0]
                    result[-1][0] = sigma
                elif sigma in key_vowel:
                    result[-1][1] = sigma
                elif sigma in key_special:
                    result[-1][0] += sigma
                else:
                    return None
            elif result[-1][0] in jong_key:
                if sigma in key_consonant:
                    result[-2][2] = result[-1][0]
                    result[-1][0] = sigma
                elif sigma in key_vowel:
                    result[-1][1] = sigma
                elif sigma in key_special:
                    result[-1][0] += sigma
                else:
                    return None
            else:
                return None
        # ㄱ + ㅏ + ㄹ + ㄱ + sigma == ㄱ + ㅏ + ㄺ + sigma
        elif q == 'q23':
            if sigma in key_consonant:
                result[-2][2] += result[-1][0]
                result[-1][0] = sigma
            elif sigma in key_vowel:
                result[-1][1] = sigma
            elif sigma in key_special:
                result[-1][0] += sigma
            else:
                return None
        # ㄱ + ㅏ + ㄹ + ㄴ + sigma
        elif q == 'q24':
            if sigma in key_vowel:
                result[-1][1] = sigma
            elif sigma == 'z':
                result[-1][0] += sigma
            else:
                return None
        # ㄱ + ㅏ + ㄹ + ㅁ + sigma == ㄱ + ㅏ + ㄻ + sigma
        elif q == 'q25':
            if sigma in key_consonant:
                result[-2][2] += result[-1][0]
                result[-1][0] = sigma
            elif sigma in key_vowel:
                result[-1][1] = sigma
            elif sigma == 'z':
                result[-1][0] += sigma
            else:
                return None
        # ㄱ + ㅏ + ㅁ + 획 + sigma == 갑 + sigma
        elif q == 'q26':
            if sigma in key_consonant:
                result[-2][2] = result[-1][0]
                result[-1][0] = sigma
            elif sigma in key_vowel:
                result[-1][1] = sigma
            elif sigma in key_special:
                result[-1][0] += sigma
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
            elif sigma in key_special:
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
    print('Type hangul to get right result. Type "exit" to exit')
    eng_in = input()
    if eng_in == 'exit':
        break
    eng_in_temp = []
    # DEBUG
    for i in range(len(eng_in)):
    # SUBMISSION
    # for i in range(len(eng_in)-1, len(eng_in)):
        eng_in_temp = eng_in[:i+1]
        current_state = 'q0'
        for letter in eng_in_temp:
            print(current_state, end=', ')
            # print(state[-5:], end=' | ')
            if batchim:
                action_func(current_state, letter)
            else:
                action_func_chosung(current_state, letter)
            current_state = state_transition_func(current_state, letter)
        print('')
        print(result, end=' vs ')
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
        state = ['q0']
        incomplete = []
    # print('exit')
    # break
