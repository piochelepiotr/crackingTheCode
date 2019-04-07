# Use a list of chars to enable inplace modification
def URLify(str, n):
    lengthAfterReplace = n
    for i in range(n):
        if str[i] == " ":
            lengthAfterReplace += 2
    j = lengthAfterReplace - 1
    for i in range(n - 1, -1, -1):
        if str[i] == " ":
            str[j] = "0"
            j -= 1
            str[j] = "2"
            j -= 1
            str[j] = "%"
            j -= 1
        else:
            str[j] = str[i]
            j -= 1
