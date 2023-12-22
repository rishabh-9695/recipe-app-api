"""

Djmango cammand to wait for DB to be available
"""

import time

from psycopg2 import OperationalError as Psycopg2Error

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django Command to wait for DB"""

    def handle(self, *args, **options):
        """Entrypoint for command"""
        self.stdout.write('waiting for DB')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write('DB not available, wait for 1 second')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('DB available'))
