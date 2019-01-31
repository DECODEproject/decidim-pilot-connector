from setuptools import setup, find_packages

setup(
    name="decidim-pilot-connector",
    version="0.0.1",
    author="Puria Nafisi Azizi",
    author_email="puria@dyne.org",
    packages=find_packages(),
    install_requires=[
        "fastapi", "pytest_runner",
    ],
    tests_require=[
        "pytest",
        "requests",
        "pytest-cov",
    ],
)
