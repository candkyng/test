from testutil.test_util import *

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