def checkRight(u): #올바른 괄호인지 확인
    stack = 0

    for st in u:
        if st == '(':
            stack += 1
        else:
            stack -= 1
            
        if stack < 0 :#스택에 )가 새로 들어온 순간종료 - 올바르지 않은 괄호
            return False
    return True

def makeReverse(u):
    reverse = ''
    u = u[1:-1]#맨 앞뒤 문자제거
    
    for i in u:
        if i == '(':
            reverse += ')'
        else:
            reverse += '('
    
    return reverse

def divide(p):
    count = 1
    for i in range(1,len(p)):
        if p[0] == p[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            u = p[:i+1]
            v = p[i+1:]
            break
    return u,v
    
def solution(p):
    if p == '':
        return p
    
    u,v = divide(p)
    
    if (checkRight(u)):             #u가 "올바른 괄호 문자열" -> v에 대해 재귀적으로 수행
        return u+solution(v)
    else:                           #u가 "올바른 괄호 문자열"이 아닐 때
        return '('+solution(v)+')'+makeReverse(u)