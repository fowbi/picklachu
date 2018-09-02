import setuptools

with open("README.md", "r") as handle:
    long_description = handle.read()

setuptools.setup(
    name="picklachu",
    version="0.0.1",
    author="tobinho",
    author_email="tobi@magier.be",
    description="Pickle data an store it",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fowbi/picklachu",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
