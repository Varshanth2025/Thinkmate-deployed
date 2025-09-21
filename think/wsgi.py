"""
WSGI config for think project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'think.settings')

import django
from django.core.management import call_command
from django.db.utils import OperationalError

django.setup()

try:
    call_command('migrate', interactive=False)
except OperationalError:
    pass

application = get_wsgi_application()
