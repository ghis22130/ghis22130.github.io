# 프로그래머스 동적프로그래밍 N으로표현 문제

## 문제 설명
아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.

12 = 5 + 5 + (5 / 5) + (5 / 5)
12 = 55 / 5 + 5 / 5
12 = (55 + 5) / 5

5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.

## 제한 사항
- N은 1 이상 9 이하입니다.
- number는 1 이상 32,000 이하입니다.
- 수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
- 최솟값이 8보다 크면 -1을 return 합니다.

## 입출력 예
| N | number | return|
|---| ---   | --- | ---|
|5|  12  | 4|
|2 |11 | 3|



## 문제 풀이
```python
def solution(N, number):
    if N == number:
        return 1
    
    s = [ set() for x in range(8) ] 
    for i,x in enumerate(s, start=1):
        x.add( int( str(N) * i ) )
        
    for i in range(1, 8):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i-j-1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)

        if  number in s[i]:
            answer = i + 1
            break

    else:
        answer = -1
    return answer
```

참고 : <https://programmers.co.kr/learn/courses/30/lessons/42895>