from itertools import islice


def normalize_copy(numbers):
    numbers = list(numbers)  #copy the iterator
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


def read_visit(data_path):
    with open(data_path, 'r') as f:
        for line in f:
            yield int(line)


def normalize_func(get_iter):
    total = sum(get_iter())
    result = []
    for value in get_iter():
        percent = 100 * value /total
        result.append(percent)
    return result


def normalize(numbers):
    total = sum(islice(numbers, 0, 1))
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


def normalize_defensive(numbers):
    if iter(numbers) is iter(numbers): #An iterator --bad!
        raise TypeError("Must supply a container")
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


class Readvisit(object):
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)
# it = read_visit('1.txt')
# percentages = normalize_copy(it)
# percentages = normalize_func(lambda: read_visit('1.txt'))
# print(percentages)
# visit = Readvisit('1.txt')
# percentages = normalize(visit)
# print(percentages)


visit = [15, 35, 80]
print(normalize_defensive(visit))
visit = Readvisit('1.txt')
print(normalize_defensive(visit))

it = read_visit('1.txt')
print(normalize_defensive(it))


