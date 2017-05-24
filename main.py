#!/usr/bin/env python
import webapp2


from handlers.topics import TopicAddHandler, TopicDetailsHandler
from handlers.base import BaseHandler, MainHandler, CookieAlertHandler
from handlers.comments import CommentAddHandler, CommentsListHandler, CommentDeleteHandler
from handlers.topics import TopicDelete, SubscribeToTopicHandler
from handlers.subscribe_to_forum import SubscribeToForumHandler
from tasks.email_new_comment import EmailNewCommentWorker
from crons.delete_topics import DeleteTopicsCron
from crons.subscribe_to_forum import SubscribeToForumCron
from crons.delete_comments import DeleteCommentsCron


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="main-page"),
    webapp2.Route('/set-cookie', CookieAlertHandler, name="cookie-alert-page"),
    webapp2.Route('/topic/add', TopicAddHandler),
    webapp2.Route('/comments/list', CommentsListHandler),
    webapp2.Route('/topic-details/<topic_id:\d+>', TopicDetailsHandler, name="topic-details"),
    webapp2.Route('/topic-details/<topic_id:\d+>/comment/add', CommentAddHandler, name="comment-add"),
    webapp2.Route('/comment/<comment_id:\d+>/delete', CommentDeleteHandler, name="comment-delete"),
    webapp2.Route('/topic/<topic_id:\d+>/delete', TopicDelete),
    webapp2.Route('/topic/<topic_id:\d+>/subscribe', SubscribeToTopicHandler),
    webapp2.Route('/subscribe', SubscribeToForumHandler),
    webapp2.Route('/task/email-new-comment', EmailNewCommentWorker),
    webapp2.Route('/cron/delete-topics', DeleteTopicsCron),
    webapp2.Route('/cron/subscribe-to-forum', SubscribeToForumCron),
    webapp2.Route('/cron/delete-comments', DeleteCommentsCron),
], debug=True)
