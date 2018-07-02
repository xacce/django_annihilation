from django.core.management import BaseCommand
from annihilation.runner import AnnihilationRunner
import os
import oyaml as yaml
import logging

logging.basicConfig(level=logging.INFO)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('config_path', type=str)

    def handle(self, *args, **options):
        if not os.path.exists(options['config_path']):
            exit('Yaml file not found')

        runner = AnnihilationRunner(config=yaml.load(open(options['config_path']).read()))
        runner.run()
