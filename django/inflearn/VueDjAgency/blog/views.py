import json

from django.views.generic import DetailView, TemplateView

from api.utils import obj_to_post, prev_next_post, obj_to_comment
from blog.models import Post, Category, Tag


# Django-js 연동 이전
# post_detail.html를 클라이언트에게 보내줌


# class PostDV(TemplateView):
#     template_name = 'blog/post_detail.html'


class PostDV(DetailView):
    # model = Post
    template_name = 'blog/post_detail.html'

    # 변경점이 따로 없어 오버라이딩할 것이 없음
    # def get_object(self, queryset=None):
    #     pass
    #
    # def get_queryset(self):
    #     pass

    def get_queryset(self):
        # M:N => select_related, 1:N => prefetch_related
        return Post.objects.all().select_related('category').prefetch_related('tags', 'comment_set')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        obj = context['object']
        post = obj_to_post(obj)
        prevPost, nextPost = prev_next_post(obj)

        qsComment = obj.comment_set.all()
        commentList = [obj_to_comment(obj) for obj in qsComment]

        qs1 = Category.objects.all()
        qs2 = Tag.objects.all()
        cateList = [cate.name for cate in qs1]
        tagList = [tag.name for tag in qs2]

        dataDict = {
            'post': post,
            'prevPost': prevPost,
            'nextPost': nextPost,
            'commentList': commentList,
            'cateList': cateList,
            'tagList': tagList,
        }

        context['myJson'] = json.dumps(dataDict)
        return context
