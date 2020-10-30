s=input()
length=len(s)
result=[]
step=0
MAX_step=length//2

for i in range(1,MAX_step+1):
  compressed = ""
  prev = s[0:step] # 앞에서부터 step만큼 문자열 뽑기
  count = 1 # 중복 수

  for n in range(step,length,step): #step부터 prev와 비교
    if prev == s[n:n+step]:
      count += 1
      compressed += count + prev
      prev = s[n:n+step]
       


    else:

    
    
    
    if (n+1)*i >= length+1:
      break
    elif s[n*i:(n+1)*i] == s[(n+1)*i:(n+2)*i]:
      print(s[n*i:(n+1)*i])
  
  
  
  """
  i=1 -> 0:1 == 1:2비교,
  i=2 -> (0:2 == 2:4), (2:4 == 4:6),,,
  i=3 -> (0:3 == 3:6), (3:6 == 6:9),,,
  """

