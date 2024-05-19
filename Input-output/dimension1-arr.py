# from shlex import join # 작은수

# a,b = list(map(int, input().split()))
# c = [d for d in input().split() if int(d) < b]
# print(join(c))

# ====================================================
# n = int(input()) 개수 세기
# s = list(map(int, input().split()))
# v = int(input())

# if 1 <= n <= 100 and len(s) == n and -100 <= v <= 100:
#     c = s.count(v) 
#     print(c)
# else:
#     print("값오류")

# ====================================================
# n = int(input()) #최소, 최대
# s = list(map(int, input().split()))
# if 1 <= n <= 1000000 and len(s) == n and all(-1000000 <= arr <= 1000000 for arr in s):
#   print(min(s), max(s))
# else:
#   print("값오류")

# ====================================================
# n = [] #최대값
# for _ in range(9):
#   num = int(input())
#   if num < 100:
#     n.append(num)
#   else:
#     print("값 오류")
#     exit(1)

# print(max(n), n.index(max(n))+1, sep='\n')

# ====================================================
# import sys  #공 넣기
# nm = list(map(int, input().split()))

# # nm[0]에 따라 초기 배열을 생성
# result = [0] * nm[0]

# if len(nm) == 2 and all(1 <= n <= 100 for n in nm):
#   for _ in range(nm[1]):
#     arr = list(map(int, input().split()))
#     if len(arr) == 3:
#       if arr[0] <= arr[1] and arr[1] <= nm[0]:
#         # arr[0]과 arr[1]을 result의 위치로 사용하고, arr[2]는 해당 위치의 값을 대체
#         result[arr[0]-1:arr[1]] = [arr[2]] * (arr[1] - arr[0] + 1)
#       else:
#         print("arr[0]의 값은 arr[1]의 값보다 작거나 같아야 하고 arr[1]의 값은 nm[0]의 값과 같거나 작아야 함")
#         sys.exit()
#     else:
#       print("배열의 길이는 3")
#       sys.exit()
# else:
#   print("값오류")
# print(' '.join(map(str, result)))

# ====================================================
# import sys #공 바꾸기
# nm = list(map(int, input().split()))
# re = [i+1 for i in range(nm[0])]

# if len(nm) == 2 and all(1 <= n <= 100 for n in nm):
#   for _ in range(nm[1]):
#     arr = list(map(int, input().split()))
#     if len(arr) == 2:
#       if 1 <= arr[0] <= arr[1]:
#         re[arr[0]-1] , re[arr[1]-1] = re[arr[1]-1], re[arr[0]-1]
#       else:
#         print("arr[0]은 1이상 arr[1] 이하")
#         sys.exit()
#     else:
#       print("arr의 길이는 2")
#       sys.exit()
        
# else:
#   print("nm의 배열 길이는 2, 배열 값은 1이상 100이하여야 함")
#   sys.exit()
# print(' '.join(map(str, re)))

# ====================================================
# import sys #배열에 없는 값 출력
# n = []
# for _ in range(28):
#   num = int(input())
#   if num < 31 and num not in n:
#     n.append(num)
#   else:
#     print("30이하의 값만 입력 및 중복값 금지")
#     sys.exit()
# for re in range(1,31):
#   if re not in n:
#     print(re)

# ====================================================
# import sys #서로 다른 나머지 값 갯수 출력
# a = []
# for _ in range(10):
#   num = int(input())
#   if 0 <= num <= 1000:
#     a.append(num % 42)
#     re = len(set(a))
#   else:
#     print("1이상 1000이하의 자연수만 입력")
#     sys.exit(0)
# print(re)

# ====================================================
# import sys #바구니 뒤집기
# nm = list(map(int, input().split())) #첫째 줄 N(nm[0])과 M(nm[1])을 입력
# result = [i+1 for i in range(nm[0])] #1부터 N까지의 수를 리스트에 담음
# if all(1 <= a <= 100  for a in nm):
#     for _ in range(nm[1]): #M번 반복
#         arr = list(map(int, input().split()))
#         if len(arr) == 2 and arr[0] <= arr[1] <= nm[0]: #i번(arr[0])이 j번(arr[1])보다 작거나 같고 j번(arr[1])이 N(nm[0])보다 작거나 같아야 함
#             result[arr[0]-1:arr[1]] = result[arr[0]-1:arr[1]][::-1] # i부터 j까지의 범위를 역순으로 변경
#         else:
#             print("arr의 길이는 2, i번은 j번보다 작거나 같고 j번은 N보다 작거나 같아야 함")
#             sys.exit(0)
# else:
#     print("N과 M은 1이상 100이하의 자연수만 입력")
#     sys.exit(0)
# print(' '.join(map(str, result))) #리스트를 문자열로 변환하여 출력

# ====================================================
# import sys #심화버전 평균계산
# import decimal

# def result():
#     n = int(input())
#     if not 1 <= n <= 1000:
#         print("1이상 100이하의 자연수만 입력")
#         sys.exit()
        
#     arr = list(map(int, input().split()))
#     if len(arr) != n and all(0 <= a <= 100 for a in arr):
#         print("현재 과목의 길이는 과목 수와 같아야 하고, 과목 점수는 0이상 100이하여야 함")
#         sys.exit()
#     arr_average = sum(arr) / len(arr) # arr의 평균 계산
#     # print("arr의 평균: ", arr_average)
    
#     def decimal_len(num):#소수점 자리수 구하기
#         return abs(decimal.Decimal(str(num)).as_tuple().exponent)
    
#     result_arr = []  # 새로운 배열 생성
#     for b in arr:  
#         c = round(b / max(arr) * 100, 2) #c에 arr의 각 요소를 최대값으로 나눈 후 100을 곱한 값을 소수점 2자리까지 반올림
#         result_arr.append(str(c))  # result_arr에 c를 문자열로 변환하여 추가
#     #print(result_arr)
    
#     last_arr = sum(float(e) for e in result_arr) / len(result_arr) # result_arr의 평균 계산
#     d = decimal_len(last_arr) # last_arr가 정수인지 확인
#     if last_arr.is_integer():  
#         print("{:.1f}".format(last_arr))  # 정수라면 소수점 1자리까지 출력
#     else:
#         d = decimal_len(last_arr)  # last_arr의 소수점 자리수 계산
#         if d > 15:  
#             print("{:.15f}".format(last_arr))  # 소수점 15자리까지 출력
#         else:
#             print("{:.{}f}".format(last_arr, d))  # 소수점 d자리까지 출력
#             # print(str(last_arr))
        
# result()