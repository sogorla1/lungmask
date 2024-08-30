import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lungmask",
    version="0.2.20.1",
    author="Johannes Hofmanninger",
    author_email="j.hofmanninger@gmail.com",
    description="Modified version of Lungmask 0.2.20, please check URL for details.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sogorla1/lungmask",
    packages=setuptools.find_packages(),
    entry_points={"console_scripts": ["lungmask = lungmask.__main__:main"]},
    install_requires=[
        "pydicom",
        "numpy<2",
        "torch",
        "scipy",
        "SimpleITK",
        "tqdm",
        "scikit-image",
        "fill_voids",
        "more-itertools",
        "pylibjpeg",
        "pylibjpeg-libjpeg",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
