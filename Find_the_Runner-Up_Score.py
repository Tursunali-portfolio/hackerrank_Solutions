"""
Link to the problem: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list
"""
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    arr.sort(reverse = True)
    i = 0
    try:
        while True:
            if arr[i]>arr[i+1]:
                print(arr[i+1])
                break
            i += 1
    except:
        print(arr[i])
