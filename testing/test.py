from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import commonteamroster


test = players.find_players_by_full_name('Stephen Curry')

test1 = teams.find_teams_by_city('miami')

test2 = teams.get_teams()

test3 = commonteamroster.CommonTeamRoster(1610612737).get_data_frames()

print(test3)
