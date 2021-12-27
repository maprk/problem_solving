"""
author : Park Min Hyeok
github : https://github.com/maprk
e-mail : alsgur9784@naver.com

title : 이차원 배열과 연산
description : 구현
"""

from collections import defaultdict


def R_operation(A):
    max_length = 0
    result = []

    for i in range(len(A)):
        number_dic = defaultdict(int)

        for j in range(len(A[0])):
            number = A[i][j]
            number_dic[number] += 1

        temp = []

        for key, value in sorted(number_dic.items(), key=lambda x: (x[1], x[0])):
            if key == 0:
                continue

            temp.append(key)
            temp.append(value)

        result.append(temp)
        max_length = max(max_length, len(temp))

    return make_R(result, max_length)


def C_operation(A):
    max_length = 0
    result = []

    for i in range(len(A[0])):
        number_dic = defaultdict(int)

        for j in range(len(A)):
            number = A[j][i]
            number_dic[number] += 1

        temp = []

        for key, value in sorted(number_dic.items(), key=lambda x: (x[1], x[0])):
            if key == 0:
                continue

            temp.append(key)
            temp.append(value)

        result.append(temp)
        max_length = max(max_length, len(temp))

    return make_C(result, max_length)


def make_R(array, max_length):
    if max_length > 100:
        max_length = 100

    result = [[0 for _ in range(max_length)] for _ in range(len(array))]

    for i in range(len(array)):
        length = len(array[i])

        if length > 100:
            length = 100

        for j in range(length):
            result[i][j] = array[i][j]

    return result


def make_C(array, max_length):
    if max_length > 100:
        max_length = 100

    result = [[0 for _ in range(len(array))] for _ in range(max_length)]

    for i in range(len(array)):
        length = len(array[i])

        if length > 100:
            length = 100

        for j in range(length):
            result[j][i] = array[i][j]

    return result


def check(r, c, k, A):
    if r - 1 < len(A) and c - 1 < len(A[0]):
        if A[r - 1][c - 1] == k:
            return True

    return False


def solution(r, c, k, A):
    time = 0

    while True:
        if check(r, c, k, A) is True:
            break

        if len(A) >= len(A[0]):
            A = R_operation(A)
        elif len(A) < len(A[0]):
            A = C_operation(A)

        time += 1

        if time == 100:
            return -1

    return time


if __name__ == "__main__":
    r, c, k = map(int, input().split())
    A = []

    for _ in range(3):
        A.append(list(map(int, input().split())))

    answer = solution(r, c, k, A)
    print(answer)
