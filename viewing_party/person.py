class Person:
    def __init__(self, name, watched, subscriptions):
        self.name = name
        self.watched = watched
        self.friends = []
        self.subscriptions = subscriptions
        
    def add_watched(self, movie):
        self.watched.append(movie)
    
    def get_num_watched(self):
        return len(self.watched)
    
    def add_friends(self,friend):
        self.friends.append(friend)
        