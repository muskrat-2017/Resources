import sqlite3

class BaseDBManager:
	conn = sqlite3.connect("contacts.db")
	c = conn.cursor()


class ContactManager( BaseDBManager ):
	

	def create( self, name ):
		self.c.execute( """INSERT INTO contact ( name ) VALUES ( ? );""", ( name, ) )
		self.conn.commit()
		return self.c.lastrowid

	def get( self ):
		self.c.execute( """SELECT id, name FROM contact;""" )
		return self.c.fetchall()

	def get_by_id( self, id ):
		self.c.execute( """SELECT id, name FROM contact WHERE id = ?;""", ( id, ) )
		return self.c.fetchone()
	
	def update( self, id, name ):
		self.c.execute( """UPDATE contact SET name = ? WHERE id = ?;""", ( name, id ) )
		return self.c.fetchone()

	def delete( self, id ):
		self.c.execute( """DELETE FROM contact WHERE id = ?;""", ( id, ) )
		self.conn.commit()
		return self.c.fetchone()


class PhoneNumberManager( BaseDBManager ):
	

	def create( self, number, contact_id ):
		self.c.execute( """INSERT INTO ( number, contact_id ) VALUES ( ?, ? );""", ( number, contact_id ) )
		self.conn.commit()
		return self.c.lastrowid

	def get( self, contact_id ):
		self.c.execute( """SELECT id, number, contact_id FROM phone WHERE contact_id = ?;""", ( contact_id, ) )
		return self.c.fetchall()

	def get_by_id( self, id ):
		self.c.execute( """SELECT id, number, contact_id FROM phone WHERE id = ?;""", ( id, ) )
		return self.c.fetchone()


	def update( self, id, number ):
		self.c.execute( """UPDATE phone SET number = ? WHERE id = ?;""", ( number, id ) )
		return self.c.fetchone()

	def delete( self, id ):
		self.c.execute( """DELETE FROM phone WHERE id = ?;""", ( id, ) )
		self.conn.commit()
		return self.c.fetchone()


class EmailAddressManager( BaseDBManager ):
	

	def create( self, address, contact_id ):
		self.c.execute( """INSERT INTO ( address, contact_id ) VALUES ( ?, ? );""", ( address, contact_id ) )
		self.conn.commit()
		return self.c.lastrowid

	def get( self, contact_id ):
		self.c.execute( """SELECT id, address, contact_id FROM email WHERE contact_id = ?;""", ( contact_id, ) )
		return self.c.fetchall()

	def get_by_id( self, id ):
		self.c.execute( """SELECT id, address, contact_id FROM email WHERE id = ?;""", ( id, ) )
		return self.c.fetchone()
	
	def update( self, id, address ):
		self.c.execute( """UPDATE email SET address = ? WHERE id = ?;""", ( address, id ) )
		return self.c.fetchone()

	def delete( self, id ):
		self.c.execute( """DELETE FROM email WHERE id = ?;""", ( id, ) )
		self.conn.commit()
		return self.c.fetchone()

