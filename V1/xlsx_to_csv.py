import csv, sys, requests
import pandas as pd
from helper import check_arguments, error, check_for_file

TOTAL = 0

argv = sys.argv
argc = len(argv)


# Use this to make CSV from EXCEL if one already is made for the week_number it will fail
excel = argv[1]
csv_out = f"week_{argv[2]}.csv"

def make_csv():
    if check_for_file(csv_out):
        error(f"csv for week number {argv[2]} already exists")

    elif check_arguments(excel, argc, argv):
        df = pd.read_excel(excel)
        df.columns = split_headers(df)
        new_dict = df.to_csv(csv_out, index=False)
    

def split_headers(excel_file):
    global TOTAL
    headers  = list()
    for i in excel_file.columns:
        if i.split("\n")[0] == "GRAND TOTAL":
            TOTAL = i.split("$")[1]
            i = "Name"
        headers.append(" ".join(i.split("\n")))
    return headers
    
class Games:
    def __init__(self, id, winner):
        self.id = id
        self.winner = winner



# OPEN CSV and parse against API

# API
url = f"http://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard?week={argv[2]}"
# url = f"http://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"
r = requests.get(url)
response = r.json()
# list of winning teams
winning_teams = list()

games = response["events"]
# LOOPS OVER EVERY GAME OF THE WEEK puts games into class with id number and winning team
for event in range(len(games)):
    winner = []
    game = games[event]["competitions"][0]["competitors"]
    for team in range(len(game)):
        try:
            if game[team]["winner"]:
                winning_teams.append(game[team]["team"]["abbreviation"])
        except KeyError:
            if team == 1:
                winning_teams.append(None)
            pass



make_csv()


picks = []
# load picks into memory
with open(csv_out) as f:
    reader = csv.DictReader(f)
    for i in reader:
        # START NEW
# THIS PUTS EVERY PICK INTO DICTIONARY {"picks": [], "name": "Billy", "points": "35.5"}
        new_dict = dict()
        new_dict["picks"] = list()
        for key, value in i.items():
            if key == "Name":
                new_dict["name"] = value
            elif key == "PTS ?":
                new_dict["points"] = value
            else:
                new_dict["picks"].append(value)
        # append to picks list which has everyone in it
        picks.append(new_dict)

# print()
# print(f"{picks[0]['name']}'s PICKS: \t\t\t {picks[0]['picks']}")
# print()
# print(f"WINNING TEAMS: \t\t\t\t {winning_teams}")
# print()



leaderboard = list()

for i in range(len(picks)):
    tally = dict()
    # counts correct guesses for winning teams
    count = 0
    name = picks[i]["name"]
    for j in range(len(winning_teams)):
        if winning_teams[j] != None:
            if winning_teams[j] == picks[i]["picks"][j]:
                count += 1
    tally["name"] = name
    tally["count"] = count
    leaderboard.append(tally)


leaderboard = sorted(leaderboard, key=lambda leader: leader["count"], reverse=True)


# PUT THIS INTO LEADERBOARD FILE
print("\nGRAND PRIZE: {TOTAL}\n")

place = 1
for i in range(len(leaderboard)-1):
    current_score = leaderboard[i]["count"]
    next_score = leaderboard[i+1]["count"]
    if current_score > next_score:
        print('{:<10} {:<20} Score: {:<20}'.format(f"{str(place)}.", leaderboard[i]["name"], leaderboard[i]["count"]))
        place += 1
    else:
        print('{:<10} {:<20} Score: {:<20}'.format(f"{str(place)}.", leaderboard[i]["name"], leaderboard[i]["count"]))
print()



