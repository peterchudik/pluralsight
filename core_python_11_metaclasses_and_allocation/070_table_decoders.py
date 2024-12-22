import json
from collections import defaultdict
from pathlib import Path
# from pprint import pprint
import csv
from io import StringIO


# class RegisterMeta(type):

#     def __new__(mcs, name, bases, namespace, **kwargs):
#         cls = super().__new__(mcs, name, bases, namespace)
#         cls.register(**kwargs)
#         return cls

# class TableDecoder(metaclass=RegisterMeta):
class TableDecoder():

    _registry = {}

    # @classmethod
    # def register(cls, extension=None):
    #     if extension is None:
    #         return
    #     cls._registry[extension] = cls

    # from Python 3.6 new method __init_subclass__ was introducet
    # this method is always called when defining any subclass
    # so we do not need to create our own metaclass

    # extension is mandatory keyword argument
    @classmethod
    def __init_subclass__(cls, *, extension, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._registry[extension] = cls

    @classmethod
    def create(cls, extension):
        decoder_class = cls._registry[extension]
        return decoder_class()

    @classmethod
    def decoders(cls):
        return list(cls._registry.keys())

    def decode(self, text):
        raise NotImplementedError


class CsvTableDecoder(TableDecoder, extension="csv"):

    def decode(self, text):
        with StringIO(text) as csv_stream:
            reader = csv.DictReader(csv_stream)
            table = defaultdict(list)
            for row in reader:
                # print(f"row    -> {row}")
                for key, value in row.items():
                    table[key].append(int(value))
        return dict(table)

# CsvTableDecoder.register()


class JsonTableDecoder(TableDecoder, extension="json"):

    def decode(self, text):
        objs = json.loads(text)
        # print(f"objs    -> {objs}")
        table = defaultdict(list)
        # print(f"table    -> {table}")
        for obj in objs:
            for key, value in obj.items():
                # print(f"key    -> {key}")
                # print(f"value  -> {value}")
                table[key].append(value)
                # print(f"table  -> {table}")
        return dict(table)

# JsonTableDecoder.register()


def load_table(filepath):

    filepath = Path(filepath)
    text = filepath.read_text()
    # print(f"text    -> {text}")
    # print(f"suffix  -> {filepath.suffix}")
    extension = filepath.suffix.removeprefix(".")
    decoder = TableDecoder.create(extension)
    table = decoder.decode(text)

    return table


def main():
    print(TableDecoder.decoders())
    table = load_table("temperatures.json")
    print(f"json -> {table}")
    table = load_table("temperatures.csv")
    print(f"csv  -> {table}")


if __name__ == "__main__":
    main()


