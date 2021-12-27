"""
author : Park Min Hyeok
github : https://github.com/maprk
e-mail : alsgur9784@naver.com

title : 연구소3
description : 구현
"""

from collections import deque
import copy


def progress(N, board, virus):
    global dx, dy

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    copy_board = copy.deepcopy(board)
    queue = deque()
    visited = [[False for _ in range(N)] for _ in range(N)]

    for i in range(len(virus)):
        x, y = virus[i]
        queue.append([x, y, 0])
        copy_board[x][y] = 0
        visited[x][y] = True

    while queue:
        now_x, now_y, now_count = queue.popleft()

        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if copy_board[nx][ny] >= 0 and visited[nx][ny] is False:
                    if board[nx][ny] == 2:
                        copy_board[nx][ny] = -1
                    else:
                        copy_board[nx][ny] = now_count + 1

                    visited[nx][ny] = True
                    queue.append([nx, ny, now_count + 1])

    return check(copy_board, virus)


def check(copy_board, virus):
    min_time = 0

    for i in range(len(copy_board)):
        min_time = max(min_time, max(copy_board[i]))

        for j in range(len(copy_board[0])):
            if copy_board[i][j] != 0:
                continue

            if [i, j] not in virus:
                return int(1e9)

    return min_time


def recursive(N, M, board, virus_position, virus, start):
    global answer

    if len(virus) == M:
        answer = min(answer, progress(N, board, virus))
        return

    for i in range(start, len(virus_position)):
        if virus_position[i] not in virus:
            virus.append(virus_position[i])
            recursive(N, M, board, virus_position, virus, i + 1)
            virus.pop()


def solution(N, M, board, virus_position):
    global answer
    answer = int(1e9)

    recursive(N, M, board, virus_position, [], 0)

    if answer == int(1e9):
        answer = -1

    return answer


if __name__ == "__main__":
    N, M = map(int, input().split())
    board = []
    virus_position = []

    for i in range(N):
        temp = list(map(int, input().split()))

        for j in range(len(temp)):
            if temp[j] == 2:
                virus_position.append([i, j])
            elif temp[j] == 1:
                temp[j] = -1

        board.append(temp)

    print(solution(N, M, board, virus_position))
