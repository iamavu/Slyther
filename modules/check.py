from shutil import which

def check_aws():
    return which('aws') is not None

if __name__ == '__main__':
    pass
