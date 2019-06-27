from django.urls import path, re_path
from . import views


urlpatterns = [
    path(r'',views.NoticesListView.as_view(),name='notices_list'),
    path(r'about/',views.AboutView.as_view(),name='about'),
    re_path(r'^notice/(?P<pk>\d+)$', views.NoticesDetailView.as_view(), name='notices_detail'),
    path(r'notice/new/', views.CreateNoticeView.as_view(), name='notices_new'),
    re_path(r'^notice/(?P<pk>\d+)/edit/$', views.NoticeUpdateView.as_view(), name='notices_edit'),
    path(r'drafts/', views.DraftListView.as_view(), name='notices_draft_list'),
    re_path(r'^notice/(?P<pk>\d+)/remove/$', views.NoticeDeleteView.as_view(), name='notices_remove'),
    re_path(r'^notice/(?P<pk>\d+)/publish/$', views.notice_publish, name='notices_publish'),
    re_path(r'^notice/(?P<pk>\d+)/comment/$', views.add_info_to_notice, name='add_info_to_notices'),
    re_path(r'^info/(?P<pk>\d+)/approve/$', views.info_approve, name='info_approve'),
    re_path(r'^info/(?P<pk>\d+)/remove/$', views.info_remove, name='info_remove'),
    path(r'quary/new/', views.CreateQueryView.as_view(), name='queries_new'),
    re_path(r'^quary/(?P<pk>\d+)$', views.QuaryDetailView.as_view(), name='queries_detail'),
    path(r'query/',views.QueryListView.as_view(),name='queries_list'),
    re_path(r'^query/(?P<pk>\d+)/remove/$', views.QueryDeleteView.as_view(), name='queries_remove'),
    path('submitted/',views.thanksView.as_view(), name='thanks'),
]
