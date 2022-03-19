'''
E. Самое длинное слово
'''

# 47ms | 3.98Mb
def get_longest_word(line: str) -> str:
    list_line = line.strip().split()
    biggest = 0
    longest_word = ''

# TODO: ппробовать сделать с list comprehension
    for i in list_line:
        if biggest < len(i):
            biggest = len(i)
            longest_word = i
        biggest = biggest
        longest_word = longest_word
    
    return longest_word

def read_input() -> str:
    _ = input()
    line = input().strip()
    return line

def print_result(result: str) -> None:
    print(result)
    print(len(result))

print_result(get_longest_word(read_input()))
