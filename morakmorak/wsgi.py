"""
WSGI config for morakmorak project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os,sys

sys.path.append('/root/morak')
sys.path.append('/root/morak/MorakMorak/morakmorak')
sys.path.append('/root/morak/MorakMorak')
sys.path.append('/root/morak/venv/lib/python3.5/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "morakmorak.settings")

application = get_wsgi_application()
