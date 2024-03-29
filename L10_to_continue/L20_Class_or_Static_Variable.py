class Player:
    team_run = 0    # static or class variable
    def __init__(self, run):
        self.run = run  # Instance Variable

    
    def hit_four(self): # Instance Method
        self.run += 4
        Player.team_run += 4

    def hit_six(self):  # Instance Method
        self.run += 6
        Player.team_run += 6

#============================================================================

print(Player.team_run) 

sakib = Player(0)
tamim = Player(0)


sakib.hit_six()
tamim.hit_four()
tamim.hit_four()


print("Sakib:", sakib.run)
print("Tamim:", tamim.run)

print("Team Run:",Player.team_run)