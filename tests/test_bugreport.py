import pytest

from qa_toolkit.bugreport import BugReport, validate_bug_report


def make_valid():
    return BugReport(
        title="Login fails on mobile",
        steps=["Open app", "Tap login"],
        expected="Dashboard shown",
        actual="Error screen shown",
        severity="high",
    )


def test_valid_report():
    assert validate_bug_report(make_valid()) == []


def test_short_title():
    r = make_valid()
    r.title = "Bug"
    assert any("Title" in p for p in validate_bug_report(r))


def test_empty_title():
    r = make_valid()
    r.title = ""
    assert any("Title" in p for p in validate_bug_report(r))


def test_single_step():
    r = make_valid()
    r.steps = ["Open app"]
    assert any("steps" in p for p in validate_bug_report(r))


def test_no_steps():
    r = make_valid()
    r.steps = []
    assert any("steps" in p for p in validate_bug_report(r))


def test_missing_expected():
    r = make_valid()
    r.expected = ""
    assert any("Expected" in p for p in validate_bug_report(r))


def test_missing_actual():
    r = make_valid()
    r.actual = ""
    assert any("Actual" in p for p in validate_bug_report(r))


def test_expected_equals_actual():
    r = make_valid()
    r.expected = r.actual = "same"
    assert any("differ" in p for p in validate_bug_report(r))


def test_invalid_severity():
    r = make_valid()
    r.severity = "blocker"
    assert any("Severity" in p for p in validate_bug_report(r))


@pytest.mark.parametrize("sev", ["low", "medium", "high", "critical"])
def test_valid_severities(sev):
    r = make_valid()
    r.severity = sev
    assert validate_bug_report(r) == []


def test_multiple_problems():
    r = BugReport(title="x", steps=[], expected="", actual="", severity="bad")
    problems = validate_bug_report(r)
    assert len(problems) >= 4


def test_title_ends_with_period():
    r = make_valid()
    r.title = "Login fails on mobile."
    assert any("period" in p for p in validate_bug_report(r))


def test_severity_with_whitespace():
    r = make_valid()
    r.severity = "  high  "
    assert validate_bug_report(r) == []
