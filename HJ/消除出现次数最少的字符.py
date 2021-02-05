# -*- coding: utf-8 -*-
def removeLeastFreStr(params_str=None):
    """ 计数
    输入1: “abbbcdc”
    输出1: “bbbcc”
    输入2: “aabbcc”
    输出2: “”
    """
    # params_str = input().strip().lower()
    list_ = list(params_str)

    dic = {}
    for i in list_:
        if dic.get(i, None) is None:
            dic[i] = 1
        else:
            dic[i] += 1

    print(min(dic.values()))
    least_fre = min(dic.values())
    for k, v in dic.items():
        if v == least_fre:
            params_str = params_str.replace(k, '')

    return params_str


if __name__ == '__main__':
    a = 'abbbcdc'
    print(removeLeastFreStr(a))

    a = 'aabbcc'
    print(removeLeastFreStr(a))

    a = 'ccabbacdyyyd'
    print(removeLeastFreStr(a))
