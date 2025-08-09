def Valid_Word_Substitution(s):
    stack=[]

    for i in s:
        if i=='c':
            if len(stack)>=2 and stack[-1]=='b' and stack[-2]=='a':
                stack.pop()
                stack.pop()
            else:
                return False
        else:
            stack.append(i)

    return len(stack)==0

sample="ababcc"
print(Valid_Word_Substitution(sample))