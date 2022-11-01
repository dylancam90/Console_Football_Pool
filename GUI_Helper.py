# START AT LINE 118
import csv, sys, requests, os
from docx.api import Document
import pandas as pd

TOTAL = 0

def make_csv(docx_path, csv_name):
    document = Document(docx_path)
    rows = read_docx(document)
    head = split_headers(rows)  
    df = pd.DataFrame(rows[1:], columns=head)
    df.to_csv(csv_name, index=False)



def read_docx(document):
    total_rows = list()
    for table in document.tables:
        for row in table.rows:
            text = [" ".join(cell.text.strip().split("\n")) for cell in row.cells if cell.text != ""]
            total_rows.append(text)
    return total_rows


def split_headers(document):
    global TOTAL
    buffer = list()
    for i in range(len(document[0])):
        current = document[0][i].strip()
        if i == 0:
            TOTAL = current.split("$")[1]
            current = "Name"
        buffer.append(" ".join(current.split("\n")))
    # if a bye column is in list it will be removed
    headers = [item for item in buffer if "BYE" not in item]
    document[0] = headers
    return headers
    


# OPEN CSV and parse against API
def api(week_num):
    # API
    url = f"http://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard?week={week_num}"
    r = requests.get(url)
    response = r.json()
    # list of winning teams
    winning_teams = list()

    games = response["events"]
    # LOOPS OVER EVERY GAME OF THE WEEK puts games into class with id number and winning team
    for event in range(len(games)):
        game = games[event]["competitions"][0]["competitors"]
        total_score = 0 # here
        for team in range(len(game)):
            try:
                total_score += int(game[team]["score"]) # here

                if game[team]["winner"]:
                    # winning_teams.append(game[team]["team"]["abbreviation"])
                    winning_teams.append({"win": game[team]["team"]["abbreviation"]})
            except KeyError:
                if team == 1:
                    # winning_teams.append(None)
                    winning_teams.append({"win": None, "score": None})
                pass
        winning_teams[event]["score"] = total_score # here
    return winning_teams




def refine_picks(csv_name):
    picks = []
    # load picks into memory
    with open(csv_name) as f:
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
    return picks



def make_leaderboard(winning_teams, picks, total):
    leaderboard = list()
    for i in range(len(picks)):
        # counts correct guesses for winning teams
        count = 0
        name = picks[i]["name"]
        # this section of changed because the api shuffled the order of events
        for j in range(len(winning_teams)):
            # if winning_teams[j] in picks[i]["picks"]:
            if winning_teams[j]["win"] in picks[i]["picks"]:
                count += 1    
        leaderboard.append({"name": name, "count": count, "points": picks[i]["points"]})

    leaderboard = sorted(leaderboard, key=lambda leader: leader["count"], reverse=True)


    # PUT THIS INTO LEADERBOARD FILE
    print(f"\nGRAND PRIZE: {TOTAL}\n")
    print(f"TOTAL PLAYERS {len(leaderboard)}\n")


    # START HERE AND TRY TO PLACE BY WIN COUNT AND SCORE
    #last_score = check_last_game(winning_teams)

    board = list()
    place = 1   
    for i in range(len(leaderboard)-1):
        current_score = leaderboard[i]["count"]
        next_score = leaderboard[i+1]["count"]
        if current_score > next_score:
            # print('{:<10} {:<20} Score: {:<20}'.format(f"{str(place)}.", leaderboard[i]["name"], leaderboard[i]["count"]))
            board.append({"place": place, "name": leaderboard[i]["name"], "count": leaderboard[i]["count"], "points": leaderboard[i]["points"]})
            place += 1
        else:
            # print('{:<10} {:<20} Score: {:<20}'.format(f"{str(place)}.", leaderboard[i]["name"], leaderboard[i]["count"]))
            board.append({"place": place, "name": leaderboard[i]["name"], "count": leaderboard[i]["count"], "points": leaderboard[i]["points"]})
    print(board[0])
    return board


def check_last_game(winning_teams):
    for i in winning_teams:
        if i["win"] == None:
            return None
    print(winning_teams[-1])
    return winning_teams[-1]["score"]











""" 

# OPEN CSV and parse against API
def api(week_num):
    # API
    url = f"http://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard?week={week_num}"
    r = requests.get(url)
    response = r.json()
    # list of winning teams
    winning_teams = list()

    games = response["events"]
    # LOOPS OVER EVERY GAME OF THE WEEK puts games into class with id number and winning team
    for event in range(len(games)):
        game = games[event]["competitions"][0]["competitors"]
        for team in range(len(game)):
            try:
                if game[team]["winner"]:
                    winning_teams.append(game[team]["team"]["abbreviation"])
            except KeyError:
                if team == 1:
                    winning_teams.append(None)
                pass
    return winning_teams



def make_leaderboard(winning_teams, picks, total):
    leaderboard = list()
    for i in range(len(picks)):
        # counts correct guesses for winning teams
        count = 0
        name = picks[i]["name"]
        # this section of changed because the api shuffled the order of events
        for j in range(len(winning_teams)):
            if winning_teams[j] in picks[i]["picks"]:
                count += 1    
        leaderboard.append({"name": name, "count": count, "points": picks[i]["points"]})

    leaderboard = sorted(leaderboard, key=lambda leader: leader["count"], reverse=True) 
    
"""