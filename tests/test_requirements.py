from qa_toolkit.requirements import check_requirements, max_length_rule


def test_all_pass():
    rules = {"not_empty": lambda v: bool(v), "is_str": lambda v: isinstance(v, str)}
    assert check_requirements("hello", rules) == {"not_empty": True, "is_str": True}


def test_some_fail():
    rules = {"not_empty": lambda v: bool(v), "is_int": lambda v: isinstance(v, int)}
    result = check_requirements("hello", rules)
    assert result["not_empty"] is True
    assert result["is_int"] is False


def test_empty_rules():
    assert check_requirements("anything", {}) == {}


def test_numeric_value():
    rules = {"positive": lambda v: v > 0, "even": lambda v: v % 2 == 0}
    assert check_requirements(4, rules) == {"positive": True, "even": True}


def test_failing_value():
    rules = {"positive": lambda v: v > 0}
    assert check_requirements(-1, rules) == {"positive": False}


def test_max_length_rule_pass():
    rules = {"short_enough": max_length_rule(10)}
    assert check_requirements("hello", rules) == {"short_enough": True}


def test_max_length_rule_fail():
    rules = {"short_enough": max_length_rule(3)}
    assert check_requirements("toolong", rules) == {"short_enough": False}
