import zlib, pickle, io

def connect(access_key, secret_key, bucket):
    import tinys3
    return tinys3.Connection(access_key, secret_key, default_bucket = bucket)

def _dumps(x):
    return zlib.compress(pickle.dumps(x))

def _loads(x):
    return pickle.loads(zlib.decompress(x))

class S3Dict:
    def __init__(self, connection):
        self.c = connection

    def __contains__(self):
        raise NotImplementedError

    def __delitem__(self, k):
        raise NotImplementedError

    def __getitem__(self, k):
        return _loads(self.c.get(k))

    def __setitem__(self, k, v):
        return self.c.upload(k, io.BytesIO(_dumps(v)))

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
        for k,v in d.items():
            self[k] = v

    def keys(self):
        raise NotImplementedError

    def values(self):
        raise NotImplementedError

    def items(self):
        raise NotImplementedError
