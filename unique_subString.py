def merge_the_tools(string, k):
    n = len(string)
    string_array = []
    a = ''
    for i in range(0,n,k):
        a = a + string[i:(i+k)]
        string_array.append(a)
        a = ''
    for j in range(0,len(string_array)):
        s = set(string_array[j])
        r = ''
        for k in s:
            r = r + k
        print(r)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
