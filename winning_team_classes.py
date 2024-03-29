"""
Complete the Team class implementation. For the instance method get_win_percentage(), the formula is:
team_wins / (team_wins + team_losses)

Note: Use floating-point division.
"""


class Team:
    def __init__(self):
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0

    def get_win_percentage(self):
        # team_wins / (team_wins + team_losses)
        return self.team_wins / (self.team_wins + self.team_losses)


if __name__ == "__main__":

    team = Team()

    team_name = input()
    team_wins = int(input())
    team_losses = int(input())

    team.team_name = team_name
    team.team_wins = team_wins
    team.team_losses = team_losses

    if team.get_win_percentage() >= 0.5:
        print('Congratulations, Team', team.team_name,'has a winning average!')
    else:
        print('Team', team.team_name, 'has a losing average.')