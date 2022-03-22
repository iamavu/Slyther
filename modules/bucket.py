import argparse
from slyther import banner


def parser():
    parser = argparse.ArgumentParser(description=banner())
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-b', metavar='bucket', help='bucket name to audit against',action='store', type=str)
    group.add_argument('-l', metavar='list', help='file with list of names of bucket',action='store', type=argparse.FileType('r'))
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    parser()