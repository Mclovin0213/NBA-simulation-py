
class Player:
    def __init__(self, fName, lName, pPos, jNum):
        self.first_name = fName
        self.last_name = lName
        self.player_position = pPos
        self.jersey_num = jNum
        
    def Season_stats(self):
        self.points_per_game
        self.rebounds_per_game
        self.assists_per_game
        self.steals_per_game
        self.blocks_per_game
        self.turnovers_per_game
        self.fouls_per_game
        
    def Influence_stats(self):
        # FG% in each area
        self.restricted_area
        self.in_the_paint
        self.midrange
        self.left_corner3
        self.right_corner3
        self.above_the_break3
        self.backcourt
        
        # % of shots in each area
        self.perc_fga_2pt
        self.perc_fga_2pt_ra
        self.perc_fga_2pt_itp
        self.perc_fga_2pt_mr
        
        self.perc_fga_3pt
        self.perc_fga_3pt_leftCorner3
        self.perc_fga_3pt_rightCorner3
        self.perc_fga_3pt_aboveTheBreak3

        # % of points in each area
        self.perc_pts_2pt
        self.perc_pts_2pt_mr
        self.perc_pts_2pt_pitp
        self.perc_pts_3pt
        self.perc_pts_ft
        