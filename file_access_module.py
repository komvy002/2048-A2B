import os
import click
from typing import Protocol, Dict


class FileAccessorProtocol(Protocol):
    def read(self, path: str) -> str:
        ...

    def write(self, path: str, content: str, mode: str = 'w') -> None:
        ...


class DefaultFileAccessor:
    def read(self, path: str) -> str:
        with open(path, 'r') as file:
            return file.read()

    def write(self, path: str, content: str, mode: str = 'w') -> None:
        with open(path, mode) as file:
            file.write(content)

class OutputPathValidator:
    VALID_FORMATS = ['.csv', '.txt']

    @staticmethod
    def validate(_ctx, _param, paths) -> Dict[str, str]:
        def getPathFormat(path):
            _base, extension = os.path.splitext(path)
            return extension.lower()

        output_spec = {}
        for path in paths:
            format = getPathFormat(path)
            if format not in OutputPathValidator.VALID_FORMATS:
                raise click.BadParameter(f"Output file {path} has an invalid format {format}. Known formats are {', '.join(OutputPathValidator.VALID_FORMATS)}.")
            output_spec[path] = format

        return output_spec