from uuid import uuid4
from random import choice

class Tournament:
	def __init__(self):
		self.participants = []
		self.tournament_format = None
		self.misc_value = None
	
	def choose_format(self, tournament_format: str ='False'):
		if type(tournament_format) is not str:
			str(tournament_format)
		tournament_format.lower()
		allowed = {
			'red sun': self.begin_elo()
		}
		if tournament_format.lower() in allowed.keys:
			pass
		else:
			pass
	
	def begin_elo(self, starting_elo = 1200):
		self.tournament_format = 'Elo'
		self.misc_value = starting_elo
			
	def get_player_by_name(self, name:str) -> list:
		potential_matches = []
		for p in self.participants:
			if name in p.associated_names:
				potential_matches.append(p)
		
		if len(potential_matches) == 0:
			return [False]
		else:
			return potential_matches
		
	def get_player_by_id(self, id):
		for p in self.participants:
			if p.id == id:
				return p
		return False
	
	def get_player(self, query):
		is_id = self.get_player_by_id(query)
		if is_id:
			return is_id
		
		names = self.get_player_by_name(query)
		if len(names) == 1:
			if names[0]:
				return names[0]
		else:
			raise(TypeError, 'multiple players with name {}'.format(query))
	
	def add_participant(self, name, wins=0, losses=0, score=0, id=uuid4()):
		self.participants.append(self.Participant(name, wins, losses, score, id, self.misc_value))
		
	def add_match(self, player_a, player_b, a_win, b_win):
		player_a = self.get_player(player_a)
		player_b = self.get_player(player_b)
		
		player_a.wins += a_win
		player_a.losses += b_win
		player_a.history.append([player_b, (a_win, b_win)])
		
		player_b.wins += b_win
		player_b.losses += a_win
		player_b.history.append([player_a, (b_win, a_win)])
		
	def score_simple(self):
		for p in self.participants:
			p.score = p.wins + p.losses/100
	
	def determine_winner(self):
		results = [(x.id, x.score) for x in self.participants]
		results.sort(key=lambda x: x[1], reverse=True)
		return results

	
class Participant:
	def __init__(self, name, wins=0, losses=0, score=0, id=uuid4(), value=0):
		self.score = score
		self.wins = wins
		self.losses = losses
		self.history = []
		self.associated_names = {name}
		self.id = id
		self.misc_value = value
		self.bye = False
	
	def add_name(self, name):
		self.associated_names.add(name)
	
	def remove_name(self, name):
		self.associated_names.remove(name)


class Round:
	def __init__(self, participants: list):
		self.participants = participants
		participants.sort(key=lambda x: x.misc_value, reverse=True)
		if len(participants)  % 2 == 1:
			bye = choice(participants)
			bye.choice = True
		matches = [x for x in participants if x.bye == False]
		for m in matches:
			pass
	
			
class Match:
	def __init__(self, id_a, id_b):
		self.player1 = id_a
		self.player2 = id_b
		self.open = True
		self.id = uuid4()
		self.reported1 = False
		self.reported2 = False
		
	def cancel_match(self):
		self.open = False
		
	def report_match(self, player, wins, losses):
		if player == self.player1:
			self.reported1 = (wins, losses)
		elif player == self.player2:
			self.reported2 = (wins, losses)
		if self.reported1 and self.reported2:
			if self.reported1 == reversed(self.reported2):
				self.open = False
			else:
				self.match_alert()
				
	def match_alert(self):
		# alerts TO to match disagreement
		pass