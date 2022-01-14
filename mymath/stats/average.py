
def data_mean(data):
    return sum(data) / len(data)
# 데이터 중앙값
def data_median(data):
    data.sort()
    n = len(data)
    if n % 2 == 0:
        return (data[n/2] + data[(n/2)-1]) / 2
    else:
        return data[(n-1)/2]