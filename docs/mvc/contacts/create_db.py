import sqlite3

def create_tables(database):
	conn = sqlite3.connect(database)
	c = conn.cursor()

	c.execute("""CREATE TABLE contact(
		id INTEGER,
		name VARCHAR,
		PRIMARY KEY('id')
	)""")

	c.execute("""CREATE TABLE phone(
		id INTEGER,
		number VARCHAR,
		contact_id INTEGER,
		PRIMARY KEY('id'),
		FOREIGN KEY('contact_id') REFERENCES contact('id')
	)""")

	c.execute("""CREATE TABLE email(
		id INTEGER,
		address VARCHAR,
		contact_id INTEGER,
		PRIMARY KEY('id'),
		FOREIGN KEY('contact_id') REFERENCES contact('id')
	)""")

	conn.commit()

def main():
	create_tables("contacts.db")

if __name__ == '__main__':
	main()