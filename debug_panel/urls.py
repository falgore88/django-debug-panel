"""
URLpatterns for the debug panel.

These should not be loaded explicitly; It is used internally by the
debug-panel application.
"""
from .views import debug_data

try:
    from django.conf.urls import url
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import url

from django.conf.urls.i18n import i18n_patterns

_PREFIX = '__debug__'

urlpatterns = i18n_patterns(
    url(r'^%s/data/(?P<cache_key>\d+\.\d+)/$' % _PREFIX, debug_data, name='debug_data'),
)
