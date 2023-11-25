# TODO решите задачу
import json


def task(filename):
    with open(filename) as json_file:
        data = json.load(json_file)

    sum_of_products = round(sum(item.get('score', 0) * item.get('weight', 0) for item in data), 3)

    return sum_of_products


result = task('input.json')
print(result)