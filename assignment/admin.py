from django.contrib import admin
from .models import About,SocialLink

# Register your models here.

class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count = About.objects.all().count()
        if count == 1 :
            return False
        else:
            return True
    

admin.site.register(SocialLink)
admin.site.register(About,AboutAdmin)