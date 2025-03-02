from setuptools import find_packages,setup
setup(
    name='mcq_gen',
    version='0.0.1',
    author='Kaif',
    author_email='doneman536@gmail.com',
    install_requires = [ "langchain","streamlit","python-dotenv", "PyPDF2"],
    packages=find_packages()
)