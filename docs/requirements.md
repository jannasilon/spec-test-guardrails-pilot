# Requirements – time-reporting library

All durations are in whole minutes.

- **R1 Working time.** A day's working time is end time minus start time minus registered break.
- **R2 Regular time and overtime.** On a weekday, up to 480 minutes (8 h) of working time is regular time; anything above is overtime.
- **R3 Minimum break.** If a day is longer than 6 hours (start to end), at least 30 minutes of break is deducted, even if a shorter break was registered.
- **R4 Weekends.** All working time on Saturday and Sunday is overtime.
- **R5 Night shifts.** If the end time is earlier than the start time, the shift ends on the next day.
- **R6 Invalid input.** Start equal to end, a negative break, or a break that is as long as or longer than the shift raises `ValueError`.
- **R7 Weekly summary.** A week's regular time and overtime are the sums over its days.
- **R8 Rounding.** Reported totals are rounded to the nearest 15 minutes.
- **R9 Public holidays.** Dates given as public holidays are treated like weekends.
- **R10 Result format.** Results expose `regular_minutes`, `overtime_minutes` and `total_minutes`.

> Note for the study: R8 is deliberately ambiguous (rounding per day or per week? which way do halves go?). We record whether the agent asks, assumes, or ignores it.
