from spiral.core.version import get_version

from setuptools import find_packages, setup


def get_readme():
    with open("README.md", encoding="utf-8") as f:
        return f.read()


setup(
    name="spiral",
    version=get_version(),
    description="Data Science Application Framework for Python",
    long_description=get_readme(),
    long_description_content_type="text/markdown",
    keywords="data science framework",
    author="Andrew Daniells",
    author_email="andrew.daniells@auticon.co.uk",
    url="https://github.com/acdaniells/spiral",
    license="BSD",
    classifiers=[
        "Development Status :: 1 - Planning ",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
    python_requires=">=3.6",
    install_requires=["cement", "pandas", "jinja2", "PyYAML"],
    packages=find_packages(exclude=["examples*", "scripts*", "tests*"]),
    package_data={
        "spiral": [
            "spiral/cli/templates/generate/*",
            "spiral/data/datasets/*",
            "spiral/data/logos/*",
            "spiral/data/plotly_themes/*",
        ]
    },
    include_package_data=True,
    entry_points={"console_scripts": ["spiral = spiral.cli.main:main"]},
    zip_safe=False,
)
