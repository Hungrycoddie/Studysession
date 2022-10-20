from typing import *
def timingSum(a: List[int], n: int) -> int:

    # Write your Code here 
    count = [0] * 60
    for i in range(n):
        count[a[i] % 60] += 1
    ans = 0
    for i in range(1, 30):
        ans += count[i] * count[60 - i]
    ans += count[0] * (count[0] - 1) // 2
    ans += count[30] * (count[30] - 1) // 2
    return ans



if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(timingSum(a, n))
    
#The above code calculates the sum of the elements of the array at indices i and j, provided that j = (60 - i) mod 60.

#For example,

#a = [1, 2, 3, 4, 5]

#The sum at indices 0 and 60 will be 1 + 5 = 6.
#The sum at indices 1 and 59 will be 2 + 4 = 6.
#The sum at indices 2 and 58 will be 3 + 3 = 6.
#The sum at indices 3 and 57 will be 4 + 2 = 6.
#The sum at indices 4 and 56 will be 5 + 1 = 6.

