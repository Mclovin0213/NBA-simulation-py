from nba_api.stats.static import players, teams

test = players.find_players_by_full_name('Stephen Curry')

test1 = teams.find_teams_by_city('miami')

print(test)
