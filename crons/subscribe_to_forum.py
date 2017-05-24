import datetime
from google.appengine.api import mail

from handlers.base import BaseHandler
from models.topic import Topic
from models.subscribe_to_forum import SubscriberToForum


class SubscribeToForumCron(BaseHandler):
    def get(self):
        dt_send_to = datetime.datetime.now() - datetime.timedelta(hours=24)
        hottest_topics = Topic.query(Topic.created <= dt_send_to).fetch()
        subscribers_to_forum = SubscriberToForum.query().fetch()

        for topic in hottest_topics:
            for email in subscribers_to_forum:
                mail.send_mail(
                    sender="luckie.luke@gmail.com",
                    to= email,
                    subject="Here are our hottest topics:",
                    body="""Topics with title %s have been created in last 24 hours
    
                        <a href='/topic-details/%s'>Link to the topic</a>"""
                         % (topic.title, topic.key.id())
                )
