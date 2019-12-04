def have_intersection(a, b):
    if a[0] > b[1] or a[1] < b[0]:
        return False
    return True


def combine(a, b):
    return [min(a[0], b[0]), max(a[1], b[1])]


def merge(intervals):
    for outer_index, interval in enumerate(intervals):
        inner_index = outer_index + 1
        size = len(intervals)
        while inner_index < size:
            if have_intersection(intervals[outer_index], intervals[inner_index]):
                intervals[outer_index] = combine(intervals[outer_index], intervals[inner_index])
                del intervals[inner_index]
                size -= 1
                inner_index = outer_index + 1
            else:
                inner_index += 1
    return intervals


