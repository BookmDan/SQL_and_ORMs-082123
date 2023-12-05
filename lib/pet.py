from __init__ import db_connection, db_cursor
# from owner import Owner

class Pet:
    all = {}

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

    def save(self):
        sql="""
            INSERT INTO pets (name, species)
            VALUES (?,?)
        """
        # bound parameter, prevents sql injections 
        
        db_cursor.execute(sql, (self.name, self.species)) 
        db_connection.commit()

        self.id = db_cursor.lastrowid


    
    # Pet("Moose", "dog")

    @classmethod
    def create(cls, name, species):
        pet = cls(name, species)
        pet.save()
        return pet
    
    def update(self):
        sql = """
            UPDATE pets 
            SET name = ?, species = ? 
            WHERE  id = ? 
        """ 

        db_cursor.execute(sql, (self.name, self.species, self.id))
        db_connection.commit()

    def delete(self):
        sql = """
            DELETE from pets 
            WHERE id = ? 
        """

        db_cursor.execute(sql, (self.id,))