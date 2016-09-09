# Vault PKI Extractor

The Vault API returns PKI bundles wrapped in JSON. For simplicity,
this wrapper will take those payloads and output them in the following files:

* ca.pem
* cert.pem
* cert-key.pem

# Usage

## extract

    vault-pki-extractor extract --input filename

If you already have the JSON payload saved to file (curl -o ...), you can pass
the file in with `--input`.

    vault-pki-extractor extract --url some_url --token some_token --cn some_common_name

Alternatively, VPE will use `requests` to call your vault server and do the needful.

## report

If you just want to see the output, you can run `report` instead and get a prettified
output of the information in your certificates. This isn't very useful except in debugging.
