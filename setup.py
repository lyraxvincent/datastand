import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name='DataStand',
    packages=['DataStand'],
    version='1.4',
    license='MIT  ',
    author="Vincent Njonge",
    author_email="njongevincent@gmail.com",
    description="""A python package to help users especially Data Scientists, Machine Learning Engineers and 
    Analysts to better understand a dataset. Gives quick insights about given data; general dataset statistics, 
    size and shape of dataset, number of unique data types, number of numerical and non-numerical columns, small 
    overview of dataset, data description, missing data statistics, missing data heatmap and provides methodology 
    to impute missing data.""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lyraxvincent/DataStand",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
 )
