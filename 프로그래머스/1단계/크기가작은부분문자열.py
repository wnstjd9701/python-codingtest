# 프로그래머스 1단계 - 크기가 작은 부분 문자열
def solution(t, p):
    answer = 0
    for i in range(len(t)-len(p)+1):
        if int(p) >= int(t[i:i+len(p)]):
            answer += 1
    return answer
print(solution("3141592", "271"))