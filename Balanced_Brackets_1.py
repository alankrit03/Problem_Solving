"""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Following Code contains only a single type of brackets
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""


def show_brackets(st, left, right):
    if left + right == 2 * n:
        print(st)
        return 0

    if left == right:
        show_brackets(st + '(', left + 1, right)

    else:
        if left == n:
            show_brackets(st + ')', left, right + 1)
        else:
            show_brackets(st + '(', left + 1, right)
            show_brackets(st + ')', left, right + 1)


n = int(input())
str1 = ''
show_brackets(str1, 0, 0)
