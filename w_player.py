from fileinput import filename
from nba_api.stats.endpoints import playerdashboardbyshootingsplits

nba_playerID = 201939
filename = 'test.txt'

i_player = playerdashboardbyshootingsplits.PlayerDashboardByShootingSplits(nba_playerID)

i_player.shot_area_player_dashboard.get_data_frame().get('FG_PCT')

with open(f"Data/PlayerStats/{filename}", 'a') as file_object:
    
    for index in range(0, 6):
        file_object.write(f"{str(i_player.shot_area_player_dashboard.get_data_frame().get('FG_PCT')[index])}\n")
        

