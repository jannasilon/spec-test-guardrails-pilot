Feature: Daily working time

  Scenario: R1/R2 Hours up to 8 on a weekday are regular time
    Given a shift on Monday 2026-11-23 from 08:00 to 16:30 with a 30-minute break
    When the day is calculated
    Then regular time is 480 minutes
    And overtime is 0 minutes

  Scenario: R2 Hours above 8 on a weekday are overtime
    Given a shift on Monday 2026-11-23 from 08:00 to 18:00 with a 60-minute break
    When the day is calculated
    Then regular time is 480 minutes
    And overtime is 60 minutes

  Scenario: R3 A long day always loses at least 30 minutes of break
    Given a shift on Tuesday 2026-11-24 from 08:00 to 15:00 with a 10-minute break
    When the day is calculated
    Then regular time is 390 minutes

  Scenario: R4 Saturday work is all overtime
    Given a shift on Saturday 2026-11-28 from 10:00 to 14:00 with a 0-minute break
    When the day is calculated
    Then regular time is 0 minutes
    And overtime is 240 minutes

  Scenario: R5 A night shift ends the next day
    Given a shift on Wednesday 2026-11-25 from 22:00 to 04:00 with a 30-minute break
    When the day is calculated
    Then regular time is 330 minutes

  Scenario: R6 A break as long as the shift is rejected
    Given a shift on Thursday 2026-11-26 from 09:00 to 10:00 with a 60-minute break
    When the day is calculated
    Then the input is rejected

  Scenario: R9 Public holidays count like weekends
    Given 2026-12-24 is a public holiday
    And a shift on Thursday 2026-12-24 from 09:00 to 12:00 with a 0-minute break
    When the day is calculated
    Then overtime is 180 minutes
