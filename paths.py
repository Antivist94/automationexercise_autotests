from pathlib import Path


def json_schema_file(file_name):
    return str(Path(__file__).parent.joinpath(f'schemas/{file_name}'))
