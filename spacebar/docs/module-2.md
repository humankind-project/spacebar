---
title: Module 2
description: ""
date: 2022-03-27T15:49:40.617Z
author:
  - Kevin Lalli
name: module-2
oxa: oxa:zyBWlmnbnltDRPejFqwi/R3rt5inQIf8lalHYNOg3
---

# Module 2

+++ {"oxa":"oxa:zyBWlmnbnltDRPejFqwi/JewM6gUvCrdF5E56useP.1"}

March 2, 2022

Let's take a look at a better testing method now that we've started off with something a bit more interesting than printing "Hello, world."  

#### Remove the \__main_\_ entry point

In module 1 the block at the bottom of bodies.py was just to let you get some satisfaction in seeing your code run.  It's pretty useless, though, so let's clean it up before we go further.  Your bodies.py should now look like this.

```{figure} https://img1.wsimg.com/isteam/ip/c73c525a-f63c-4ceb-8bca-6ec4e3be8131/Screenshot%20from%202022-03-03%2000-00-23.png/:/rs=w:1280
:name: D6VWrxFtpm
```

#### Create \__init_\_.py files

Next, we need to allow python to recognize paths where modules reside.  To do that, we need to add an empty \__init_\_.py file in all directories.  I've added a screenshot of my directory tree below.  Note that it includes some tests we'll be adding here and a linalg.py file that we'll create in the next module.

```{figure} https://img1.wsimg.com/isteam/ip/c73c525a-f63c-4ceb-8bca-6ec4e3be8131/Screenshot%20from%202022-03-02%2020-25-47.png/:/rs=w:1280
:name: qsvGYIfDEp
```

#### Create tests

As you've probably already seen, we're going to be creating a mirrored "tests" directory.  This structure will mimic the "spacebar" structure, but all .py files will now include a "test\_" prefix.  Be sure to follow the structure shown above exactly to prevent import issues.  After you've created the folders and test_bodies.py file, open the file for editing.

```{figure} https://img1.wsimg.com/isteam/ip/c73c525a-f63c-4ceb-8bca-6ec4e3be8131/Screenshot%20from%202022-03-03%2000-01-33.png/:/cr=t:0%25,l:0%25,w:100%25,h:100%25/rs=w:1280
:name: oCN0OqFSF0
```

You'll see that the tests are pretty basic, but this structure will be vital as our project grows.  

#### Run tests

After you've edited your test_bodies.py file, go to the terminal and execute the tests.

```{figure} https://img1.wsimg.com/isteam/ip/c73c525a-f63c-4ceb-8bca-6ec4e3be8131/Screenshot%20from%202022-03-02%2020-34-43.png/:/cr=t:0%25,l:0%25,w:100%25,h:100%25/rs=w:1280
:name: ozVQQSKknf
```

Inspect the output to insure 2 tests were run successfully.  If the tests were not detected, verify that \__init_\_.py files are in all directories.  If the tests ran but failed, check your assertions on lines 14 and 20 of test_bodies.py or check your mu and equatorial_radius settings on lines 6 and 7 of bodies.py

