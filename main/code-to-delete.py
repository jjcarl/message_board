# @login_required
# def message_detail(request, id):
#     context = {}

#     if request.method == 'GET':
#         message = Message.objects.get(id=id)
#         context["message"] = message
#         comments = Comment.objects.filter(message=message).order_by('-date_posted')
#         context['comments'] = comments
#         user = request.user
#         if message.favorite == user.favorites:
#             context['favorite'] = True
#         return render(request, 'message-detail.html', context)

#     elif request.method == 'PUT':
#         message = Message.objects.get(id=id)
#         if message.pin == False:
#             message.pin = True
#             message.save()
#             return HttpResponse(status=204)

#         message.pin = False
#         message.save()
#         return HttpResponse(status=204)

#     elif request.method == 'DELETE':
#         if request.user.is_superuser:
#             Message.objects.get(id=id).delete()
#             return HttpResponse(status=204)

#         else:
#             return HttpResponse(status=401)

#     elif request.POST['type'] == 'comment':
#         message = Message.objects.get(id=id)
#         comments = Comment.objects.filter(message=message).order_by('-date_posted')
#         context = {'comments': comments}

#         form = CommentForm(request.POST)

#         if request.method == 'POST':
#             if form.is_valid:
#                 comment = form.save()
#                 context['comment'] = 'Youre comment has been saved'
#                 context['message'] = message
#             else:
#                 context['comment'] = form.errors

#         return render(request, 'message-detail.html', context)

#     elif request.POST['type'] == 'favorite':
#             if request.method == 'POST':
#                 message = Message.objects.get(id=id)
#                 user = request.user
#                 user.favorites.add(message)
#                 return HttpResponse(status=204)

#     elif request.POST['type'] == 'unfavorite':
#             if request.method == 'POST':
#                 message = Message.objects.get(id=id)
#                 user = request.user
#                 user.favorites.remove(message)
#                 return HttpResponse(status=204)


# =========== Main Message Board Page ========