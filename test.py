


han_list = [
    'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
]

unit_list = ['hundred', 'thousand', 'million', 'billion']

def digit(num) :
    integer = int(num)
    return round((num - integer) * 100)

number_list = list(" 一二三四五六七八九")
unit_list = list("十 百 千 万".split(" "))

print(unit_list)


def convert(num) :
    i = 0
    res = ""
    integer = int(num)
    while integer != 0 :

        num = integer % 10
        integer = integer // 10
        if i > 0 and num != 0:
            res = unit_list[i % 4  - 1] + res
        if i > 0 and (i + 1)% 9 == 0:
            res = "亿" + res[1:]
        if num != 0 :
            res = number_list[num] + res


        i += 1

    print(res)

convert(123450000000000)