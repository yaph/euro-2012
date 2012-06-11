# -*- coding: utf-8 -*-
# Built a graph structure for each participating country showing players'
# connections to team (country) and club mates. Players in the country graphs 
# are grouped by club.
#
# Force Layout
# http://bl.ocks.org/950642
# https://github.com/mbostock/d3/wiki/Force-Layout

import csv, json, itertools
from collections import defaultdict

graphs = {}
players = {}
players_by_teams = defaultdict(list)
players_by_clubs = defaultdict(list)
clubs = []
teams = []

def get_id(li, item):
    if item not in li:
        li.append(item)
    return li.index(item)


def add_links(iterable, item):
    for i in iterable:
        players[i]['nodeid'] = get_id(nodes,
            {'name': players[i]['name'], 'group': get_id(clubs, players[i]['club']), 'team': players[i]['team']})
        # don't link player to himself
        if players[item]['nodeid'] != players[i]['nodeid']:
            links.append({'source': players[item]['nodeid'], 'target': players[i]['nodeid']})


fcsv = open('players.csv', 'r')
reader = csv.reader(fcsv)
headers = reader.next()
for idx, record in enumerate(reader):
    firstname, lastname, age, height, team, position, appearances, goals, club = record
    # with team and club name without country suffix so player name is unique
    player = ('%s %s (%s) %s' % (firstname, lastname, team, ' '.join(club.split(' ')[:-1]))).strip()
    players[player] = {'idx': idx, 'name': player, 'team': team, 'club': club}
    players_by_clubs[club].append(player)
    players_by_teams[team].append(player)
fcsv.close()

for team, pls in players_by_teams.items():
    nodes = []
    links = []
    teams.append(team)
    for p in pls:
        team = players[p]['team']
        club = players[p]['club']
        name = players[p]['name']
        players[p]['nodeid'] = get_id(nodes,
            {'name': name, 'group': get_id(clubs, club), 'team': team})
        add_links(players_by_clubs[club], name)
    graphs[team] = {'nodes': nodes, 'links': links}

js = 'var teams=%s;var graphs=%s;' % (json.dumps(sorted(teams)), json.dumps(graphs))
print( js )

