import datetime
import itertools


class Cache:

    def __init__(self, size=5, ttl=10*60):
        self._size = size
        self._ttl = ttl
        self._cache = {}
        self._counter = itertools.count()

    def size(self):
        return len(self._cache)

    def get(self, key):
        if key not in self._cache:
            return None
        entry = self._cache[key]
        if not entry.valid:
            del self._cache[key]
            return None
        entry._access_time = next(self._counter)
        return entry.data

    def remove(self, key):
        if key in self._cache:
            del self._cache[key]

    def clear(self):
        self._cache = {}

    def contains(self, key):
        return key in self._cache

    def add(self, key, data, ttl=None):
        if ttl is None:
            ttl = self._ttl

        entry = Entry(data, ttl, next(self._counter))
        self._cache[key] = entry

        if self._size < len(self._cache):
            self._cache = dict(filter(lambda it: it.valid, entry.items()))

        if self._size <= len(self._cache):
            del self._cache[min(self._cache.items(), key=lambda it: it.valid)]


class Entry:
    def __init__(self, data, ttl, access_time):
        self._ttl = ttl
        self._data = data
        self._created = datetime.datetime.now()
        self._access_time = access_time

    @property
    def data(self):
        return self._data

    @property
    def ttl(self):
        return self._ttl

    @ttl.setter
    def ttl(self, value):
        self._ttl = datetime.timedelta(seconds=value)

    @property
    def access_time(self):
        return self._access_count

    @access_time.setter
    def access_time(self, value):
        self._access_time = value

    def valid(self):
        return self._created + self._ttl <= datetime.datetime.now();

