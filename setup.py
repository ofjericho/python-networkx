import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="graph-pkg",  # Replace with your own username
    version="0.0.1",
    author="Fabio Maia",
    author_email="maia73@gmail.com",
    description="Create edges on netwokx",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "bleach==3.1.4",
        "certifi==2020.4.5.1",
        "chardet==3.0.4",
        "cycler==0.10.0",
        "decorator==4.4.2",
        "docutils==0.16",
        "idna==2.9",
        "importlib-metadata==1.6.0",
        "keyring==21.2.0",
        "kiwisolver==1.2.0",
        "matplot==0.1.9",
        "matplotlib==3.2.1",
        "networkx==2.4",
        "numpy==1.18.3",
        "pkginfo==1.5.0.1",
        "Pygments==2.6.1",
        "pyloco==0.0.139",
        "pyparsing==2.4.7",
        "python-dateutil==2.8.1",
        "pywin32-ctypes==0.2.0",
        "readme-renderer==25.0",
        "requests==2.23.0",
        "requests-toolbelt==0.9.1",
        "SimpleWebSocketServer==0.1.1",
        "six==1.14.0",
        "tqdm==4.45.0",
        "twine==3.1.1",
        "typing==3.7.4.1",
        "urllib3==1.26.5",
        "ushlex==0.99.1",
        "webencodings==0.5.1",
        "websocket-client==0.57.0",
        "zipp==3.1.0"
    ]
)
