from pathlib import Path
from pydantic import BaseModel, RootModel
import strictyaml


class IndexEntry(BaseModel):
    name: str | None = None
    url: str
    
    def model_post_init(self, __context):
        if not self.name:
            # Get file name from url
            self.name = self.url.rpartition("/")[2]


class IndexInfo(RootModel):
    root: dict[str, list[IndexEntry]]


def load_index(path: Path):
    with open(path) as config_file:
        yaml = strictyaml.load(config_file.read())
        return IndexInfo.model_validate(yaml.data)
