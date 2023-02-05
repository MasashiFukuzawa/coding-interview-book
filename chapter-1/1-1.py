def is_unique_chars(s: str) -> bool:
    if (len(s) > 128):
        return False

    char_set = {}
    for i in range(len(s)):
        key = s[i]
        if char_set.get(key):
            return False
        char_set[key] = True  # 入れる値は何でも良い
    return True

if __name__ == '__main__':
    print(is_unique_chars('aaa'))  # False
    print(is_unique_chars('abc'))  # True
    print(is_unique_chars('abcdefghijklmnopqrstuvwxyza'))  # False
    print(is_unique_chars('abcdefghijklmnopqrstuvwxyz'))  # True
