def brackets(line):
    from collections import deque
    dq = deque()
    for bracket in line:
        if bracket == "(":
            dq.append(bracket)
        elif bracket == ")":
            if len(dq) != 0:
                dq.pop()
            else:
                dq.append(bracket)
    if len(dq)==0:
        return True
    else: 
        return False
    
print(brackets(")"))