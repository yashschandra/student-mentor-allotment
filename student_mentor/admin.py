from django.contrib import admin
from .models import Club, Council, Event, Student, Mentor, Participant, Team, Meeting_Participant, Meeting_Team, Pending_Team, Mentor_Event, Team_Event

admin.site.register(Council)
admin.site.register(Club)
admin.site.register(Event)
admin.site.register(Student)
admin.site.register(Mentor)
admin.site.register(Participant)
admin.site.register(Team)
admin.site.register(Meeting_Participant)
admin.site.register(Meeting_Team)
admin.site.register(Pending_Team)
admin.site.register(Team_Event)
admin.site.register(Mentor_Event)
