# Custom Permissions

## To implement a custom permission, override BasePermisison and implement either, or both, of the following ethod:
- has_permission(self, request, view)
- has_object_permission(self, request, view, obj)