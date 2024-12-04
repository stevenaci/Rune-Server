import pickle

# Here we can save new users, load user settings and
# variable paths... such as private folders ..

def load_name(name, password):

    userdata = pickle.load(open("/SaveData/UserData", "rb"))
    for username, passwd in userdata.items():
        # check username exists
        if username == name:
            # check pass is correct
            if passwd == password:
                return {"Code": 888, "Response": "NULL"}  # positive response
            else:
                return {"Code": 555, "Response": "password_not_valid"}
        else:
            return {"Code": 555, "Response": "name_not_valid"}  # negative response

def save_name(name, password):

    # to do, add auth^^^, add encryption
    userdata = pickle.load(open("/SaveData/UserData", "rb"))

    # see if name exists already
    for username in userdata.items():
        if username == name:
            return {"Code": 555, "Response": "name_exists"}

    userdata = userdata[:1]  # take away closing parentheses
    usersave = "," + name + ":" + password + "}"  # add it on the end
    writedata = userdata + usersave

    pickle_out = open("/SaveData/UserData", "wb")
    pickle.dump(writedata, pickle_out)
    pickle_out.close()
    return {"Code": 888, "Response": "NULL"}
