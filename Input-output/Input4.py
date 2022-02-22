A = list(map(int, input().split()))
a = (A[0])
b = (A[1])

bx = list(map(int, str(b))) 
bx1 = (bx[2])
bx2 = (bx[1])
bx3 = (bx[0])

an3 = (a*bx1)/100
an2 = (a*bx2)/10
an1 = (a*bx3)
an0 = an3 + an2 + an1
an = int(an0*100)

print(a*bx1)
print(a*bx2)
print(a*bx3)
print(an)