import cgi
from google.appengine.api import users

from handlers.base import BaseHandler
from models.topic import Topic
from models.comment import Comment
from utils.decorators import validate_csrf


class TopicAddHandler(BaseHandler):
    def get(self):
        return self.render_template_with_csrf("topic_add.html")

    @validate_csrf
    def post(self):
        user = users.get_current_user()
        if not user:
            return self.write("You're not logged in.")
        title = cgi.escape(self.request.get("title"))
        text = cgi.escape(self.request.get("text"))
        new_topic = Topic.create(title=title, text=text, user=user)
        return self.redirect_to("topic-details", topic_id= new_topic.key.id())


class TopicDetailsHandler(BaseHandler):
    def get(self, topic_id):
        topic = Topic.get_by_id(int(topic_id))
        comments = Comment.query(Comment.topic_id == topic.key.id(), Comment.deleted == False).fetch()
        params = {"topic": topic, "comments": comments}
        return self.render_template_with_csrf("topic_details.html", params=params)


class TopicDelete(BaseHandler):
    @validate_csrf
    def post(self, topic_id):
        topic = Topic.get_by_id(int(topic_id))
        user = users.get_current_user()
        if topic.author_email == user.email() or users.is_current_user_admin():
            topic.deleted = True
            topic.put()
        return self.redirect("/")


class SubscribeToTopicHandler(BaseHandler):
    @validate_csrf
    def post(self, topic_id):
        user = users.get_current_user()
        if not user:
            return self.write("You're not logged in.")
        topic = Topic.get_by_id(int(topic_id))
        current_user_email = user.email()
        topic.subscribers.append(current_user_email)
        topic.put()
        return self.write("You are successfully subscribed to topic: %s " % topic.title)


class SubscribeToForumHandler(BaseHandler):
    def get(self):
        return self.render_template_with_csrf("subscribe_to_forum.html")

    @validate_csrf
    def post(self):
        user = users.get_current_user()
        if not user:
            return self.write("You're not logged in.")
        current_user_email = user.email()
        topics = Topic.query().fetch()
        for topic in topics:
            topic.subscribers_to_forum.append(current_user_email)
            topic.put()
        return self.write("You are successfully subscribed to hottest topics!")