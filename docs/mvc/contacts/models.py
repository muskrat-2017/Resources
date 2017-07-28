from db_manager import (
	ContactManager, PhoneNumberManager, EmailAddressManager
)


class Contact:
	
	manager = ContactManager()

	def __init__( self, id, name ):
		self.id = id
		self.name = name


class PhoneNumber:

	manager = PhoneNumberManager()

	def __init__( self, id, number, contact_id ):
		self.id = id
		self.number = number
		self.contact_id = contact_id


class Email:
	
	manager = EmailAddressManager()

	def __init__( self, id, address, contact_id ):
		self.id = id
		self.address = address
		self.contact_id = contact_id



class ContactApp:

	##############################################
	# Read Methods

	def get_contacts( self ):
		contacts = Contact.manager.get()
		return contacts

	
	def get_contact_emails( self, contact ):
		emails = Email.manager.get( contact[ 0 ] )
		return emails 

	
	def get_contact_phone_numbers( self, contact ):
		phone_numbers = PhoneNumber.manager.get( contact[ 0 ] )
		return phone_numbers

	##############################################
	# Create Methods

	def add_contact( self, name ):
		contact_id = Contact.manager.create( name=name )
		contact = Contact.manager.get_by_id( contact_id )
		return contact

	def add_email( self, address, contact_id ):
		email_id = Email.manager.create( address=address, contact_id=contact_id )
		email = Email.manager.get_by_id( email_id )
		return email


	def add_phone_number( self, number, contact_id ):
		number_id = PhoneNumber.manager.create( number=number, contact_id=contact_id )
		contact = PhoneNumber.manager.get_by_id( number_id )
		return contact

	##############################################
	# Update Methods

	def update_contact( self, id, name ):
		res = Contact.manager.update( id=id, name=name )
		contact = Contact.manager.get_by_id( id )
		return contact


	def update_email( self, id, address ):
		res = Email.manager.update( id=id, address=address )
		email = Email.manager.get_by_id( id )
		return email


	def update_phone_number( self, id, number ):
		res = PhoneNumber.manager.update( id=id, number=number )
		contact = PhoneNumber.manager.get_by_id( id )
		return contact

	##############################################
	# Delete Methods

	def delete_contact( self, id ):
		res = Contact.manager.delete( id=id )
		return res


	def delete_email( self, id ):
		res = Email.manager.delete( id=id )
		return res


	def delete_phone_number( self, id ):
		res = PhoneNumber.manager.delete( id=id )
		return res


