# A,B = map(int, input().split()) #두수비교

# if(-10000<= A and B <= 10000):
#   if(A>=B):
#     if(A>B):
#       print(">")
#     else:
#       print("==")
#   else:
#     print("<")
# else:
#   print("값오류")

# A = int(input()) #학점계산

# if (0<=A<= 100):
#   if(90<=A):
#     print("A")
#   else:
#     if(80<=A):
#       print("B")
#     else:
#       if(70<=A):
#         print("C")
#       else:
#         if(60<=A):
#           print("D")
#         else:
#           print("F")
# else:
#   print("값오류")

# A = int(input()) #윤년

# if(1<=A<=4000):
#   if((A%4 == 0 and A%100 != 0) or A%400 ==0  ):
#     print("1")
#   else:
#     print("0")
# else:
#   print("값오류")


# A = int(input()) #사분면
# B = int(input())

# if ((-1000 <= A <= 1000 and A!=0) and (-1000 <= B <= 1000 and B!=0)):
#   if(A>0):
#     if(B>0):
#       print("1")
#     else:
#       print("4")
#   else:
#     if(B>0):
#       print("2")
#     else:
#       print("3")
# else:
#   print("값오류")

# A,B = map(int, input().split()) #알람시계

# if(0<= A <= 23 and 0<= B <= 59):
#   if A != 0:
#     if B<45:
#       print(A-1,(60-(45-B)))
#     else:
#       print(A, B-45)
#   else:
#     if B<45:
#       print(24-1,(60-(45-B)))
#     else:
#       print(A, B-45)
# else:
#   print("값오류")

# A,B = map(int, input().split()) #타이머
# C = int(input())
# b =  B+C
# d = b//60
# e = A+d
# f = 60*d

# if(0<= A <= 23 and 0<= B <= 59 and 0<= C <= 1000):
#   if b<60:
#       print(A,b)
#   else:
#     if e<24:
#       if 120<b:
#         print(e, b-f)
#       else:
#         if b-60 == 60:
#           print(e,0)
#         else:
#           print(e, b-60)
#     else :
#       if 120<b:
#         print(e-24, b-f)
#       else:
#         if b-60 == 60:
#           print(e-24,0)
#         else:
#           print(e-24, b-60)
# else:
#   print("값오류")

# import random
# a = random.randint(1, 2147483647)
# print(a)

# A,B,C = map(int, input().split()) #같은 갯수 주사위
# a = [A,B,C]
# if (1<= A <= 6) and (1<= A <= 6) and (1<= A <= 6):
#   if (A+B+C)/3 == A:
#     if B == C:
#       print(10000+A*1000)
#     else:
#       print(max(a)*100)
#   else:
#     if A==B or A==C:
#       print(1000+A*100)
#     else:
#       if B == C:
#         print(1000+B*100)
#       else:
#         print(max(a)*100)
# else:
#   print("값오류")