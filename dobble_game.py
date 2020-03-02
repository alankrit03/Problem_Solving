import string
import random
symbols=list(string.ascii_letters)
card1=[0]*5
card2=[0]*5
pos1=random.randint(0,5)
pos2=random.randint(0,5)
#pos1 and pos2 are same symbol position
same_symbol=random.choice(symbols)
symbols.remove(same_symbol)