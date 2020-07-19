# Write your code here
X = 212072634227239451

if __name__ == "__main__":
    row, col = map(int,input().split())

    matrix = []
    for i in range(row):
        temp = input().split()
        for j in range(col):
            temp[i] = int(temp[i])
        matrix.append(temp)

    dp = [[0]*col for i in range(row)]

    if matrix[-1][-1] % X == 0:
        print(0)
        exit()
    else:
        dp[-1][-1] = 1

    """this loop is used to set the values for last column."""
    for i in range(row-2, -1, -1):
        if dp[i+1][col-1]==0 or (matrix[i+1][col-1] * matrix[i][j-1]) % X == 0:
            dp[i][col-1] = 0
            matrix[i][col-1] = X
        else:
            if X%matrix[i][col-1]==0 or X%matrix[i+1][col-1]==0:
                matrix[i][col - 1] *= matrix[i+1][col-1]
            dp[i][col - 1] = 1

    for j in range(col-2, -1, -1):
        if dp[row-1][j+1]==0 or (matrix[row-1][j+1] * matrix[row-1][j]) % X == 0:
            dp[row-1][j] = 0
            matrix[row-1][j] = X
        else:
            if X%matrix[row-1][j]==0 or X%matrix[row-1][j+1]==0:
                matrix[row-1][j] *= matrix[row-1][j+1]
            dp[row-1][j] = 1

    for i in range(row - 2, -1, -1):
        for j in range(col - 2, -1, -1):

            if X % matrix[i][j]:
                dp[i][j] = dp[i+1][j] + dp[i][j+1]
                matrix[i][j] = matrix[i+1][j] * matrix [i][j+1]
            else:
                if ((matrix[i][j]*matrix[i+1][j]) % X==0 and (matrix[i][j]*matrix[i][j+1]) % X == 0) or matrix[i][j] % X == 0 :
                    dp[i][j] = 0
                    matrix[i][j] = 1

                elif (matrix[i][j]*matrix[i+1][j]) % X==0 or (matrix[i][j]*matrix[i][j+1]) % X == 0:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1] - 1
                    matrix[i][j] = 1
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
                    matrix[i][j] *= matrix[i + 1][j] * matrix[i][j + 1]

    print(dp[0][0])



