# this is the solution for the problem 
#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/range-query-2/

def solve(n, arr, q, que):
   
    ans=[]
    for i in range(q):
        x=que[i][0]
        y=que[i][1]
        z=que[i][2]
        if x==0:
           arr[y]=z
        elif x==1:
            ans.append(len([i for i in arr[y:z+1] if i%2==0]))
        else:
            count=0
            for j in range(y,z+1):
                if arr[j]%2==1:
                    count+=1
            ans.append(count)
    return ans