def solution(n,stages):
    answer = []
    fail = []
    userNum = len(stages)

    for stage in range(1,n+1):
        noClear = stages.count(stage)
        if userNum == 0:
            failRate = 0
        else:
            failRate = noClear/userNum
        
        userNum -= noClear
        fail.append((failRate,stage))   

    fail.sort(key=lambda x:-x[0])
    answer = [i[1] for i in fail]
    print(answer)

    return answer