from views import View	
from models import Game



class Controller:

	def __init__(self, view, game):
		self.view = view
		self.game = game

	def run(self):
		self.setup()
		self.play()


	def setup(self):
		self.view.display_instructions(self.game.instructions)
		
		max_score = self.view.set_max_score()
		self.game.set_max_score(max_score)
		
		player_count = self.view.set_number_or_players()
		self.game.set_number_or_players(player_count)
		
		for _ in range(player_count):
			name = self.view.add_player()
			self.game.add_player(name)


	def play(self):

		self.game.start()
		
		while self.game.is_active:
			self.execute_turn()
			self.view.end_turn()

		# the game is over

	def execute_turn(self):
		result = dict(is_active=True)

		while result.get("is_active"):
			player = self.game.get_active_player()
			command = self.view.prompt_player(player.name)
			if command in ('r', 'roll'):
				self.roll()
			elif command in ('b', 'bank'):
				self.bank()
			else:
				self.view.end_turn()

	def roll(self):
		result = self.game.roll()
		self.view.roll(
			result["name"], result["score"], 
			result["turn_score"], result["dice"]
		)

	def bank(self):
		result = self.game.bank()
		if result.get("has_error"):
			self.view.end_turn("You cannot bank now, please choose r!")
		else:
			self.view.bank(result["name"], result["score"])

def main():
	controller = Controller(View(), Game())
	controller.run()


if __name__ == '__main__':
	main()