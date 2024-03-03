def digit_sum(num):
   
    return sum(int(digit) for digit in str(num))

def solution(A):
   
    num_dict = {}

   
    for num in A:
        sum_digits = digit_sum(num)
        if sum_digits in num_dict:
            num_dict[sum_digits].append(num)
        else:
            num_dict[sum_digits] = [num]

    max_sum = -1

    
    for key in num_dict:
        if len(num_dict[key]) >= 2:
            pairs = num_dict[key]
            for i in range(len(pairs)):
                for j in range(i + 1, len(pairs)):
                    pair_sum = pairs[i] + pairs[j]
                    max_sum = max(max_sum, pair_sum)

    return max_sum

# Test cases
print(solution([51, 71, 17, 42])) 
print(solution([42, 33, 60])) 
print(solution([51, 32, 43])) 
