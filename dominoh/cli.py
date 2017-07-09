#! /usr/bin/env python
import click

@click.command()
@click.argument(
        'input_path',
        required=True)
def main(input_path):
    click.echo("Hello World!")

