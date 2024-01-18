import click

from .mgs_core.realm import split_realm
import mgs.version as version



def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo(f'magasin CLI v{version.get_version()}')
    ctx.exit()


@click.group()
@click.option('-v', '--verbose', count=True)
@click.option('--version', is_flag=True, callback=print_version,
              expose_value=False, is_eager=True)
@click.pass_context
def cli(ctx, verbose):
    """magasin client is the glue between magasin components, it makes easier common tasks"""
    ctx.ensure_object(dict)

# TODO add this as dynamically
    
from mgs.mgs_dagster import dagster
cli.add_command(dagster)

from mgs.mgs_minio import minio
cli.add_command(minio)

from mgs.mgs_superset import superset
cli.add_command(superset)

from mgs.mgs_daskhub import daskhub
cli.add_command(daskhub)

if __name__ == "__main__":
    cli()