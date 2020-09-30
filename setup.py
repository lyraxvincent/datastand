import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name='DataStand',
    packages=['DataStand'],
    version='1.2',
    license='MIT  ',
    author="Vincent Njonge",
    author_email="njongevincent@gmail.com",
    description="A python package that helps Data Scientists, Machine Learning Engineers and Analysts to quickly explore and understand a dataset.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lyraxvincent/DataStand",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
 )
