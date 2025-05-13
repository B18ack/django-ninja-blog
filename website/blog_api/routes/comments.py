from ninja import Router, Form
from blog_app.models import Comment
from django.shortcuts import get_object_or_404
from blog_api.schemas.comments import (
    CommentShortSchema,
    CommentPaginatedSchema,
    CommentUpdateCreateSchema
    )
from blog_api.services.comment import comments_service

router = Router(tags=['Comments'])

@router.get('/comments/', response=CommentPaginatedSchema)
def get_comments(request, limit: int = 5, offset: int = 0):
    return comments_service.get_comments(limit=limit, offset=offset)


@router.get('/comments/{id}/', response=CommentShortSchema)
def get_comment_detail(request, id: int):
    return comments_service.get_detail_comment(id=id)


@router.post('/comments/', response=CommentShortSchema)
def create_comment_object(request, comment_data: Form[CommentUpdateCreateSchema]):
    return comments_service.create_comment(comment_data=comment_data)


@router.put('/comments/{id}/update/', response=CommentShortSchema)
def update_comment(request, id:int, comment_data: CommentUpdateCreateSchema):
    return comments_service.update_comment(id=id,comment_data=comment_data)


@router.delete('/comments/{id}/delete/')
def delete_article(request, id:int):
    return comments_service.delete_comment(id=id)
