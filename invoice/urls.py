from django.conf.urls import url

from invoice import views

urlpatterns = [
    # /invoice/
    url(r'^$', views.index, name='index'),
    # /invoice/1001
    url(r'^(?P<sticker_id>\d+)$', views.stickerDetail, name='stickerDetail'),
    url(r'^unprinted/', views.stickerUnprinted, name='stickerUnprinted'),
]
