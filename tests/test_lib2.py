from toto2.lib import who_am_i


def test_whoami2():

    res = who_am_i()

    assert "Santiago" in res.split()


def test_whoami2_fail():

    res = who_am_i()

    assert "Santiago" in res.split()
