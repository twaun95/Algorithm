#럭키 스트레이트
"""
게임의 아웃복서 캐릭터는 필살기인 '럭키'스트레이트'기술이 있습니다. 이 기술은 매우 강력한 대신에 게임 내에서 점수가 특정 조건을 만족할 때만 사용할 수 있습니다.
특정 조건이란 현재 캐릭터의 점수를 N이라고 할 때 자릿수를 기준으로 점수N을 반으로 나누어 왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합을 더한 값이 동일한 상황을 의미합니다.
예를 들어 현재 점수가 123,402라면 왼쪽 부분의 각 자릿수의 합은 1+2+3, 오른쪽 부분의 각 자릿수의 합은 4+0+2이므로 두 합이 6으로 동일하여 럭키 스트레이트를 사용할 수 있습니다.
현재 점수 N이 주어지면 럭키 스트레이트를 사용할 수 있는 상태인지 아닌지를 알려주는 프로그램을 작성하세요.

* 입력조건
- 첫째 줄에 점수 N이 정수로 주어집니다.(10<=N<=99,999,999) 단, 점수 N의 자릿수는 항상 짝수 형태로만 주어집니다. 예를 들어 자릿수가 5인 12345와 같은 수는 입력으로 들어오지 않습니다.

* 출력조건
- 첫째 줄에 럭키 스트레이트를 사용할 수 있다면 "LUCKY"를, 사용할 수 없다면 "READY"를 출력합니다.

*입력예시            *출력예시
123402               LUCKY

7755                 READY
"""