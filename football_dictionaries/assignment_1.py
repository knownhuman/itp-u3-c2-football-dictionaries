def players_as_dictionaries(squads_list):
    players = []
    for player in squads_list:
        p = {
        'caps' : player[4],
        'club' : player[5],
        'club_country' : player[7],
        'country' : player[6],
        'date_of_birth' : player[3],
        'name' : player[2],
        'number' : player[0],
        'position' : player[1],
        'year' : player[8]
        }
        players.append(p)
    return players
