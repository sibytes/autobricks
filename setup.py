import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "PYPI.md").read_text()

# This call to setup() does all the work
setup(
    name="autobricks",
    version="0.9.0",
    description="Databricks Deployment Utils",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://autobricks.readthedocs.io/en/latest/",
    project_urls={
        'GitHub': 'https://github.com/semanticinsight/autobricks',
        'Documentation': 'https://autobricks.readthedocs.io/en/latest/'
    },
    author="Shaun Ryan",
    author_email="shaun_chiburi@hotmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=[
        "autobricks",
        "autobricks.api_service"],
    install_requires=[
          'requests',
          'PyYAML',
          'adal'
      ],
    zip_safe=False
)
