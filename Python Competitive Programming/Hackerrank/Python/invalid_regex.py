import re

def isValidRegex(pattern: str) -> bool:
    try:
        re_compiled = re.compile(pattern)
        return True
    except re.error :
        return False

if __name__ == '__main__':
    inp = input()
    print(isValidRegex(inp))
