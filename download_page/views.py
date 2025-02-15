from django.http import HttpResponse

def download(request):
    filename = 'file.txt'

    response = HttpResponse('test', content_type='txt')
    response['Content-Disposition'] = f"attachment; filename={filename}"
    return response