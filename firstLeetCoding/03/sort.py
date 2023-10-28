def bubble_sort(li):
    for i in range(len(li) - 1, 1, -1):
        for j in range(i):
            if li[j] > li[j + 1]:
                tmp = li[j + 1]
                li[j + 1] = li[j]
                li[j] = tmp
    print(li)


def select_sort(li):
    new_li = []
    length = len(li)
    for i in range(length):
        if len(li) == 1:
            new_li.append(li[0])
        else:
            max_v = max(li)
            new_li.append(max_v)
            li.remove(max_v)
    print(new_li)


def insert_sort(li):
    for i in range(1, len(li)):
        for j in range(i, 0, -1):
            if li[j] < li[j - 1]:
                v = li[j - 1]
                li[j - 1] = li[j]
                li[j] = v
    print(li)


def merge_sort(li):
    if len(li) > 1:
        split_index = int(len(li) / 2)
        left_li = merge_sort(li[:split_index])
        right_li = merge_sort(li[split_index:])
    else:
        return li

    merge_li = []
    i = 0
    j = 0
    while i < len(left_li) or j < len(right_li):
        if i == len(left_li):
            merge_li.extend(right_li[j:])
            break
        if j == len(right_li):
            merge_li.extend(left_li[i:])
            break
        if left_li[i] < right_li[j]:
            merge_li.append(left_li[i])
            i += 1
        else:
            merge_li.append(right_li[j])
            j += 1
    return merge_li


def quick_sort(li):
    if len(li) <= 1:
        return li

    index = 0
    left_li = []
    right_li = []
    while left_li == [] or right_li == []:
        # 当index==len(li)时，说明没有找到基准值将li分割成非空的两个部分，则可以推理出，li中的值都是相等的
        if index == len(li):
            return li
        left_li = []
        right_li = []
        v = li[index]
        for a in li:
            if a > v:
                right_li.append(a)
            else:
                left_li.append(a)
        index += 1

    return quick_sort(left_li) + quick_sort(right_li)


if __name__ == '__main__':
    li = [4, 5, 2, 6, 0, 0, 0, 0, 2]
    # bubble_sort(li)

    # select_sort(li)

    # insert_sort(li)

    # res = merge_sort(li)
    # print(res)

    # res = quick_sort(li)
    # print(res)
