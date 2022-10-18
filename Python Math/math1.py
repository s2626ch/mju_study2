values = [1, 2, 3, 4, 5]

def cal_mean(numbers):
    s = sum(numbers)
    n = len(numbers)

    return s/n

mean = int(cal_mean(values))
print(mean)

