## Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


### 접근법

* 주어진 여러 수의 최소공배수를 구하는 문제
* 주어진 숫자 리스트 = stack, 오름차순으로 정렬되어 있음
* answer = stack.pop(), 일단 제일 큰 수를 1에 곱하는 효과
* 다음으로 1씩 줄여가면서(e) 테스트한다. 누적곱인 answer가 해당 숫자(e)로 나눠 떨어지는지 확인한다.
    * 만약 나눠 떨어지지 않는다면, answer와 해당 수의 최대 공약수를 구한 뒤, 해당수를 그 최대 공약수로 나눈 나머지에 해당하는 숫자를 answer에 곱해준다. 

```python
def solution() : 
    def gcd(u, v):
        if v : return gcd(v, u%v)
        else: return u

    n = int(input())
    stack = [e for e in range(1,n+1)]
    answer = stack.pop()
  
    for e in stack[::-1]:
        if answer % e:
            answer *= e//gcd(answer, e)
    print(answer )
            
solution()  
```