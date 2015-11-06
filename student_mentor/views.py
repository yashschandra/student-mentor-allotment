from django.shortcuts import render, redirect
from student_mentor.models import Council, Club, Event, Student, Mentor, Participant, Team, Meeting_Participant, Meeting_Team, Pending_Team, Team_Event, Mentor_Event, Club_Form, Notification, Notification_Form
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, Count
from django.views.decorators.csrf import csrf_exempt

def index(request):
    if not 'logged_in' in request.session:
        return render(request, 'index.html')
    else:
        return redirect('home')
        
def signin(request):
    if not 'logged_in' in request.session:
        return render(request, 'signin.html')
    else:
        return redirect('home')
        
def profile(request):
    if request.method == 'POST':
        post = request.POST
        if post['query'] == 'signin_user':
            return redirect('home')
        elif post['query'] == 'signout':
            if 'logged_in' in request.session:
                del request.session['student_id']
                del request.session['id_token']
                del request.session['logged_in']
                del request.session['email']
            return redirect('signin')
        else:
            return redirect(post['query'])
    else:
        if 'logged_in' in request.session:
            return render(request, 'profile.html', {'id_token': request.session['id_token'], 'student_id': request.session['email']})
        else:
            return redirect('index')

def home(request):
    if request.method == 'POST':
        post = request.POST
        if post['query'] == 'signin_user':
            return redirect('home')
        elif post['query'] == 'signout':
            if 'logged_in' in request.session:
                del request.session['student_id']
                del request.session['id_token']
                del request.session['logged_in']
                del request.session['email']
            return redirect('signin')
        else:
            return redirect(post['query'])  
    else:
        if 'logged_in' in request.session:
            return render(request, 'home.html', {'id_token': request.session['id_token'], 'student_id': request.session['email']})
        else:
            return redirect('index')

def register(request):
    if request.method == 'POST':
        post = request.POST
        event = Event.objects.get(event_id = post['event'])
        if event.teamevent:
            return redirect('register_team', post['event'])
        else:
            student = Student.objects.get(student_id = request.session['student_id'])
            try:
                participant = Participant.objects.get(Q(student = student), Q(event = event))
                return redirect('error', 2)
            except ObjectDoesNotExist:
                if student.year <= event.participant_year_cutoff:
                    try:
                        mentor = Mentor.objects.get(Q(student = student), Q(event = event))
                        return redirect('error', 1)
                    except ObjectDoesNotExist:
                        participant = Participant(student = student, event = event)
                        participant.save()
                        if event.mentorevent:
                            mentor = Mentor.objects.filter(event = event).annotate(Count('participant')).order_by('participant__count').first()
                            participant.mentor = mentor
                            participant.save(update_fields = ['mentor'])
                        return redirect('success')
                else:
                    return redirect('error', 8)
    else:
        if 'logged_in' in request.session:
            events = Event.objects.filter(startdate_participant__lt = datetime.now()).filter(deadline_participant__gt = datetime.now())
            return render(request, 'register.html', {'events': events, 'id_token': request.session['id_token'], 'student_id': request.session['email']})
        else:
            return redirect('index')
   
def register_team(request, q):
    if request.method == 'POST':
        post = request.POST
        event = Event.objects.get(event_id = int(q))
        students = []
        for student in post.getlist('student_email'):
            try:
                student = Student.objects.get(email = student)
                try:
                    mentor = Mentor.objects.get(Q(student = student), Q(event = event))
                    return redirect('error', 1)
                except ObjectDoesNotExist:
                    if student.year <= event.participant_year_cutoff:
                        try:
                            team = Team.objects.get(Q(students = student), Q(event = event))
                            return redirect('error', 10)
                        except ObjectDoesNotExist:
                            students.append(student)
                    else:
                        return redirect('error', 8)
            except ObjectDoesNotExist:
                return redirect('error', 9)
        team = Team(team_name = post['team_name'], event = event)
        team.save()
        team.students.add(students[0])
        pending_team = Pending_Team(team_name = post['team_name'], event = event, team = team)
        pending_team.save()
        for student in students[1:]:
            pending_team.students.add(student)
        return redirect('success')
    else:
        if 'logged_in' in request.session:
            try:
                event = Event.objects.get(event_id = int(q))
                if not event.team_event:
                    return redirect('error', 11)
            except ObjectDoesNotExist:
                return redirect('error', 11)
            team_event = Team_Event.objects.get(event = event)
            return render(request, 'register_team.html', {'event': event, 'student_email': request.session['email'], 'min': team_event.min_participants, 'id_token': request.session['id_token'], 'student_id': request.session['email']})
        else:
            return redirect('index')
            
