from google.appengine.ext import ndb


class SubscriberToForum(ndb.Model):
    email = ndb.StringProperty()
