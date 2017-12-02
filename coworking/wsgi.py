"""
WSGI config for coworking project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
# from mezzanine.utils.conf import real_project_name

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "coworking.production")

# os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      # "%s.production" % real_project_name("coworking"))

application = get_wsgi_application()
