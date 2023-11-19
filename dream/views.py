from django.shortcuts import render,redirect, get_object_or_404
from .models import Preference, Preference_Tag,Agenda,Agenda_Tag,Recruitment,Preference_people,Agenda_people,Recruitment_people,Recruitment_Tag, Preference_GroupMessage,Agenda_GroupMessage
from accounts.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib import messages
from django.db import IntegrityError



@login_required       
def index(request):
        name=request.user.username
        preference = Preference_people.objects.filter(username=name)
        agenda = Agenda_people.objects.filter(username=name)
        recruitment = Recruitment_people.objects.filter(username=name)
        context = {
            'preference': preference,
            'agenda': agenda,
            'recruitment': recruitment,
        }
        #print("all_data:", all_data)
        return render(request, 'dream/index.html', context)

@login_required
def preference_list(request):
    all_data = Preference.objects.all().order_by('-create_date')
    
    context = {
        'all_data':all_data,
    }

    return render(request, 'dream/preference_list.html', context)
    
@login_required
def agenda_list(request):
    all_data = Agenda.objects.all().order_by('-create_date')
    context = {
        'all_data':all_data,
    }
    return render(request, 'dream/agenda_list.html', context)

@login_required
def recruitment_list(request):
    all_data = Recruitment.objects.all().order_by('-create_date')
    context = {
        'all_data':all_data,
    }
    return render(request, 'dream/recruitment_list.html', context)

@login_required
def preference_create(request):
    if request.method == 'POST':
            title = request.POST['title']
            body = request.POST['body']
            #tags = request.POST['tags']
            
            try:
                preference = Preference(title = title, body = body)
                preference.save()
                
                ''' if new_tag:
                    print("追加前：", preference.tags.all())
                    for tag in new_tag.split():
                        is_exists = Preference_Tag.objects.filter(name=tag)
                        if not is_exists:
                            Preference_Tag.objects.create(name=tag)
                        
                        Preference.tags.add(tag)
                    print("追加後：", preference.tags.all())'''

                all_data = Preference.objects.all().order_by('-create_date')
                context = {
                    'all_data':all_data,
                }
                return render(request, 'dream/preference_list.html', context)

            except IntegrityError:
                error_message = "このtitleは既に使用されています。別のtitleを使用してください"
                all_data = Preference.objects.all().order_by('-create_date')
                context = {
                    'all_data':all_data,
                    'error_message':error_message,
                }
                return render(request, 'dream/preference_create.html', context)
                
    return render(request, 'dream/preference_create.html')


'''
@login_required
def preference_create(self, form,request):
    if request.method == 'POST':
            preference = form.save()
            new_tag = self.request.POST.get("new_tag")
            
            
            if new_tag:
                print("追加前：", preference.tags.all())
                for tag in new_tag.split():
                    is_exists = Preference_Tag.objects.filter(name=tag)
                    if not is_exists:
                        Preference_Tag.objects.create(name=tag)
                    
                    Preference.tags.add(tag)
                print("追加後：", preference.tags.all())
                
            return redirect("preference_list")
        
    return render(request, 'dream/preference_create.html')
    
    
'''
'''
class PreferenceCreateView(CreateView):
    model = Preference
    template_name = "dream/preference_create.html"
    fields = "__all__"
    success_url = reverse_lazy("preference_list")
    
    def form_valid(self, form):
            preference = form.save()
            new_tag = self.request.POST.get("new_tag")
            
            
            if new_tag:
                print("追加前：", preference.tags.all())
                for tag in new_tag.split():
                    is_exists = Preference_Tag.objects.filter(name=tag)
                    if not is_exists:
                        Preference_Tag.objects.create(name=tag)
                    
                    Preference.tags.add(tag)
                print("追加後：", preference.tags.all())
                
            return redirect("preference_list")
            
 '''
 
                
    
