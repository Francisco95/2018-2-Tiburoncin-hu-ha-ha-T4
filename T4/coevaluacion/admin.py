from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Course)
admin.site.register(UserInCourse)
admin.site.register(Group)
admin.site.register(Question)
admin.site.register(CoEvaluation)