def team_request(request):
    if request.method == 'POST':
        post = request.POST
        team = Team.objects.get(team_id = post['team_id'])
        team_event = Team_Event.objects.get(event = team.event)
        if team.students.count() == team_event.max_participants:
            return redirect('error', 5)
        student = Student.objects.get(student_id = request.session['student_id'])
        team.students.add(student)
        if team.students.count() == team_event.min_participants:
            team.eligible = True
            team.save(update_fields = ['eligible'])
            if team.event.mentorevent:
                mentor = Mentor.objects.filter(event = team.event).annotate(Count('team')).order_by('team__count').first()
                team.mentor = mentor
                team.save(update_fields = ['mentor'])
        pending_teams = Pending_Team.objects.filter(students = student)
        for pending_team in pending_teams:
            pending_team.students.remove(student)
        return redirect('success')
    else:
        if 'logged_in' in request.session:
            student = Student.objects.get(student_id = request.session['student_id'])
            team_requests = Pending_Team.objects.filter(students = student)
            return render(request, 'team_requests.html', {'requests': team_requests, 'id_token': request.session['id_token'], 'student_id': request.session['email']})
        else:
            return redirect('index')
            
def requests(request):
    if request.method == 'POST':
        if request.method == 'POST':
            return redirect(request.POST['query'])
    else:
        if 'logged_in' in request.session:
            return render(request, 'requests.html', {'id_token': request.session['id_token'], 'student_id': request.session['email']})
        else:
            return redirect('index')
            
def success(request):
    if request.method == 'POST':
        post = request.POST
        if 'home' in post:
            return redirect('home')
    else:
        return render(request, 'success.html', {'id_token': request.session['id_token']})
    
def error(request, q):
    if request.method == 'POST':
        post = request.POST
        if 'home' in post:
            return redirect('home')
    else:
        if q == '1':
            msg = 'Mentors cannot participate in events.'
        elif q == '2':
            msg = 'You are already a participant.'
        elif q == '3':
            msg = 'You are already a mentor.'
        elif q == '4':
            msg = 'Participants cannot mentor event.'
        elif q == '5':
            msg = 'Team can have no more participants.'
        elif q == '6':
            msg = 'You cannot fix this meeting.'
        elif q == '7':
            msg = 'You are already in a team.'
        elif q == '8':
            msg = 'You do not satisfy the year cut off criteria.'
        elif q == '9':
            msg = 'Invalid email id given.'
        elif q == '10':
            msg = 'Someone is already in a team.'
        elif q == '11':
            msg = 'Invalid page request.'
        elif q == '12':
            msg = 'Student is already in the club.'
        elif q == '13':
            msg = 'There is some error in form.'
        elif q == '14':
            msg = 'Invalid url.'
        elif q == '15':
            msg = 'Event not found.'
        elif q == '16':
            msg = 'Club not found.'
        elif q == '17':
            msg = 'You do not belong to this team.'
        else:
            msg = 'Invalid error. Do not try to be oversmart..:P'
        return render(request, 'error.html', {'msg': msg, 'id_token': request.session['id_token']})
        
def error1(request):
    return redirect('error', '12')
        
def getinfo(request):
    return render(request, 'getinfo.html', {'id_token': request.session['id_token']})
    
def getinfo1(request, q):
    if q == 'council':
        obj = Council.objects.all()
    elif q == 'club':
        obj = Club.objects.all()
    elif q == 'event':
        obj = Event.objects.all()
    else:
        return redirect('error', 11)
    return render(request, 'getinfo1.html', {'object':reversed(obj), 'query': q, 'id_token': request.session['id_token']})

