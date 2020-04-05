def bit_to_string(x):
    s = ""
    step = 1
    for i in range(32):
        if x >= step:
            x -= step
            s = s + '1'
        else:
            s = s + '0'
        step /= 2
    if x > 0:
        return "ERROR"
    return s
