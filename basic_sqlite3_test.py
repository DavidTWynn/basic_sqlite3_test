import sqlite3


class DbTests:
    def __init__(self, db_name: str = "database.db"):
        """Sets up database object. Creates database.db in current dir
        if not specified.

        Example:\n
        with DbTests() as database:\n
            database.add_new_device("asdf-rtr01", "Cisco", "2921")\n
            all_devices = database.get_all_devices()\n
        """
        self.db_name = db_name

    def __enter__(self):
        """Context manager to establish DB connection"""
        self.cursor = self._connect_to_db()
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        """Context manager ending to close connection to DB."""
        self.cursor.close()

    def add_new_device(self, hostname, vendor, model):
        self.cursor.execute(
            f"INSERT INTO devices VALUES ('{hostname}', '{vendor}', '{model}')"
        )

    def get_all_devices(self) -> str:
        """Returns a list of tuples of all of the columns
        and rows of the devices table."""
        command = "SELECT * FROM devices"
        return self.cursor.execute(command).fetchall()

    def clear_devices(self):
        """Deletes all entries in the devices table."""
        command = "DELETE FROM devices"
        self.cursor.execute(command)

    def _connect_to_db(self) -> sqlite3.Cursor:
        """Connects to file location of sqlite3 database"""
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        return cursor

    def _create_new_table(self):
        """Creates new table for sqlite3 database to store device info"""
        self.cursor.execute(
            "CREATE TABLE devices (hostname TEXT, vendor TEXT, model TEXT)"
        )
        return True


def main():
    # Handle connections to the database and save devices
    with DbTests() as database:
        # Store device info in the database
        database.add_new_device("asdf-rtr01", "Cisco", "2921")
        database.add_new_device("asdf-rtr02", "Cisco", "2921")
        database.add_new_device("asdf-dsw01", "Cisco", "3560")
        database.add_new_device("asdf-dsw02", "Cisco", "3560")

        # Get info on all devices and print
        all_devices = database.get_all_devices()
        print(all_devices)
        # Output:
        # [('asdf-rtr01', 'Cisco', '2921'), ('asdf-rtr02', 'Cisco', '2921'),
        # ('asdf-dsw01', 'Cisco', '3560'), ('asdf-dsw02', 'Cisco', '3560')]

        # Delete everything in the database
        print("Clearing devices...")
        database.clear_devices()

        # Show that nothing is in the database
        all_devices = database.get_all_devices()
        print(all_devices)
        # Output:
        # []


if __name__ == "__main__":
    main()
