
import os.path
import marshal
import random
import time
import xmlrpclib

from redis import Redis
from rq import Queue

import fileinfo

from extractdatapypi import get_package_data

ONE_MONTH = 60 * 60 * 24 * 30


if __name__ == '__main__':
    client = xmlrpclib.ServerProxy('http://pypi.python.org/pypi')

    filename = 'data/all_packages.bin'
    if os.path.exists(filename):
        with open(filename) as f:
            packages = marshal.load(f)
    else:
        packages = client.list_packages()
        with open(filename, 'wb') as f:
            marshal.dump(packages, f)

    packages = [p for p in packages if not fileinfo.exists(p, fileinfo.PYPI_DATA_DIR)]

    random.shuffle(packages)

    q = Queue(connection=Redis())

    results = [q.enqueue(get_package_data, args=[job], timeout=ONE_MONTH) for job in packages]

    done = False
    while not done:
        jobs_statuses = [1 for r in results if r.is_finished]
        jobs_left = len(results) - len(jobs_statuses)
        done = (jobs_left == 0)
        if not done:
            print "Number of jobs left: %s" % (jobs_left, )
            time.sleep(30)

