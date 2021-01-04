from rest_framework.pagination import LimitOffsetPagination

class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    limit_query_param = 'mylimit' # change the parma name
    offset_query_param = 'myoffset'
    max_limit = 6
    


