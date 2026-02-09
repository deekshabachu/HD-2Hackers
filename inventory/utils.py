from .models import Chemical, Equipment, Alert


def create_chemical_alert(chemical):
    if chemical.quantity < chemical.min_threshold:
        Alert.objects.get_or_create(
            lab=chemical.lab,
            alert_type="CHEMICAL",
            message=f"Low stock: {chemical.name} in {chemical.lab.name}"
        )


def create_equipment_alert(equipment):
    if equipment.available_quantity < equipment.min_threshold:
        Alert.objects.get_or_create(
            lab=equipment.lab,
            alert_type="EQUIPMENT",
            message=f"Low availability: {equipment.name} in {equipment.lab.name}"
        )


def apply_scaling_for_lab(lab_settings):
    """
    Apply compounding scaling ONCE per cycle.
    """
    if lab_settings.scaling_applied:
        return

    lab = lab_settings.lab
    factor = lab_settings.scaling_factor

    for chem in Chemical.objects.filter(lab=lab):
        chem.min_threshold = int(chem.min_threshold * factor)
        chem.save()
        create_chemical_alert(chem)

    for eq in Equipment.objects.filter(lab=lab):
        eq.min_threshold = int(eq.min_threshold * factor)
        eq.save()
        create_equipment_alert(eq)

    lab_settings.scaling_applied = True
    lab_settings.save()
