import types
from tools import logger


class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.cur_position = -1
        self.next_position = 0
        self.len_list_of_lists = len(self.list_of_list)

    def __iter__(self):
        # вход в цикл
        self.cur_position += 1
        self.next_position = 0
        return self

    def __next__(self):
        while self.cur_position - self.len_list_of_lists and \
                self.next_position == len(self.list_of_list[self.cur_position]):
            iter(self)
        if self.cur_position == self.len_list_of_lists:
            # выход из цикла
            raise StopIteration
        self.next_position += 1
        item = self.list_of_list[self.cur_position][self.next_position - 1]
        print(item)
        return item


@logger
def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


def flat_generator(list_of_lists):
    for lst in list_of_lists:
        for element in lst:
            print(element)
            yield element


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_1()
    test_2()
