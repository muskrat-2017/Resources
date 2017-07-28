class View:
	def display_instructions(self, insturctions):
		print(insturctions)


	def prompt_player(self, name):
		is_valid = False
		while not is_valid:
			response = input("{} enter r for roll, b for bank:\n".format(name)).strip().lower()
			if response in ("r", "b", "roll", "bank"):
				return response
				is_valid = True
			else:
				print("'{}' is not a valid option.".format(response))

	def set_max_score(self):
		is_valid = False
		while not is_valid:
			response = input("Please set the max score(Enter a whole number):\n").strip()
			if response.isnumeric():
				return int(response)
			else:
				print("'{}' is not a whole number.".format(response))

	def set_number_or_players(self):
		is_valid = False
		while not is_valid:
			response = input("Please set the number of players(Enter a whole number):\n").strip()
			if response.isnumeric():
				return int(response)
			else:
				print("'{}' is not a whole number.".format(response))

	def add_player(self):
		is_valid = False
		while not is_valid:
			response = input("Please enter your name:\n").strip()
			if response.isalpha():
				return response
			else:
				print("'{}' is not a valid name.".format(response))

	def end_turn(self, message=None):
		if message: print(message)
		print("="*80)

	def bank(self, name, score):
		print(name, " total score:", score)


	def roll(self, name, score, turn_score, dice):
		roll_score = sum(dice)
		
		print(name, " Result: ", *dice)
		
		if(dice[0] == dice[1]) and (dice[0] == "1"):
			# handles snake_eyes
			print("Snake-eyes!")

		elif(dice[0] == 1) or (dice[1] == 1):
			# handles pig
			print("Pig!")
		
		else:
			if(dice[0] == dice[1]):
				# handles doubles
				print("Doubles!")
			
			print("Roll Score:", roll_score)
			print("Current Score:", turn_score, "\n")
		
		print(name, " total score:", score)


def main():
	pass

if __name__ == '__main__':
	main()