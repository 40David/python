def convertion(second):
    hours=second // 3600
    min= second // 60
    remaining= second - hours * 3600 - min * 60
    return hours, min, remaining
 
hours, min, second = convertion(5000)
print(hours, min, second)