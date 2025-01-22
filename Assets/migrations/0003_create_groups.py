from django.db import migrations


def create_groups(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Permission = apps.get_model("auth", "Permission")
    roles = ["Administrator", "Asset Manager", "Technician", "User","Reporters","Auditor"]

    for role in roles:
        group, created = Group.objects.get_or_create(name=role)
        if role == "Asset Manager":
            permissions = Permission.objects.filter(codename__in=[
                "add_asset", "change_asset", "delete_asset", "view_asset"
            ])
            group.permissions.set(permissions)


class Migration(migrations.Migration):
    dependencies = [
        ('Assets', '0002_alter_asset_serialnumber'),  
        ('auth', '0012_alter_user_first_name_max_length'), 
    ]

    operations = [
        migrations.RunPython(create_groups),
    ]
