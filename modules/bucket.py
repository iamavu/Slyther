import argparse
from slyther import banner


def parser():
    parser = argparse.ArgumentParser(description=banner())
    parser.add_argument('-b', metavar='bucket', help='bucket name to audit against',action='store',required=True)
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    parser()
