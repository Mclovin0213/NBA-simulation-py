import imp

from nba_api.stats.endpoints import playerdashboardbyshootingsplits

test = playerdashboardbyshootingsplits.PlayerDashboardByShootingSplits(player_id=201939)

roasted = test.shot_area_player_dashboard.get_data_frame().get('FG_PCT')[0]

print(roasted)