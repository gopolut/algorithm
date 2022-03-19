# ленивый алгоритм
# Работает со скоростью N x K
def moving_average(timeseries, K):
    result = []
    for begin_index in range(0, len(timeseries) - K):
        end_index = begin_index + K
        # Просматриваем окно шириной K.
        current_sum = 0
        for v in timeseries[begin_index:end_index]:
            current_sum += v
        current_avg = current_sum / K
        result.append(current_avg)
    return result 

# Оптимизированный 'ленивый' алгоритм - "метод двух указателей"
# Новый алгоритм будет работать быстрее примерно в K раз.
def moving_average(timeseries, K):
    timeseries = list(map(int, timeseries.split()))
    result = []  # Пустой массив.
    # Первый раз вычисляем значение честно и сохраняем результат.
    current_sum = sum(timeseries[0:K])
    result.append(current_sum / K)
    for i in range(0, len(timeseries) - K):
        current_sum -= timeseries[i]
        current_sum += timeseries[i+K]
        current_avg = current_sum / K
        result.append(current_avg)
    return result

print(moving_average('4 3 8 1 5 6 3', 3))
