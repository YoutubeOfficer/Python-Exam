# a = int(input())

# if 1 <= a <= 9: #구구단
#   for i in range(1,10):
#     print(a, '*', i, '=', a * i)
# else:
#   print("값오류")

# c = int(input()) #A+B 변형
# for i in range(c):
#   a,b = list(map(int, input().split()))
#   if 0 < a and b < 10:
#     print(a+b)  
#   else:
#     print("값오류")

# a = int(input()) #합계산
# b = 0
# for i in range(1,a+1) :
#    b+=i
# print(b)

# import sys
# c = int(input()) #빠른 A+B 변형
# for i in range(c):
#   a,b = list(map(int, sys.stdin.readline().strip().split()))
#   if 1<= a <= 1000 and 1<= b <= 1000:
#     print(a+b)  
#   else:
#     print("값오류")

# a = int(input())  #range = 연속적인 숫자개체 생성후 반환, reversed = range의 역순 반환 #출력역으로
# for i in reversed(range(1,a+1)):
#   print(i)

# c = int(input()) #A+B 변형2
# for i in range(1,c+1):
#   a,b = list(map(int, input().split()))
#   if 0 < a and b < 10:
#     print("Case #%d:" %i, a+b)  
#   else:
#     print("값오류")
#     break

# c = int(input()) #A+B 변형3
# for i in range(1,c+1):
#   a,b = list(map(int, input().split()))
#   if 0 < a and b < 10:
#     print("Case #%d: %d + %d =" %(i, a, b), a+b)  
#   else:
#     print("값오류")
#     break

# c = int(input()) #별찍기
# for i in range(1,c+1):
#   print("*" * i)
    
# c = int(input()) #별찍기공백포함
# for i in (range(1,c+1)):
#   print(" " * (c-i) + "*" * (i))


# from shlex import join # 작은수

# a,b = list(map(int, input().split()))
# c = [d for d in input().split() if int(d) < b]
# print(join(c))