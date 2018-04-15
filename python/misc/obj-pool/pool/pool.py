import logging
import sys
from collections import deque
from threading import RLock


LOGGER = logging.getLogger(__name__)


class Pool():
    '''Object pool for building and caching arbitrary objects.'''
    MIN_OBJS = 2

    class IdGenerator():
        '''Circular integer ID generator.'''
        NULL_ID = -1

        def __init__(self, limit):
            self.limit = limit
            self.val = -1

        def __call__(self):
            self.val += 1

            if self.val > self.limit:
                self.val = 0

            return self.val

    def __init__(self, factory, startsize=0, maxsize=None):
        self.factory = factory
        self.idgen = Pool.IdGenerator(limit=sys.maxsize)
        self.leased = {}
        self.lock = RLock()
        self.maxsize = maxsize or sys.maxsize
        self.objs = deque([factory() for _ in range(startsize)])
        self.total = startsize

    def replenish(self):
        with self.lock:
            while len(self.objs) < Pool.MIN_OBJS and self.total < self.maxsize:
                self.objs.append(self.factory())
                self.total += 1

    def lease(self):
        try:
            with self.lock:
                self.replenish()

                obj = self.objs.popleft()
                _id = self.idgen()
                self.leased[_id] = obj

                LOGGER.debug('leased %d', _id)
                return _id, obj
        except IndexError:
            # We've degraded to an inability to cache further.
            # TODO: Log warning: consider increasing maxsize.
            LOGGER.debug('could not lease')
            return Pool.IdGenerator.NULL_ID, self.factory()

    def relinquish(self, _id):
        # TODO: Leak happens if thread dies without relinquishing obj.
        try:
            obj = self.leased.pop(_id)
            with self.lock:
                LOGGER.debug('relinquished %d', _id)
                self.objs.append(obj)
        except KeyError:
            pass

    def clear(self):
        with self.lock:
            self.total -= len(self.objs)
            self.objs.clear()
