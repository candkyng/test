import json

import requests
import pytest

from data.pet_data import Pet
from testutil.petstore_util import *


@pytest.mark.usefixtures("setup_pet_data")
class TestPetStoreApi:

    pet_id = 1214

    @pytest.fixture(scope="class")
    def setup_pet_data(self):

        # Add a pet for all testcases
        r_add = requests.post(get_pet_endpoint(), json=Pet(self.pet_id).json())
        assert r_add.status_code == 200

        yield

        # Delete the pet after running testcases in this class
        r_delete = requests.delete(get_pet_endpoint() + str(self.pet_id))
        assert r_delete.status_code == 200

    def test_pet_findById(self):
        response = requests.get(get_pet_endpoint() + str(self.pet_id))
        assert response.status_code == 200
        pet_res = json.loads(response.text)
        pet_expected = Pet(self.pet_id)
        assert pet_res["id"] == pet_expected.id, "Pet id does not match"
        assert pet_res["name"] == pet_expected.pet_name, "Pet name does not match"
        assert pet_res["status"] == pet_expected.status, "Pet status does not match"

    def test_pet_find_idNotFound(self):
        response = requests.get(get_pet_endpoint() + "999999")
        assert response.status_code == 404
        error_msg = "Pet not found"
        result = json.loads(response.text)
        assert result["message"] == error_msg

    def test_pet_findByStatus(self):
        pass

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


