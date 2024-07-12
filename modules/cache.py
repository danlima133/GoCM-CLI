class Cache:
    def __init__(self):
        self.__cache = {}
    
    def get(self, key):
        try:
            return self.__cache[key]
        except KeyError:
            return None

    def set(self, key, value):
        self.__cache[key] = value

    def clear(self):
        self.__cache.clear()
            
    