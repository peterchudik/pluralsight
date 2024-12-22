"""Read and print integer series"""
import sys

# def read_series(filename):
#     f = open(filename, mode='rt', encoding='utf-8')
#     series = []
#     for line in f:
#         a = int(line.strip())
#         series.append(a)
#     f.close()
#     return series

# adding try - finally to properly close file in case of exception
# also we can shorten code by list comprehesion in return clause
# def read_series(filename):
#     try:
#         f = open(filename, mode='rt', encoding='utf-8')
#         return [int(line.strip()) for line in f]
#     finally:
#         f.close()

# refactor using with-block
def read_series(filename):
    with open(filename, mode='rt', encoding='utf-8') as f:
        return [int(line.strip()) for line in f]

def print_series(filename):
    series = read_series(filename)
    print(series)

if __name__ == "__name__":
	print_series(filename=sys.argv[1])
