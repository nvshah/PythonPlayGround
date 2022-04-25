import re
import string

def isAlphaNum(c):

    def a1():
        #regex = r"^[a-zA-Z\d]$"
        regex = r"[a-zA-Z\d]"
        return bool(re.fullmatch(regex, c))

    def a2():
        return ((c in string.ascii_lowercase)
                or (c in string.ascii_uppercase)
                or (c in string.digits))

    def a3():
        code = ord(c)
        return (ord('A') <= code <= ord('Z')
                or ord('a') <= code <= ord('z')
                or ord('1') <= code <= ord('9'))

    def a4():
        return c.isalnum()



