import requests, json, pandas as pd
import psycopg2

def get_hero_name(id_h): 
	i ={1: 'Anti-Mage'
	, 2: 'Axe'
	, 3: 'Bane'
	, 4: 'Bloodseeker'
	, 5: 'Crystal Maiden'
	, 6: 'Drow Ranger'
	, 7: 'Earthshaker'
	, 8: 'Juggernaut'
	, 9: 'Mirana'
	, 10: 'Morphling'
	, 11: 'Shadow Fiend'
	, 12: 'Phantom Lancer'
	, 13: 'Puck'
	, 14: 'Pudge'
	, 15: 'Razor'
	, 16: 'Sand King'
	, 17: 'Storm Spirit'
	, 18: 'Sven'
	, 19: 'Tiny'
	, 20: 'Vengeful Spirit'
	, 21: 'Windranger'
	, 22: 'Zeus'
	, 23: 'Kunkka'
	, 25: 'Lina'
	, 26: 'Lion'
	, 27: 'Shadow Shaman'
	, 28: 'Slardar'
	, 29: 'Tidehunter'
	, 30: 'Witch Doctor'
	, 31: 'Lich'
	, 32: 'Riki'
	, 33: 'Enigma'
	, 34: 'Tinker'
	, 35: 'Sniper'
	, 36: 'Necrophos'
	, 37: 'Warlock'
	, 38: 'Beastmaster'
	, 39: 'Queen of Pain'
	, 40: 'Venomancer'
	, 41: 'Faceless Void'
	, 42: 'Wraith King'
	, 43: 'Death Prophet'
	, 44: 'Phantom Assassin'
	, 45: 'Pugna'
	, 46: 'Templar Assassin'
	, 47: 'Viper'
	, 48: 'Luna'
	, 49: 'Dragon Knight'	
	, 50: 'Dragon Knight'
	, 51: 'Clockwerk'
	, 52: 'Leshrac'
	, 53: "Nature's Prophet"
	, 54: 'Lifestealer'
	, 55: 'Dark Seer'
	, 56: 'Clinkz'
	, 57: 'Omniknight'
	, 58: 'Enchantress'
	, 59: 'Huskar'
	, 60: 'Night Stalker'
	, 61: 'Broodmother'
	, 62: 'Bounty Hunter'
	, 63: 'Weaver'
	, 64: 'Jakiro'
	, 65: 'Batrider'
	, 66: 'Chen'
	, 67: 'Spectre'
	, 68: 'Ancient Apparition'
	, 69: 'Doom'
	, 70: 'Ursa'
	, 71: 'Spirit Breaker'
	, 72: 'Gyrocopter'
	, 73: 'Alchemist'
	, 74: 'Invoker'
	, 75: 'Silencer'
	, 76: 'Outworld Destroyer'
	, 77: 'Lycan'
	, 78: 'Brewmaster'
	, 79: 'Shadow Demon'	
	, 80: 'Lone Druid'
	, 81: 'Chaos Knight'
	, 82: 'Meepo'
	, 83: 'Treant Protector'
	, 84: 'Ogre Magi'
	, 85: 'Undying'
	, 86: 'Rubick'
	, 87: 'Disruptor'
	, 88: 'Nyx Assassin'
	, 89: 'Naga Siren'	
	, 90: 'Keeper of the Light'
	, 91: 'Io'
	, 92: 'Visage'
	, 93: 'Slark'
	, 94: 'Medusa'
	, 95: 'Troll Warlord'
	, 96: 'Centaur Warrunner'
	, 97: 'Magnus'
	, 98: 'Timbersaw'
	, 99: 'Bristleback'
	 ,100: 'Tusk'
	 ,101: 'Skywrath Mage'
	 ,102: 'Abaddon'
	 ,103: 'Elder Titan'
	 ,104: 'Legion Commander'
	 ,105: 'Techies'
	 ,106: 'Ember Spirit'
	 ,107: 'Earth Spirit'
	 ,108: 'Underlord'
	 ,109: 'Terrorblade'	
	 ,110: 'Phoenix'
	 ,111: 'Oracle'
	 ,112: 'Winter Wyvern'
	 ,113: 'Arc Warden'
	 ,114: 'Monkey King'	
	 ,119: 'Dark Willow'
	 ,120: 'Pangolier'
	 ,121: 'Grimstroke'
	 ,123: 'Hoodwink'
	 ,126: 'Void Spirit'
	 ,128: 'Snapfire'
	 ,129: 'Mars'
	 ,135: 'Dawnbreaker'
	 ,136: 'Marci'
	 ,137: 'Primal Beast'}
	 return i[id_h]

