import json
from data.pet_data import *
import requests
import pytest

from data.pet_data import Pet


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
        test = "pending,sold"

    def test_pet_findByStatus_invalidStatus(self):
        pass

    def test_pet_update_name(self):
        pass

    def test_pet_update_status(self):
        pass

    def test_pet_uploadImage_success(self):
        pass
        # url = "https://petstore.swagger.io/v2/pet/5030/uploadImage"
        # files = {'file': open('C:\\Users\\candk\\OneDrive\\Pictures\\cat.PNG', 'rb')}

    # r = requests.post(url, file = files)
    # print(r.status_code)
    # print(r.text)


