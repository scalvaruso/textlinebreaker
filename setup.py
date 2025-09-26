from setuptools import setup, find_packages

setup(
    # Other setup configurations

    # Use find_packages and exclude the folder
    packages=find_packages(
        exclude=['tests', 'VE_textlinebreaker']
    ),
)