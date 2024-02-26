# TODO: Имеется список, положительных целых чисел(integer).
#  Необходимо сформировать все триплеты [nums[i], nums[j], nums[k]],
#  для которых выполняются следующие условия: i != j != k и
#  nums[i] * nums[j] * nums[k] == 0. Каждый триплет должен быть записан
#  в качестве списка в выходную последовательность.
#  result = [[1, 2, 0], [1, 0, 3], [2, 0, 3], [0, 3, 0], [0, 0, 4]]

nums = [1, 2, 0, 3, 0, 4]


def compare(n):
    res, length = [], len(n)
    for i in range(length - 2):
        for j in range(i + 1, length - 1):
            k = j + 1

            if i != j != k and n[i] * n[j] * n[k] == 0:
                res.append([n[i], n[j], n[k]])

    return res


triplet = compare(nums)
print(triplet)
