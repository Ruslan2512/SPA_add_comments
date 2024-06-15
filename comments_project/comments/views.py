from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import CommentForm
from .models import Comment


def comment_list(request):
    sort_by = request.GET.get('sort_by', 'created_at')
    order = request.GET.get('order', 'desc')

    if order == 'asc':
        sort_by = sort_by
    else:
        sort_by = f'-{sort_by}'

    comments = Comment.objects.filter(parent__isnull=True).order_by(sort_by)
    paginator = Paginator(comments, 25)  # 25 комментариев на страницу

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    form = CommentForm() if 'show_form' in request.GET else None
    return render(request, 'comments/comment_list.html', {'page_obj': page_obj, 'form': form})


def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comment_list')
    return redirect('comment_list')
