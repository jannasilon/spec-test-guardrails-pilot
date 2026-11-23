from datetime import date, time

import pytest
from pytest_bdd import given, parsers, scenarios, then, when

from timesheet import work_day

scenarios("work_day.feature")


@pytest.fixture
def ctx():
    return {"holidays": set()}


def _t(s: str) -> time:
    h, m = s.split(":")
    return time(int(h), int(m))


@given(parsers.parse("{d} is a public holiday"))
def holiday(ctx, d):
    ctx["holidays"].add(date.fromisoformat(d))


@given(parsers.parse("a shift on {weekday} {d} from {start} to {end} with a {brk:d}-minute break"))
def shift(ctx, weekday, d, start, end, brk):
    ctx.update(day=date.fromisoformat(d), start=_t(start), end=_t(end), brk=brk)


@when("the day is calculated")
def calculate(ctx):
    try:
        ctx["result"] = work_day(ctx["day"], ctx["start"], ctx["end"], ctx["brk"], ctx["holidays"])
    except ValueError as e:
        ctx["error"] = e


@then(parsers.parse("regular time is {m:d} minutes"))
def regular(ctx, m):
    assert ctx["result"].regular_minutes == m


@then(parsers.parse("overtime is {m:d} minutes"))
def overtime(ctx, m):
    assert ctx["result"].overtime_minutes == m


@then("the input is rejected")
def rejected(ctx):
    assert "error" in ctx
