from setuptools import setup

setup(
    name="decidim-pilot-connector",
    setup_requires=[
        "fastapi",
    ],
    tests_require=[
        "pytest",
        "requests",
        "pytest-cov",
    ],
)
