from django.contrib import admin

from .models import About
from .models import Slider
from .models import Client
from .models import Contact

admin.site.register(About)
admin.site.register(Slider)
admin.site.register(Client)
admin.site.register(Contact)
