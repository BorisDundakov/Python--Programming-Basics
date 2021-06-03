# start time -> 12:31
# end time -> 12:55
from math import floor


year_type = input()
holidays_per_year = int(input())
weekends_hometown = int(input())

leap_games = 0.15
weekends_sofia = 48 - weekends_hometown
saturday_games_sofia = weekends_sofia * 3/4
holiday_games_sofia = holidays_per_year * 2 /3
total_games = saturday_games_sofia + holiday_games_sofia + weekends_hometown

if year_type == "leap":
    total_games = total_games * leap_games + total_games

print(floor(total_games))