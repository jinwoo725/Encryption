from secrets import randbelow

def miller_rabin(p):
    match p:
        case 0 | 1 | 4:
            return 0
        case 2 | 3:
            return 1

    d = p - 1
    s = 0

    while True:
        if d % 2 != 0:
            break
        d = d // 2
        s += 1

    for _ in range(64):
        a = 2 + randbelow(p - 3)
        v = pow(a, d, p)

        if v == p - 1 or v == 1:
            continue
        
        for _ in range(1, s):
            v = pow(v, 2, p)
            if v == p - 1:
                break
        else:
            return 0
        
    return 1