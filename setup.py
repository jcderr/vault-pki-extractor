from setuptools import setup, find_packages

setup(
    name='vault-pki-extractor',
    version='1.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click==6.6',
        'requests==2.11.1',
    ],
    entry_points='''
        [console_scripts]
        vault-pki-extractor=extractor.cli:cli
    ''',
)
