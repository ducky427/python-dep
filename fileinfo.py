
import os.path
import marshal

DATA_DIR = 'data/'
PYPI_DATA_DIR = 'data2/'


def get_file_name(package, data_dir=DATA_DIR):
    return os.path.join(data_dir, '%s.bin' % package)


def exists(package, data_dir=DATA_DIR):
    file_name = get_file_name(package, data_dir)
    return os.path.exists(file_name)

def save_data(name, package_info, data_dir=DATA_DIR):
    file_name = get_file_name(name, data_dir)
    with open(file_name, 'wb') as f:
        marshal.dump(package_info, f)
