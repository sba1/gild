The gild tools
==============

The gild tools are several scripts for managing patches with help of ```git```.
It is derived from the patch management system I devised for the 
[adtools](https://github.com/sba1/adtools), where I use it to to maintain patches
against e.g. gcc. It is general enough that it can be used also for other projects.

The use case of the gildtools is similar to ```quilt``` which, according to my
knowledge, provides no tight integration of git.

Background
----------

The main idea is that the patches for one or more components are developed in form
of git commits applied to a baseline, which means that you can use every day git
commands to maintain your changes. The gild tools merely assist you to create patches
from it and to apply them afterwards on fresh checkouts. For now, the baseline must
be specified as a git repository, similary to a git submodule.
