# 수들의 합2

N, M = map(int, input().split())
num_list = list(map(int, input().split()))

answer = 0
start = end = 0
sum = num_list[0]
while end < N:
    if sum == M :
        answer += 1
    if sum <= M:
        end += 1
        if end < N:
            sum += num_list[end]
    else:
        sum -= num_list[start]
        start += 1

print(answer)