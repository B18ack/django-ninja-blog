from blog_api.schemas import comments
from blog_app.models import Comment, Article
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404

class CommentService:
    def get_comments(
            self, 
            limit: int = 5, 
            offset: int = 0
    ) -> comments.CommentPaginatedSchema:
        objects = Comment.objects.all()
        total_comments = objects.count()
        return comments.CommentPaginatedSchema(
            total = total_comments,
            limit = limit,
            offset= offset,
            comments=objects[offset:limit]
        )
    

    def get_detail_comment(
            self, 
            id: int
        ) -> Comment:
        comments = get_object_or_404(Comment, id = id)
        return comments
    
    def create_comment(
            self,
            comment_data: comments.CommentUpdateCreateSchema
    ) -> Comment:
        data = comment_data.dict()
        article_id = data.pop('article_id')
        author_id = data.pop('author_id')
        
        article = get_object_or_404(Article, pk=article_id)
        author = get_object_or_404(User, pk=author_id)

        new_comment = Comment.objects.create(text=data.get('text'), article = article, author=author)
        new_comment.save()
        return new_comment

    def update_comment(
            self,
            id: int,
            comment_data: comments.CommentUpdateCreateSchema 
    )-> Comment:
        comment = get_object_or_404(Comment, id=id)
        temp_dict = {}
        for key, value in comment_data.dict().items():
            setattr(comment, key, value)

        comment.save()
        return comment

    def delete_comment(self, id:int):
        comment = get_object_or_404(Comment, id=id)
        comment.delete()
        return {'is_deleted': True}
    

comments_service = CommentService()