def join_club(request):
    if request.method == 'POST':
        post = request.POST
        if post['password'] == 'BIU#T78u3grbjdg78*TI':
            student = Student.objects.get(email = post['email'])
            club = Club.objects.get(club_id = post['club'])
            for c in student.clubs.all():
                if c.club_id == club.club_id:
                    return redirect('error', 12)
            student.clubs.add(club)
            return redirect('success')
        else:
            return redirect('error', 13) 
    else:
        if 'logged_in' in request.session:
            clubs = Club.objects.all()
            return render(request, 'join_club.html', {'clubs': clubs, 'id_token': request.session['id_token'], 'student_id': request.session['email']})
        else:
            return redirect('index')
        
def mentor_event(request):
    if request.method == 'POST':
        post = request.POST
        event = Event.objects.get(event_id = post['event'])
        student = Student.objects.get(student_id = request.session['student_id'])
        try:
            mentor = Mentor.objects.get(Q(student = student), Q(event = event))
            return redirect('error', 3)
        except ObjectDoesNotExist:
            if event.teamevent:
                try:
                    team = Team.objects.get(Q(event = event), Q(students = student))
                    return redirect('error', 7)
                except ObjectDoesNotExist:
                    cutoff = Mentor_Event.objects.get(event = event).mentor_year_cutoff
                    if student.year <= cutoff and student.year > 1:
                        mentor = Mentor(event = event, student = student)
                        mentor.save()
                        pending_teams = Pending_Team.objects.filter(Q(students = student), Q(event = event))
                        for pending_team in pending_teams:
                            pending_team.students.remove(student)
                        return redirect('success')
                    else:
                        return redirect('error', 8)
            else:
                try:
                    participant = Participant.objects.get(Q(student = student), Q(event = event))
                    return redirect('error', 2)
                except ObjectDoesNotExist:
                    cutoff = Mentor_Event.objects.get(event = event).mentor_year_cutoff
                    if student.year <= cutoff and student.year > 1:
                        mentor = Mentor(event = event, student = student)
                        mentor.save()
                        return redirect('success')
                    else:
                        return redirect('error', 8)
    else:
        if 'logged_in' in request.session:
            student = Student.objects.get(student_id = request.session['student_id'])
            clubs = student.clubs.all()
            events = []
            for club in clubs:
                event = Event.objects.filter(club = club).filter(mentorevent = True).filter(mentor_event__deadline_mentor__gt = datetime.now())
                if event:
                    events.append(event)
            return render(request, 'mentor_event.html', {'events': events, 'id_token': request.session['id_token'], 'student_id': request.session['email']})
        else:
            return redirect('index')
    
def my_clubs(request):
    if request.method == 'POST':
        pass
    else:
        if 'logged_in' in request.session:
            clubs = Student.objects.get(student_id = request.session['student_id']).clubs.all()
            return render(request, 'my_clubs.html', {'clubs': reversed(clubs), 'id_token': request.session['id_token'], 'student_id': request.session['email']})
        else:
            return redirect('index')
  
def my_events(request):
    if request.method == 'POST':
        post = request.POST
        if post['query'] == 'request_meeting_participant':
            participant = Participant.objects.get(participant_id = post['id'])
            participant.meeting_request = 'Pending'
            participant.save(update_fields = ['meeting_request'])
            return redirect('my_events')
        elif post['query'] == 'request_meeting_team':
            team = Team.objects.get(team_id = post['id'])
            team.meeting_request = 'Pending'
            team.save(update_fields = ['meeting_request'])
            return redirect('my_events')
        elif post['query'] == 'leave_event':
            participant = Participant.objects.get(participant_id = post['id'])
            participant.delete()
            return redirect('success')
    else:
        if 'logged_in' in request.session:
            student = Student.objects.get(student_id = request.session['student_id'])
            events = []
            participant = Participant.objects.filter(student = student).filter(event__on__gt = datetime.now())
            for p in participant:
                if p.meeting_request == 'Accepted':
                    try:
                        meeting_participant = Meeting_Participant.objects.get(Q(participant = p), Q(time__lte = datetime.now()))
                        p.meeting_request = 'None'
                        p.save(update_fields = ['meeting_request'])
                    except ObjectDoesNotExist:
                        pass
                events.append(p)
            team = Team.objects.filter(students = student).filter(eligible = True).filter(event__on__gt = datetime.now())
            for t in team:
                if t.meeting_request == 'Accepted':
                    try:
                        meeting_team = Meeting_Team.objects.get(Q(team = t), Q(time__lte = datetime.now()))
                        t.meeting_request = 'None'
                        t.save(update_fields = ['meeting_request'])
                    except ObjectDoesNotExist:
                        pass
                events.append(t)
            return render(request, 'my_events.html', {'events': events, 'id_token': request.session['id_token'], 'student_id': request.session['email']})
        else:
            return redirect('index')
     
