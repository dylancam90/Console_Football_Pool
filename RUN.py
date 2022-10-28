import csv, sys, requests
from docx.api import Document
import pandas as pd
from new_helper import check_arguments, error, check_for_file, remove_file

argv = sys.argv
argc = len(argv)

TOTAL = 0

# Use this to make CSV from EXCEL if one already is made for the week_number it will fail
doc = argv[1]
csv_out = f"Week {argv[2]}.csv"


def main():
    make_csv()
    winning_teams = api()
    picks = refine_picks()
    make_leaderboard(winning_teams, picks, TOTAL)
    remove_file(csv_out)


def make_csv():
    if check_arguments(doc, argc, argv):
        document = Document(doc)
        rows = read_docx(document)
        head = split_headers(rows)  

        df = pd.DataFrame(rows[1:], columns=head)
        df.to_csv(csv_out, index=False)



def read_docx(document):
    total_rows = list()
    for table in document.tables:
        for row in table.rows:
            text = [" ".join(cell.text.strip().split("\n")) for cell in row.cells if cell.text != ""] # if cell.text not in ("BYE", "")
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
def api():
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
    return winning_teams







def refine_picks():
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
    return picks



def make_leaderboard(winning_teams, picks, total):
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
    print(f"\nGRAND PRIZE: {TOTAL}\n")

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



if __name__ == "__main__":
    main()


# print()
# print(f"{picks[0]['name']}'s PICKS: \t\t\t {picks[0]['picks']}")
# print()
# print(f"WINNING TEAMS: \t\t\t\t {winning_teams}")
# print()