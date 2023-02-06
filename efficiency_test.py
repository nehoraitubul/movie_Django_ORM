import os
import django

os.environ["DJANGO_SETTINGS_MODULE"] = "movies.settings"

django.setup()

from movies_app.models import *


for m in Movie.objects.all().prefetch_related('actors'):
    print(m.actors.all())