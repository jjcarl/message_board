from django.shortcuts import render, redirect, render_to_response
from main.models import Message, Comment, Tag
from main.forms import MessageForm, CommentForm, TagForm
from django.contrib.auth import views, authenticate, login
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.core import serializers
from django.template import RequestContext


def new(request):
    return redirect('mbhome')


def home(request):
    context = {}
    return render(request, 'home.html', context)


# ========== Message Board ===========


def mbhome(request):
    recent = Message.objects.all().order_by('-date_posted')[0:5]
    pinned = Message.objects.filter(pin=True).order_by('-date_posted')
    context = {'recent': recent, 'pinned': pinned}

    return render(request, 'mbhome.html', context)


def message_board(request):
    messages = Message.objects.filter(pin=True).order_by('-date_posted')

    context = {'messages': messages}

    return render(request, 'message-board.html', context)


def short_messages(request):

    page = int(request.GET.get('page', 0))
    page_size = 6

    start = page * page_size
    end = (page + 1) * page_size

    messages = Message.objects.all().order_by('-date_posted')[start:end]
    context = {'messages': messages}
    if len(messages) > 0:
        return render(request, 'short-messages.html', context)
    else:
        return HttpResponse('')


@login_required
def create_message(request):
    messages = Message.objects.all()
    tags = Tag.objects.all()
    context = {'messages': messages, 'tags': tags, 'tagform': TagForm}
    form = MessageForm(request.POST, request.FILES, prefix="message")
    tags = TagForm(request.POST)
    if request.method == "POST":
        cleaned_tags = []
        if tags.is_valid():
            tag_list = []

            tag = tags.save(commit=False)

            words = tags.cleaned_data['word']
            tag_list = words.split(',')
            for word in tag_list:
                tag, created = Tag.objects.get_or_create(word=word)
                cleaned_tags.append(tag)

            context['tag'] = "Your tags have been saved"

        if form.is_valid():

            message = form.save()
            for tag in cleaned_tags:
                message.tag.add(tag)
            context['message'] = "Your message has been saved"
            return redirect('mbhome')
        else:
            context['message'] = form.errors

    return render(request, 'create-message.html', context)


# =========== Message Detail =============


class MessageDetail(View):

    def get(self, request, id):
        context = {}
        message = Message.objects.get(id=id)
        context["message"] = message
        comments = Comment.objects.filter(
            message=message).order_by('-date_posted')
        context['comments'] = comments
        return render(request, 'message-detail.html', context)

    @method_decorator(login_required)
    def put(self, request, id):
        message = Message.objects.get(id=id)
        if message.pin is False:
            message.pin = True
            message.save()
            return HttpResponse(status=204)

        message.pin = False
        message.save()
        return HttpResponse(status=204)

    @method_decorator(login_required)
    def delete(self, request, id):
        Message.objects.get(id=id).delete()
        return HttpResponse(status=204)

    @method_decorator(login_required)
    def post(self, request, id):
        context = {}
        message = Message.objects.get(id=id)
        user = request.user

        if request.POST['type'] == 'comment':
            comments = Comment.objects.filter(
                message=message).order_by('-date_posted')
            context = {'comments': comments}
            form = CommentForm(request.POST)

            if form.is_valid:
                comment = form.save()
                context['comment'] = 'Youre comment has been saved'
                context['message'] = message
            else:
                context['comment'] = form.errors

            return render(request, 'message-detail.html', context)

        elif request.POST['type'] == 'edit':
            id = request.POST.get('id')

            if id:
                form = MessageForm(
                    request.POST, request.FILES, instance=message)

            if form.is_valid:
                message = form.save()
                context['text'] = "Your message has been saved"
                context['message'] = message
            else:
                context['text'] = form.errors

            return render(request, 'message-detail.html', context)

        elif request.POST['type'] == 'favorite':
            user.favorites.add(message)
            return HttpResponse(status=204)

        elif request.POST['type'] == 'unfavorite':
                user.favorites.remove(message)
                return HttpResponse(status=204)


@login_required
def message_admin(request):
    if request.method == 'GET':
        messages = Message.objects.all().order_by('-date_posted')
        context = {'messages': messages}

        return render(request, 'message-admin.html', context)


@login_required
def message_json(request, id):
    message = Message.objects.get(id=id)
    message_json = serializers.serialize('json', [message])

    return HttpResponse(message_json, content_type='application/json')


# ============ SEARCH ===============

def message_search(request):
    request_context = RequestContext(request)
    context = {}
    messages = Message.objects.all()

    if request.method == 'POST':
        form = request.POST
        context['form'] = form

        word = form['word']

        context['message_titles'] = messages.filter(title__icontains=word)
        context['message_texts'] = messages.filter(text__icontains=word)

        context['valid'] = "Form is Valid"

        return render_to_response(
            "message_search.html", context, context_instance=request_context)

    else:
        form = request.POST
        context['form'] = form

        return render_to_response(
            "message_search.html", context, context_instance=request_context)


# ============= AUTHENTICATION ==================


def create_account(request):
    new_user_form = UserCreationForm(request.POST)

    context = {"completed_form": UserCreationForm()}

    if new_user_form.is_valid():
        user = new_user_form.save()
        user.email = request.POST['email']
        user.save()

        group = Group.objects.get(name='Users')
        group.user_set.add(user)

        user = authenticate(username=user.username,
                            password=request.POST['password1'])

        login(request, user)

        return redirect('message_board')
    else:
        context['completed_form'] = new_user_form
        context['error_on_create'] = True

    return render(request, 'create-account.html', context)
