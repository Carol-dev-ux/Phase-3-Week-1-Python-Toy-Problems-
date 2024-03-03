def solution(A):
    N = len(A)
    target = 10
    moves = 0
    
    for i in range(N):
        diff = A[i] - target
        
        if diff > 0:
            if i + 1 < N:
                A[i + 1] += diff
                moves += diff
            else:
                return -1  
            
        elif diff < 0:
            if i + 1 < N:
                A[i + 1] += diff
                moves += abs(diff)
            else:
                return -1  
    
    return moves

# Test cases
print(solution([7, 15, 10, 8]))  
print(solution([11, 10, 8, 12, 8, 10, 11]))  
print(solution([7, 14, 10])) 






