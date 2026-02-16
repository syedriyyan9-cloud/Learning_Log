from django.shortcuts import render, redirect

from .models import Topics, Entry

from .forms import TopicForm, EntryForm

from django.contrib.auth.decorators import login_required

from django.http import Http404

# Create your views here.
def index(request):
    """renders Home page"""
    return render(request,'learning_logs/index.html')

@login_required
def topics(request):
    """Displays topics to topic.html template"""
    topics = Topics.objects.filter(owner = request.user).order_by('date')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """show a single topic and all its entries"""
    topic = Topics.objects.get(id=topic_id)
    check_topic_user(request, topic)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries':entries}
    return render(request, 'learning_logs/topic.html', context)

# TIY 19.3
def check_topic_user(request,topic):
    """Check if the current user is the owner"""
    if topic.owner != request.user:
        raise Http404

@login_required
def new_topic(request):
    """adds new topics"""
    if request.method != 'POST': # no data submitted, create new form
        form = TopicForm()
    else:   # data submitted, process data
        form = TopicForm(data = request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')
    # display a blank or invalid form
    context = {'form':form}
    return render(request, 'learning_logs/new_topic.html',context)

@login_required
def new_entry(request, topic_id):
    """add new entires"""
    topic = Topics.objects.get(id = topic_id)
    # TIY 19.4
    check_topic_user(request, topic)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data = request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id = topic_id)
    context = {'topic':topic,'form':form}
    return render(request,'learning_logs/new_entry.html',context)

@login_required
def edit_entry(request, entry_id):
    """Edit existing entires"""
    entry = Entry.objects.get(id = entry_id)
    topic = entry.topic
    check_topic_user(request, topic)
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic',topic_id=topic.id)
    context = {'entry':entry, 'topic':topic, 'form':form}
    return render(request, 'learning_logs/edit_entry.html',context)