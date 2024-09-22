from setuptools import setup, find_packages

setup(
    name="dockergpustats",
    version="0.1",
    packages=find_packages(),
    description="A Python tool for GPU process monitoring in Docker containers and retrieving Jupyter Notebook tokens from Colab images.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Pichuelectrico/dockergpustats.git",
    author="Joshua Reinoso",
    author_email="pichuelectrico@gmail.com",
    license="MIT",
    install_requires=[
        "python-dotenv==1.0.1",
        "requests==2.32.3",
        "setuptools==58.1.0",
        "pprintpp==0.4.0",
        "regex==2023.10.3",
        "prettytable==3.11.0",
    ],
    entry_points={
        "console_scripts": [
            "dockergpustats=dockergpustats.client:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: System :: Monitoring",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.6",
)