def meeting_request(request):
    if request.method == 'POST':
        post = request.POST
        if post['query'] == 'fix_meeting':
            return redirect('fix', post['type'], post['id'])
    else:
        if 'logged_in' in request.session:
            participant_meeting_requests = Participant.objects.filter(Q(mentor__student__student_id = request.session['student_id']), Q(meeting_request = 'Pending'))
            team_meeting_requests = Team.objects.filter(Q(mentor__student__student_id = request.session['student_id']), Q(meeting_request = 'Pending'))
            return render(request, 'meeting_request.html', {'participant_meeting_requests': participant_meeting_requests, 'team_meeting_requests': team_meeting_requests, 'id_token': request.session['id_token'], 'student_id': request.session['email']})
        else:
            return redirect('index')
            
def fix(request, t, q):
    if request.method == 'POST':
        post = request.POST
        if t == 'participant':
            participant = Participant.objects.get(participant_id = int(q))
            participant.meeting_request = 'Accepted'
            participant.save(update_fields = ['meeting_request'])
            try:
                meeting_participant = Meeting_Participant.objects.get(participant = participant)
                meeting_participant.time = post['date_time']
                meeting_participant.place = post['place']
                meeting_participant.save(update_fields = ['time', 'place'])
            except ObjectDoesNotExist:
                meeting_participant = Meeting_Participant(participant = participant, time = post['date_time'], place = post['place'])
                meeting_participant.save()
            return redirect('meeting_request')
        elif t == 'team':
            team = Team.objects.get(team_id = int(q))
            team.meeting_request = 'Accepted'
            team.save(update_fields = ['meeting_request'])
            try:
                meeting_team = Meeting_Team.objects.get(team = team)
                meeting_team.time = post['date_time']
                meeting_team.place = post['place']
                meeting_team.save(update_fields = ['time', 'place'])
            except ObjectDoesNotExist:
                meeting_team = Meeting_Team(team = team, time = post['date_time'], place = post['place'])
                meeting_team.save()
            return redirect('meeting_request')
    else:
        if 'logged_in' in request.session:
            if t == 'participant':
                try:
                    participant = Participant.objects.get(participant_id = int(q))
                except ObjectDoesNotExist:
                    return redirect('error', 14)
                student = Student.objects.get(student_id = request.session['student_id'])
                if participant.mentor.student == student:
                    return render(request, 'fix.html', {'id_token': request.session['id_token'], 'datetime': participant.event.on})
                else:
                    return redirect('error', 6)
            elif t == 'team':
                try:
                    team = Team.objects.get(team_id = int(q))
                except ObjectDoesNotExist:
                    return redirect('error', 14)
                student = Student.objects.get(student_id = request.session['student_id'])
                if team.mentor.student == student:
                    return render(request, 'fix.html', {'id_token': request.session['id_token'], 'datetime': team.event.on, 'student_id': request.session['email']})
                else:
                    return redirect('error', 6)
        else:
            return redirect('index')

