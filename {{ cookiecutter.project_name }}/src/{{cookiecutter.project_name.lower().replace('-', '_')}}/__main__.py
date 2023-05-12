from {{ cookiecutter.project_name.lower().replace('-', '_') }}.cli import cli

if __name__ == "__main__":
    cli(obj={})
