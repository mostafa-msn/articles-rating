from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):

    def get_list_display(self, request):
        return self.list_display + ['modified_time', 'created_time']
