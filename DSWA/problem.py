x = 0
def testcase_function(n):
    print(x)
    x++
    testcase_function(n-1)

t = int(input())
testcase_function(t)