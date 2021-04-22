#https://programmers.co.kr/learn/courses/30/lessons/60057
#앞에서부터 짤라야함!
#전체길이 구학
#하나압축, 두개압축,,,전체길이의 반만큼 해서 가장 짧은 것 채택.
s = input()
pre = ""
now = ""
szip = ""
answer = len(s)

#n개 단위로 압축했을때
for n in range(1, len(s)//2+1):
    pre = s[:n]
    szip = ""
    count = 1 #중복개수

    for i in range(1, len(s)//n):#check
        now = s[i*n:i*n+n]#check
        print("n: ", n) 
        print("pre: ", pre)
        print("now: ", now)
        if now == pre:
            count += 1
        else:
            szip += str(count) + pre
            szip = szip.replace("1","")    
            count = 1 #count초기화
        print("count:",count)

        pre = now
        print("szip:", szip)
        
    
    print("szip: ", szip)
    answer = min(answer, len(szip))

print(answer)