from dataclasses import dataclass

VALID_SEVERITIES = {"low", "medium", "high", "critical"}


@dataclass
class BugReport:
    title: str
    steps: list[str]
    expected: str
    actual: str
    severity: str


def validate_bug_report(report: BugReport) -> list[str]:
    problems = []

    if not report.title or len(report.title.strip()) < 5:
        problems.append("Title is missing or too short (min 5 chars).")

    if not report.steps or len(report.steps) < 2:
        problems.append("Provide at least two reproduction steps.")

    if not report.expected:
        problems.append("Expected result is missing.")

    if not report.actual:
        problems.append("Actual result is missing.")

    if report.expected and report.actual and report.expected == report.actual:
        problems.append("Expected and actual results must differ.")

    if report.severity.lower() not in VALID_SEVERITIES:
        problems.append(f"Severity must be one of {sorted(VALID_SEVERITIES)}.")

    return problems
