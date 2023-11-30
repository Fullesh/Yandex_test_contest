# https://contest.yandex.ru/contest/50668/problems/B/


import datetime as dt
n = int(input())
logs = []
for i in range(n):
    logs.append(input())


def analysis(n, logs):
    total_array = []
    for i in range(n):
        tmp_var = (logs[i].split(' '))
        total_array.append(tmp_var)
    return total_array


total_rockets = []
total_array = analysis(n, logs)
sorted_array_by_id = sorted(total_array, key=lambda x: (x[3], x[0]), reverse=False)

for i in range(len(sorted_array_by_id)):
    total_rockets.append(sorted_array_by_id[i][-2])


total_rockets = list(set(total_rockets))
total_time = 0

result = dict.fromkeys([rocket for rocket in total_rockets],[])
print(result)

for i in range(len(sorted_array_by_id)):
    if sorted_array_by_id[i][-2] in total_rockets:
        result[f'{sorted_array_by_id[i][-2]}'].append(':'.join(sorted_array_by_id[i][0:3]))

for key, value in result.items():
    print(key, value)
