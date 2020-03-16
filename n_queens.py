#Debugging needed

def initialise(n):
    for key in ['queen','row','col','nw_to_se','sw_to_ne']:
        board[key]={}
    for i in range(n):
        board['queen'][i]=-1
        board['row'][i]=0
        board['col'][i]=0
    for i in range(-(n-1),n):
        board['nw_to_se'][i]=0
    for i in range((2*n)-1):
        board['sw_to_ne'][i]=0
    print_full_board()
	
def printboard(): #Update this function asap
	for row in sorted(board['queen'].keys()):
		print(row,board['queen'][row])

def free(i,j):
	print('free checker',i,j)
	print_full_board()
	return (board['row'][i]==0 and board['col'][j]==0 and board['nw_to_se'][j-i]==0 and board['sw_to_ne'][j+i]==0)

def addqueen(i,j):
	board['queen'][i]=j
	board['row'][i]=1
	board['col'][i]=1
	board['nw_to_se'][j-i]=1
	board['sw_to_ne'][j+i]=1

def undoqueen(i,j):
	board['queen'][i]=-1
	board['row'][i]=0
	board['col'][i]=0
	board['nw_to_se'][j-i]=0
	board['sw_to_ne'][j+i]=0

def placequeen(i):
    n=len(board['queen'].keys())
    ext_coun=1
    for j in range(n):
        if free(i,j):
            addqueen(i,j)
            print('queen added at ',j)
            print('board after adding')
            print_full_board()
            if i==(n-1):
                return True
            else:
                extendsoln=placequeen(i+1)
            if extendsoln:
                print("extension no ",ext_coun)
                ext_coun+=1
                return True
            else:	
                print('undoing ',i,j)
                undoqueen(i,j)
    else:
        return False

def print_full_board():
    print()
    print("Current board")
    for x,y in board.items():
        print(x,'=',y)
    print()


board={}
n=int(input("How many queens? "))
initialise(n)
if placequeen(0):
	printboard()

#print('\n ',board)