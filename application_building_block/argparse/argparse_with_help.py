import argparse
parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-a', action="store_true", default=True)
parser.add_argument('-b', action="store", dest="b")
parser.add_argument('-c', action="store", dest="c", type=int)
print(parser.parse_args())
