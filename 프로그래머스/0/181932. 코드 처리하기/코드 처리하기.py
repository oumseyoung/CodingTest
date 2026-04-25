def solution(code):
    mode = 0
    ret = ''
    for idx in range(len(code)):
        if mode == 0:
            if code[idx] == '1': mode = 1
            elif idx % 2 == 0: ret = ret + code[idx]
        else:
            if code[idx] == '1': mode = 0
            elif idx % 2: ret = ret + code[idx]
    if ret == '': return 'EMPTY'
    else: return ret