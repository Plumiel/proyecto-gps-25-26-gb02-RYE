import collections

# Fix for Python 3.9+ where collections.Callable was moved to collections.abc
if not hasattr(collections, 'Callable'):
    import collections.abc
    collections.Callable = collections.abc.Callable