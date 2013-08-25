
import subprocess

import fileinfo


def process(package_name):
    if fileinfo.exists(package_name):
        return

    subprocess.call(['pip', 'install', '--no-deps', package_name])

    subprocess.call(['python', 'extractdatapip.py', package_name])



if __name__ == '__main__':
    process('pandas')
