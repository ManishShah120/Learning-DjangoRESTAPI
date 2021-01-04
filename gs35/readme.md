# Search Filter

The SearchFilter class supports simple single query parameter based searching, and is based on the Django admin's search functionality.

## SearchFilter
- '^' Starts-with search.
- '=' Exact matches.
- '@' Full-text search. (Currently only supported Django's PostgreSQL backend)
- '$' Regex search

### Example
searrch_fields = ['^name',]