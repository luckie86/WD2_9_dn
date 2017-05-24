from google.appengine.api import users

from handlers.base import BaseHandler
from models.topic import Topic
from models.subscribe_to_forum import SubscriberToForum
from utils.decorators import validate_csrf


class SubscribeToForumHandler(BaseHandler):
    def get(self):
        return self.render_template_with_csrf("subscribe_to_forum.html")

    @validate_csrf
    def post(self):
        user = users.get_current_user()
        if not user:
            return self.write("You're not logged in.")
        forum_subscriber = SubscriberToForum(email=user.email())
        forum_subscriber.put()
        return self.write("You are successfully subscribed to hottest topics")
