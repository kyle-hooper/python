import random
import time

"""This is a simple python sweepstake for World Cup 2022 based on prettystatics method https://prettystatic.com/euro2020-sweepstake-with-python/

Here's how you could set up your sweepstake:
 - £5 for 1 entry
 - £5 gets you 2 teams
 - There are 32 teams, so a maximum of 16 people can enter
 - Teams are split into 2 tiers based on https://www.fifa.com/fifa-world-ranking/men?dateId=id13792
 - Every person gets 1 team from tier_one and one team from tier_two

Total prize pot of £80 (£5 x 16). Possible Prizes:
 - The winning team - £30
 - The runner-up team - £20
 - The tier_two team who finishes furthest (decided by points in group stage if no tier_two team reaches the knock outs, then goal difference in case of a tie) - £10
 - The team with the lowest points in the group stage (decided by worst goal difference, then most goals conceded in case of a tie) - £10
 - The team with the worst goal difference in one game (decided on number of goals conceded in case of tie, then most goals conceded in one half in case of a tie) - £10

Note:
 - If someone enters twice, put their name in twice, if someone enters three times, put their name in three times etc etc
 - I put in a 2 second delay between each draw in case you want to record your screen and do some running commentary

Hope you have some fun organising this! Come on England
"""

tier_one_teams = ["Brazil", "Belgium", "Argentina", "France", 
"England", "Netherlands", "Portugal", "Denmark", 
"Germany", "Croatia", "Mexico", "Uruguay", 
"USA", "Senegal", "Spain", "Wales"]

tier_two_teams = ["Qatar", "Ecuador", "Saudi Arabia", "Poland", 
"Australia", "Tunisia", "IR Iran", "Costa Rica", 
"Japan", "Canada", "Morocco", "Serbia",
"Switzerland", "Cameroon", "Ghana", "Korea"]

names = ["Name 1", "Name 2", "Name 3", "Name 4", 
"Name 5", "Name 6", "Name 7", "Name 8", 
"Name 9", "Name 10", "Name 11", "Name 12", 
"Name 13", "Name 14", "Name 15", "Name 16"]

random.shuffle(tier_one_teams)
random.shuffle(tier_two_teams)
random.shuffle(names)

tier_one_sweep = list(zip(tier_one_teams, names))
tier_two_sweep = list(zip(tier_two_teams, names))

for s in tier_one_sweep:
    print(s[0] + ' --> ' + s[1])
    time.sleep(2)

for s in tier_two_sweep:
    print(s[0] + ' --> ' + s[1])
    time.sleep(2)