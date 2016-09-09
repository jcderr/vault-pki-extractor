FROM python:2.7-onbuild

RUN python setup.py install

CMD vault-pki-extractor