def get_slots(request):
    if request.method == 'POST':
        post = request.POST
        student = Student.objects.get(student_id = request.session['student_id'])
        start = datetime.strptime(str(post['date']), "%Y-%m-%d %H:%M") + timedelta(minutes = -30)
        end = start + timedelta(hours = 1)
        data = {}
        data['busy_slots'] = {}
        data['busy_slots'][0] = list(Meeting_Participant.objects.filter(participant__mentor__student = student).filter(time__range = (start, end)).values('time'))
        data['busy_slots'][1] = list(Meeting_Team.objects.filter(team__mentor__student = student).filter(time__range = (start, end)).values('time'))
        data['busy_slots'][2] = list(Meeting_Participant.objects.filter(participant__student = student).filter(time__range = (start, end)).values('time'))
        data['busy_slots'][3] = list(Meeting_Team.objects.filter(team__students = student).filter(time__range = (start, end)).values('time'))
        #print data
        return JsonResponse(data)

#@csrf_exempt        
def check_name(request):
    if request.method == 'POST':
        post = request.POST
        try:
            event = Event.objects.get(event_name = post['name'])
            return JsonResponse({'data': 'Not OK'})
        except ObjectDoesNotExist:
            return JsonResponse({'data': 'OK'})
             
def meetings(request):
    if request.method == 'POST':
        pass
    else:
        if 'logged_in' in request.session:
            student = Student.objects.get(student_id = request.session['student_id'])
            participant_meeting = Meeting_Participant.objects.filter(time__gt = datetime.now()).filter(Q(participant__mentor__student = student) | Q(participant__student = student))
            team_meeting = Meeting_Team.objects.filter(time__gt = datetime.now()).filter(team__students = student)
            team_meeting_mentor = Meeting_Team.objects.filter(time__gt = datetime.now()).filter(team__mentor__student = student)
            return render(request, 'meetings.html', {'participant_meeting': participant_meeting, 'team_meeting': team_meeting, 'team_meeting_mentor': team_meeting_mentor, 'id_token': request.session['id_token'], 'student_id': request.session['email']})
        else:
            return redirect('index')
    
def check_mail(request):
    if request.method == 'POST':
        post = request.POST
        if post['email'].split('@')[1] == 'itbhu.ac.in' or post['email'].split('@')[1] == 'iitbhu.ac.in':
        #if True:
            try:
                student = Student.objects.get(email = post['email'])
            except ObjectDoesNotExist:
                year = 16 - int(post['email'].split('@')[0][-2:])
                #year = 3
                student = Student(year = year, email = post['email'], student_name = post['name'].split(',')[0].rstrip())
                student.save()
            request.session['student_id'] = student.student_id
            request.session['id_token'] = post['id_token']
            request.session['logged_in'] = True
            request.session['email'] = post['email']
            return JsonResponse({'data': 'OK'})
        else:
            return JsonResponse({'data': 'Not OK'})
            
def add(request, q):
    if request.method == 'POST':
        post = request.POST
        if q == 'event' and post['password'] == 'gadjgi87*y*(YKJhkjhkes':
            event = Event(event_name = post['name'], club = Club.objects.get(club_id = post['club']), startdate_participant = post['startdate_participant'], deadline_participant = post['deadline_participant'], participant_year_cutoff = post['participant_year_cutoff'], event_type = post['event_type'], description = post['description'], on = post['on'])
            event.save()
            if post['team_event'] == 'yes':
                event.teamevent = True
                event.save(update_fields = ['teamevent'])
                team_event = Team_Event(event = event, min_participants = post['min_participants'], max_participants = post['max_participants'])
                team_event.save()
            if post['mentor_provided'] == 'yes':
                event.mentorevent = True
                event.save(update_fields = ['mentorevent'])
                mentor_event = Mentor_Event(event = event, deadline_mentor = post['deadline_mentor'], mentor_year_cutoff = post['mentor_year_cutoff'])
                mentor_event.save()
            return redirect('success')
        elif q == 'club' and post['password'] == '!#%$DGHSfjyt78uGU&%':
            form = Club_Form(post)
            if form.is_valid():
                form.save()
                return redirect('success')
            else:
                return redirect('error', 13)
        else:
            return redirect('error', 13)
    else:
        if 'logged_in' in request.session:
            if q == 'event':
                clubs = Club.objects.all()
                return render(request, 'add_event.html', {'clubs': clubs, 'id_token': request.session['id_token'], 'student_id': request.session['email']})
            elif q == 'club':
                form = Club_Form()
                return render(request, 'add_club.html', {'form': form, 'id_token': request.session['id_token'], 'student_id': request.session['email']})
            else:
                return redirect('error', 14)
        else:
            return redirect('index')
            
