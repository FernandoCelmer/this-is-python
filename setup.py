import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="this-is",
    version="0.0.1",
    author="Fernando Celmer",
    author_email="email@fernandocelmer.com",
    description="This is Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FernandoCelmer/this-is-python",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "this"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)