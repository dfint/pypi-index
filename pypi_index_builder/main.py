from jinja2 import Environment, FileSystemLoader
from loguru import logger
from pydantic import ValidationError
from typer import Typer

from pypi_index_builder.settings import Settings
from pypi_index_builder.load_index_yaml import load_index


app = Typer()


@logger.catch()
def main():
    try:
        settings = Settings()
    except ValidationError as ex:
        logger.error(str(ex))
        return
    
    index_data = load_index(settings.index)
    
    env = Environment(loader=FileSystemLoader(settings.templates))
    template = env.get_template('index.html')
    
    with open(settings.output / "index.html", "wt") as index_file:
        index_file.write(template.render(index=index_data.keys()))


if __name__ == "__main__":
    main()
