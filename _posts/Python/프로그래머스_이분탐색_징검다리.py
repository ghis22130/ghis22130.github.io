def solution(distance, rocks, n):
    answer = 0 
    
    rocks.sort()
    rocks.append(distance)
    
    left, right = 0, distance
    
    while left<=right :
        mid = (left+right)//2
        min_d = 1000000001
        cur = 0
        remove_rocks = 0
        for rock in rocks :
            distance = rock - cur
            if distance < mid :
                remove_rocks += 1
            else :
                cur = rock
                min_d = min(min_d,distance)
        
        if remove_rocks > n :
            right = mid - 1
        else :
            answer = min_d
            left = mid + 1
            
    return answer
    
    
    # 출처 : https://programmers.co.kr/learn/courses/30/lessons/43236
    # 참고 : https://deok2kim.tistory.com/122
