import zlib, pickle, io
import s3


def _dumps(x):
    return zlib.compress(pickle.dumps(x))

def _loads(x):
    return pickle.loads(zlib.decompress(x))

class S3Dict:
    def __init__(self, access_key, secret_key, bucket):
        self.upload = lambda k,v: s3.upload_to_s3(access_key, secret_key, bucket, k, v, 'application/python-pickle', 'zlib')

    def __contains__(self, k):
        raise NotImplementedError

    def __delitem__(self, k):
        raise NotImplementedError

    def __getitem__(self, k):
        raise NotImplementedError
        # return _loads

    def __setitem__(self, k, v):
        return self.upload(k, _dumps(v))

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
