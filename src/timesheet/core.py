"""Time-reporting library. Intentionally unimplemented: see docs/requirements.md."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date, time
from typing import Iterable


@dataclass(frozen=True)
class DayResult:
    regular_minutes: int
    overtime_minutes: int

    @property
    def total_minutes(self) -> int:
        return self.regular_minutes + self.overtime_minutes


@dataclass(frozen=True)
class WeekResult:
    regular_minutes: int
    overtime_minutes: int

    @property
    def total_minutes(self) -> int:
        return self.regular_minutes + self.overtime_minutes


@dataclass(frozen=True)
class Entry:
    day: date
    start: time
    end: time
    break_minutes: int = 0


def work_day(
    day: date,
    start: time,
    end: time,
    break_minutes: int = 0,
    holidays: Iterable[date] = (),
) -> DayResult:
    raise NotImplementedError


def work_week(entries: Iterable[Entry], holidays: Iterable[date] = ()) -> WeekResult:
    raise NotImplementedError
