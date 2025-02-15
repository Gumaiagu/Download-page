from django.http import HttpResponse

def download(request):
    filename = 'download_page.zip'

    response = HttpResponse('test', content_type='zip')
    response['Content-Disposition'] = f"attachment; filename={filename}"
    return response