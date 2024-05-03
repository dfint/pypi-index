from jinja2 import Environment, FileSystemLoader
from loguru import logger
from pydantic import ValidationError

from pypi_index_builder.load_index import load_index
from pypi_index_builder.settings import Settings


@logger.catch()
def main():
    try:
        settings = Settings()
    except ValidationError as ex:
        logger.error(str(ex))
        return

    index_data = load_index(settings.index)

    env = Environment(loader=FileSystemLoader(settings.templates))
    template = env.get_template("index.html")

    settings.output.mkdir(parents=True, exist_ok=True)

    with open(settings.output / "index.html", "w") as index_file:
        index_file.write(template.render(index=index_data.keys()))

    template = env.get_template("package.html")
    for name, entries in index_data.items():
        with open(settings.output / f"{name}.html", "w") as package_file:
            package_file.write(template.render(data=entries))


if __name__ == "__main__":
    main()
