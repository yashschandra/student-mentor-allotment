from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from datetime import datetime

year_cutoff_choices = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))
event_type_choices = (('Informal', 'Informal'), ('Formal', 'Formal'))
meeting_request_choices = (('None', 'None'), ('Accepted', 'Accepted'), ('Pending', 'Pending'))
notification_choices = (('mentor event', 'mentor event'), ('participate in event', 'participate in event'), ('event rescheduled', 'event rescheduled'))

class Council(models.Model):
    council_id = models.AutoField(primary_key = True)
    council_name = models.CharField(max_length = 30, unique = True)
    def __unicode__(self):
        return u'%s' % (self.council_name)
    
class Club(models.Model):
    club_id = models.AutoField(primary_key = True)
    club_name = models.CharField(max_length = 30, unique = True)
    council = models.ForeignKey(Council)
    def __unicode__(self):
        return u'%s %s' % (self.club_name, self.council.council_name)
        
class Club_Form(ModelForm):
    class Meta:
        model = Club
        fields = '__all__'
    
class Event(models.Model):
    event_id = models.AutoField(primary_key = True)
    event_name = models.CharField(max_length = 50)
    club = models.ForeignKey(Club)
    startdate_participant = models.DateTimeField()
    deadline_participant = models.DateTimeField()
    on = models.DateTimeField()
    participant_year_cutoff = models.SmallIntegerField(default = 5, choices = year_cutoff_choices)
    description = models.TextField(blank = True)
    mentorevent = models.BooleanField(default = False)
    teamevent = models.BooleanField(default = False)
    event_type = models.CharField(max_length = 10, choices = event_type_choices, default = 'Formal')
    def __unicode__(self):
        return u'%s %s' % (self.event_name, self.club.club_name)
        
class Team_Event(models.Model):
    event = models.OneToOneField(Event)
    min_participants = models.SmallIntegerField()
    max_participants = models.SmallIntegerField()
    def __unicode__(self):
        return u'%s' % (self.event)
        
class Mentor_Event(models.Model):
    event = models.OneToOneField(Event)
    deadline_mentor = models.DateTimeField()
    mentor_year_cutoff = models.SmallIntegerField(default = 2, choices = year_cutoff_choices)
    def __unicode__(self):
        return u'%s' % (self.event)
        
class Student(models.Model):
    student_id = models.AutoField(primary_key = True)
    student_name = models.CharField(max_length = 50)
    year = models.SmallIntegerField(default = 1)
    email = models.EmailField(unique = True, null = True)
    clubs = models.ManyToManyField(Club)
    def __unicode__(self):
        return u'%s %s' % (self.student_name, self.email)

class Mentor(models.Model):
    mentor_id = models.AutoField(primary_key = True)
    student = models.ForeignKey(Student)
    event = models.ForeignKey(Event)
    def __unicode__(self):
        return u'%s %s' % (self.student.student_name, self.event.event_name)
    
class Participant(models.Model):
    participant_id = models.AutoField(primary_key = True)
    student = models.ForeignKey(Student)
    event = models.ForeignKey(Event)
    mentor = models.ForeignKey(Mentor, null = True)
    meeting_request = models.CharField(max_length = 10, choices = meeting_request_choices, default = 'None')
    def __unicode__(self):
        return u'%s %s' % (self.student, self.event.event_name)
        
class Team(models.Model):
    team_id = models.AutoField(primary_key = True)
    team_name = models.CharField(max_length = 30)
    students = models.ManyToManyField(Student)
    event = models.ForeignKey(Event)
    mentor = models.ForeignKey(Mentor, null = True)
    eligible = models.BooleanField(default = False)
    meeting_request = models.CharField(max_length = 10, choices = meeting_request_choices, default = 'None')
    def __unicode__(self):
        return u'%s %s %s' % (self.team_name, self.event.event_name, ', '.join(student.student_name for student in self.students.all()))
        
class Pending_Team(models.Model):
    team_name = models.CharField(max_length = 30)
    students = models.ManyToManyField(Student)
    team = models.OneToOneField(Team)
    event = models.ForeignKey(Event)
    def __unicode__(self):
        return u'%s' % self.team
    
class Meeting_Participant(models.Model):
    time = models.DateTimeField()
    place = models.CharField(max_length = 30)
    participant = models.OneToOneField(Participant)
    def __unicode__(self):
        return u'%s %s' % (self.participant.student.student_name, self.participant.mentor)
    
class Meeting_Team(models.Model):
    time = models.DateTimeField()
    place = models.CharField(max_length = 30)
    team = models.OneToOneField(Team)
    def __unicode__(self):
        return u'%s %s' % (self.team.team_name, self.team.mentor)
        
class Notification(models.Model):
    notification_id = models.AutoField(primary_key = True)
    notification_type = models.CharField(max_length = 20, choices = notification_choices)
    event = models.ForeignKey(Event)
    on = models.DateTimeField(auto_now_add = True, default = datetime.now())
    message = models.TextField()
    def __unicode__(self):
         return u'%s %s' % (self.event.event_name, self.notification_type)
         
class Notification_Form(ModelForm):
    class Meta:
        model = Notification
        fields = '__all__'
