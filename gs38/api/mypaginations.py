from rest_framework.pagination import PageNumberPagination

class MyPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'p' # change the pagination query param present in the url
    page_size_query_param = 'records' # Client can decide how many fields he or she wants to see.
    max_page_size = 7 # give a constraint that an user can request upto only 7 records in each request. i.e., records < 7
    # last_page_strings = 'end'


