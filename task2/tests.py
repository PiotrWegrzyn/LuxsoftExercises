import pytest

from task2.task import merge, have_intersection, combine


def test_have_intersection_a_contains_b():
    a = [1, 4]
    b = [2, 3]
    assert have_intersection(a, b) is True


def test_have_intersection_returns_false_when_no_intersection():
    a = [3, 3]
    b = [6, 6]
    assert have_intersection(a, b) is False


@pytest.mark.parametrize(
    "a,b,result",
    [
        ([1, 10],[2, 9], True),
        ([1, 10],[0, 2], True),
        ([1, 10],[9, 11], True),
        ([14, 88],[14, 88], True),
        ([1, 10],[21, 37], False),
        ([1, 10],[-1, 0], False),
    ],
)
def test_have_intersection(a, b, result):
    assert have_intersection(a, b) is result


def test_combine():
    a = [1, 4]
    b = [2, 3]
    assert combine(a, b) == [1, 4]


def test_merge_returns_list():
    intervals = [[1, 3], [2, 4], [3, 5]]
    returned_value = merge(intervals)
    assert type(returned_value) is list


def test_merge_returns_all_when_no_intersections():
    intervals = [[21, 37], [9, 11]]
    assert merge(intervals) == intervals


def test_merge_all_intersect():
    intervals = [[1, 3], [2, 4], [3, 5]]
    assert merge(intervals) == [[1, 5]]


def test_merge_all_have_only_one_point_common():
    intervals = [[1, 2], [2, 4], [4, 5]]
    assert merge(intervals) == [[1, 5]]


def test_merge_returns_2_lists_when_2_groups_found():
    intervals = [[1, 3], [2, 4], [101, 103], [102, 104], [1, 1]]
    assert merge(intervals) == [[1, 4], [101, 104]]


def test_merge_returns_empty_when_empty_input():
    intervals = []
    assert merge(intervals) == []


def test_merge_random_data():
    intervals = [[1, 3], [20, 30], [40, 50], [2, 4], [101, 103], [15, 50], [203, 303], [102, 104], [1, 1], [3, 10]]
    assert merge(intervals) == [[1, 10], [15, 50], [101, 104], [203, 303]]


