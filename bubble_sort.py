# 정렬치고는 굉장히 별로인 알고리즘.
# 직관적이라 알고리즘 시작 step으로 가볍게 밟기 좋아 시작.

# 변수 리스트 생성
list1 = [3, 5, 2, 8]
a = 0;

for i in range(len(list1)):
    print(list1)      #순차 과정 출력
    for j in range(len(list1)-i-1):
        if list1[j] > list1[j+1]:
            a = a + 1
            list1[j], list1[j+1] = list1[j+1], list1[j]


print("SWap")
print("swap 횟수 : " + str(a))