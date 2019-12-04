# start from the beggining of the string take one letter this iteration and take a one letter longer string each iteration
# check whether set contains this portion of string if so then
# check whether the rest of the string can be created
# if not then try next iteration
# if all iterations fail return false


def preprocess(tokens):
    return set(tokens)   # this will prune out duplicates


def validate(tokens, tested_string):
    if tested_string is "":
        return True

    for i in range(1, len(tested_string)+1):
        substring = tested_string[:i]
        if substring in tokens:  # tokens is a set so the lookup has time complexity of O(1)
            if validate(tokens, tested_string[i:]):
                return True
    return False

