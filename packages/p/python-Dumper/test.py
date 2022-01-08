from __future__ import print_function
from dumper import dump, dumps, Dumper
import dumper
import io
import sys

buff = io.StringIO()
dumper.default_dumper = Dumper(output=buff)

# BEGIN TEST CASES

def do_dump_scalars():
    dump(1)
    dump('a')
    dump("foo")
    dump('''string
with a newline''')
    return "1'a''foo''string\\nwith a newline'"

def test_do_dump_scalars():
    assert_output_as_expected(do_dump_scalars)
    
def do_dumps_multi_values():
    s = dumps(1, " is less than ", 10) # returns unicode string in py2
    if sys.version < (3, 0):
        s = s.encode('ascii', 'replace') # convert back to regular string
    dump(s)
    return "\"1' is less than '10\""

def test_dumps_multi_values():
    assert_output_as_expected(do_dumps_multi_values)
    
def do_dump_json():
    obj = {
            "httpCode": 200,
            "extensionData": [
                {
                    "extensionValue": "egg"
                }
            ]
        }
    dump(obj)
    return '''
<dict at {WORD}>:
  httpCode: 200
  extensionData: <list at {WORD}>
    0: <dict at {WORD}>:
      extensionValue: 'egg'
'''

def test_do_dump_json():
    assert_output_matches_template(do_dump_json)
    
# END TEST CASES
    
def text_type(val):
    if sys.version < '3':
        return unicode(val)
    else:
        return str(val)
    
def assertMatching(a, b):
    ''' Asserts that the lines from string, a, match the lines in the string, b.
    a is the expected string / pattern
    b is the actual string
    We ignore leading/trailing whitespace
    '''
    a_lines = a.strip().split("\n")
    b_lines = b.strip().split("\n")
    if len(a_lines) != len(b_lines):
        raise AssertionError("a has " + text_type(len(a_lines)) + ", but b has " + text_type(len(b_lines)) + " lines: a={" + a + "}, b={" + b + "}")
    for i in range(0, len(a_lines)):
        assert a_lines[i] == b_lines[i]

def assert_output_matches_template(func):
    # TODO: implement this
    pass
  
def assert_output_as_expected(func):
    # buffer stdout
    try:
        output = func()
        assertMatching(output, buff.getvalue())
    finally:
        # reset the buffer for the next test
        buff.truncate(0)
        buff.seek(0)

if __name__ == "__main__":
    
    l1 = [3, 5, 'hello']
    t1 = ('uh', 'oh')
    l2 = ['foo', t1]
    d1 = {'k1': 'val1',
          'k2': l1,
          'k2': l2}

    print("a list: ", dumps (l1), "; a tuple: ", dumps (t1))
    print("a complex list: ")
    dump (l2)
    dump (d1)
    print("same dict, printed from dumps(): ")
    print(dumps(d1))
    dump (19)
    dump ("\nMy birth year!\n")

    dumper = Dumper (max_depth=1)
    l = ['foo', ['bar', 'baz', (1, 2, 3)]]
    dumper.dump (l)
    dumper.max_depth = 2
    dumper.dump (l)
    l[1][2] = tuple (range (11))
    dumper.dump (l)
    dumper.max_depth = None
    print(dumper.max_depth)
    
    class Foo: pass
    class Bar: pass
