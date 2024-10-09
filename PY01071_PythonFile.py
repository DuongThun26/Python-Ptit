def check(s):
    if len(s) < 1 or len(s) > 128: return False
    for i in s:
        if (i >= 'a' and i <= 'z') or(i >= 'A' and i <= 'Z') or(i == '.') or i == '_':
            continue
        else:
            return False
    return True
a = input()
s = a[-3:]
if check(a) and s.lower() == ".py":
    print('yes')
else:
    print('no')