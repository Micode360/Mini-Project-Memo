from django.shortcuts import render, redirect, get_object_or_404
from .forms import MemoForm
from .models import Memo
# import logging

# logger = logging.getLogger(__name__)

# Create your views here.
def home(request):
    if request.method == 'POST':
        print(request.POST, request.FILES)
        form = MemoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/message')
        # else:
        #     print(form.errors)
    else:
        form = MemoForm()

    memos = Memo.objects.all()
    return render(request, 'index.html', {'memo_data': memos})

def details_func(request, pk):
    filter_memo = get_object_or_404(Memo, pk=pk)
    return render(request, 'details.html', {'memo_data': filter_memo})

def message_func(request):
    return render(request, 'message.html')