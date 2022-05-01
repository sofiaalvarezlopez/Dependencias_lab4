import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Dependencias_Lab4",
    version="0.0.1",
    author="sofiaalvarezlopez",
    author_email="ms.alvarezl@uniandes.edu.co",
    description="Dependencias para el laboratorio 4 de Inteligencia de Negocios.",
    long_description=long_description,
    url="https://github.com/sofiaalvarezlopez/Dependencias_lab4",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
   'numpy'],
)