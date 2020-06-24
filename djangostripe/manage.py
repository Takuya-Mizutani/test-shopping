#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
sys.path.append('/private/var/mobile/Containers/Shared/AppGroup/F08856A9-B931-4DFF-9D47-CF440DA4BEF3/File\ Provider\ Storage/Repositories/test-shopping/djangostripe')
sys.path.append('/private/var/mobile/Containers/Shared/AppGroup/35669AB3-2277-40CF-A722-3FE7384592AE/File\ Provider\ Storage/Repositories/test-shopping/djangostripe')

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangostripe.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
