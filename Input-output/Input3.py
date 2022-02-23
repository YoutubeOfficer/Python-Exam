A,B,C = map(int, input().split())

while (2 <= A and B and C <=10000):
  print((A+B)%C)
  print(((A%C) + (B%C))%C) 
  print((A*B)%C)
  print(((A%C) * (B%C))%C)
  break
else:
    print("에러")
    
# A = list(map(int, input().split())) #덧셈곱셈1
# a = (A[0])
# b = (A[1])

# bx = list(map(int, str(b))) 
# bx1 = (bx[2])
# bx2 = (bx[1])
# bx3 = (bx[0])

# an3 = (a*bx1)/100
# an2 = (a*bx2)/10
# an1 = (a*bx3)
# an0 = an3 + an2 + an1
# an = int(an0*100)

# print(a*bx1)
# print(a*bx2)
# print(a*bx3)
# print(an)

# A = int(input())  #덧셈곱셈2
# B = int(input())
# b = list(map(int, str(B)))
# bx1 = (b[2])
# bx2 = (b[1])
# bx3 = (b[0])

# an1 = (A*bx1)
# an2 = (A*bx2)
# an3 = (A*bx3)
# print(an1)
# print(an2)
# print(an3)
# print(A*B)
  
