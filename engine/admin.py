from django.contrib import admin

from .models import Cost, IncomeSource, Category, Account

admin.site.register(Cost)
admin.site.register(IncomeSource)
admin.site.register(Category)
admin.site.register(Account)
