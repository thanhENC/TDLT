def merge_the_tools(string, k):
    # your code goes here
    t = []
    for i in range(int(len(string)/k)):
        t.append(string[k*i:k*(i+1)])
    
    u = []
    for word in t:
        s = ''
        for char in word:
            if char not in s:
                s += char
        u.append(s)
        print(s)
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)