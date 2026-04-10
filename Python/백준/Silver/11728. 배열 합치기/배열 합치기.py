# 배열 합치기

N, M = map(int, input().split())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))
pA = pB = 0
merged_list = []

while pA < N and pB < M:
    if A_list[pA] < B_list[pB]:
        merged_list.append(A_list[pA])
        pA += 1
    else:
        merged_list.append(B_list[pB])
        pB += 1

while pA < N:
    merged_list.append(A_list[pA])
    pA += 1

while pB < M:
    merged_list.append(B_list[pB])
    pB += 1

for i in merged_list:
    print(i, end=' ')