---
title: Module 1
description: Python installation, PIP structure, and basic Earth object creation
date: 2022-03-26T23:01:52.366Z
author:
  - Brandon Sexton
name: module-1
oxa: oxa:zyBWlmnbnltDRPejFqwi/pbXeJXnaITQbVuUlGull
---

# Module 1

+++ {"oxa":"oxa:zyBWlmnbnltDRPejFqwi/FtMoswhFlFZxePlGYNO0.16"}

This document contains the basic steps needed to create a distribution-ready python project. The intent in this document as well as future documents is to provide concise details of how to perform the tasks while minimizing unnecessary background details. An overview of the material covered in this module is below.

* Getting Started - resources for beginners
  * Install Python - links to download Python installers
  * Integrated Development Environments - links to download IDEs for creating code
* Packaging - tips for creating a distribution-ready python project
  * PIP Installations - links and simple background on Python packaging
  * Package Structure - screenshots and code snippets required for packaging
* Code - snippets of project scripts
  * Earth Object - create a basic class to hold Earth properties
  * Earth Test - create a test class to validate the new Earth object

# Getting Started

## Install Python

You can download any version of python 3; however, we’ll be using [Python 3.8.10](https://www.python.org/downloads/release/python-3810/) to facilitate consistency in future coding tutorials. Download the appropriate [Python](https://www.python.org/downloads/) installer for your platform and follow the Installation Wizard instructions.

## Integrated Development Environments

Although python scripts can be edited in a basic editor like [notepad++](https://notepad-plus-plus.org/) or even in the terminal window using things like [nano](https://www.nano-editor.org/dist/v2.2/nano.html) and [vim](https://www.vim.org/download.php), I’d recommend a more capable IDE with language-specific extensions. My favorite is [Visual Studio](https://visualstudio.microsoft.com/downloads/), but some other options are listed below.

* [pycharm](https://www.jetbrains.com/pycharm/)
* [JupyterLab](https://jupyter.org/)
* [spyder](https://www.spyder-ide.org/)
* [IDLE](https://docs.python.org/3/library/idle.html)

The right answer when choosing an IDE is the one that offers the most intuitive navigation for you. If you have familiarity with IDEs already, I’d suggest following these tutorials using the IDE with which you are most experienced. If you are a complete beginner, I’d suggest sticking with VS Code to minimize variances from the tutorials. If you are somewhere in the middle, you should absolutely try a few before you get too far in the examples.

# Packaging

## PIP Installations

This section isn’t entirely necessary if you just want to see some quick code examples. If you plan to follow these tutorials through major milestones, though, this knowledge will be fairly valuable. Specifically, this section will provide the background information necessary for package [installation](https://packaging.python.org/en/latest/tutorials/installing-packages/) and distribution. Detailed documentation on pip can be found [here](https://pip.pypa.io/en/stable/), but all you really need to know is that pip will allow you to install your project along PYTHONPATH so you can treat it just like any other module. The major tool we need to build such a package is [wheel](https://pypi.org/project/wheel/).

Open a command terminal and install wheel by issuing this command:

```python
pip install wheel
```

Package Structure will provide further detail on how to prepare the actual project for distribution.

## Package Structure

Like PIP Installations, this section can be skipped if you are not interested in following the tutorials through major milestones; however, the information could still be useful if you ever want to create a python package that can be distributed to other users.

### Create the appropriate files and folders

1. Create a folder named “spacebar” anywhere on your system
2. Open the newly created folder
3. Create another folder named “spacebar”
4. Create a file named setup.py

Your new file structure should look like the list below.

* spacebar
  * spacebar
  * setup.py

### Edit setup.py

```python
#!/usr/bin/env python

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

setup(
	name="spacebar",
	version="0.1.0",
	packages=find_packages()
)
```

### Test installation

1. Open a command terminal
2. Navigate to the top-level spacebar directory
3. Issue the following command:

   ```python
   pip install .
   ```

You should see some build processes occur followed by a successful installation message. If you do not see the successful install message. Revisit the steps above to verify everything is correct.

# Code

## Earth Object

### Create files and folders

Start by editing your project folder structure to be consistent with the following list:

* spacebar
  * spacebar
    * \__init_\_.py
    * astro
      * \__init_\_.py
      * bodies.py

The \__init_\_.py files will be empty, but they will be necessary for Python to recognize the paths of modules that can be imported. The bodies.py file will contain our code.

### Edit bodies.py

```python
class Earth:
    """
    Class used to represent Earth.  Values are defined using EGM96 geopotential
    model.  Constant naming convention is intentionally not used since the 
    values defined here may be updated in the future by introducing other
    geopotential models
    """
    mu = 3.986004415e5 #km^3/s^2
    equatorial_radius = 6378.1363 #km
```

Here we define a class that contains some key characteristics of Earth. Usually a class would contain an \__init_\_ method; however, we will omit that for classes like this because we will not want to instantiate new objects each time we need Earth.

Also, we have used a naming convention of all lowercase for our variables. A naming convention of all uppercase would have been used if these values were intended to be constant. Instead, we are preparing for future revisions of the code that may allow changing from one geopotential model to another.

## Earth Test

### Create files and folders

Edit your project structure to include the “tests” directory and paths listed below.

* spacebar
  * spacebar
    * \__init_\_.py
    * astro
      * \__init_\_.py
      * bodies.py
    * tests
      * astro
        * \__init_\_.py
        * test_bodies.py

### Edit test_bodies.py

```python
import unittest

from spacebar.astro.bodies import Earth

class TestEarth(unittest.TestCase):
    """
    Test class to validate Earth model
    """

    def test_mu(self):
        """
        Test to verify the mu value is set according to EGM96 model
        """
        self.assertAlmostEqual(398600.4415, Earth.mu)

    def test_radius(self):
        """
        Test to verify the equatorial radius is set according to EGM96 model
        """
        self.assertAlmostEqual(6378.1363, Earth.equatorial_radius)
```

The process defined here of creating a test module with each script addition can quickly become time-consuming, but the benefits are unparalleled as the project continues to grow. To finish up the tutorial and use the test module, follow these steps:

1. Navigate to the top-level spacebar directory
2. Install your package

   ```python
   pip install .
   ```
3. Run the test modules

   ```python
   python -m unittest
   ```

After running the test module, you should receive an indication of the number of passed/failed tests.

