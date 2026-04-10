# 균형잡힌 세상

data = []


while True:
    data = input()
    if data == '.':
        break

    stack = []
    result = 'yes'

    for i in data:
        # if data[-1] == '.':
        #     break

        if i == '(' or i == '[':
            stack.append(i)

        if i == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    result = 'no'
                    break
            else:
                result = 'no'
                break
        elif i == ']':
            if stack:  
                if stack[-1] == '[':
                    stack.pop()
                else:
                    result = 'no'
                    break
            else:
                result = 'no'
                break
        # elif not stack:
        #     result = 'yes'
        # else:
        #     result = 'no'
        #     break

        # if stack[-1] == ']' or stack[-1] == ')':
        #     result = 'no'
        #     break

        if i == '.':
            break

    if stack:
        result = 'no'
    print(result)