@login_required
def agenda_create(request):
    if request.method == 'POST':
            
            title = request.POST['title']
            body = request.POST['body']
            #tags = request.POST['tags']
            #new_tag = request.POST['new_tag']
            #if new_tag:
            #    print("追加前：", agenda.tags.all())
            #    for tag in new_tag.split():
            #        is_exists = Agenda_Tag.objects.filter(name=tag)
            #        if not is_exists:
            #            Agenda_Tag.objects.create(name=tag)
            #        
            #        Agenda.tags.add(tag)
            #    print("追加後：", agenda.tags.all())
            try:
                agenda = Agenda(title = title, body = body)
                agenda.save()
                all_data = Agenda.objects.all().order_by('-create_date')
                context = {
                    'all_data':all_data,
                }
                return render(request, 'dream/agenda_list.html', context)
            except IntegrityError:
                error_message = "このtitleは既に使用されています。別のtitleを使用してください"
                all_data = Preference.objects.all().order_by('-create_date')
                context = {
                    'all_data':all_data,
                    'error_message':error_message,
                }
                return render(request, 'dream/agenda_create.html', context)
            
    return render(request, 'dream/agenda_create.html')
 
@login_required   
def recruitment_create(request):
    if request.method == 'POST':
            
            title = request.POST['title']
            body = request.POST['body']
            adress = request.POST['adress']
            author = request.user.username
            
            '''if new_tag:
                print("追加前：", recruitment.tags.all())
                for tag in new_tag.split():
                    is_exists = Recruitment_Tag.objects.filter(name=tag)
                    if not is_exists:
                        Recruitment_Tag.objects.create(name=tag)
                    
                    Recruitment.tags.add(tag)
                print("追加後：", recruitment.tags.all()) '''
            try:
                recruitment = Recruitment(title = title, body = body, adress =adress,author=author)
                recruitment.save()
                
                all_data = Recruitment.objects.all().order_by('-create_date')
                context = {
                    'all_data':all_data,
                }
                return render(request, 'dream/recruitment_list.html', context)
            except IntegrityError:
                error_message = "このtitleは既に使用されています。別のtitleを使用してください"
                all_data = Recruitment.objects.all().order_by('-create_date')
                context = {
                    'all_data':all_data,
                    'error_message':error_message
                }
                return render(request, 'dream/recruitment_create.html', context)
    return render(request, 'dream/recruitment_create.html')


@login_required
def preference_groupchat(request, room_name):
    if request.method == 'POST':
        username = request.user.username
        message = request.POST.get('message')
        title = Preference.objects.get(title=room_name)
        preference = Preference_GroupMessage(title = title, username=username, message=message)
        #Preference_GroupMessage.objects.create(title = title, username=username, message=message)
        #return redirect('preference_groupchat', room_name = room_name)
        preference.save()
        
    messages = Preference_GroupMessage.objects.filter(title=room_name)
    context = {'messages': messages,
               'room_name':room_name,
               }
    return render(request, 'dream/preference_groupchat.html', context)

    
'''   
@login_required
def preference_groupchat(request, room_name):
    
    all_data = Preference_GroupMessage.objects.all().order_by('-create_date')
    context = {
        'room_name':room_name,
        'all_data':all_data,
    }
    
    if request.method == 'POST' and request.is_ajax():         
            body = request.POST.get("message")
            user_name = request.user
            title = Preference.objects.get(title=room_name)
            preference_groupmessage = Preference_GroupMessage(title = title, body = body, user_name = user_name)
            preference_groupmessage.save()
            return redirect ("preference_groupchat", room_name = room_name)
    else:
        return render(request, 'dream/preference_groupchat.html', context)
'''
'''   
@login_required
def preference_groupchat(request, room_name):
    form = Preference_GroupMessageForm()
    if form.is_valid():
        message = form.save(commit=False)
        message.username = request.username
        message.title = room_name
        message.body = form.cleaned_data['message']
       
        message.save()
        
    else:
        form = Preference_GroupMessageForm()
        
    messages = Preference_GroupMessage.objects.filter(title = room_name)
    return render(request,'dream/preference_groupchat.html', {
            'room_name':room_name,
            'messages':messages,
            'form':form
        })
 '''   
@login_required
def agenda_groupchat(request, room_name):
    if request.method == 'POST':
        username = request.user.username
        message = request.POST.get('message')
        title = Agenda.objects.get(title=room_name)
        agenda = Agenda_GroupMessage(title = title, username=username, message=message)
        #Agenda_GroupMessage.objects.create(title = title, username=username, message=message)
        #return redirect ("agenda_groupchat", room_name = room_name)
        agenda.save()

    messages = Agenda_GroupMessage.objects.filter(title=room_name)
    context = {'messages': messages,
               'room_name':room_name,}
    return render(request, 'dream/agenda_groupchat.html', context)
    
