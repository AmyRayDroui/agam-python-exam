import click
import json

@click.command()
@click.argument('command')
@click.option('--key', help='dict key')
@click.option('--value', 
              help='dict value')


def main(command, key, value):
    with open('data.json') as json_file:
        dict = json.load(json_file)
        if command == 'set':
            dict[key] = value
        elif command == 'get':
            print(dict[key])
        elif command == 'remove':
            del dict[key]
        elif command == 'key':
            print(dict.keys())
        elif command == 'get-all':
            print(dict)
        json.dump(dict,json_file)
        
    
if __name__ == '__main__':
    main()