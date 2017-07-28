from models import ContactApp
from views import View

class Controller(BaseController):


	def __init__( self, app, view ):
		self.app = app
		self.view = view
		self.next_ = self.main_menu

	##############################################
	# Utility Methods
	

	def not_implemented( self ):
		self.view.display_output( "\nNot Implemented\n" )
		self.next_ = self.main_menu

	def select_next( self, choice ):
		
		if choice == "exit":
			self.next_ = None
		
		else:
			self.next_ = self.main_menu

	##############################################


	def run( self ):

		while self.next_:
			self.next_()


	def main_menu( self ):
		choice = self.view.main_menu()
		
		if choice == "1":
			self.next_ = self.contacts_menu
		elif choice == "2":
			self.next_ = self.add_contact_menu
		else:
			self.select_next( choice )


	##############################################
	# Contact Menus

	def contacts_menu( self ):
		contacts = self.app.get_contacts()
		choice = self.view.contact.collection_menu( contacts )
		
		if isinstance( choice, ( str, ) ):
			self.select_next( choice )
		
		else:
		 	self.contact_editor_menu( choice )

	def contact_editor_menu( self, contact ):
		choice = self.view.contact.detail_menu( contact )
		
		if choice == "1":
			# update contact
			self.update_contact_menu( contact )
		
		elif choice == "2":
			# view emails
			self.emails_menu( contact )
		
		elif choice == "3":
			# add email
			self.add_email_menu( contact )

		elif choice == "4":
			# view numbers
			self.phone_numbers_menu( contact )
		
		elif choice == "5":
			# add number
			self.add_phone_number_menu( contact )
		
		elif choice == "6":
			# delete contact
			self.next_ = self.delete_contact_menu
		
		else:
			self.select_next( choice )


	##############################################
	# Phone Number Menus

	def phone_numbers_menu(self, contact):
		numbers = self.app.get_contact_phone_numbers( contact )
		choice = self.view.phone_number.collection_menu( numbers )

		if isinstance( choice, ( str, )):
			self.select_next( choice )

		else:
		 	self.phone_number_editor_menu( choice )

	
	def phone_number_editor_menu( self, number ):
		choice = self.view.phone_number.detail_menu( number )
		
		if choice == "1":
			# update number
			self.update_phone_number_menu( number )
		
		elif choice == "2":
			# delete number
			self.delete_phone_number_menu( number )
		
		else:
			self.select_next( choice )	

	##############################################
	# Email Menus

	def emails_menu( self, contact ):
		emails = self.app.get_contact_emails( contact )
		choice = self.view.email.collection_menu( emails )

		if isinstance( choice, ( str, )):
			self.select_next( choice )

		else:
		 	self.email_editor_menu( choice )

	
	def email_editor_menu( self, email ):
		choice = self.view.email.detail_menu( email )
		
		if choice == "1":
			# update email
			self.update_email_menu( email )
		
		elif choice == "2":
			# delete email
			self.delete_email_menu( email )
		
		else:
			self.select_next( choice )	


	##############################################
	# Create Menus

	def add_contact_menu( self ):
		name = self.view.contact.create()
		if name is None:
			self.next_ = self.main_menu
		else:
			contact = self.app.add_contact( name )
			choice = self.view.contact.post_create_menu()
			
			if choice == "1":
				# edit new contact
				self.contact_editor_menu( contact )
			elif choice == "2":
				# add another contact
				self.next_ = self.add_contact_menu
			else:
				self.select_next( choice )

	
	def add_phone_number_menu( self, contact ):
		number = self.view.phone_number.create()
		if number is None:
			self.next_ = self.main_menu
		else:
			phone_number = self.app.add_phone_number( number, contact[ 0 ] )
			choice = self.view.phone_number.post_create_menu()
			
			if choice == "1":
				# edit new phone number
				self.update_phone_number( phone_number )
			elif choice == "2":
				# add another phone number
				self.next_ = self.add_phone_number_menu
			else:
				self.select_next( choice )

	
	def add_email_menu( self, contact ):
		address = self.view.email.create()
		if address is None:
			self.next_ = self.main_menu
		else:
			email = self.app.add_email( address, contact[ 0 ] )
			choice = self.view.email.post_create_menu()
		
			if choice == "1":
				# edit new address
				self.update_address( email )
			elif choice == "2":
				# add another address
				self.next_ = self.add_email_menu
			else:
				self.select_next( choice )

	##############################################
	# Update Menus

	def update_contact_menu( self, contact ):
		name = self.view.contact.update( contact )
		if name is None:
			self.next_ = self.main_menu
		else:
			contact = self.app.update_contact( contact[ 0 ], name )
		
			self.contact_editor_menu( contact )

	
	def update_phone_number_menu( self, phone_number ):
		number = self.view.phone_number.update( phone_number )
		if number is None:
			self.next_ = self.main_menu
		else:
			phone_number = self.app.update_phone_number( phone_number[ 0 ], number )
			self.phone_number_editor_menu( phone_number )
		

	
	def update_email_menu( self, email ):
		address = self.view.email.update( email )
		if address is None:
			self.next_ = self.main_menu
		else:
			email = self.app.update_email( email[ 0 ], address )
			self.email_editor_menu( email )

	##############################################
	# Delete Menus

	def delete_contact_menu( self, contact ):
		choice = self.view.contact.delete( contact )
		if choice:
			contact = self.app.delete_contact( contact[ 0 ] )
			self.next_ = self.main_menu
		else:
			self.contact_editor_menu( contact )

	
	def delete_phone_number_menu( self, phone_number ):
		choice = self.view.phone_number.delete( phone_number )
		if choice:
			phone_number = self.app.delete_phone_number( phone_number[ 0 ] )
			self.next_ = self.main_menu
		else:
			self.phone_number_editor_menu( phone_number )
		

	def delete_email_menu( self, email ):
		choice = self.view.email.delete( email )
		if choice:
			email = self.app.delete_email( email[ 0 ] )
			self.next_ = self.main_menu
		else:
			self.email_editor_menu( email )

def main():
	app = ContactApp()
	view = View()
	controller = Controller( app, view )
	controller.run()


if __name__ == '__main__':
	main()