# Download project

In this project, i'll just make a download page with django.

I used [this site](https://djangoadventures.com/how-to-create-file-download-links-in-django/) to understand about download pages in django

## Executing

To execute, you need to have Python and a virtual environviment (this one is not obligatory).

Then, install:

```
pip install django
```

Then, finaly, execute with:

### Unix/Mac OS

```
python3 manage.py runserver
```

### Windows

```
py manage.py runserver
```

## Changing the file

If you want to change the file that you'll download when you click the button, do inside the download function in download_page/views.py:

* Change the value of "filename" to the name of the file
* Change "content_type" of HttpResponse to the file type.
