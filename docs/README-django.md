Backend of this project is develop with Django.

## Set up environment

Navigate with terminal at `server` folder and type these commads to create virtualenv:

> $ pip install virtualenv\
> $ virtualenv dogger\

After activate the virtualenv:

- `Linux/Mac`
> $ source dogger/bin/activate\

- `Windows`
> $ dogger/Scripts/activate\

And install every project requeriment

> $ pip install -r requeriments.txt

When everything is installed, set every migration:
> $ python manage.py migrate

Then turn on django server with:

> $ python manage.py runserver

And now, django server is up and ready to be used within `localhost:8000`.
