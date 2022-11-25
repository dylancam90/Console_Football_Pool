from more_itertools import first, last
from numpy import sort


leaderboard = [{'name': 'LA DONA', 'count': 12, 'points': '46'}, {'name': 'MADNESS', 'count': 12, 'points': '44'}, {'name': 'JT', 'count': 12, 'points': '54'}, {'name': 'HOT SAUCE', 'count': 11, 'points': '51'}, {'name': 'COOP', 'count': 11, 'points': '47'}, {'name': 'DYAN', 'count': 11, 'points': '58'}, {'name': 'VIOLATOR', 'count': 11, 'points': '49.5'}, {'name': 'HOLLAND', 'count': 11, 'points': '48'}, {'name': 'SPORTMOMMA', 'count': 11, 'points': '47'}, {'name': 'AMY', 'count': 11, 'points': '59'}, {'name': 'BLACK FALCONS', 'count': 11, 'points': '55'}, {'name': 'WUTANG', 'count': 10, 'points': '47'}, {'name': 'GHOST', 'count': 10, 'points': '47'}, {'name': 'GRAND NATIONAL KID', 'count': 10, 'points': '45'}, {'name': 'VYNAL', 'count': 10, 'points': '48'}, {'name': 'JOSH ANFANG', 'count': 10, 'points': '57'}, {'name': 'DAVID MARTIN', 'count': 10, 'points': '48'}, {'name': 'GRIEFO', 'count': 10, 'points': '54.5'}, {'name': 'VINNY', 'count': 10, 'points': '50'}, {'name': 'PAIGE', 'count': 10, 'points': '61'}, {'name': 'BLACK BEARD', 'count': 10, 'points': '50.5'}, {'name': 'DREW', 'count': 10, 'points': '53'}, {'name': 'AJ MIKE', 'count': 10, 'points': '47'}, {'name': 'CHUKAS', 'count': 10, 'points': '55'}, {'name': 'AUBREY', 'count': 9, 'points': '43'}, {'name': 'SWIFT', 'count': 9, 'points': '37'}, {'name': 'RIZZ GOD', 'count': 9, 'points': '37'}, {'name': 'BANG BANG', 'count': 9, 'points': '50.5'}, {'name': 'NO MO BS', 'count': 9, 'points': '51'}, {'name': 'CAMPBELL', 'count': 9, 'points': '49'}, {'name': 'YEEZUS', 'count': 9, 'points': '48'}, {'name': 'DILL27', 'count': 9, 'points': '51'}, {'name': 'GREY BUSH', 'count': 9, 'points': '56'}, {'name': 'SNAKES', 'count': 9, 'points': '45'}, {'name': 'J.C', 'count': 9, 'points': '46'}, {'name': 'BOBO', 'count': 9, 'points': '58'}, {'name': 'JAB', 'count': 9, 'points': '47'}, {'name': 'CHUY', 'count': 9, 'points': '48'}, {'name': 'MARIO', 'count': 9, 'points': '43'}, {'name': 'ARMANI', 'count': 9, 'points': '48'}, {'name': 'HUGO C.', 'count': 9, 'points': '42'}, {'name': 'VEE', 'count': 9, 'points': '50'}, {'name': 'RULAS 1', 'count': 8, 'points': '48'}, {'name': 'EL GUEY', 'count': 8, 'points': '45'}, {'name': 'CALACO', 'count': 8, 'points': '48'}, {'name': 'THE KING', 'count': 8, 'points': '39'}, {'name': 'PHX', 'count': 8, 'points': '38'}, {'name': 'BIZO', 'count': 8, 'points': '45'}, {'name': 'RAIDER DAVID', 'count': 8, 'points': '45'}, {'name': 'DA BEARS', 'count': 8, 'points': '49'}, {'name': 'JEMMA', 'count': 8, 'points': '42'}, {'name': 'MERK', 'count': 8, 'points': '63'}, {'name': 'EL CHAVO', 'count': 8, 'points': '42'}, {'name': 'LA GATA', 'count': 8, 'points': '45'}, {'name': 'MIKE STODDARD', 'count': 8, 'points': '45'}, {'name': 'OSCAR', 'count': 8, 'points': '48'}, {'name': 'GORDINFLAS', 'count': 7, 'points': '46'}, {'name': 'EL ESTUPID', 'count': 7, 'points': '44'}, {'name': 'RS', 'count': 7, 'points': '47'}, {'name': 'CHILAN', 'count': 7, 'points': '50'}, {'name': 'FINIKERA', 'count': 7, 'points': '44'}, {'name': 'NIGG', 'count': 7, 'points': '48'}, {'name': 'NATE', 'count': 7, 'points': '55'}, {'name': 'NADDYA', 'count': 7, 'points': '50'}, {'name': 'JUNIOR D', 'count': 7, 'points': '54'}, {'name': 'ESTE VATO', 'count': 7, 'points': '45.5'}, {'name': 'CHRIS PARALIEU', 'count': 6, 'points': '47.5'}, {'name': 'TU PAPI', 'count': 6, 'points': '36'}, {'name': 'SBNINJA', 'count': 5, 'points': '52'}, {'name': 'JOSE R.M.', 'count': 4, 'points': '45'}]
winning_teams = [{'win': 'BAL', 'score': 49}, {'win': 'DEN', 'score': 38}, {'win': 'ATL', 'score': 71}, {'win': 'DAL', 'score': 78}, {'win': 'MIA', 'score': 58}, {'win': 'MIN', 'score': 60}, {'win': 'NO', 'score': 24}, {'win': 'NE', 'score': 39}, {'win': 'PHI', 'score': 48}, {'win': 'TEN', 'score': 27}, {'win': 'WSH', 'score': 33}, {'win': 'SF', 'score': 45}, {'win': 'SEA', 'score': 40}, {'win': 'BUF', 'score': 44}, {'win': 'CLE', 'score': 45}]


