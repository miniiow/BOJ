# 좋은 단어

turn = int(input())
count = 0
stack = []

for _ in range(turn):
    num = list(input())
    stack = []
    stack.append(num[0])
    for i in range(1, len(num)):
        if stack and stack[-1] == num[i]:
            stack.pop()
            # print(stack)
        else:
            stack.append(num[i])
            # print(stack)
    if not stack:
        count += 1
print(count)