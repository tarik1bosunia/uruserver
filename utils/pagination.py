from rest_framework.pagination import PageNumberPagination


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 5
    # page_query_param = 'pg'
    page_size_query_param = 'page_size'
    max_page_size = 30
    # last_page_strings = 'l'

