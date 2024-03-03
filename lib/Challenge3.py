def solution(N):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_length = len(alphabet)
    result = alphabet * (N // alphabet_length)
    remainder = N % alphabet_length
    result += alphabet[:remainder]
    return result

# Test cases
print(solution(3))
print(solution(5))
print(solution(26))