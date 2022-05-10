def is_valid(string):
    lst = [char for char in string]
    opposite = ""
    try:
        for i in range(int(len(string)/2)):
            if lst[0] == '(':
                opposite = ")"
            elif lst[0] == "[":
                opposite = "]"
            elif lst[0] == "{":
                opposite = "}"
            else:
                return False
            lst.remove(lst[0])
            try:
                lst.remove(opposite)
            except ValueError:    # Couldn't find match
                return False
    except TypeError:    # This means that there is an uneven amount of open and closed characters... invalid.
        return False
    if len(lst) != 0:
        return False
    return True

print(is_valid("()"))
print(is_valid("(]"))
print(is_valid('((((()))))'))
print(is_valid("()[]{}"))

# ---- Accepted LeetCode Solution ----

class Solution:
    def isValid(self, s: str) -> bool:
        lst = [char for char in s]
        opposite = ""
        try:
            for i in range(int(len(s)/2)):
                if lst[0] == '(':
                    opposite = ")"
                elif lst[0] == "[":
                    opposite = "]"
                elif lst[0] == "{":
                    opposite = "}"
                else:
                    return False
                lst.remove(lst[0])
                try:
                    lst.remove(opposite)
                except ValueError:    # Couldn't find match
                    return False
        except TypeError:    # This means that there is an uneven amount of open and closed characters... invalid.
            return False
        if len(lst) != 0:
            return False
        return True

# NOTE: this passes 87/91 tests
