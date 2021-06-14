from django.db import models
from django.urls import reverse


class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    def __str__(self):
        return f'이름 : {self.site_name},  주소 : {self.url}'

    def get_absolute_url(self):   # 객체의 상세 화면 주소를 반환하는 메서드
        # reverse :  URL 패턴의 이름과 추가인자를 전달받아 URL을 생성하는 메서드
        return reverse('detail', args=[str(self.id)])
