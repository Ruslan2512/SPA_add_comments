from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from .forms import CommentForm
from .models import Comment
from lxml.html.clean import Cleaner

ALLOWED_HTML_TAGS = ['a', 'code', 'i', 'strong']

@csrf_exempt
def preview_comment(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        cleaner = Cleaner(
            safe_attrs_only=True,
            safe_attrs=frozenset(['href', 'title']),
            allow_tags=frozenset(ALLOWED_HTML_TAGS),
        )
        cleaned_text = cleaner.clean_html(text)
        return JsonResponse({'preview': cleaned_text})

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
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            if 'image' in request.FILES:
                image = Image.open(request.FILES['image'])
                if image.size[0] > 320 or image.size[1] > 240:
                    output_size = (320, 240)
                    image.thumbnail(output_size, Image.LANCZOS)
                    output = BytesIO()
                    image.save(output, format=image.format)
                    output.seek(0)
                    comment.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % request.FILES['image'].name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
            if 'text_file' in request.FILES:
                text_file = request.FILES['text_file']
                if text_file.size > 100 * 1024:
                    form.add_error('text_file', 'Text file size must be under 100KB.')
                    comments = Comment.objects.filter(parent__isnull=True).order_by('-created_at')
                    paginator = Paginator(comments, 25)
                    page_number = request.GET.get('page')
                    page_obj = paginator.get_page(page_number)
                    return render(request, 'comments/comment_list.html', {'page_obj': page_obj, 'form': form})
                comment.text_file = text_file
            comment.save()
            return redirect('comment_list')
        else:
            # Возвращаем форму с ошибками на страницу
            comments = Comment.objects.filter(parent__isnull=True).order_by('-created_at')
            paginator = Paginator(comments, 25)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request, 'comments/comment_list.html', {'page_obj': page_obj, 'form': form})

    return redirect('comment_list')
