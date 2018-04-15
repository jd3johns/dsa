import threading

import pytest

from pool.pool import Pool


@pytest.fixture(scope='module')
def factory():
    def fn():
        return 1

    return fn


def test_pool(factory):
    p = Pool(factory, startsize=2, maxsize=10)

    assert not len(p.leased)
    assert len(p.objs) == 2
    assert p.total == 2

    def do_work():
        _id, obj = p.lease()
        obj += 1
        p.relinquish(_id)

    threads = []
    for _ in range(1000):
        t = threading.Thread(target=do_work)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    assert not len(p.leased)
    assert len(p.objs) == 10
    assert p.total == 10