def edit(request, p, q):
    if request.method == 'POST':
        post = request.POST
        event = Event.objects.get(event_id = int(q))
        if p == 'event' and post['password'] == 'YYAJGF^&T@UJEGKJLneffls':
            event.event_name = post['name']
            event.club = Club.objects.get(club_id = post['club'])
            event.startdate_participant = post['startdate_participant']
            event.deadline_participant = post['deadline_participant']
            event.participant_year_cutoff = post['participant_year_cutoff']
            event.event_type = post['event_type']
            event.description = post['description']
            event.on = post['on']
            event.save()
            if post['team_event'] == 'yes':
                event.teamevent = True
                event.save(update_fields = ['teamevent'])
                try:
                    team_event = Team_Event.objects.get(event = event)
                    team_event.min_participants = post['min_participants']
                    team_event.max_participants = post['max_participants']
                except ObjectDoesNotExist:
                    team_event = Team_Event(event = event, min_participants = post['min_participants'], max_participants = post['max_participants'])
                team_event.save()
            else:
                event.teamevent = False
                event.save(update_fields = ['teamevent'])
                try:
                    team_event = Team_Event.objects.get(event = event)
                    team_event.delete()
                except ObjectDoesNotExist:
                    pass
            if post['mentor_provided'] == 'yes':
                event.mentorevent = True
                event.save(update_fields = ['mentorevent'])
                try:
                    mentor_event = Mentor_Event.objects.get(event = event)
                    mentor_event.deadline_mentor = post['deadline_mentor']
                    mentor_event.mentor_year_cutoff = post['mentor_year_cutoff']
                except ObjectDoesNotExist:
                    mentor_event = Mentor_Event(event = event, deadline_mentor = post['deadline_mentor'], mentor_year_cutoff = post['mentor_year_cutoff'])
                mentor_event.save()
            else:
                event.mentorevent = False
                event.save(update_fields = ['mentorevent'])
                try:
                    mentor_event = Mentor_Event.objects.get(event = event)
                    mentor_event.delete()
                except ObjectDoesNotExist:
                    pass
            return redirect('success')
    else:
        if 'logged_in' in request.session:
            if p == 'event':
                try:
                    event = Event.objects.get(event_id = int(q))
                except ObjectDoesNotExist:
                    return redirect('error', 15) 
                min_participants = 0
                max_participants = 0
                mentor_year_cutoff = 2
                deadline_mentor = datetime.now()
                if event.teamevent:
                    team_event = Team_Event.objects.get(event = event)
                    min_participants = team_event.min_participants
                    max_participants = team_event.max_participants
                if event.mentorevent:
                    mentor_event = Mentor_Event.objects.get(event = event)
                    mentor_year_cutoff = mentor_event.mentor_year_cutoff
                    deadline_mentor = mentor_event.deadline_mentor
                clubs = Club.objects.all()
                return render(request, 'edit_event.html', {'name': event.event_name, 'on': event.on, 'teamevent': event.teamevent, 'mentor_year_cutoff': mentor_year_cutoff, 'participant_year_cutoff': event.participant_year_cutoff, 'club': event.club.club_id, 'mentorevent': event.mentorevent, 'description': event.description, 'max_participants': max_participants, 'min_participants': min_participants, 'startdate_participant': event.startdate_participant, 'deadline_participant': event.deadline_participant, 'deadline_mentor': deadline_mentor, 'clubs': clubs, 'event_type': event.event_type})
            elif p == 'club':
                try:
                    club = Club.objects.get(event_id = int(q))
                except ObjectDoesNotExist:
                    return redirect('error', 16)
            else:
                return redirect('error', 14)
        else:
            return redirect('index')
            
