import json
from data.pet_data import *
import requests
import pytest


@pytest.mark.usefixtures("setup_pet_data")
class TestPetStoreApi:

    @pytest.fixture(scope="class")
    def setup_pet_data(self):

        import_pet_data()        # load pet data into the database
        pets = get_pet_data()    # get pet data from database to post
        for pet in pets:
            r_add = requests.post(get_pet_endpoint(), json=pet.json())
            assert r_add.status_code == 200, f"Unable to add pet {pet.id}"

        yield

        # Delete each pet after running testcases in this class
        for pet in pets:
            r_delete = requests.delete(get_pet_endpoint() + str(pet.id))
            assert r_delete.status_code == 200, f"Unable to clean up pet {pet.id}"
        drop_pet_db()

    def test_pet_findById(self):
        pets = get_pet_data()
        pet_expected = pets[0]
        response = requests.get(get_pet_endpoint() + str(pet_expected.id))
        assert response.status_code == 200
        pet_res = json.loads(response.text)

        assert pet_res["id"] == pet_expected.id, "Pet id does not match"
        assert pet_res["name"] == pet_expected.pet_name, "Pet name does not match"
        assert pet_res["status"] == pet_expected.status, "Pet status does not match"

    def test_pet_find_idNotFound(self):
        response = requests.get(get_pet_endpoint() + "999999")
        assert response.status_code == 404
        error_msg = "Pet not found"
        result = json.loads(response.text)
        assert result["message"] == error_msg

    def test_pet_findByOneStatus(self):
        # Ensure only pets with available status are returned
        # Ensure the last pet in the result is the "available" pet we posted
        status = "available"

        pets = get_pet_data(status)
        response = requests.get(get_pet_endpoint() + "findByStatus", params={"status": status},)
        assert response.status_code == 200
        result = json.loads(response.text)
        count_status = sum(map(lambda x: x["status"] == status, result))
        assert count_status == len(result), "The number of available pets should be the total number returned (i.e. all are available)"
        assert result[-1]["id"] == pets[-1].id and result[-1]["name"] == pets[-1].pet_name, f"Last pet is not the {status} pet we posted"

    def test_pet_findByMultipleStatus(self):
        # Ensure only pets with pending or sold status are returned
        # Ensure the pending / sold pets we posted is in the resulted list
        test = "pending,sold"
        status_list = str.split(test, ",")
        pets = get_pet_data(test)
        response = requests.get(get_pet_endpoint() + "findByStatus", params={"status": test}, )
        assert response.status_code == 200
        result = json.loads(response.text)
        count_status = 0
        for status in status_list:
            count_status += sum(map(lambda x: x["status"] == status, result))
        assert count_status == len(
            result), f"The sum of {test} pets should be the total number returned"
        # Find pet in the result
        pets_found = 0
        for pet in pets:
            for res in result:
                if pet.id == res["id"]:
                    pets_found += 1
                    break
        assert pets_found == len(pets)

    def test_pet_update(self):

        pet_id = 1023
        parameters = {"name": "Pussy", "status": "sold"}
        response = requests.post(get_pet_endpoint() + str(pet_id), data=parameters,)
        assert response.status_code == 200
        result = json.loads(response.text)
        assert result["message"] == str(pet_id)
        response = requests.get(get_pet_endpoint() + str(pet_id))
        assert response.status_code == 200
        result = json.loads(response.text)
        assert result["name"] == parameters["name"]
        assert result["status"] == parameters["status"]

    def test_pet_uploadImage_success(self):

        pets = get_pet_data()
        pet_to_update = pets[0]
        files = {'file': open('C:\\Users\\candk\\OneDrive\\Pictures\\cat.PNG', 'rb')}
        response = requests.post(get_pet_endpoint() + str(pet_to_update.id) + "/uploadImage", files=files)
        assert response.status_code == 200
        assert "File uploaded to" in response.text





