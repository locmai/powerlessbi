from setuptools import setup

setup(
    name='powerlessbi',
    version='0.0.1',
    author="Loc Mai",
    author_email="locmai0201@gmail.com",
    description="Powerless BI",
    packages=['src'],
    install_requires=[
        'Click',
        'PyYAML',
        'simple_chalk',
        'typing-extensions',
    ],
    entry_points='''
        [console_scripts]
        pbi=src.main:main
    '''
)