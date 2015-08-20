from django.conf.urls import include, url
from django.contrib.auth import views
import django.contrib.auth.urls
from main.views import MessageDetail


urlpatterns = [
    url(r'^$', 'main.views.new', name='new'),
    url(r'^mbhome/$', 'main.views.mbhome', name='mbhome'),
    url(r'^create-message/$',
        'main.views.create_message', name='create_message'),
    url(r'^message-board/$', 'main.views.message_board', name='message_board'),
    url(r'^message-admin/$',
        'main.views.message_admin', name='message_admin'),
    url(r'^short-messages/$',
        'main.views.short_messages', name='short_messages'),
    url(r'^message-detail/(?P<id>[0-9]+)/$',
        MessageDetail.as_view(), name='message_detail'),
    url(r'^message-detail/(?P<id>[0-9]+)/json/$',
        'main.views.message_json', name='message_json'),
    url(r'^login/$', views.login,
        {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', views.logout,
        {'next_page': '/message/login/', 'template_name': 'logout.html'},
        name='logout'),
    url(r'^create-account/$',
        'main.views.create_account', name='create_account'),
    url(r'^password/reset/$',
        views.password_reset,
        {"template_name": "password_reset/password-reset-form.html"},
        name="password_reset"
        ),
    url(r'^password/reset/done/$',
        views.password_reset_done,
        {'template_name': 'password_reset/password-reset-done.html'},
        name="password_reset_done"),
    url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
        views.password_reset_confirm,
        {'template_name': 'password_reset/password-reset-confirm.html'},
        name="password_reset_confirm"),
    url(r'^password/reset/confirm/complete/$',
        views.password_reset_complete,
        {'template_name': 'password_reset/password-reset-complete.html'},
        name="password_reset_complete"),

]
