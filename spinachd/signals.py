from django.db import reset_queries, close_old_connections
from spinach import signals

from .apps import spin


@signals.job_started.connect_via(spin.namespace)
def job_started(*args, **kwargs):
    reset_queries()
    close_old_connections()


@signals.job_finished.connect_via(spin.namespace)
def job_finished(*args, **kwargs):
    close_old_connections()
