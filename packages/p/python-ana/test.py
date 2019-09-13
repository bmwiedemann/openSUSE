import os
import gc
import ana
import nose
import pickle

import logging
l = logging.getLogger("ana.test")

class A(ana.Storable):
    def __init__(self, n):
        nose.tools.assert_false(hasattr(self, 'n'))

        self.n = n
        l.debug("%s.__init__", self)

    def __repr__(self):
        return "<A %s>" % str(self.n)

    def _ana_getstate(self):
        l.debug("%s._ana_getstate", self)
        return (self.n,)

    def _ana_setstate(self, s):
        self.n = s[0]
        l.debug("%s._ana_setstate", self)

    def _ana_getliteral(self):
        return { 'n': self.n }

def test_simple():
    ana.set_dl(ana.SimpleDataLayer())
    one = A(1)
    one.make_uuid()
    o = pickle.dumps(one)
    one_copy = pickle.loads(o)
    assert one is one_copy

    two = A(1)
    t = pickle.dumps(one)
    two_copy = pickle.loads(t)
    assert two_copy is not two

    assert pickle.load(open(os.path.join(os.path.dirname(__file__), 'test_pickle.p'), 'rb')).n == 1337

def write_a1337():
    a1337 = A(1337)
    a1337.make_uuid()
    pickle.dump(a1337, open(os.path.join(os.path.dirname(__file__), 'test_pickle.p'), 'w'))

def test_dict():
    ana.set_dl(ana.DictDataLayer())
    l.debug("Initializing 1")
    one = A(1)
    l.debug("Initializing 2")
    two = A(2)

    one.make_uuid()

    l.debug("Copying 1")
    one_p = pickle.dumps(one)
    one_copy = pickle.loads(one_p)
    l.debug("Copying 2")
    two_p = pickle.dumps(two)
    two_copy = pickle.loads(two_p)

    nose.tools.assert_is(one_copy, one)
    nose.tools.assert_is_not(two_copy, two)
    nose.tools.assert_equal(str(two_copy), str(two))

    nose.tools.assert_is(one, A.ana_load(one.ana_store()))
    nose.tools.assert_is(two, A.ana_load(two.ana_store()))

    two_copy2 = pickle.loads(pickle.dumps(two))
    nose.tools.assert_equal(str(two_copy2), str(two))

    l.debug("Initializing 3")
    three = A(3)
    three_str = str(three)
    l.debug("Storing 3")
    three_uuid = three.ana_store()
    l.debug("Deleting 3")
    del three
    gc.collect()
    nose.tools.assert_false(three_uuid in ana.get_dl().uuid_cache)
    l.debug("Loading 3")
    three_copy = A.ana_load(three_uuid)
    nose.tools.assert_equal(three_copy.ana_uuid, three_uuid) #pylint:disable=no-member
    nose.tools.assert_equal(str(three_copy), three_str)

    known = set()
    first_json = three_copy.to_literal(known)
    nose.tools.assert_true(three_copy.ana_uuid in first_json['objects'])
    nose.tools.assert_equal(first_json['objects'][three_copy.ana_uuid]['object']['n'], three_copy.n)
    nose.tools.assert_equal(first_json['value']['ana_uuid'], three_copy.ana_uuid)

    second_json = three_copy.to_literal(known)
    nose.tools.assert_false(three_copy.ana_uuid in second_json['objects'])
    nose.tools.assert_equal(second_json['value']['ana_uuid'], three_copy.ana_uuid)

def test_dir():
    ana.dl = ana.DirDataLayer(pickle_dir="/tmp/test_ana")
    one = A(1)
    nose.tools.assert_is(one, A.ana_load(one.ana_store()))
    nose.tools.assert_true(os.path.exists("/tmp/test_ana/%s.p" % one.ana_uuid))

    uuid = one.ana_uuid
    old_id = id(one)
    del one
    gc.collect()
    ana.dl = ana.DirDataLayer(pickle_dir="/tmp/test_ana")
    two = A.ana_load(uuid)
    nose.tools.assert_equals(uuid, two.ana_uuid)
    nose.tools.assert_not_equals(old_id, id(two))

    # reset the datalayer to make sure we handle it properly
    ana.set_dl(ana.DictDataLayer())
    try:
        two = A.ana_load(uuid)
        assert False
    except KeyError:
        pass
    two.ana_store()
    del two
    three = A.ana_load(uuid)
    assert uuid, three.ana_uuid

if __name__ == '__main__':
    import sys
    logging.getLogger("ana.test").setLevel(logging.DEBUG)
    logging.getLogger("ana.storable").setLevel(logging.DEBUG)
    logging.getLogger("ana.datalayer").setLevel(logging.DEBUG)
    logging.getLogger("ana.d").setLevel(logging.DEBUG)

    if len(sys.argv) > 1:
        globals()['test_%s' % sys.argv[1]]()
    else:
        test_simple()
        test_dict()
        test_dir()