def print_l(board):
    for i in board[:3]:
        print(i)

print_l(leaderboard)

def check_last_game(winning_teams):
    for i in winning_teams:
        if i["win"] == None:
            return None
    return winning_teams[-1]["score"]


last_score = check_last_game(winning_teams)
place = 1   

# USE THIS JUST FOR FIRST PLACE TEAMS WHILE SORTING
# https://www.geeksforgeeks.org/python-program-for-insertion-sort/

for i in range(len(leaderboard)):
    if i == len(leaderboard) - 1:
        current_score, next_score = leaderboard[len(leaderboard)-1]["count"], leaderboard[len(leaderboard)-2]["count"]
    else:
        current_score, next_score = leaderboard[i]["count"], leaderboard[i+1]["count"]
    
    if last_score != None and place == 1:
        current_points, next_points = last_score - float(leaderboard[i]["points"]), last_score - float(leaderboard[i+1]["points"])
        print(current_points, next_points)
        if current_points < next_points:
            wins = leaderboard[i]['count']
            first_place = [i for i in leaderboard if i['count'] == wins]
            

    if current_score > next_score:
        leaderboard[i]["place"] = place
        place += 1
    else:
        leaderboard[i]["place"] = place


# leaderboard = sorted(leaderboard, key=lambda leader: leader["count"], reverse=True)

# NOT SURE HOW THIS WORKS BUT #1 IS IN RIGHT ORDER
def sort(item):
    return (item["count"], float(item["points"])<last_score)

l = sorted(leaderboard, key=sort, reverse=True)

# print_l(l)

# print_l(leaderboard)
# first = [i for i in leaderboard if i["place"] == 1]
# for i in first:
#     print(i)




# if last_score != None and place == 1:
#     current_points, next_points = last_score - float(leaderboard[i]["points"]), last_score - float(leaderboard[i+1]["points"])
#     if current_score > next_score:
#         leaderboard[i]["place"] = place
#         place += 1
#     else:
#         leaderboard[i]["place"] = place