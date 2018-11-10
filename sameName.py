#동명이인 찾기
# 입력 : 리스트 (사람이름이 들어가있음) - 동명이인이 있는지를 찾을거야...
# 출력 : 이름중에 반복되는 이름을 집합으로 출력

# ex) list : [tom, mike, a, b, tom, sj, sj, google, naver, google, sj]
# 결과 : {tom ,sj, google}



# 리스트를 입력받는다
# 리스트 1번을 2~n 까지 비교, 같은 것이 있으면 결과집합에 넣음
# n-1 까지 반복

# a = [tom, tom, hello, hello, sj, kiki, sj, google, sj, google, naver, google]

def find_same_name(names):
    n = len(names)
    result = set()
    for i in range(0,n-1):
        for j in range(i+1 ,n):
            if names[i] == names[j]:
                result.add(names[i])
    return result


                
