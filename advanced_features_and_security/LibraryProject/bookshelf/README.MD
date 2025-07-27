# Permissions and Groups Setup

We defined custom permissions for the `Book` model:

- can_view
- can_create
- can_edit
- can_delete

## Groups
- **Viewers** → can_view
- **Editors** → can_view, can_create, can_edit
- **Admins** → All permissions

## How to Test
1. Create users in Django admin.
2. Assign them to the appropriate group.
3. Try accessing views like `/view_books/`, `/create_book/`, etc.
4. You should get `403 Forbidden` if a user lacks permission.
