"""
mongo模块
"""
import pymongo
import sys

if sys.version.startswith('2.7'):
    from urllib import quote_plus
else:
    # TODO python3 for quote_plus
    from urllib.parse import quote_plus


class MongoPool(object):
    def __init__(self, host, username, password):
        uri = "mongodb://%s:%s@%s" % (quote_plus(username),
                                      quote_plus(password), quote_plus(host))
        self.mc = pymongo.MongoClient(uri)

    def close(self):
        self.mc.close()
