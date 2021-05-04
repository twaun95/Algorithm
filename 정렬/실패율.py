#예제1
#n = 5
#tages = [2,1,2,6,2,4,3,3]
#예제2
#n=4
#stages = [4,4,4,4,4]

def solution(n,stages):
    answer = []
    fail = []
    userNum = len(stages) #사용자의 수

    for stage in range(1,n+1):
        noClear = stages.count(stage) #스테이지별 실패한 사용자 수
        if userNum == 0: 
            failRate = 0
        else:
            failRate = noClear/userNum
        
        userNum -= noClear
        fail.append((failRate,stage)) #failRate와 해당stage를 fail리스트에

    fail.sort(key=lambda x:-x[0]) #failRate에 대해 정렬
    answer = [i[1] for i in fail]

    return answer
