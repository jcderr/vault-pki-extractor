import click
import json

from extractor import utils

@click.group()
@click.option('--debug/--no-debug', default=False)
@click.pass_context
def cli(ctx, debug):
    if debug:
        DEBUG = True

@cli.command()
@click.pass_context
@click.option('--input', type=click.File('rb'), required=False)
@click.option('--url', required=False)
@click.option('--token', default=None)
@click.option('--cn', default=None)
def report(ctx, input, url, token, cn):
    _input = ''
    if url and token and cn:
        import requests
        r = requests.post(
            url,
            headers={'X-Vault-Token': token},
            data=json.dumps({'common_name': cn}),
        )
        _input = r.text
        print _input
    else:
        while True:
            chunk = input.read(1024)
            if not chunk:
                break
            _input += chunk

    _json_data = json.loads(_input)

    pkidata = utils.VaultPKIObject(_json_data)
    print(pkidata)

@cli.command()
@click.pass_context
@click.option('--input', type=click.File('rb'), required=False)
@click.option('--url', required=False)
@click.option('--token', default=None)
@click.option('--cn', default=None)
def extract(ctx, input, token, cn):
    _input = ''
    if url and token and cn:
        import requests
        r = requests.post(
            url,
            headers={'X-Vault-Token': token},
            data=json.dumps({'common_name': cn}),
        )
        _input = r.text
    else:
        while True:
            chunk = input.read(1024)
            if not chunk:
                break
            _input += chunk

    pkidata = utils.VaultPKIObject(json.loads(_input))

    with open('ca.pem', 'w') as fh:
        fh.write(pkidata.data.issuing_ca)

    with open('cert.pem', 'w') as fh:
        fh.write(pkidata.data.certificate)

    with open('cert-key.pem', 'w') as fh:
        fh.write(pkidata.data.private_key)
