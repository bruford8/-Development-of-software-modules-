from collections.abc import Iterator, Iterable


class Student_Group(Iterator):
    _position: int = None
    _reverse: bool = False

    def __init__(self, collection, reverse=False):
        self._collection = sorted(collection)
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return value


class Student(Iterable):
    def __init__(self):
        self._collection = ["Макар", "Финлядндия", "Один"],\
        ["Андрей", "Буркина-Фасо", "Пять"], ["Майкл", "Жваневски", "Десять"]

    def __iter__(self):
        return Student_Group(self._collection)


if __name__ == "__main__":
    wordsCollection = Student()
    print(list(wordsCollection))