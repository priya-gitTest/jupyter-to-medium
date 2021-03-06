import re

import setuptools

from jupyter_to_medium import __version__


with open("README.md", "r") as fh:
    long_description = fh.read()

pat = r'!\[png\]\('
repl = r'![png](https://raw.githubusercontent.com/dexplo/jupyter-to-medium/master/'
long_description = re.sub(pat, repl, long_description)

setuptools.setup(
    name="jupyter_to_medium",
    version=__version__,
    author="Ted Petrou",
    author_email="petrou.theodore@gmail.com",
    description="Publish a Jupyter Notebook as a Medium blogpost",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="Jupyter Notebook Medium Blog",
    url="https://github.com/dexplo/jupyter-to-medium",
    packages=setuptools.find_packages(),
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={'console_scripts': ['jupyter_to_medium=jupyter_to_medium._command_line:main']},
    include_package_data=True,
    data_files=[("etc/jupyter/nbconfig/notebook.d", [
                "jupyter-config/nbconfig/notebook.d/jupyter_to_medium.json"])],
    install_requires=['nbconvert', 'requests']

    )