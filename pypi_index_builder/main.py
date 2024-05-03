from loguru import logger
from typer import Typer

from pypi_index_builder.settings import Settings

app = Typer()


@logger.catch()
def main():
    settings = Settings()
    print(settings)


if __name__ == "__main__":
    main()
