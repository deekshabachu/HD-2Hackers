from django.contrib import admin
from .models import Lab, Chemical, Equipment, LabSettings, Alert
from .utils import create_chemical_alert, create_equipment_alert


# Register your models here.
admin.site.register(Lab)
admin.site.register(LabSettings)




@admin.register(Chemical)
class ChemicalAdmin(admin.ModelAdmin):
    list_display = ("name", "quantity", "min_threshold", "max_threshold","lab")

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        create_chemical_alert(obj)


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ("name", "available_quantity", "min_threshold", "max_threshold", "lab")

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        create_equipment_alert(obj)

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ("alert_type", "message", "lab", "created_at")