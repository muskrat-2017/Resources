import random, uuid

class Player:
	def __init__(self, name):
		self.name = name
		self._id = uuid.uuid4().hex
		self.score = 0



class Turn:
	def __init__(self, player):
		self.player = player
		self.score = 0
		self.can_bank = True
		self.is_active = True

	def bank(self):
		if not self.can_bank:
			return dict(
				is_active=self.is_active,
				has_error=True
			)
		else:
			self.player.score += self.score
			self.can_bank = False
			self.is_active = False
			return dict(
				name=self.player.name, 
				score=self.player.score,
				is_active=self.is_active
			)


	def roll(self):

		result_dice = self._dice_sim()
		roll_score = sum(result_dice)

		self.score += roll_score
		
		if(result_dice[0] == result_dice[1]) and (result_dice[0] == "1"):
			# handles snake_eyes
			self._snake_eyes()
		
		elif(result_dice[0] == result_dice[1]):
			# handles doubles
			self._doubles(roll_score)

		elif(result_dice[0] == 1) or (result_dice[1] == 1):
			# handles pig
			self._pig()

		else:
			# default
			self._default(roll_score)
		
		return dict(
			name=self.player.name,
			score=self.player.score,
			turn_score=self.score,
			dice=result_dice,
			is_active=self.is_active
		)

	
	def _snake_eyes(self):
		self.score = 0
		self.can_bank = False
		self.is_active = False

		self.player.score = 0

	
	def _pig(self):
		self.score = 0
		self.can_bank = False
		self.is_active = False
	
	def _doubles(self, roll_score):
		self.can_bank = False


	def _default(self, roll_score):
		self.can_bank = True


	def _dice_sim(self):
		return [random.randrange(1, 6) for _ in range(2)]


class Game:

	def __init__(self):
		self.max_score = 0
		self.player_count = 0
		self.players = []

		self.log = []

		self.turn_count = 0
		self.is_active = True

		self.instructions = "<Placeholder For Instructions>"


	def start(self):
		self.log.append(Turn(self.get_active_player()))

	def get_active_player(self):
		return self.players[self.turn_count%len(self.players)]


	def roll(self):
		turn = self.log[-1]
		result = turn.roll()
		if not turn.is_active:
			self.end_turn()
		return result


	def bank(self):
		turn = self.log[-1]
		result = turn.bank()
		if not turn.is_active:
			self.end_turn()
		return result

	def set_max_score(self, max_score):
		self.max_score = max_score


	def set_number_or_players(self, player_count):
		self.player_count = player_count


	def add_player(self, name):
		self.players.append(Player(name))


	def end_turn(self):
		self.is_game_over()
		self.turn_count += 1
		self.log.append(Turn(self.get_active_player()))


	def is_game_over(self):
		# if game is over set self.is_active to false
		self.is_active = not any(player.score >= self.max_score for player in self.players)



def main():
	pass

if __name__ == '__main__':
	main()
