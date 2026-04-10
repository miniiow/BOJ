# 약수 구하기

N, K = map(int, input().split())
result = []

for i in range(1, N+1):
    if N%i == 0:
        result.append(i)
        # print(result)
if K-1 >= len(result):
    print(0)
else:
    print(result[K-1])