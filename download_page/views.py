from django.shortcuts import render
import mimetypes

def download(request):
    fl_path = '/home/gustavo/Programacao/Lenguages/learning/learning_django_projects/download_page/download_page/static/file'
    filename = 'file.txt'

    mime_type, _ = mimetypes.guess_type(fl_path)
    response = render(request, 'home/index.html', content_type=mime_type)
    response['Content-Disposition'] = f"attachment; filename={filename}"
    return response