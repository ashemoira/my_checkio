# 面積が最大の値を返す
"""
[5] == 5
[5, 3] == 6
[1, 1, 4, 1] == 4
[1, 1, 3, 1] == 4
[2, 1, 4, 5, 1, 3, 3] == 8
"""
def histogram(histogram):
    ma = 0
    mi = 0
    count = 0
    result = 0
    for x in histogram:
        if mi == 0 and ma == 0:
            mi = x
            ma = x
            result = x

        if x < mi:
            mi = x

        count += 1
        if ma >= x:
            if result < count * x:
                result = count * x
        else:
            if result < count * ma:
                result = count * ma
            count = 1
        ma = x
    if result < mi * len(histogram):
        return mi * len(histogram)
    else:
        return result

print(histogram([5]))
print(histogram([5, 3]))
print(histogram([1, 1, 4, 1]))
print(histogram([1, 1, 3, 1]))
print(histogram([2, 1, 4, 5, 1, 3, 3]))
