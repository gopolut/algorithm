from typing import List

'''
D. Хаотичность погоды
'''

# 135ms | 12.77Mb
# 138ms | 13.00Mb c массивом m
# 
def get_weather_randomness(temperatures: List[int]) -> int:
    z = len(temperatures)-1 # последний индекс списка
    count = 0
    m = []
    if len(temperatures) == 1:
        count = 1
    elif len(set(temperatures)) == 1:
        count = 0
    else: 
        for i in range(0, len(temperatures)):    
            if i == 0 and temperatures[i] > temperatures[i + 1]:
                m.append(temperatures[i])
                count += 1
            elif i == z and temperatures[i] > temperatures[i-1]:
                m.append(temperatures[i])
                count += 1 
            elif temperatures[i-1] < temperatures[i] > temperatures[i+1]:
                m.append(temperatures[i])
                count += 1

    return count, m

def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures

temperatures = read_input()
print(get_weather_randomness(temperatures))
