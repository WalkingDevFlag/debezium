import os
from functools import lru_cache
from pathlib import Path

import tomli
from pydantic_settings import BaseSettings


class ServerSettings(BaseSettings):
    @property
    def project_name_api(self):
        return self._get_project().get('name')

    @property
    def project_version_api(self):
        return self._get_project().get('version')

    @property
    def project_description_api(self):
        return self._get_project().get('description')

    @property
    def project_contact_api(self):
        return self._get_pyproject('contact')

    def _get_project(self):
        return self._get_pyproject('project')

    def _get_pyproject(self, key: str):
        with open(f'{Path(__file__).resolve().parent.parent}{os.sep}pyproject.toml', 'rb') as reader:
            pyproject = tomli.load(reader)
        return pyproject.get(key, {})


class KafkaSettings(BaseSettings):
    kafka_host: str = 'kafka-debezium:9092'
    group_id: str = 'marvel'
    topic: str = 'postgres.public.super_heroes'


class EnvSettings(BaseSettings):
    kafka: KafkaSettings = KafkaSettings()
    server: ServerSettings = ServerSettings()


@lru_cache
def get_settings() -> EnvSettings:
    return EnvSettings()
