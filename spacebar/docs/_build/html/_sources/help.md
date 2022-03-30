---
title: Help
description: Screenshots and tips for building the Jupyter book
date: 2022-03-27T15:51:41.714Z
author:
  - Kevin Lalli
name: help
oxa: oxa:zyBWlmnbnltDRPejFqwi/ZRQihfPH7IZ4JHU6FJJc
---

# Help

+++ {"oxa":"oxa:zyBWlmnbnltDRPejFqwi/naMedjfsW8zrXj6YamVQ.3"}

This would be the content for the landing page. To get all of the Curvenote content out to HTML, you need to have [Curvenote CLI](https://cli.curvenote.dev/) installed. Also, you’ll need to register a token for your account if the project is private.

Then, from terminal, it’s just:

`curvenote export jb https://curvenote.com/@sextonb/spacebar/`

Which will give you a .md (MyST) file for each page as well as a `_config.yaml` and `_toc.yml` that are used in a Jupyter Book build. From whatever directory you exported the markdown to:

`jupyter-book build .`

Will take the markdown & config / TOC files and turn into a Jupyter Book (finished HTML with content, navbars, etc.)

+++ {"oxa":"oxa:zyBWlmnbnltDRPejFqwi/HEbNKRHl5GzgjgQ9hKCi.2"}


```{note}
Note: Curvenote CLI is in beta development! Expect some bugs. Not all features of web GUI are supported in CLI, export yet.
```

There were a couple of issues on this first export. One is with the left-side page navbar.

See below vs. “Modules\[Module 1, Module 2\] and Index Page” in Curvenote.

```{figure} images/zyBWlmnbnltDRPejFqwi-ISURGjTtNu53NyGtm1HJ-v1.png
:name: iHoFndJ3h9
```

The other is that sub-section links do not survive the export. Is this a planned feature? TODO: tag in @curvenotesupport

```{figure} images/zyBWlmnbnltDRPejFqwi-k3awJC20DWuq73zoS189-v1.png
:name: GdSHTycKl8
```

+++ {"oxa":"oxa:zyBWlmnbnltDRPejFqwi/UUGxOnWpN2qPUJVjq45t.1"}

On the plus side, we get the right-side “article navbar” for free, with Jupyter Book’s default build

```{figure} images/zyBWlmnbnltDRPejFqwi-ReHJYEApTh8zPXPJgYTt-v1.png
:name: N1fVpD8Z1B
```

+++ {"oxa":"oxa:zyBWlmnbnltDRPejFqwi/jrCvutvMojCeAjM79lCY.1"}

Here is a screenshot of the directory once both `curvenote export` and `jupyter-book build` have ran

```{figure} images/zyBWlmnbnltDRPejFqwi-LRnSahb22c3nHakmNg3H-v1.png
:name: FprXjv6VrO
```

