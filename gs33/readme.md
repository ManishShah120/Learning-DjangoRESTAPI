# Filtering & Django filter in DRF

The simplest way to filter the queryset of any view that subclasses **GenericAPIView** is to override the `.get_queryset()` method.
