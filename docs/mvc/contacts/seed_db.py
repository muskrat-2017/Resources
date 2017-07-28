import sqlite3, random
import faker



def seed_tables(database, contact_count):
	conn = sqlite3.connect(database)
	c = conn.cursor()
	fake = faker.Factory.create()

	seed_contacts(c, *((fake.name(),) for _ in range(contact_count)))
	conn.commit()
	seed_emails(c, *((fake.email(), random.randint(1, contact_count)) for _ in range(contact_count * 3)))
	conn.commit()
	seed_phones(c, *((fake.phone_number(), random.randint(1, contact_count)) for _ in range(contact_count * 3)))
	conn.commit()


def seed_contacts(c, *contacts):
	c.executemany("""INSERT INTO contact (name) VALUES (?)""", contacts)


def seed_emails(c, *params):
	c.executemany("""INSERT INTO email (address, contact_id) VALUES (?,?)""", params)


def seed_phones(c, *params):
	c.executemany("""INSERT INTO phone (number, contact_id) VALUES (?,?)""", params)



def main():
	seed_tables("contacts.db", random.randint(50, 100))

if __name__ == '__main__':
	main()