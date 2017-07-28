class BaseView:
	PER_PAGE = 5
	##############################################
	# Utility Views

	def clear(self):
		print( "\033[2J\033[;H" )

	def confirmation_prompt(self, selection):
		
		print( "You have entered: ", selection, sep="\n")

		confirmation = input( "Is this correct?(Yes/No)\n" ).strip().lower()
		return confirmation in ( "yes", "y" )

	def display_output( self, data ):
		"""
		A generic print function to be used as a placeholder for 
		future view methods
		"""
		print(data)

	def paginate( self, start, stop, end, direction=True):
		increment = self.PER_PAGE * ( 1 if direction else -1 )
		new_stop = min( stop + ( increment if (direction or start != 0) and (stop != end or not direction) else 0 ), end )
		start = ( start + ( increment if ( start != 0 or direction ) and (stop != end or not direction) else 0 ) )
		
		if stop == end and not direction:
			stop = start
			start = start + increment
		else:
			stop = new_stop

		back = "( < back )" if start else ""
		next = "" if stop + 1 >= end else "( next > )"
		return start, stop, back, next

	##############################################


class BaseCRUDView(BaseView):
	

	def detail_menu(self, obj):
		"""
		
		"""
		self.clear()
		
		# NEW CONFIGURABLE render_detail_template
		print( self.render_detail_template( obj ) )

		# NEW CONFIGURABLE render_detail_menu
		print( self.render_detail_menu() )
		return input().strip().lower()


	def collection_menu( self, collection ):
		choice = ""	
		start, stop, back, next = self.paginate( 
			-self.PER_PAGE, 0, len( collection ) 
		)
		
		while choice.lower() != "exit":
			# TODO clean this up
			for idx in range( start, stop ):
				# NEW CONFIGURABLE get_item_preview_template
				preview = self.get_item_preview_template().format( 
					idx + 1 - start, 
					# NEW CONFIGURABLE item_preview
					self.item_preview( 
						collection[ idx ]
					) 
				)
				print(preview)
			
			print( "{}					{}".format( back, next ) )

			# NEW CONFIGURABLE get_select_prompt
			choice = input( self.get_select_prompt() ).strip().lower()

			if choice.isdigit() and 0 < int( choice ) < len( collection ):
				
				item = collection[ start + int( choice ) - 1 ]
				
				# NEW CONFIGURABLE get_confirmation_prompt
				confirmation_prompt = self.get_confirmation_prompt( item )
				
				if self.confirmation_prompt( confirmation_prompt ):
					return item

			elif choice in ( "next", "n", "b", "back" ):

				start, stop, back, next = self.paginate( 
					start, stop, len( collection ), choice[0] == "n" 
				)
			
			self.clear()
		return choice.lower()


	def create( self ):
		# NEW CONFIGURABLE render_create_prompt
		value = input( self.render_create_prompt() ).strip()
		if self.confirmation_prompt( value ):
			return value


	def post_create_menu(self):
		"""
		Choices
		"""

		self.clear()
		# NEW CONFIGURABLE render_post_create_menu
		print( self.render_post_create_menu() )
		return input().strip().lower()


	def update( self, obj ):
		# NEW CONFIGURABLE render_update_prompt
		value = input( self.render_update_prompt() ).strip()
		if self.confirmation_prompt( value ):
			return value


	def delete( self, obj ):
		# NEW CONFIGURABLE render_deletion_confirmation_prompt
		print( self.render_deletion_confirmation_prompt() )
		if self.confirmation_prompt( obj ):
			return obj


class ContactCRUDView(BaseCRUDView):
	def render_detail_template( self, obj ):
		return "{}) {}".format( *obj )

	def render_detail_menu( self ):
		return """
1) Update Contact
2) View Emails
3) Add Email
4) View Numbers
5) Add Number
6) Delete Contact
7) Main Menu
(type 'exit' to quit)
"""

	def get_item_preview_template( self ):
		return "{}) {}"

	def item_preview( self, obj ):
		return obj[ 1 ]

	def get_select_prompt( self ):
		return "Select a contact: "

	def get_confirmation_prompt( self, obj ):
		return "{}) {}".format( obj[ 0 ], obj[ 1 ] )

	def render_create_prompt( self ):
		return "Enter the name of your new contact: \n"

	def render_post_create_menu( self ):
		return """
1) View and Edit new Contact
2) Add Another Contact
3) Main Menu
(type 'exit' to quit)
"""

	def render_update_prompt( self ):
		return "Enter the new number for this contact: \n"

	def render_deletion_confirmation_prompt( self ):
		return "Please confirm deletion of contact:"


class EmailCRUDView(BaseCRUDView):
	def render_detail_template( self, obj ):
		"{}) {}".format( obj[0], obj[1] )

	def render_detail_menu( self ):
		return """
	1) Update Email
	2) Delete Email
	3) Main Menu
	(type 'exit' to quit)
			"""

	def get_item_preview_template( self ):
		return "{}) {}"

	def item_preview( self, obj ):
		return obj[ 1 ]

	def get_select_prompt( self ):
		return "Select an email: "

	def get_confirmation_prompt( self, obj ):
		return "{}) {}".format( obj[ 0 ], obj[ 1 ] )

	def render_create_prompt( self ):
		return "Enter the new email address: \n"

	def render_post_create_menu( self ):
		return """
1) View and Edit new Contact
2) Add Another Contact
3) Main Menu
(type 'exit' to quit)
"""

	def render_update_prompt( self ):
		return "Enter the new email address for this contact: \n"

	def render_deletion_confirmation_prompt( self ):
		return "Please confirm deletion of email:"


class PhoneNumberCRUDView(BaseCRUDView):
	def render_detail_template( self, obj ):
		"{}) {}".format( obj[0], obj[1] )

	def render_detail_menu( self ):
		return """
1) Update Number
2) Delete Number
3) Main Menu
(type 'exit' to quit)
"""

	def get_item_preview_template( self ):
		return "{}) {}"

	def item_preview( self, obj ):
		return obj[ 1 ]

	def get_select_prompt( self ):
		return "Select a number: "

	def get_confirmation_prompt( self, obj ):
		return "{}) {}".format( obj[ 0 ], obj[ 1 ] )

	def render_create_prompt( self ):
		return "Enter the new phone number: \n"

	def render_post_create_menu( self ):
		return """
1) View and Edit new Phone Number
2) Add Another Phone Number
3) Main Menu
(type 'exit' to quit)
"""

	def render_update_prompt( self ):
		return "Enter the new name for this contact: \n"

	def render_deletion_confirmation_prompt( self ):
		return "Please confirm deletion of phone number:"


class View(BaseView):
	contact = ContactCRUDView()
	phone_number = PhoneNumberCRUDView()
	email = EmailCRUDView()


	def main_menu(self):
		"""
		main_menu 
		1) View Contacts Menu
		2) Add Contact
		"""
		choice = None
		while choice != "exit" and choice not in ( "1", "2" ):
			self.clear()
			print( """
1) View Contacts
2) Add Contact
(type 'exit' to quit)
			""" )
			choice = input().strip().lower()
		return choice