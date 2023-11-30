# https://contest.yandex.ru/contest/50668/problems/A/

n = int(input())
full_string, full_name, quantity_unique, day, month, year, sum_of_month, cipher = [], [], [], [], [], [], [], []
alphabet = {}
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
for i in range(len(letters)):
    alphabet[letters[i]] = i + 1


def numbers_plus(month, day):
    result = 0
    for i in range(len(day)):
        result += int(day[i])
    for i in range(len(month)):
        result += int(month[i])
    return result


for i in range(n):
    full_string.append(input())

for i in range(n):
    full_name.append(full_string[i].split(',')[0]+full_string[i].split(',')[1]+full_string[i].split(',')[2])
    day.append(full_string[i].split(',')[3])
    month.append(full_string[i].split(',')[4])
    year.append(full_string[i].split(',')[5])
    quantity_unique.append(len(set(full_name[i])))
    sum_of_month.append(numbers_plus(day[i], month[i]))
    position = 0
    if full_name[i][0].lower() in alphabet.keys():
        position = alphabet[full_name[i][0].lower()]
    result = int(quantity_unique[i]) + (int(sum_of_month[i])*64) + (int(position)*256)
    total = str(hex(result)[2:])
    if len(total) < 3:
        while len(total) != 3:
            print(total)
            total += '0' + str(hex(result)[2:])
    else:
        print(total.upper()[-3:], end=' ')