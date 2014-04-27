# Mythea Formatter


mythea = '''June 1st, YR2	Albert Wesker(6:2) ambushed armies from Stock Killer(4:10) and took 73 acres of land.
	June 1st, YR2	the hawaiian(4:10) captured 111 acres of land from Albert Wesker(6:2).
	June 1st, YR2	An unknown province from Good Chance I Will Retal(11:2) invaded the hawaiian(4:10) and captured 165 acres of land.
	June 4th, YR2	Deathbringer(4:10) captured 94 acres of land from hello(7:5).
	June 4th, YR2	Barry Burton(6:2) attempted an invasion of Stock Killer(4:10), but was repelled.
	June 4th, YR2	Barry Burton(6:2) invaded Stock Killer(4:10) to gather intelligence.
	June 6th, YR2	Stock Killer(4:10) recaptured 113 acres of land from Albert Wesker(6:2).
	June 6th, YR2	Stock Killer(4:10) recaptured 95 acres of land from Albert Wesker(6:2).
	June 6th, YR2	Mister Cool(4:10) has sent an aid shipment to Stock Killer(4:10)
	June 6th, YR2	Mister Cool(4:10) has sent an aid shipment to Stock Killer(4:10)
	June 7th, YR2	Mister Cool(4:10) has sent an aid shipment to Stock Killer(4:10)
	June 7th, YR2	a Fools Gold spell incoming from STARS(6:2) has worsened our relations.
	June 7th, YR2	Notorious(4:10) captured 95 acres of land from Rebecca Chambers(6:2).
	June 9th, YR2	The Cat II(2:4) invaded the hawaiian(4:10) and captured 165 acres of land.
	June 13th, YR2	hello(7:5) ambushed armies from Deathbringer(4:10) and took 47 acres of land.
	June 15th, YR2	a Incite Riots operation incoming from STARS(6:2) has worsened our relations.
	June 17th, YR2	Stock Killer(4:10) captured 217 acres of land from Lose Mind(2:4).
	June 18th, YR2	Deathbringer(4:10) captured 26 acres of land from Loooooooooooo(13:4).
	June 18th, YR2	Deathbringer(4:10) captured 22 acres of land from Loooooooooooo(13:4).
	June 18th, YR2	Deathbringer(4:10) captured 19 acres of land from Loooooooooooo(13:4).
	June 18th, YR2	Deathbringer(4:10) captured 16 acres of land from Loooooooooooo(13:4).
	June 19th, YR2	The Cat II(2:4) invaded Stock Killer(4:10) and captured 302 acres of land.
	June 20th, YR2	a Nightmares spell incoming from STARS(6:2) has worsened our relations.
	June 20th, YR2	a Nightmares spell incoming from STARS(6:2) has worsened our relations.
	June 20th, YR2	Albert Wesker(6:2) invaded Stock Killer(4:10) and captured 150 acres of land.
	June 20th, YR2	Albert Wesker(6:2) invaded Stock Killer(4:10) and captured 78 acres of land.
	June 20th, YR2	Albert Wesker(6:2) invaded Stock Killer(4:10)and conquered 21 acres of land.
	June 20th, YR2	a Night Strike operation incoming from STARS(6:2) has worsened our relations.
	June 20th, YR2	Joseph Frost(6:2) invaded Stock Killer(4:10) and captured 47 acres of land.
	June 20th, YR2	Joseph Frost(6:2) invaded Stock Killer(4:10) and captured 29 acres of land.
	June 20th, YR2	LIOU EMPIRE(2:4) invaded Stock Killer(4:10) and captured 11 acres of land.
	June 21st, YR2	Barry Burton(6:2) invaded Stock Killer(4:10) to gather intelligence.
	June 21st, YR2	Barry Burton(6:2) invaded and stole from Stock Killer(4:10)
	June 23rd, YR2	Chris Redfield(6:2) invaded Stock Killer(4:10) and captured 28 acres of land.
	June 24th, YR2	Barry Burton(6:2) invaded Stock Killer(4:10) and razed 15 acres of land.'''
	
	#to determine if event is attack, op(thief or mystic) , aid, relations change, or 
	#war declare or end, defect,  might need a couple more functions...
def get_province(mythea):
	world = []
	current = mythea.index('YR')
	if current == -1:
	 	return None, 0
	else:
		province_start = str(mythea.index(current + 4))
		procvince_end = mythea.index('(' , province_start)
		province = mythea[ province_start : procvince_end]
		world.append( province)
		current = current[province_end]
#print get_province(mythea)
		#return current, world
print mythea [ mythea.index('YR') + 4 : mythea.find('(')]
print mythea.index( 'YR' )

		
	

	#The data structure gets slightly complicated, but I think you would want to set it up like this:

#world = {king1:{prov1:acre1, prov2:acre2}, king2:{prov1:acre1, prov2:acre2}}

	#Iterating over dictionaries is kind of a pain, but I've never googled for the best ways to do it either.  If I were going to adjust acres after a battle, I'd do something like this:

# def acre_change(world, winning_prov, losing_prov, acres):
#     for king in world:
#         if winning_prov in world[king]:
#             world[king][winning_prov] += acres
#         if losing_prov in world[king]:
#             world[king][losing_prov] -= acres
#     return world