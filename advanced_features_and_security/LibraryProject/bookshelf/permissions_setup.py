# bookshelf/permissions_setup.py

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book

content_type = ContentType.objects.get_for_model(Book)

# Create groups
editors_group, _ = Group.objects.get_or_create(name="Editors")
viewers_group, _ = Group.objects.get_or_create(name="Viewers")
admins_group, _ = Group.objects.get_or_create(name="Admins")

# Get permissions
can_view = Permission.objects.get(codename='can_view')
can_create = Permission.objects.get(codename='can_create')
can_edit = Permission.objects.get(codename='can_edit')
can_delete = Permission.objects.get(codename='can_delete')

# Assign permissions
editors_group.permissions.set([can_view, can_create, can_edit])
viewers_group.permissions.set([can_view])
admins_group.permissions.set([can_view, can_create, can_edit, can_delete])
