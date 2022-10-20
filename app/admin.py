from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Movies)
admin.site.register(StreamingPlatform)
admin.site.register(ActorsDetails)
admin.site.register(Generes)
admin.site.register(TechnicalSpecs)
admin.site.register(Directors)
admin.site.register(Reviews)
admin.site.register(Writers)






