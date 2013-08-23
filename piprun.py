
import os.path
import subprocess

INSTALLED = """argparse
Cython
Flask
itsdangerous
Jinja2
MarkupSafe
numpy
pip
python-dateutil
pytz
redis
rq
rq-dashboard
setuptools
simplejson
six
times
virtualenv
virtualenvwrapper
Werkzeug
wheel
wsgiref""".split('\n')


def process(package_name):
    filename = 'data/%s.bin' % package_name

    if os.path.exists(filename):
        return

    if package_name not in INSTALLED:
        subprocess.call(['pip', 'install', '--no-deps', package_name])

    subprocess.call(['python', 'saveinfo.py', package_name])

    if package_name not in INSTALLED:
        subprocess.call(['pip', 'uninstall', '-y', package_name])



if __name__ == '__main__':
    process('pandas')
