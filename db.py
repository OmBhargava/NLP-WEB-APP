import json


class DataBase:
    def insert(self, name, email, password):
        with open('users.json', 'r') as f:
            text = json.load(f)
            if email in text:
                return 0
            else:
                text[email] = [name, password]
        with open('users.json', 'w') as f:
            json.dump(text, f, indent=4)
            return 1

    def search(self,email, password):
        with open('users.json', 'r') as f:
            text = json.load(f)
            if email in text:
                if text[email][1] == password:
                    return 1
                else:
                    return 0
            else:
                return 0
