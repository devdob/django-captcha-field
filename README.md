# Example Package

This is an example boilerplate template to start a python package.

The following notes are available in 
[Python Packaging Tutorial](https://packaging.python.org/tutorials/packaging-projects/)
and
Little Big Programming [A Simple Guide for Python Packaging](https://medium.com/small-things-about-python/lets-talk-about-python-packaging-6d84b81f1bb5)


To start, your package should be structured as follows:

```text
/python_package_boilerplate
  /my_package
    __init__.py
```

Now edit your `__init__.py` file to include your package name, it is set to
`my-package` for the purpose of this example

```python
name = "my_package"
```

Now create the rest of the package files `setup.py`, `LICENSE` and `README.md`.
You package structure should now look like this,

```text
/python_package_boilerplate
  /my_package
    __init__.py
    serialize.py
  setup.py
  LICENSE
  README.md
```

In your `setup.py` add the following. This will specify how your package should
be installed.

```python
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="my-package-anassif",
    version="0.0.1",
    author="Abdallah Nassif",
    author_email="a.nassif@sit-mena.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # Make sure you add all your package dependencies here.
    # You can specify versions like below, but its better 
    # not to specify any, and make sure your package always 
    # works with latest version.
    install_requires=[
        "requests==2.21.0",
        "gevent==1.2.2",
    ],
)
```

Note: The package name is important as it will be used when uploading your
package to pypi, so it must be unique.

Read more about the setup.py 
[here](https://packaging.python.org/tutorials/packaging-projects/#creating-setup-py).


The `README.md` file is the text you are currently reading. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.

You must include a License file and this can contain any type of license or a SIT
specific one (We don't have one currently). For general purposes use MIT open source
software license

```text
Copyright (c) 2018 The Python Packaging Authority

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

# Packaging

Now that you are done setting up your package and adding your functionality, its 
time to package your new module. In order to do so, you need to have the `setuptools`
 and `wheel` installed and up-to-date. Make sure you do so using,
 
```bash
python3 -m pip install --user --upgrade setuptools wheel
```

Now create your package by running this command,

```bash
python3 setup.py sdist bdist_wheel
```

# Upload to pypi

If your package **PUBLIC**, follow the steps in the tutorial about uploading using
`twine` [here](https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives)
