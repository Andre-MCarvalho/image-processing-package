from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()    

setup(
    name="image-processing-package",
    version="0.0.1",
    author=" Andre Martins",
    author_email="andrem.dec@outlook.com",
    description="Exemplo de pacote Python de processamento de imagem"
    long_description=page_description,
    long_description_content_type="text/markdown",
    url=https://github.com/Andre-MCarvalho/image-processing-package.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.6",
)