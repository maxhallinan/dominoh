#! /usr/bin/env python
import click

@click.command()
@click.argument(
        'input_path',
        required=True)
def main(input_path):
    with open(input_path, 'r', encoding='utf-8-sig') as input_file:
        click.echo(input_file.read())
