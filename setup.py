from setuptools import find_packages,setup

setup(
    name='MCQGENERATOR',
    version='0.0.1',
    author='Kanishka Rani',
    author_email='kanishka22043@gmail.com',
    install_requires=["transformers","accelerate","langchain","streamlit","python-dotenv","PyPDF2","pandas","numpy"],
    packages=find_packages()
)

