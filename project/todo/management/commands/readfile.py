from django.core.management.base import BaseCommand, CommandError
from os.path import exists

class Command(BaseCommand):
    help = "Read the contain of a list of files and insert the reads into our DB."

    def add_arguments(self, parser):
        parser.add_argument("files", nargs="+", type=str)

    def handle(self, *args, **options):
        for file in options["files"]:
            try:
                file_exists = exists(file)
                if file_exists:
                    pass

            except Exception as e:
                raise CommandError('Failure reading "%s"' % file)

            self.stdout.write(
                self.style.SUCCESS('Successfully read "%s"' % file)
            )