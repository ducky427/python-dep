
import os.path

DATA_DIR = 'data/'


def get_file_name(package):
    return os.path.join(DATA_DIR, '%s.bin' % package)


def exists(package):
    file_name = get_file_name(package)
    return os.path.exists(file_name)
