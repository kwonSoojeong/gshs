#리스트
#리스트 이름중 12 번쨰 비교
#리스트 1,n 2,n, 3,n  n, n-1 까지 비교
#비교해서 서로 같으면 집합에 넣음

            
            



def same_name(NameList):
    n = len(NameList)
    same_name=set()
    for x in range (0,n-2):
        for i in range (x+1,n-1):
            if NameList[x]== NameList[i]:
                same_name.add(NameList[x])
    return same_name

NameList = ["Tom", "Mik6", "jack", "Tom", "jerry" ]

print(same_name(NameList))
