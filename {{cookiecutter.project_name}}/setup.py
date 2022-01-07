import setuptools
import os

with open("README.md", "r", encoding='UTF8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="{{ cookiecutter.project_name }}",
    version=os.getenv("GITHUB_REF_NAME", "v0.0.1"),
    author="Avikus",
    author_email="dev@avikus.ai",
    description="A nas library package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/avikus-ai/{{ cookiecutter.project_name }}",
    packages=setuptools.find_packages(exclude=["*tests*","*examples*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    setup_requires=['wheel'],
    install_requires=[],
    python_requires='>=3.6',
)
