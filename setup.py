from setuptools import setup, find_packages

setup(
    name='vault-pki-extractor',
    version='1.0.3',
    packages=find_packages(),
    author='Jeremy Derr',
    author_email='jeremy@derr.me',
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
