import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='blackjack',
    version='0.0.0',
    author='Trevor Maseleme',
    author_email='tkmaseleme@gmail.com',
    description='Package to allow you to simulate the game of black jack in your code',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/tkmaseleme/blackjack',
    project_urls = {
        "Bug Tracker": "https://github.com/tkmaseleme/blackjack/issues"
    },
    license='MIT',
    packages=['blackjack'],
    install_requires=[''],
)