# ZeroDivisionError
# This error is raised when the second argument of a division or modulo operation is zero.

# ValueError
# This error is raised when a built-in operation or function receives an argument that has the right type but an inappropriate value.

# Handling Exceptions
# The statements try and except can be used to handle selected exceptions. A try statement may have more than one except clause to specify handlers for different exceptions.

# #Code
# try:
#     print 1/0
# except ZeroDivisionError as e:
#     print "Error Code:",e

def main():
    T = int(input())
    num = []
    for _ in range(T):
        num.append([x for x in input().split()])

    for i in range(T):
        try:
            print(int(num[i][0]) // int(num[i][1]))
        except Exception as e:
            print('Error Code: ', e)

if __name__ == '__main__':
    main()