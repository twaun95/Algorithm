#문자열 압축
#링크: https://programmers.co.kr/learn/courses/30/lessons/60057
"""
데이터 처리 전문가가 되고 싶은 "어피치"는 문자열을 압축하는 방법에 대해 공부를 하고 있습니다. 최근에 대량의 데이터 처리를 위한 간단한 비손실 압축 방법에 대해 공부를 하고 있는데, 문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여 더 짧은 문자열로 줄여서 표현하는 알고리즘을 공부하고 있습니다.
간단한 예로 "aabbaccc"의 경우 "2a2ba3c"(1은 생략)와 같이 표현할 수 있는데, 이러한 방식은 반복되는 문자가 적은 경우 압축률이 낮다는 단점이 있습니다. 예를 들면, "abcabcdede"와 같은 문자열은 전혀 압축되지 않습니다. 어피치는 이러한 단점을 해결하기 위해 문자열을 1개 이상의 단위로 잘라서 압축하여 더 짧은 문자열로 표현할 수 있는지 방법을 찾아보려고 합니다. 
예를 들어, "ababcdcdababcdcd"의 경우 문자를 1개 단위로 자르면 전혀 압축되지 않지만, 2개 단위로 잘라서 압추한다면 "2ab2cd2ab2cd"로 표현할 수 있습니다. 다른 방법으로 8개 단위로 잘라서 압축한다면 "2ababcdcd"로 표현할 수 있으며, 이때가 가장 짧게 압축하여 표현할 수 있는 방법입니다. 
다른 예로, "abcabcdede"와 같은 경우, 문자를 2개 단위로 잘라서 압축하면 "abcabc2de"가 되지만, 3개 단위로 자른다면 "2abcdede"가 되어 3개 단위가 가장 짧은 압축 방법이 됩니다. 이때 3개 단위로 자르고 마지막에 남는 문자열은 그대로 붙여주면 됩니다.
압축할 문자열 s가 매개변수로 주어질 때, 위에 설명한 방법으로 2개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가자 짧은 것의 길이를 return 하도록 solution 함수를 완성해주세요.

* 제한사항
- s의 길이는 1이상 1000이하
- s는 알파벳 소문자

* 입력 예시                     *출력
aabbaccc                        7
ababcdcdababcdcd                9
abcabcdede                      8
abcabcabcabcdededededede        14
xababcdcdababcdcd               17

"""




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

