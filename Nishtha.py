import re
def main():
    print("Enter the two names:")
    name1=input()
    name2=input()
    result=check_love(name1,name2)
    print(result)


















def check_love(name1,name2):
    result = 'I am not sure if '+name1+ ' and '+ name2+ ' like each other.'
    if check_name_kittu(name1):
        if check_name_cheeku(name2):
            result='Congratulations '+name1+' and '+name2+' form a very great pair!!!!!\nHappy Valentines Day to both of you guys.'
    elif check_name_cheeku(name1):
        if check_name_kittu(name2):
            result = 'Congratulations '+ name1+ ' and '+ name2+ ' form a very great pair!!!!!'
    return result


def check_name_kittu(name):
    st=name.lower()
    pat=re.compile('[nishtha|nishi|cheittu|kittu|nishu|marie]')
    mo=re.search(pat,st)
    if mo:
        return True
    else:
        return False


def check_name_cheeku(name):
    st=name.lower()
    pat=re.compile('[cheeku|alankrit|alanku|cheittu|bandar|gadha|]')
    mo=re.search(pat,st)
    if mo:
        return True
    else:
        return False


if __name__=='__main__':
    main()