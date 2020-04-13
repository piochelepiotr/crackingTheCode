def bool_exp(s, result):
    m = {}
    def bool_exp_rec(s, result):
        if len(s) == 1:
            if result:
                return 1 if s == "1" else 0
            else:
                return 1 if s == "0" else 0
        key = "{}_{}".format(s, result)
        if key in m:
            return m[key]
        total_ways = 0
        # only odd indexes have an operator
        for i in range(1, len(s), 2):
            left = s[:i]
            right = s[i+1:]
            c = s[i]
            left_true = bool_exp_rec(left, True)
            left_false = bool_exp_rec(left, False)
            right_true = bool_exp_rec(right, True)
            right_false = bool_exp_rec(right, False)
            total_left = left_true + left_false
            total_right = right_true + right_false
            total = total_left * total_right
            ways = 0
            if c == "&":
                ways = left_true * right_true
            elif c == "^":
                ways = left_true * right_false + left_false * right_true
            else:
                ways = left_true * right_false + left_true * right_true + left_false * right_true
            if not result:
                ways = total - ways
            total_ways += ways
        m[key] = total_ways
        return total_ways
    return bool_exp_rec(s, result)
