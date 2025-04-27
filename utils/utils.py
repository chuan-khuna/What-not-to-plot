import yaml


def load_yaml(file_name):
    with open(file_name) as f:
        return yaml.load(f, yaml.Loader)