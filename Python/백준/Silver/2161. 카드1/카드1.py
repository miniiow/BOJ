# 카드 1

from collections import deque
queue = deque()
N = int(input())
count = 1

for i in range(1, N+1):
    queue.append(i)

# print(queue.popleft())
while len(queue) > 1:
    print(queue.popleft(), end=' ')
    count += 1
    if count <= 2:
        card = queue.popleft()
        queue.append(card)
        count = 1
    # else:
    #     # print(card, end=' ')
    #     count = 1
print(queue.popleft())