def get_rank_name(rank):
	if not rank:
		return 'Não rankeado'
	elif rank < 20:
		return 'Herald'
	elif rank < 30:
		return 'Guardian'
	elif rank < 40:
		return 'Crusader'
	elif rank < 50:
		return 'Archon'
	elif rank < 60:
		return 'Legend'	
	elif rank < 70:
		return 'Ancient'
	elif rank < 80:
		return 'Divine'
	else:
		return 'Imortal'


def get_info_player(player_id):
	api_data_per_player = {}
	api_data_per_player[player_id] = {}
	
	BASE_URL = 'https://api.opendota.com/api'
	get_player_url = '%s/players/%s' % (BASE_URL, str(player_id))  #request para API do player
	player_response = requests.get(get_player_url)
	players_result = json.loads(player_response.text)
	api_data_per_player[player_id]['general'] = players_result

	get_player_win_lose_url = '%s/players/%s/wl' % (BASE_URL, str(player_id)) #request para API do win/loss do player
	player_win_lose_response = requests.get(get_player_win_lose_url)
	players_win_lose_result = json.loads(player_win_lose_response.text)
	api_data_per_player[player_id]['win_lose'] = players_win_lose_result

	get_player_per_hero_url = '%s/players/%s/heroes' % (BASE_URL, str(player_id)) #request para API dos heroisdo  player
	player_per_hero_response = requests.get(get_player_per_hero_url)
	players_hero_result = json.loads(player_per_hero_response.text)
	api_data_per_player[player_id]['heroes'] = players_hero_result

	player_info = {}
	player_info[player_id] = {}
	player_info[player_id]['account_id'] = api_data_per_player[player_id]['general']['profile']['account_id']
	player_info[player_id]['nome_de_usuario'] = api_data_per_player[player_id]['general']['profile']['personaname']
	player_info[player_id]['medalha'] = get_rank_name(api_data_per_player[player_id]['general'].get('rank_tier'))
	player_info[player_id]['total_de_jogos'] = api_data_per_player[player_id]['win_lose']['win'] + api_data_per_player[player_id]['win_lose']['lose']
	player_info[player_id]['total_de_vitorias'] = api_data_per_player[player_id]['win_lose']['win']
	player_info[player_id]['total_de_derrotas'] = api_data_per_player[player_id]['win_lose']['lose']
	player_info[player_id]['win_rate_total'] = api_data_per_player[player_id]['win_lose']['win']/player_info[player_id]['total_de_jogos']

	for heroid in api_data_per_player[player_id]['heroes']:

		player_info[player_id][heroid['hero_id']] = {}
		player_info[player_id][heroid['hero_id']]['heroi'] = get_hero_name(int(heroid['hero_id']))
		player_info[player_id][heroid['hero_id']]['Total_de_jogos_H'] =  heroid['games']
		player_info[player_id][heroid['hero_id']]['Vitorias_H'] = heroid['win']

	return player_info


def add_player_sql(player_id):

    con = psycopg2.connect(host='localhost', database='regiao',
    user='postgres', password='postgres123')

    player_sql = get_info_player(player_id)

    cur = con.cursor()

    sql_player_query = (f'''INSERT INTO players 
                    VALUES 
                    ({player_sql['account_id']},
                    {player_sql['nome_de_usuario']},
                    {player_sql['medalha']},
                    {player_sql['total_de_jogos']},
                    {player_sql['total_de_vitorias']},
                    {player_sql['total_de_derrotas']},
                    {player_sql['win_rate_total']},);''')
    cur.execute(sql_player_query)
    con.commit()

	for heroid in player_sql[player_id][heroid['hero_id']]
        
        ql_player_query = (f'''INSERT INTO players_heroes 
                       VALUES 
                        ({player_sql['account_id']},
                        {heroid},
                        {player_sql[player_id][heroid['hero_id']]['Total_de_jogos_H']},
                        {player_sql[player_id][heroid['hero_id']]['Vitorias_H'] });''')

        cur.execute(sql_player_query)
        con.commit()
    con.close()


def get_player_sql(player_id):

    con = psycopg2.connect(host='localhost', database='regiao',
    user='postgres', password='postgres123')
    cur = con.cursor()

    cur.execute('''
    ''')