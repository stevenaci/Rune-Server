from utilities import JSONLoader

def get_configuration(configfileaddress='../config/config.json'):
    return JSONLoader.get_json(configfileaddress)
