"""
WSGI config for think project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command
from django.db.utils import OperationalError

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'think.settings')

import django
django.setup()

# Automatically run migrations
try:
    call_command('migrate', interactive=False)
except OperationalError:
    pass
except Exception:
    pass

# Automatically collect static files (needed for free tier deployments without terminal)
try:
    call_command('collectstatic', interactive=False, verbosity=0, clear=False)
except Exception:
    pass

application = get_wsgi_application()

