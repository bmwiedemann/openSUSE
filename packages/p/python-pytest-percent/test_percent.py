import pytest


def test_1(required_percent):
    assert isinstance(required_percent, int)


def test_2():
    assert True


def test_3():
    assert True


def test_4():
    assert True


def test_5():
    assert False


@pytest.mark.skip
def test_6():
    pass


@pytest.mark.xfail
def test_7():
    assert False


@pytest.mark.xfail
def test_8():
    assert True
