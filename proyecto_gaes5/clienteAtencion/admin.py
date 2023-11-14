from django.contrib import admin
from .models import occupation
from .models import worker
from .models import typeOfService
from .models import cite
from .models import comment
from .models import contacts

admin.site.register(occupation)
admin.site.register(worker)
admin.site.register(typeOfService)
admin.site.register(cite)
admin.site.register(comment)
admin.site.register(contacts)
