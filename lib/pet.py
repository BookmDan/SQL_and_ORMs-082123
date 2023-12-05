from __init__ import db_connection, db_cursor
# from owner import Owner
import ipdb

class Pet:
    all = {}

    def __init__(self, name, species, owner_id, id=None):
        self.id = id
        self.name = name
        self.species = species
        self.owner_id = owner_id

    def __repr__(self):
        return f"<Pet {self.id}: {self.name} - {self.species}>"
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS pets(
            id INTEGER PRIMARY KEY,
            name TEXT,
            species TEXT,
            owner_id INTEGER,
            FOREIGN KEY (owner_id) REFERENCES owners(id))
        """

        # import ipdb; 
        # ipdb.set_trace()
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
            INSERT INTO pets (name, species, owner_id)
            VALUES (?,?,?)
        """
        # bound parameter, prevents sql injections 
        
        db_cursor.execute(sql, (self.name, self.species, self.owner_id)) 
        db_connection.commit()

        self.id = db_cursor.lastrowid

        Pet.all[self.id] = self


    
    # Pet("Moose", "dog")

    @classmethod
    def create(cls, name, species, owner_id):
        pet = cls(name, species, owner_id)
        pet.save()
        return pet
    
    def update(self):
        sql = """
            UPDATE pets 
            SET name = ?, species = ? , owner_id = ?
            WHERE  id = ? 
        """ 

        db_cursor.execute(sql, (self.name, self.species, self.owner_id, self.id))
        db_connection.commit()

    def delete(self):
        sql = """
            DELETE from pets 
            WHERE id = ? 
        """

        db_cursor.execute(sql, (self.id,))
        db_connection.commit()

        del Pet.all[self.id]
        self.id = None 

    @classmethod 
    def instance_from_db(cls, row):
        #check dictionary for existing instance of pet, using primary key 
        pet = cls.all.get(row[0])

        if pet: 
            pet.name = row[1]
            pet.species = row[2]
            pet.owner_id = row[3]
        else:
            pet = cls(row[1], row[2], row[3])
            pet.id = row[0]
            cls.all[pet.id] = pet
        return pet
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM pets

        """

        rows = db_cursor.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows ]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * 
            FROM pets 
            WHERE id = ? 
        """

        row = db_cursor.execute(sql, (id,)).fetchone()

        return cls.instance_from_db(row) if row else None 
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * 
            FROM pets 
            WHERE name = ? 
        """

        row = db_cursor.execute(sql, (name,)).fetchone()

        return cls.instance_from_db(row) if row else None 


