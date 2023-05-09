import math

class Recommender:
    def __init__(self, c=1):
        self.items = set()
        self.user_preferences = {}
        self.c = c

    def add_item(self, item):
        self.items.add(item)
        self.user_preferences[item] = {}

    def update_preferences(self, user_id, item, reward):
        if item not in self.items:
            raise ValueError("Invalid item")

        if user_id not in self.user_preferences:
            self.user_preferences[user_id] = {}

        n = len(self.user_preferences[user_id])
        if n == 0:
            self.user_preferences[user_id][item] = reward
        else:
            total_reward = sum(self.user_preferences[user_id].values())
            avg_reward = total_reward / n
            delta_i = math.sqrt(2 * math.log(n) / n)
            ucb = avg_reward + self.c * delta_i
            if item in self.user_preferences[user_id]:
                self.user_preferences[user_id][item] = ((n - 1) / n) * self.user_preferences[user_id][item] + (1 / n) * reward
            else:
                self.user_preferences[user_id][item] = reward
            self.user_preferences[user_id][item] += ucb

    def get_top_n_preferences(self, user_id, n):
        if user_id not in self.user_preferences:
            return []
        return sorted(self.user_preferences[user_id].items(), key=lambda x: x[1], reverse=True)[:n]
