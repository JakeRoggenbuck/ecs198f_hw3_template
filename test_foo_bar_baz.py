import pytest


def test_basic_inputs():
    from foo_bar_baz import foo_bar_baz

    assert foo_bar_baz(0) == ""
    assert foo_bar_baz(1) == "1"
    assert foo_bar_baz(2) == "1 2"

    assert foo_bar_baz(3) == "1 2 Foo"
    assert foo_bar_baz(5) == "1 2 Foo 4 Bar"

    assert foo_bar_baz(15) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz"

    out = foo_bar_baz(30)
    assert out.count("Foo") == 8
    assert out.count("Bar") == 4
    assert out.count("Baz") == 2

    out = foo_bar_baz(100)
    assert out.count("Foo") == 27
    assert out.count("Bar") == 14
    assert out.count("Baz") == 6

    assert "Foo" in foo_bar_baz(333)
    assert "Bar" in foo_bar_baz(200)

    for i in range(15):
        assert "Baz" not in foo_bar_baz(i)


def test_output_type():
    from foo_bar_baz import foo_bar_baz

    assert isinstance(foo_bar_baz(0), str)
    assert isinstance(foo_bar_baz(1), str)
    assert isinstance(foo_bar_baz(10), str)
    assert isinstance(foo_bar_baz(100), str)

    assert isinstance(foo_bar_baz(-1), str)

    assert isinstance(foo_bar_baz(3), str)
    assert isinstance(foo_bar_baz(5), str)
    assert isinstance(foo_bar_baz(30), str)


def test_edge_case_ints():
    from foo_bar_baz import foo_bar_baz

    import sys
    assert foo_bar_baz(-1) == ""
    assert foo_bar_baz(-sys.maxsize) == ""


def test_more_edge_case_ints():
    from foo_bar_baz import foo_bar_baz

    import sys
    assert foo_bar_baz(-1) == ""
    assert foo_bar_baz(-sys.maxsize) == ""

    assert foo_bar_baz(-100) == ""
    assert foo_bar_baz(0) == ""


def test_wrong_type():
    from foo_bar_baz import foo_bar_baz

    with pytest.raises(TypeError):
        foo_bar_baz("Rust")

    with pytest.raises(TypeError):
        foo_bar_baz(lambda x: x + 1)

    with pytest.raises(TypeError):
        foo_bar_baz(1.1)

    with pytest.raises(TypeError):
        foo_bar_baz(type)

    with pytest.raises(TypeError):
        foo_bar_baz(str)
