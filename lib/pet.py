from __init__ import db_connection, db_cursor
# from owner import Owner

class Pet:

    def __init__(self, name, species, id=None):
        self.id = id
        self.name = name
        self.species = species

    def __repr__(self):
        return f"<Pet {self.id}: {self.name} - {self.species}>"
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS pets(
            id INTEGER PRIMARY KEY,
            name TEXT,
            species TEXT)
        """

        import ipdb; ipdb.set_trace()
        db_cursor.execute(sql)
        db_connection.commit()

    @classmethod
    def drop_table(csl):
        sql = """
            DROP TABLE IF EXISTS pets
        """

        db_cursor.execute(sql)
        db_connection.commit()



    
    # Pet("Moose", "dog")