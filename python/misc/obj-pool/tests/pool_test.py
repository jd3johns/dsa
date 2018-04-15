import logging
import threading

import pytest

from pool.pool import Pool


MAX_POOL_SIZE = 10


@pytest.fixture(scope='function')
def pool():
    def factory():
        return {}

    return Pool(factory, startsize=2, maxsize=MAX_POOL_SIZE)


def test_pool_init(pool):
    assert not len(pool.leased)
    assert len(pool.objs) == 2
    assert pool.total == 2


def test_pool_relinquish(pool):
    _id, _ = pool.lease()
    assert len(pool.leased) == 1

    for _ in range(3):
        pool.lease()

    assert len(pool.leased) == 4
    assert pool.total == 4 + 1

    pool.relinquish(_id)

    assert len(pool.leased) == 3
    assert pool.total == 4 + 1


def test_pool_max(pool):
    for _ in range(11):
        pool.lease()

    assert len(pool.leased) == MAX_POOL_SIZE


def test_pool_threading(pool):
    def do_work():
        _id, obj = pool.lease()
        obj['foo'] = 1
        pool.relinquish(_id)

    threads = []
    for _ in range(1000):
        t = threading.Thread(target=do_work)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    assert not len(pool.leased)
    assert len(pool.objs) >= 2
    assert pool.total >= 2

    # State persists.
    for obj in pool.objs:
        assert obj.get('foo') == 1
