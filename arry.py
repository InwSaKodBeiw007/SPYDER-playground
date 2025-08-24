#%%

n = 4
matrix = [[0]*n for _ in range(n)]
num = 1

for diag in range(2*n-1):
    if diag % 2 == 0 and diag != 0:
        for i in range(n):
            thisistheMAINPOINT = diag - i
            if 0 <= thisistheMAINPOINT < n:
                matrix[i][thisistheMAINPOINT] = num
                num += 1
    else:
        for i in range(n):
            j = diag - i
            if 0 <= j < n:
                matrix[j][i] = num
                num += 1
        #elif j>2:
         #   matrix

# แสดงผลลัพธ์
for row in matrix:
    print(" ".join(f"{val:2}" for val in row))
#// แถมให้คำสั่งรันของ Python คือ python arry.py