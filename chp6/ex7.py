from random import randrange

def get_proportion(n_families):
    n_girls = 0
    n_boys = 0
    for i in range(n_families):
        has_girl = False
        while not has_girl:
            has_girl = (randrange(2) == 0)
            if has_girl:
                n_girls += 1
            else:
                n_boys += 1
    return n_girls/(n_boys+n_girls)

if __name__ == "__main__":
    print(get_proportion(100))
