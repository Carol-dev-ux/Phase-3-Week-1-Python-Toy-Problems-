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
                return -1  # Not possible to redistribute bricks
            
        elif diff < 0:
            if i + 1 < N:
                A[i + 1] += diff
                moves += abs(diff)
            else:
                return -1  # Not possible to redistribute bricks
    
    return moves

# Test cases
print(solution([7, 15, 10, 8]))  # Output should be 7
print(solution([11, 10, 8, 12, 8, 10, 11]))  # Output should be 6
print(solution([7, 14, 10]))  # Output should be -1






