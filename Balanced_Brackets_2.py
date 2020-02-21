"""''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Following Code contains 2 types of brackets.
1st bracket = ()
2nd bracket = {}
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""

def display_brackets(st, l1, r1, l2, r2, stack):

    if l1 + r1 == 2 * n and l2 + r2 == 2 * m:
        # print(f'l1={l1} r1={r1} l2={l2} r2={r2}')
        print(st)
        return 0

    if l1 != n:
        stack.append('(')
        display_brackets(st + '(', l1 + 1, r1, l2, r2, stack[:])
        stack.pop()

    if l2 != m:
        stack.append('{')
        display_brackets(st + '{', l1, r1, l2 + 1, r2, stack[:])
        stack.pop()

    if stack and stack[-1] == '(':
        stack.pop()
        display_brackets(st + ')', l1, r1 + 1, l2, r2, stack[:])

    if stack and stack[-1] == '{':
        stack.pop()
        display_brackets(st + '}', l1, r1, l2, r2 + 1, stack[:])




n , m = map(int,input().split())
str1 = ''
display_brackets(str1, 0, 0, 0, 0, [])
