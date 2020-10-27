import configparser


def get_config():
    config = configparser.ConfigParser()
    config.read("..\\test.config.ini")
    return config


def get_pet_endpoint():
    petstore_section = get_config()["petstore"]
    pet_url = petstore_section["base_url"] + petstore_section["pet_endpoint"]
    return pet_url
