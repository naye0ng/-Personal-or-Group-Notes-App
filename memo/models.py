from django.db import models
from django.conf import settings

# Create your models here.
class Memo(models.Model) :
    title = models.CharField(max_length=50)
    content = models.TextField()
    # TODO : 태그목록 추가
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Meom는 자신을 좋아하는 user를 like_users로 조회
    # User는 자신이 좋아하는 memo를 like_memos로 조회
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_memos', blank=True)

    def __str__(self) :
        return f'{self.id} | {self.title} | {self.user}'