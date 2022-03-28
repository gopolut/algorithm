'''
F. Палиндром
'''
# 52ms | 4.01Mb

def is_palindrome(line: str) -> bool:
    news = ''
    for i in line:
        if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122 or 48 <= ord(i) <= 57: 
            news += i
    print(news)
    print(news[::-1])
    if news.lower() == news[::-1].lower():
        return True
    return False
   

print(is_palindrome(input().strip()))
