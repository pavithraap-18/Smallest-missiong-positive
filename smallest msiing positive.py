# Python program to find the first missing positive number 
# using visited array

def missingNumber(arr):
    n = len(arr)

    # To mark the occurrence of elements
    vis = [False] * n
    for i in range(n):

        # if element is in range from 1 to n
        # then mark it as visited
        if 0 < arr[i] <= n:
            vis[arr[i] - 1] = True

    # Find the first element which is unvisited
    # in the original array
    for i in range(1, n + 1):
        if not vis[i - 1]:
            return i

    # if all elements from 1 to n are visited
    # then n+1 will be first positive missing number
    return n + 1

if __name__ == "__main__":
    arr = [2, -3, 4, 1, 1, 7]
    print(missingNumber(arr))
