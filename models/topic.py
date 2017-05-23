from google.appengine.ext import ndb


class Topic(ndb.Model):
    title = ndb.StringProperty()
    content = ndb.TextProperty()
    author_email = ndb.StringProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)
    deleted = ndb.BooleanProperty(default=False)
    subscribers = ndb.StringProperty(repeated=True)
    subscribers_to_forum = ndb.StringProperty(repeated=True)

    @staticmethod
    def create(title, text, user):
        new_topic = Topic(title=title, content=text, author_email=user.email())
        new_topic.put()
        return new_topic
