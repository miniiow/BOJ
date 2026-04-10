# 괄호

turn = int(input())
stack = []
count = 0
for i in range(turn):
    stack = input()
    count = 0
    for j in range(len(stack)):
        if stack[j] == '(':
            count += 1
            # print(count)
        elif stack[j] == ')':
            count -= 1
            # print(count)

        if count < 0:
            print('NO')
            break

    if count == 0:
        print('YES')
    elif count > 0:
        print('NO')