from typer import Typer


app = Typer()


@app.command()
def main():
    pass


if __name__ == "__main__":
    app()
