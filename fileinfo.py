
import os.path
import marshal

DATA_DIR = 'data/'


def get_file_name(package):
    return os.path.join(DATA_DIR, '%s.bin' % package)


def exists(package):
    file_name = get_file_name(package)
    return os.path.exists(file_name)

def save_data(name, package_info):
    file_name = get_file_name(name)
    with open(file_name, 'wb') as f:
        marshal.dump(package_info, f)
