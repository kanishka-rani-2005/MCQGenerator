from setuptools import find_packages, setup

setup(
    name='MCQGENERATOR',
    version='0.0.1',
    author='Kanishka Rani',
    author_email='kanishka22043@gmail.com',
    description='An MCQ generator using Hugging Face and LangChain',
    packages=find_packages(),
    install_requires=[
        "transformers>=4.40.0",
        "langchain>=0.1.0",
        "streamlit",
        "python-dotenv",
        "PyPDF2",
        "pandas",
        "numpy"
    ],
    python_requires=">=3.8",
)
