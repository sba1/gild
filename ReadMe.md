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

Usage
-----

The gild tools are in a very early stage. All tools are placed in the ```bin```
directory, most of them require Python. There is a script called ```gild``` that
wraps all available scripts, in which case these become commands to ```gild```.

Commands
--------

```
usage: gild <command> [<args>]

Available commands:
   checkout   Checkout a specific version of a specific component
   clone      Clone all repositories managed by gild
   genpatch   Generate patches for a component against a baseline
   get        Get baseline archive
   list       List gild-managed components and versions

```

Repository Layout
-----------------

At the moment, ```gild``` requires a very specfic repository layout in order to
function properly. Each project that you want to manage with gild in a
repository needs a folder in the repository whose name determines the name of
the component that you are going to manage. It shall contain at least two
files: ```repo.url``` and ```series```. The former file contains just a single
URL pointing to the upstream git repository of the component against you want
to develop patches.

The second file is a tab-separated table that relates the version specifier
that you want to use for ```gild``` to a name of a branch (or commit SHA1)
for which you want to develop patches. The third row is a URL that identfies a
tar ball or similiar full archive. This may be useful when packaging.

At the moment, the layout have to be created manually by yourself. In the
future, ```gild``` may assist you in maintaining this information.

For instance, in the [adtools](https://github.com/sba1/adtools) we manage at
least three components, namely, binutils, coreutils, and gcc. The repo layout
looks like this:

```
 binutils (dir)
   repo.url (file)
     https://github.com/bminor/binutils-gdb
   series (file)
     2.23.2	binutils-2_23_2	http://ftp.gnu.org/gnu/binutils/binutils-2.23.2.tar.bz2
 coreutils (dir)
   repo.url (file)
     git://git.sv.gnu.org/coreutils
  series (file)
     5.2	808f8a1f569303c3f6838f2c8706442939d92593	https://ftp.gnu.org/gnu/coreutils/coreutils-5.2.1.tar.bz2
 gcc (dir)
   repo.url (file)
     https://github.com/gcc-mirror/gcc
   series (file)
     4.9	876d41ed80ce13e060084ed5a552c37c301e5563	http://ftp.gnu.org/gnu/gcc/gcc-4.9.3/gcc-4.9.3.tar.bz2
     5	2bc376d60753a58b10cb179f8edb7d72bee7a88b	http://ftp.gnu.org/gnu/gcc/gcc-5.3.0/gcc-5.3.0.tar.bz2
```

Note that the structure is subject to change.
