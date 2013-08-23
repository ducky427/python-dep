
import sys
from rq import Queue, Worker, Connection


if __name__ == '__main__':
    # Tell rq what Redis connection to use
    with Connection():
        q = Queue()
        if len(sys.argv) > 1:
            Worker(q, name=sys.argv[1]).work()
        else:
            Worker(q).work()

