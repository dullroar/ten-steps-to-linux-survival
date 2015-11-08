  
# Step 1

## Come Out of Your Shell

## What is a shell?

Windows has a shell.

Two, in fact:

> * `CMD.EXE`
> * `PowerShell.EXE`

. . .

Technically, Windows Explorer is a "shell" for the GUI environment.

## "UNIX" has **lots** of shells

> * **`sh`** - Bourne shell
>     * **`ash`** - Almquist shell
>         * **`dash`** - Debian Almquist shell
>     * **`bash`** - "Bourne-again" shell
>     * **`ksh`** - Korn shell
>     * **`zsh`** - Z shell
> * **`csh`** - C shell
> * ***and many more!***

## Linux default shell

Typically `bash`

# Comparing `CMD.EXE` and `bash`

## `set` in `bash`

```
$ set
ALLUSERSPROFILE='C:\ProgramData'
APPDATA='C:\Users\myuser\AppData\Roaming'
BASH=/bin/bash
...and so on...
```

## `set` in `CMD.EXE`

```
C:\> set
ALLUSERSPROFILE=C:\ProgramData
APPDATA=C:\Users\myuser\AppData\Roaming
CLIENTNAME=MYMACHINE
...and so on...
```

## `echo`

**`bash`:**

(Inside Cygwin)

```
$ echo $HOMEDRIVE
C:
```

**`CMD.EXE`:**

```
C:\> echo %homedrive%
C:
```

## Similar, but different

> * `$variable` (`bash`) vs. `%variable%` (`CMD.EXE`)
> * `bash` is case-sensitive, `CMD.EXE` is not

## Product of your environment

## Setting variables

```
$ FOO=myval /home/myuser/myscript

$ CURRDATE=`date`

$ echo $CURRDATE
Wed Oct 28 11:43:38 CDT 2015
```

## A path! A path!

```
$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:...
```

## Getting lazy

> * Tab expansion
> * Command history
  