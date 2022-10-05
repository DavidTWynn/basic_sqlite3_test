# Working on learning SQLite3

![GitHub last commit](https://img.shields.io/github/last-commit/davidtwynn/basic_sqlite3_test?style=plastic&color=blue)
![commits](https://badgen.net/github/commits/davidtwynn/basic_sqlite3_test?icon=github&color=blue)
![Python version](https://img.shields.io/badge/python%20version-3.10-blue)
![Coding style](https://img.shields.io/badge/code%20style-black-000000.svg)

Just a place for some basic examples

## Basics:

    1. Create connection
    2. Setup a cursor on connection
    3. Execute a command on cursor
    4. Commit the command statements on connection
    5. Close the connection

## Example usage of DbTests:

```python
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

        # Commit database changes
        print("Committing database changes...")
        database.commit()

        # Delete everything in the database
        print("Clearing devices...")
        database.clear_devices()

        # Show that nothing is in the database
        all_devices = database.get_all_devices()
        print(all_devices)
        # Output:
        # []

        # Commit changes
        print("Committing database changes...")
        database.commit()
```

## Run:

```bash
> python .\basic_sqlite3_test.py
```

#### Output:

```bash
[('asdf-rtr01', 'Cisco', '2921'), ('asdf-rtr02', 'Cisco', '2921'), ('asdf-dsw01', 'Cisco', '3560'), ('asdf-dsw02', 'Cisco', '3560')]
Committing database changes...
Clearing devices...
[]
Committing database changes...
```

## Resources:

Corey Schafer - https://www.youtube.com/watch?v=pd-0G0MigUA

SQLite docs - https://www.sqlite.org/docs.html

DigitalOcean - https://www.digitalocean.com/community/tutorials/how-to-use-the-sqlite3-module-in-python-3

Giraffe Academy - https://www.youtube.com/watch?v=HXV3zeQKqGY
