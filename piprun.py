
import subprocess

def process(package_name):
    subprocess.call(['pip', 'install', '--no-deps', package_name])
    subprocess.call(['python', 'saveinfo.py', package_name])
    subprocess.call(['pip', 'uninstall', '-y', package_name])



if __name__ == '__main__':
    process('pandas')
