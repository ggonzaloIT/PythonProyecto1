from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm

@login_required
def inbox_view(request):
    messages = Message.objects.filter(recipient=request.user)
    return render(request, 'messaging/inbox.html', {'messages': messages})

@login_required
def sent_view(request):
    messages = Message.objects.filter(sender=request.user)
    return render(request, 'messaging/sent.html', {'messages': messages})

@login_required
def send_message_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('messaging:inbox')
    else:
        form = MessageForm()
    return render(request, 'messaging/send_message.html', {'form': form})