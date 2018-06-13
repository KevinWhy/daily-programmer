#!py -3
#
#Input Description
#File containing a list of basketball games.
#Should follow the output from from:
#	https://www.masseyratings.com/scores.php?s=298892&sub=12801&all=1
#Assumes that the last game = championship game.
#
#Output Description
#A list of transitive champions.
#Aka: All teams who beat the champion team
#

import argparse
import re

# Parse one line of the input file
gameRegexStr = (
		r'^(\d{4})-(\d{2})-(\d{2})' # Date = 1st 3 groups
		+ r'\s+@?(\D+[^\s\d])\s+'   # 1st team name  = 4th group (excludes optional @ prefix)
		+ r'(\d+)'                  # 1st team score = 5th group
		+ r'\s+@?(\D+[^\s\d])\s+'   # 2nd team name  = 6th group (excludes optional @ prefix)
		+ r'(\d+)'                  # 2nd team score = 7th group
)
gameRegex = re.compile(gameRegexStr)

#-----------------------------------

class GameInfo:
	team1 = None
	team2 = None
	winning_team = None
	losing_team = None
	def __init__(self, regex_match):
		self.team1 = regex_match.group(4)
		self.score1 = int(  regex_match.group(5)  )
		self.team2 = regex_match.group(6)
		self.score2 = int(  regex_match.group(7)  )
		if self.score1 > self.score2:
			self.winning_team = self.team1
			self.losing_team = self.team2
		elif self.score2 > self.score1:
			self.losing_team = self.team1
			self.winning_team = self.team2
	
	def __str__(self):
		return (
				  '<GAME_INFO____Winner: '+ self.winning_team +'\n'
				+ '\tTeam 1: '+ self.team1 +'\t\tScore: '+ str(self.score1) +'\n'
				+ '\tTeam 2: '+ self.team2 +'\t\tScore: '+ str(self.score2)
				+ '>'
		)

#-----------------------------------

parser = argparse.ArgumentParser(description='Calculate a list of transitive champions.')
parser.add_argument('input_file', metavar='file', type=argparse.FileType('r'),
                    help='File to read basketball games from')
args = parser.parse_args()

# Read file for teams that won
games = []
for line in args.input_file:
	regex_match = gameRegex.search(line)
	if regex_match:
		games.append(GameInfo(regex_match))
champion_team = games[-1].winning_team

# Build dictionary of teams
teams = set() # Set of all teams that were in this match
winners = {}  # Key = team that lost. Value = set of teams that won against that team
for game in games:
	teams.add(game.team1)
	teams.add(game.team2)
	if not winners.get(game.losing_team, None):
		winners[game.losing_team] = set()
	winners[game.losing_team].add(game.winning_team)

# Finally, find list of transitive winners
transitive_champs = set({champion_team}) # Champion =/= transitive champ, but is needed to kick-start the loop
prev_num_transitive_champs = 0
while prev_num_transitive_champs != len(transitive_champs): # If any team added to set, keep loop going
	prev_num_transitive_champs = len(transitive_champs)
	# If a team beat any transitive_champ, add them to set of transitive_champs
	for losing_team, winning_teams in winners.items():
		if losing_team in transitive_champs:
			transitive_champs = winning_teams | transitive_champs

transitive_champs.remove(champion_team) # Don't include champion_team in transitive_champs

#--------------------------------------
# Print results

print('Number of Teams:', len(teams))
print('Champion Team:')
print('--------------------------')
print('\t',champion_team)
print()

print('Number of Transitive Champions:', len(transitive_champs))
print('Transitive Champions:')
print('--------------------------')
print('\t' + '\n\t'.join(transitive_champs))
