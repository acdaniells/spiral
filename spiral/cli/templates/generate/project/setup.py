from setuptools import find_packages, setup

from {{label}}.core.version import get_version


def get_readme():
    with open("README.md", encoding="utf-8") as f:
        return f.read()


setup(
    name="{{ label }}",
    version=get_version(),
    description="{{ description }}",
    long_description=get_readme(),
    long_description_content_type="text/markdown",
    author="{{ creator }}",
    author_email="{{ creator_email }}",
    url="{{ url }}",
    license="{{ license }}",
    python_requires=">=3.6",
    install_requires=["spiral"],
    packages=find_packages(exclude=["tests*"]),
    package_data={"{{ label }}": ["templates/*"]},
    include_package_data=True,
    entry_points={"console_scripts": ["{{ label }} = {{ label }}.main:main"]},
)
