from testutil.test_util import *
import os


class Pet:

    def __init__(self, id, pet_name="Pussy", cat_id=0, cat_name="N/A", status="available"):
        self.id = id
        self.category_id = cat_id
        self.category_name = cat_name
        self.pet_name = pet_name
        self.status = status

    def json(self):
        """
        json representation of Pet
        :return:
        """
        return {"id": self.id, "category": {"id": self.category_id, "name": self.category_name}, "name": self.pet_name,
                "photoUrls": ["string"], "tags": [{"id": 1, "name": "cat"}], "status": self.status}


def get_pet_endpoint():
    petstore_section = get_config()["petstore"]
    pet_url = petstore_section["base_url"] + "pet/"
    return pet_url


def import_pet_data(filename="pet_data.sql"):
    current_dir = os.path.dirname(__file__)
    run_sql_script(current_dir + "\\" + filename)


def get_pet_data(status=None):
    """
    Get pet data from pets table from petsore database
    :param status: if status is none, return pets of any status
    :return: return list of Pet object
    """

    if status is None:
        query = "Select * from petstore.pets;"
    else:
        query = f"Select * from petstore.pets where pet_status='{status}';"
    pets = run_sql_query(query)   # result is a list of tuples (id, pet_name, category_id, category_name, pet_status)
    return [Pet(*p) for p in pets]


def drop_pet_db():
    query = "DROP DATABASE PetStore;"
    run_sql_query(query)

