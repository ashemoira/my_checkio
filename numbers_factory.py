# 回文が存在するか、また存在する場合回文を出力する
"""
case1: artrartrt
case2: abacaba
case3: aaaa
"""
def test(x):
    xb = x
    set = [2,3,4,5,6,7,8,9]
    index = len(set) - 1
    result = []
    while index >= -1:
        if xb % set[index] == 0:
            result.insert(0, set[index])
            xb = xb / set[index]
        else:
            index -= 1
    if int(xb) > 9:
        return 0
    return int(''.join(map(str, result)))


print(test(20))
print(test(21))
print(test(17))
print(test(33))
