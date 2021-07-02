import statsapi
team = statsapi.get('draft', {'year':2020,'teamId':147})
print(team)