Class S3Dict:
    def __init__(self, bucket):
        self.bucket = bucket

    def __contains__(self):
        raise NotImplementedError

    def __delitem__(self, k):
        raise NotImplementedError

    def __getitem__(self, k):
        raise NotImplementedError

    def __setitem__(self, k, v):
        raise NotImplementedError

    def get(self, k, d = None):
        if k in self:
            return self[k]
        else:
            return d

    def setdefault(self, key, default):
        if key not in self:
            self[key] = default
        return self[key]

    def update(self, d):
        raise NotImplementedError

    def keys(self):
        raise NotImplementedError

    def values(self):
        raise NotImplementedError

    def items(self):
        raise NotImplementedError
