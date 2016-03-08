from itertools import *

def read_items():
	items = { "weapons": [], "armor": [], "rings":[] }
	fp = open("data")
	for l in fp:
		l = l.lower().split()
		if len(l) <= 0:
			continue
		elif l[0] == "weapons" or l[0] == "armor" or l[0] == "rings":
			itemtype = l[0]
		elif itemtype == "rings":
			items[itemtype].append({"name": l[0] + l[1], "cost": int(l[2]), "damage": int(l[3]), "armor": int(l[4])})
		else:
			items[itemtype].append({"name": l[0], "cost": int(l[1]), "damage": int(l[2]), "armor": int(l[3])})

	items["armor"].append({"name": "null", "cost": 0, "damage": 0, "armor": 0})
	return items

items = read_items()
#print items["weapons"]
#print items["armor"]
#print items["rings"]

def calculate_cda(items):
	#print items
	cost = damage = armor = 0
	for i in items:
		cost += i["cost"]
		damage += i["damage"]
		armor += i["armor"]
	return cost, damage, armor
	
def select_player_items(itemlist):
	weapons = items["weapons"]
	armor = items["armor"]
	rings = list(combinations(items["rings"], 2)) + list(combinations(items["rings"], 1)) + list(combinations(items["rings"], 0))

	l = list(product(weapons, armor, rings))
	for i in l:
		yield [i[0], i[1]] + [j for j in i[2]]

def do_attack(attacker, defender):
	adamage, darmor = attacker["damage"], defender["armor"]
	damage = max(adamage - darmor, 1)
	defender["health"] -= damage

def do_fight(player, enemy):
	attacker, defender = player, enemy
	while (player["health"] > 0 and enemy["health"] > 0):
		do_attack(attacker, defender)
		attacker, defender = defender, attacker
		#print player, enemy

	if player["health"] <= 0:
		return "enemy"
	else:
		return "player"

def run_simulation_part1():
		best = 9999999
		for player_items in select_player_items(items):
			cost, damage, armor = calculate_cda(player_items)
			player = { "health": 100, "damage": damage, "armor": armor }
			enemy = { "health" : 109, "damage": 8, "armor": 2 }
			winner = do_fight(player, enemy)
			if winner == "player":
				print "player won", cost, player_items
				best = min(cost, best)
		print best

def run_simulation_part2():
		best = -999999
		for player_items in select_player_items(items):
			cost, damage, armor = calculate_cda(player_items)
			player = { "health": 100, "damage": damage, "armor": armor }
			enemy = { "health" : 109, "damage": 8, "armor": 2 }
			winner = do_fight(player, enemy)
			if winner == "enemy":
				print "player lost", cost, player_items
				best = max(cost, best)
		print best

run_simulation_part2()

