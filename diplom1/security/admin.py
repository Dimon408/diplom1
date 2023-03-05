from django.contrib import admin


from .models import Client_Time, Worker, Error, Prohod_place, Protect_points, Dostups

admin.site.register(Client_Time)
admin.site.register(Worker)
admin.site.register(Error)
admin.site.register(Prohod_place)
admin.site.register(Protect_points)
admin.site.register(Dostups)
# Register your models here.