'''
@login_required
def agenda_groupchat(request, room_name):
    form = Agenda_GroupMessageForm()
    if form.validate_on_submit():
        message = Agenda_GroupMessage(body=form.message.data,
            username=request.username, title=room_name)
        form.save()
    messages = Agenda_GroupMessage.objects.filter(
        Agenda_GroupMessage.title == room_name
    )
    return render('agenda_groupchat.html', room_name=room_name,
        messages=messages, form=form)
'''
    
def detail(request, title):
    data = get_object_or_404(Recruitment, title=title)
    context = {
        'data': data,
    }
    return render(request, 'dream/detail.html',context)

def preference_like_delete(request, id):
    delete_data = get_object_or_404(Preference_people, pk=id)
    delete_data.delete()
    messages.success(request, 'data deleted.')
    name=request.user.username
    preference = Preference_people.objects.filter(username=name)
    agenda = Agenda_people.objects.filter(username=name)
    recruitment = Recruitment_people.objects.filter(username=name)
    context = {
            'preference': preference,
            'agenda': agenda,
            'recruitment': recruitment,
        }
        #print("all_data:", all_data)
    return render(request, 'dream/index.html', context)

def agenda_like_delete(request, id):
    delete_data = get_object_or_404(Agenda_people, pk=id)
    delete_data.delete()
    messages.success(request, 'data deleted.')
    name=request.user.username
    preference = Preference_people.objects.filter(username=name)
    agenda = Agenda_people.objects.filter(username=name)
    recruitment = Recruitment_people.objects.filter(username=name)
    context = {
            'preference': preference,
            'agenda': agenda,
            'recruitment': recruitment,
        }
        #print("all_data:", all_data)
    return render(request, 'dream/index.html', context)

def recruitment_like_delete(request, id):
    delete_data = get_object_or_404(Recruitment_people, pk=id)
    delete_data.delete()
    messages.success(request, 'data deleted.')
    name=request.user.username
    preference = Preference_people.objects.filter(username=name)
    agenda = Agenda_people.objects.filter(username=name)
    recruitment = Recruitment_people.objects.filter(username=name)
    context = {
            'preference': preference,
            'agenda': agenda,
            'recruitment': recruitment,
        }
        #print("all_data:", all_data)
    return render(request, 'dream/index.html', context)


    
    
def delete(request, title):
    delete_data = get_object_or_404(Recruitment, title=title)
    delete_data.delete()
    messages.success(request, 'data deleted')
    name=request.user.username
    preference = Preference_people.objects.filter(username=name)
    agenda = Agenda_people.objects.filter(username=name)
    recruitment = Recruitment_people.objects.filter(username=name)
    context = {
            'preference': preference,
            'agenda': agenda,
            'recruitment': recruitment,
        }
        #print("all_data:", all_data)
    return render(request, 'dream/index.html', context)

def preference_search(request):
    keyword = request.GET.get("keyword")
    data =Preference.objects.all()
    queryset="a"
    error_message="a"
    list = []
    for da in data:
        search = da.title
        list.append(search)
    
    if keyword in list:
            queryset = "b"
    else:
            error_message = "That title does not exist."
        
    all_data = Preference.objects.all().order_by('-create_date')
    context = {
        "queryset":queryset,
        "all_data" :all_data,
        "keyword": keyword,
        "error_message":error_message,
    }
    return render(request, "dream/preference_list.html", context)



