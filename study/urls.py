from django.conf.urls import url
from study import views


urlpatterns = [
    #学習/クラス
    url(r'^study/$', views.study_list, name='study_list'), #一覧
    url(r'^study/add/$', views.study_edit, name='study_add'), #登録
    url(r'^study/edit/(?P<study_id>\d+)/$', views.study_edit, name='study_edit'),  # 修正
    url(r'^study/del/(?P<study_id>\d+)/$', views.study_del, name='study_del'),  # 削除

]