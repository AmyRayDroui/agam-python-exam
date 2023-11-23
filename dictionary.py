import click
import json
from pathlib import Path

DATA_FILE = "data.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data


def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=2)


@click.command()
@click.argument('command')
@click.option("--key", help="Key of the dictionary.")
@click.option("--value", help="Value corresponding to the key.")
def dictionary(command, key, value):
    data = load_data()
    match command:
        case "set":
            error_message = check_input_validity({'key': key,'value':value})
            if error_message:
                return click.echo(error_message)
            return set(data, key, value)
        case "get":
            error_message = check_input_validity({'key':key})
            if error_message:
                return click.echo(error_message)
            return get(data, key)
        case "remove":
            error_message = check_input_validity({'key':key})
            if error_message:
                return click.echo(error_message)
            return remove(data, key)
        case "keys":
            return keys(data)
        case "get-all":
            return get_all(data)
        case _:
            return click.echo(f"Command: {command} not found")


def check_input_validity(inputs):
    for input in inputs.keys():
        if not inputs[input]:
            return f"Error: Input --{input} not found"


def set(data, key, value):
    data[key] = value
    save_data(data)
    click.echo(f">> Added {key}: {value}")

def get(data,key):
    value = data.get(key)
    if value is not None:
        click.echo(f">> {key}: {value}")
    else:
        click.echo(f"Key: {key} not found")

def remove(data, key):
    if key in data:
        del data[key]
        save_data(data)
        click.echo(f">> Removed key: {key}")
    else:
        click.echo(f"Key: {key} not found")

def keys(data):
    click.echo("Keys in the dictionary:")
    for key in data:
        click.echo(f">> {key}")


def get_all(data):
    data = load_data()
    click.echo("All data in the dictionary:")
    for key, value in data.items():
        click.echo(f">> {key}: {value}")


if __name__ == "__main__":
    Path(DATA_FILE).touch()
    dictionary()