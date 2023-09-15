from setuptools import setup, find_packages

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()


setup(
    name= "CricBuzzScr",
    # version= "0.0",
    author= "Sai Siddhanth S",
    author_email= "saisiddhanthreddy@gmail.com",
    description= "You can get the live scores from cricbuzz.com. You can also view commentary and scorecard.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    packages= find_packages(),
    install_requires= [
        'beautifulsoup4'
    ],
    python_requires = ">=3.7",
    include_package_data= True,
)