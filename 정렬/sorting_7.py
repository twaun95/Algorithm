#국영수
"""
도현이네 반 학생 N명의 이름과 국어, 영어, 수학 점수가 주어집니다. 이떄, 다음과 같은 조건으로 학생의 성적을 정렬하는 프로그램을 작성하세요.
  1. 국어 점수가 감소하는 순서로
  2. 국어 점수가 같으면 영어 점수가 증가하는 순서로
  3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
  4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 (단, 아스키코드에서 대문자는 소문자보다 작으므로 사전 순으로 앞에 옵니다.)

* 입력조건
- 첫째 줄에 도현이네 반의 학생 수 N(1<=N<=100000)이 주어집니다.
- 둘째 줄부터 한 줄에 하나씩 각 학생의 이름, 국어, 영어, 수학 점수가 공백으로 구분해 주어집니다.
- 점수는 1보다 크거나 같고, 100보다 작거나 같은 자연수입니다.
- 이름은 알파벳 대소문자로 이루어진 문자열이고, 길이는 10자리를 넘지 않습니다.
* 출력조건
- 문제에 나와 있는 정렬 기준으로 정렬한 후 첫째 줄부터 N개의 줄에 걸쳐 각 학생의 이름을 출력합니다.

*입력예시                     *출력예시
12
Junkyu 50 60 100              Donghyuk
Sangkeun 80 60 50             Sangkeun
Sunyoung 80 70 100            Sunyoung
Soong 50 60 90                nsj
Haebin 50 60 100              Wonseob
Kangsoo 60 80 100             Sanghyun
Donghyuk 80 60 100            Sei
Sei 70 70 70                  Kangsoo
Wonseob 70 70 90              Haebin
Sanghyun 70 70 80             Junkyu
nsj 80 80 80                  Soong
Taewhan 50 60 90              Taewhan
"""