def delete(request, p, q):
    if request.method == 'POST':
        post = request.POST
        if p == 'event' and post['password'] == 'JSQOY*D(#HKWDHIdfe':
            Event.objects.get(event_id = int(q)).delete()
            return redirect('success')
        if p == 'club' and post['password'] == '&^RFYWHV&S*Tguig87*':
            Club.objects.get(club_id = int(q)).delete()
            return redirect('success')
    else:
        if 'logged_in' in request.session:
            if p == 'event':
                try:
                    event = Event.objects.get(event_id = int(q))
                except ObjectDoesNotExist:
                    return redirect('error', 15)
                return render(request, 'delete_event.html', {'event': event})
            elif p == 'club':
                try:
                    club = Club.objects.get(club_id = int(q))
                except ObjectDoesNotExist:
                    return redirect('error', 16)
                return render(request, 'delete_club.html', {'club': club})
            else:
                return redirect('error', 14)
        else:
            return redirect('index')
            
def my_teams(request):
    if request.method == 'POST':
        post = request.POST
        if post['query'] == 'leave_team':
            student = Student.objects.get(email = request.session['email'])
            team = Team.objects.get(team_id = post['id'])
            team.students.remove(student)
            if team.students.count() == 0:
                team.delete()
            elif team.students.count() < Team_Event.objects.get(event = team.event).min_participants:
                team.eligible = False
                team.mentor = None
                team.save(update_fields = ['eligible', 'mentor'])
            return redirect('my_events')
    else:
        if 'logged_in' in request.session:
            student = Student.objects.get(email = request.session['email'])
            teams = Team.objects.filter(students = student)
            return render(request, 'my_teams.html', {'teams': teams, 'id_token': request.session['id_token'], 'student_id': request.session['email']})
        else:
            return redirect('index')
            
def add_team_members(request, q):
    if request.method == 'POST':
        post = request.POST
        team = Team.objects.get(team_id = int(q))
        students = []
        for student in post.getlist('student_email'):
            try:
                student = Student.objects.get(email = student)
                try:
                    mentor = Mentor.objects.get(Q(student = student), Q(event = team.event))
                    return redirect('error', 1)
                except ObjectDoesNotExist:
                    if student.year <= team.event.participant_year_cutoff:
                        try:
                            team = Team.objects.get(Q(students = student), Q(event = team.event))
                            return redirect('error', 10)
                        except ObjectDoesNotExist:
                            students.append(student)
                    else:
                        return redirect('error', 8)
            except ObjectDoesNotExist:
                return redirect('error', 9)
        pending_team = Pending_Team.objects.get(team = team)
        for student in students:
            pending_team.students.add(student)
        return redirect('success')
    else:
        if 'logged_in' in request.session:
            try:
                team = Team.objects.get(team_id = int(q))
            except ObjectDoesNotExist:
                return redirect('error', 14)
            student = Student.objects.get(email = request.session['email'])
            team_event = Team_Event.objects.get(event = team.event)
            if student in team.students.all():
                return render(request, 'add_team_members.html', {'team': team, 'count': team.students.count(), 'min': team_event.min_participants, 'id_token': request.session['id_token'], 'student_id': request.session['email']})
            else:
                return redirect('error', 17)
        else:
            return redirect('index')
            
def notifications(request):
    if request.method == 'POST':
        pass
    else:
        if 'logged_in' in request.session:
            notifications = Notification.objects.all()[:50]
            return render(request, 'notifications.html', {'notifications': reversed(notifications), 'id_token': request.session['id_token'], 'student_id': request.session['email']})
        else:
            return redirect('index')
            
def add_notification(request):
    if request.method == 'POST':
        post = request.POST
        if post['password'] == 'Y*#GDJGjefdy7t&*YTIUHkjbs,':
            form = Notification_Form(post)
            if form.is_valid():
                form.save()
                return redirect('success')
            else:
                return redirect('error', 13)
        else:
            return redirect('error', 13)
    else:
        if 'logged_in' in request.session:
            form = Notification_Form()
            return render(request, 'add_notification.html', {'form': form, 'id_token': request.session['id_token']})
        else:
            return redirect('index')
            
def kuchbhi(request, q):
    if 'logged_in' in request.session:
        return redirect('error', 14)
    else:
        return redirect('index')
