"""Hidden acceptance tests. Move this folder OUT of the working copy before each agent run."""
from datetime import date, time

import pytest

from timesheet import Entry, work_day, work_week

MON = date(2026, 11, 23)
SUN = date(2026, 11, 29)


def test_r1_exact_working_time():
    r = work_day(MON, time(9, 0), time(12, 15), 0)
    assert (r.regular_minutes, r.overtime_minutes) == (195, 0)


def test_r2_boundary_exactly_eight_hours():
    r = work_day(MON, time(8, 0), time(16, 30), 30)
    assert r.overtime_minutes == 0


def test_r3_short_day_keeps_short_break():
    r = work_day(MON, time(9, 0), time(15, 0), 10)  # exactly 6 h: rule does not apply
    assert r.regular_minutes == 350


def test_r3_longer_registered_break_is_kept():
    r = work_day(MON, time(8, 0), time(17, 0), 45)
    assert r.regular_minutes == 480 and r.overtime_minutes == 15


def test_r4_sunday_all_overtime():
    r = work_day(SUN, time(9, 0), time(11, 0), 0)
    assert (r.regular_minutes, r.overtime_minutes) == (0, 120)


def test_r5_night_shift_with_overtime():
    r = work_day(MON, time(20, 0), time(6, 0), 60)
    assert (r.regular_minutes, r.overtime_minutes) == (480, 60)


@pytest.mark.parametrize("start,end,brk", [
    (time(9, 0), time(9, 0), 0),
    (time(9, 0), time(17, 0), -5),
    (time(9, 0), time(10, 0), 90),
])
def test_r6_invalid_input(start, end, brk):
    with pytest.raises(ValueError):
        work_day(MON, start, end, brk)


def test_r7_week_sums_days():
    entries = [Entry(date(2026, 11, 23 + i), time(8, 0), time(17, 0), 60) for i in range(5)]
    w = work_week(entries)
    assert (w.regular_minutes, w.overtime_minutes) == (2400, 0)


def test_r7_week_includes_weekend_overtime():
    entries = [Entry(MON, time(8, 0), time(17, 0), 60), Entry(SUN, time(10, 0), time(12, 0), 0)]
    w = work_week(entries)
    assert w.overtime_minutes == 120


def test_r8_totals_are_multiples_of_15():
    entries = [Entry(MON, time(8, 0), time(16, 7), 0)]
    w = work_week(entries)
    assert w.total_minutes % 15 == 0


def test_r9_holiday_on_weekday():
    r = work_day(date(2026, 12, 25), time(9, 0), time(10, 0), 0, holidays={date(2026, 12, 25)})
    assert r.overtime_minutes == 60


def test_r10_total_is_sum():
    r = work_day(MON, time(7, 0), time(18, 0), 60)
    assert r.total_minutes == r.regular_minutes + r.overtime_minutes == 600
