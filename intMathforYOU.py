a = input("Enter number : \n")

bb = int(a,16)

print(bb)

#%%

typeee0 = input("ใส่เลขมา : ") ## 089

myfinalAns = 0

for rap in typeee0:
    if rap.isdigit():
        if int(rap) % 2 == 1 and int(rap) != 0:## 0 คู่ 1 คี่ ใช้ int() ดา
            myfinalAns +=1

print(myfinalAns)
#%%

mytyp = input("LLLL").lower()
myyyy = 0

uojo = "aeiou"

for i in range(len(mytyp) - 1):
    if mytyp[i] in uojo and mytyp[i+1] in uojo:
        myyyy += 1
        
print(myyyy)
#%%

my = input("ONO  ")

ouo = int(my,2)
print(ouo)