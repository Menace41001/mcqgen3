from setuptools import find_packages,setup

setup(
    name="mcqgenerator1",
    version='0.0.1',
    author="Kush",
    author_email="Kush.1001@hotmail.com",
    install_requires = ["langchain","streamlit","huggingface_hub","transformers","PyPDF2","python-dotenv","langchain-community","cohere"],
    packages=find_packages()
)