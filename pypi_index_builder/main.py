from loguru import logger
from typer import Typer

from pypi_index_builder.settings import Settings
from pypi_index_builder.load_index_yaml import load_index


app = Typer()


@logger.catch()
def main():
    settings = Settings()
    logger.info(settings)
    
    index_data = load_index(settings.index)
    logger.info(index_data)


if __name__ == "__main__":
    main()
