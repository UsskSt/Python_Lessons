a = []
for i in range(1, 1001, 2):
    a.append(i ** 3)
print (a)

b = []
sum = 0
for num in a:
    while num != 0:
        sum += num % 10
        num = num // 10
    if sum % 7 == 0:
        b.append(num)
        sum = 0
print(b)


sum_num_plus = 0
for num in a:
    sum = 0
    i = num
    num += 17
    while num != 0:
        sum += num % 10
        num = num // 10
    if sum % 7 == 0:
        sum_num_plus += i

print (sum_num_plus)

