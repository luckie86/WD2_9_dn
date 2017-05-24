import datetime
from handlers.base import BaseHandler
from models.comment import Comment


class DeleteCommentsCron(BaseHandler):
    def get(self):
        dt_delete_to = datetime.datetime.now() - datetime.timedelta(days=30)
        deleted_comments = Comment.query(Comment.deleted == True, Comment.created <= dt_delete_to).fetch()

        for commment in deleted_comments:
            commment.key.delete()