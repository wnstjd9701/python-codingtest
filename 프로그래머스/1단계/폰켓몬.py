# 프로그래머스 1단계 - 폰켓몬
def solution(nums):
    answer = 0
    leng = len(set(nums))
    if len(nums) // 2 > leng:
        return leng
    else:
        return len(nums) // 2