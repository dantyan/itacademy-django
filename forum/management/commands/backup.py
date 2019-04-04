import os
from datetime import datetime

from django.conf import settings
from django.core.management.base import BaseCommand

from forum.models import Thread


class Command(BaseCommand):
    help = 'Backup forum app'

    def handle(self, *args, **options):

        threads = Thread.objects.all()

        now = datetime.now()

        with open(os.path.join(settings.BASE_DIR, 'backups', 'backup-{}.csv'.format(now)), 'w') as fh:
            for thread in threads:
                fh.write(','.join([
                    str(thread.pk),
                    thread.title,
                    thread.description,
                    str(thread.private),
                    str(thread.add_time),
                    str(thread.post_cnt),
                    str(thread.comment_cnt)
                ]))
                fh.write('\n')

        self.stdout.write(self.style.SUCCESS('forum backup handle'))
