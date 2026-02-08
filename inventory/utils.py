from .models import Alert

def create_chemical_alert(chemical):
    
    #Create alert if chemical quantity falls below threshold
    
    if chemical.quantity < chemical.min_threshold:
        Alert.objects.get_or_create(
            lab=chemical.lab,
            alert_type="CHEMICAL",
            message=f"Low stock alert: {chemical.name} in {chemical.lab.name}"
        )


def create_equipment_alert(equipment):
    
    #Create alert if equipment availability falls below threshold
 
    if equipment.available_quantity < equipment.min_threshold:
        Alert.objects.get_or_create(
            lab=equipment.lab,
            alert_type="EQUIPMENT",
            message=f"Low availability alert: {equipment.name} in {equipment.lab.name}"
        )
