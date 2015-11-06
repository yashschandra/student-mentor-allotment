from django.conf.urls import patterns, url, include
from student_mentor import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('', 
    url(r'^$', views.index, name = 'index'),
    url(r'signin/$', views.signin, name = 'signin'),
    url(r'home/$', views.home, name = 'home'),
    url(r'register/$', views.register, name = 'register'),
    url(r'success/$', views.success, name = 'success'),
    url(r'error/(?P<q>\w+)$', views.error, name = 'error'),
    url(r'error/$', views.error1, name = 'error1'),
    url(r'register_team/(?P<q>\w+)$', views.register_team, name = 'register_team'),
    url(r'add_team_members/(?P<q>\w+)$', views.add_team_members, name = 'add_team_members'),
    url(r'my_teams/$', views.my_teams, name = 'my_teams'),
    url(r'getinfo$', views.getinfo, name = 'getinfo'),
    url(r'getinfo/(?P<q>\w+)$', views.getinfo1, name = 'getinfo1'),
    url(r'getinfo/(?P<q>\w+)/add/$', views.add, name = 'add'),
    url(r'join_club/$', views.join_club, name = 'join_club'),
    url(r'mentor_event/$', views.mentor_event, name = 'mentor_event'),
    url(r'my_clubs/$', views.my_clubs, name = 'my_clubs'),
    url(r'my_events/$', views.my_events, name = 'my_events'),
    url(r'fix/(?P<t>\w+)/(?P<q>\w+)$', views.fix, name = 'fix'),
    url(r'requests/$', views.requests, name = 'requests'),
    url(r'meeting_request/$', views.meeting_request, name = 'meeting_request'),
    url(r'team_request/$', views.team_request, name = 'team_request'),
    url(r'meetings/$', views.meetings, name = 'meetings'),
    url(r'notifications/$', views.notifications, name = 'notifications'),
    url(r'notifications/add/$', views.add_notification, name = 'add_notification'),
    url(r'check_mail/$', views.check_mail, name = 'check_mail'),
    url(r'check_name/$', views.check_name, name = 'check_name'),
    url(r'get_slots/$', views.get_slots, name = 'get_slots'),
    url(r'profile/$', views.profile, name = 'profile'),
    url(r'(?P<q>\w+)/$', views.kuchbhi, name = 'kuchbhi'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)