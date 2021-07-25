import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="runeserver-STEVENACI",
    version="0.0.1",
    author="Steve C",
    author_email="stevenalexcarino@gmail.com",
    description="A cross-platform file server using basic Flask, accessible in the browser.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Tracking": "https://github.com/stevenaci/runeserver/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "runeserver"},
    packages=setuptools.find_packages(where="runeserver"),
    python_requires=">=3.6",
)