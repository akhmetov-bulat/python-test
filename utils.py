import json


def read_users():
    with open('users.json', 'r', encoding='utf-8') as f:
        raw_json = f.read()
        if raw_json == "":
            users = []
        else:
            users = json.loads(raw_json)
    return users


def write_users(name, age, is_blocked, date):
    with open('users.json', 'r', encoding='utf-8') as f:
        raw_json = f.read()
        if raw_json == "":
            users = []
        else:
            users = json.loads(raw_json)
    if is_blocked:
        users.append({"name": name, "age": age,
                      "is_blocked": is_blocked,
                      "unblock_date": date})
    else:
        users.append({"name": name, "age": age})
    with open('users.json', 'w', encoding='utf-8') as f:
        raw_json = json.dumps(users)
        f.write(raw_json)
    return users