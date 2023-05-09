class Recommender:
    def __init__(self):
        self.items = set()
        self.user_preferences = {}

    def add_item(self, item):
        self.items.add(item)
        self.user_preferences[item] = {}

    def update_preferences(self, user_id, item, reward):
        if item not in self.items:
            raise ValueError("Invalid item")

        if user_id not in self.user_preferences:
            self.user_preferences[user_id] = {}

        self.user_preferences[user_id][item] = reward