'''
class PreferenceSearchView(View):
    template_name = "dream/preference_list.html"
    def get(self, request, *args, ** kwargs):
        post_data = Preference.objects.order_by('-id')
        keyword = request.GET.get('keyword')
        
        if keyword:
            exclusion_list = set([' ', '  '])
            query_list =''
            for word in keyword:
                if not word in exclusion_list:
                    queryset += word
            query = reduce(and_, [Q(title_icontains=q) | Q(content_icontains=q) for q in query_list])
            post_data = post_data.filter(query)
            
        return render(request, 'dream/preference_list', 
                      {
            'keyword': keyword,
            'post_data': post_data
        })
'''
def agenda_search(request):
    keyword = request.GET.get("keyword")
    data =Agenda.objects.all()
    queryset="a"
    error_message="a"
    list = []
    for da in data:
        search = da.title
        list.append(search)
    
    if keyword in list:
            queryset = "b"
    else:
            error_message = "That title does not exist."
        
    all_data = Agenda.objects.all().order_by('-create_date')
    context = {
        "queryset":queryset,
        "all_data" :all_data,
        "keyword": keyword,
        "error_message":error_message,
    }
    return render(request, "dream/agenda_list.html", context)

def recruitment_search(request):
    keyword = request.GET.get("keyword")
    data =Recruitment.objects.all()
    queryset="a"
    error_message="a"
    list = []
    for da in data:
        search = da.title
        list.append(search)
    
    if keyword in list:
            queryset = "b"
    else:
            error_message = "That title does not exist."
        
    all_data = Recruitment.objects.all().order_by('-create_date')
    context = {
        "queryset":queryset,
        "all_data" :all_data,
        "keyword": keyword,
        "error_message":error_message,
    }
    return render(request, "dream/recruitment_list.html", context)
@login_required
def preference_like(request, room_name):
    all_data = Preference.objects.all().order_by('-create_date')

    if request.method == 'POST':        
            title = Preference.objects.get(title=room_name)
            if Preference_people.objects.filter(title=title).exists():
                error_message = 'すでに登録されています'
                return render(request, 'dream/preference_list.html',
                              {'error_message': error_message,
                               'all_data': all_data
                               }
                              )
            else:
                username=request.user.username
                preference_people = Preference_people(title = title, username=username)
                preference_people.save()
                preference = Preference_people.objects.filter(username=request.user.username)
                agenda = Agenda_people.objects.filter(username=request.user.username)
                recruitment = Recruitment_people.objects.filter(username=request.user.username)
                context = {
                            'preference': preference,
                            'agenda': agenda,
                            'recruitment': recruitment,
                            }
                return render (request, "dream/index.html",context )
        
    return render(request, 'dream/preference_list.html',{'all_data':all_data })

@login_required
def agenda_like(request, room_name):
    all_data = Agenda.objects.all().order_by('-create_date')

    if request.method == 'POST':        
            title = Agenda.objects.get(title=room_name)
            if Agenda_people.objects.filter(title=title).exists():
                error_message = 'すでに登録されています'
                return render(request, 'dream/agenda_list.html',
                              {'error_message': error_message,
                               'all_data': all_data
                               }
                              )
            else:
                username=request.user.username
                agenda_people = Agenda_people(title = title, username=username)
                agenda_people.save()
                preference = Preference_people.objects.filter(username=request.user.username)
                agenda = Agenda_people.objects.filter(username=request.user.username)
                recruitment = Recruitment_people.objects.filter(username=request.user.username)
                context = {
                            'preference': preference,
                            'agenda': agenda,
                            'recruitment': recruitment,
                            }
                return render (request, "dream/index.html",context )
        
    return render(request, 'dream/agenda_list.html',{'all_data':all_data })

@login_required
def recruitment_like(request, room_name):
    all_data = Recruitment.objects.all().order_by('-create_date')

    if request.method == 'POST':        
            title = Recruitment.objects.get(title=room_name)
            if Recruitment_people.objects.filter(title=title).exists():
                error_message = 'すでに登録されています'
                return render(request, 'dream/recruitment_list.html',
                              {'error_message': error_message,
                               'all_data': all_data
                               }
                              )
            else:
                username=request.user.username
                recruitment_people = Recruitment_people(title = title, username=username)
                recruitment_people.save()
                preference = Preference_people.objects.filter(username=request.user.username)
                agenda = Agenda_people.objects.filter(username=request.user.username)
                recruitment = Recruitment_people.objects.filter(username=request.user.username)
                context = {
                            'preference': preference,
                            'agenda': agenda,
                            'recruitment': recruitment,
                            }
                return render (request, "dream/index.html",context )
        
    return render(request, 'dream/recruitment_list.html',{'all_data':all_data })


def introduction_view(request):
    return render(request,'dream/introduction.html')
