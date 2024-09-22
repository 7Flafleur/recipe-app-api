"""
Django command to wait for database to be available
"""
import time

from psycopg2 import OperationalError as Psycopg2Error

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **options):
        """Entrypoint for command."""
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                """ check raises exceptions mentioned below unless db is ready,code enters except part,
                following line is only executed if exceptions were not raised """
                db_up = True 
            except(Psycopg2Error,OperationalError):
                self.stdout.write('Database unavailable, waiting  second...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))


