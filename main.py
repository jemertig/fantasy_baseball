from pybaseball import cache
from pybaseball import batting_stats_range
from pybaseball import pitching_stats_range



cache.enable()


with open('team.txt') as f:
    team = f.read().splitlines()

# retrieve all players' stats for the 2024 season
pitcher_data = pitching_stats_range("2023-01-21", "2023-12-31")
batter_data = batting_stats_range("2023-01-21", "2023-12-31")

batter_data = batter_data[batter_data['Name'].isin(team)]
pitcher_data = pitcher_data[pitcher_data['Name'].isin(team)]

#batter_data.drop(batter_data[batter_data['Name'] != 'Ronald Acuna Jr.'].index, inplace = True)
batter_data.to_csv("output.csv", index=False)
pitcher_data.to_csv("output.csv", index=False, mode="a")


print(batter_data)
print(pitcher_data)


