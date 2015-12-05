  
# How Do You Know What You Don’t Know, `man`?

***`man`, `info`, `apropos`, Linux Documentation Project, Debian and Arch
guides, StackOverflow and the dangers of searching for “`man find`” or
“`man touch`” on the internet.***

> *"You're soaking in it."* - Palmolive commercial

The biggest issue with bootstrapping into "UNIX" is not the lack of
documentation but almost the surplus of it, coupled with a severe "RTFM"
attitude by most old-timers toward most newbies. Besides the typical
"Google" and "StackOverflow" answers, there are actually lots of very
reliable places to turn to for information:

## `man`, is that `info` `apropos`?

There are three commands that are the basis for reading "UNIX" documentation
within "UNIX" itself - [`man`](http://linux.die.net/man/1/man),
[`info`](http://linux.die.net/man/1/info) and
[`apropos`](http://linux.die.net/man/1/apropos).

`man` is short for *manual pages*, and is used to display the main help for
most "UNIX" commands. For example, `man ls` shows:

```
LS(1)                                                             User C...

NAME
       ls - list directory contents

SYNOPSIS
       ls [OPTION]... [FILE]...

DESCRIPTION
       List information about the FILEs (the current directory by
       default).  Sort entries alphabetically if none of -cftuvSUX nor
       --sort is specified.

       Mandatory arguments to long options are mandatory for short optio...

       -a, --all
              do not ignore entries starting with .

       -A, --almost-all
              do not list implied . and ..
...and so on...
```

**Note:** `man` uses `less` as a paginator, with all that means, including
the same navigation and search keys, and most important to remember - `Q`
to quit. How do I know this? Because of course you can `man man`!

Notice the `LS(1)` part. The UNIX manual was originally divided into
multiple sections by AT&T. Section 1 is normal user commands. Section 5 is
file formats (like for config files), and section 8 is for system
administration commands. You usually don't care, and can `man ls` or `man
ifconfig` to your heart's content.

But sometimes there are duplicate names in the different sections. For
example, there is both a `passwd` command and a `passwd` file format (for
`/etc/passwd`). By default, `man passwd` will show you the documentation
from the lowest numbered section with a match, in this case section 1,
usually referred to as `passwd(1)` to disambiguate which thing we're
talking about:

```
PASSWD(1)                                                         User C...

NAME
       passwd - change user password

SYNOPSIS
       passwd [options] [LOGIN]

DESCRIPTION
       The passwd command changes passwords for user accounts. A normal user
       may only change the password for his/her own account, while the
       superuser may change the password for any account.  passwd also
       changes the account or associated password validity period.

   Password Changes
       The user is first prompted for his/her old password, if one is
       present. This password is then encrypted and compared against the
       stored
...and so on...
```

To see the `man` page for the `passwd` file format, we have to explicitly
specify the section, in this case by using `man 5 passwd`:

```
PASSWD(5)                                                  File Formats ...

NAME
       passwd - the password file

DESCRIPTION
       /etc/passwd contains one line for each user account, with seven
       fields delimited by colons (“:”). These fields are:

       ·   login name

       ·   optional encrypted password

       ·   numerical user ID

       ·   numerical group ID
...and so on...
```

Besides `man`, many GNU tools come with help in `info` format, which is
from `emacs`. While `info` is much better at enabling complex help files
with navigation I am not a fan because I tend not to hold all the
keystrokes in my head. The biggest thing to remember if you do something
like `info vi` is that `q` quits the `info` command.

Finally, what if you don't know the name of the command? Well, each "man
page" has a title and brief description, e.g., "passwd - change user
password" in the `man passwd` output above. The `apropos` command can
simply search those titles and descriptions for a word or phrase and show
you all the results:

```
# apropos edit
dpatch-edit-patch (1) - maintain dpatch patches for a Debian source package
edit (1)             - execute programs via entries in the mailcap file
rediff (1)           - fix offsets and counts of a hand-edited diff
editor (1)           - Nano's ANOther editor, an enhanced free Pico clone
elfedit (1)          - Update the ELF header of ELF files.
ex (1)               - Vi IMproved, a programmers text editor
grub-editenv (1)     - edit GRUB environment block
msgfilter (1)        - edit translations of message catalog
nano (1)             - Nano's ANOther editor, an enhanced free Pico clone
pdbedit (8)          - manage the SAM database (Database of Samba Users)
pico (1)             - Nano's ANOther editor, an enhanced free Pico clone
psed (1)             - a stream editor
readline (3readline) - get a line from a user with editing
rnano (1)            - Restricted mode for Nano's ANOther editor, an enh...
rview (1)            - Vi IMproved, a programmers text editor
rvim (1)             - Vi IMproved, a programmers text editor
s2p (1)              - a stream editor
sed (1)              - stream editor for filtering and transforming text
sensible-browser (1) - sensible editing, paging, and web browsing
sensible-editor (1)  - sensible editing, paging, and web browsing
sensible-pager (1)   - sensible editing, paging, and web browsing
sudoedit (8)         - execute a command as another user
vi (1)               - Vi IMproved, a programmers text editor
view (1)             - Vi IMproved, a programmers text editor
vigr (8)             - edit the password, group, shadow-password or shad...
vim (1)              - Vi IMproved, a programmers text editor
vimdiff (1)          - edit two, three or four versions of a file with V...
vipw (8)             - edit the password, group, shadow-password or shad...
visudo (8)           - edit the sudoers file

```

Note the `man` section numbers after each command name. Also note that
`apropos` is not sophisticated - it is simply searching for the exact
string you give it in the very limited "brief descriptions" from the `man`
pages. That's all. But a lot of time that's all you need to remember, "Ah,
yes, `nano` is the other editor I was thinking about and like better than
`vi`."

**Note:** `man`, `info` and `apropos` are just normal "UNIX" commands like all
the others, so while they may default to displaying with a paginator on an
interactive terminal, you can run their output through other commands, just
like any other. For example, maybe we remember only that the command had
something with "edit" and was a system administration ("section 8")
command:

```
$ apropos edit | grep "(8)"
jfs_debugfs (8)      - shell-type JFS file system editor
pdbedit (8)          - manage the SAM database (Database of Samba Users)
samba-regedit (8)    - ncurses based tool to manage the Samba registry
sudoedit (8)         - execute a command as another user
vigr (8)             - edit the password, group, shadow-password or shad...
vipw (8)             - edit the password, group, shadow-password or shad...
visudo (8)           - edit the sudoers file
```

Or maybe you can't remember whether it's `-r`, `-R` or `--recursive` to
copy subdirectories recursively with `cp`:

```
$ man cp | grep -i "recurs"
              copy contents of special files when recursive
       -R, -r, --recursive
              copy directories recursively
```

Whaddya know. It can be any of the three.

And yes, you can `man man`, `man info`, `info info` and `info man`, for
that matter!

## How Do You Google, `man`?

You can often search the internet for "UNIX" documentation, and the `man`
pages have long been online. A site I like (and link to a lot here) is
[http://linux.die.net/man/](http://linux.die.net/man/). Often, though,
you can just google ["man ls"](https://www.google.com/#q=man+ls) and the
top hits will be what you want.

***However***, there are times you need to be careful. Googling for either
`man touch` or `man tail`, for example, will probably not give you the
results you seek and may set off filters at work, so be careful out there
and remember to bookmark a couple of actual `man` page sites so that you
can go there directly and look up a command.

## Books and Stuff

There are several consistently high-quality free sources of information on
various parts of Linux and related systems on the internet.

* [**The Linux Documentation Project (LDP)**](http://www.tldp.org/guides.html) -
has fallen a bit behind over the years, but still has two of the best
`bash` scripting books out there,
[*Bash Guide for Beginners*](http://www.tldp.org/LDP/Bash-Beginners-Guide/html/index.html)
and
[*Advanced Bash-Scripting Guide*](http://www.tldp.org/LDP/abs/html/index.html).
I continue to use the latter all the time.

* [**Arch Linux Wiki**](https://wiki.archlinux.org/) - you may not think
this would be useful if you are running Debian or Fedora or something else,
but remember most "UNIX" systems are all very similar, and often the best
documentation on a package or setting something up in Linux is in the Arch
wiki.

* [**Debian documentation**](https://www.debian.org/doc/) - again, even if
you are not running a Debian-based distro, this can be handy because it
describes how to administer Linux in a way that often transcends distro
specifics (and at least explains how Debian approaches the differences).
The best books in the series are
[*The Debian Administrator's Handbook*](https://www.debian.org/doc/manuals/debian-handbook/)
and the
[*Debian Reference*](https://www.debian.org/doc/manuals/debian-reference/),
which is a lot more formal attempt at the same type of territory this
guide covers.

Ubuntu, Mint and some other distros have quite active message fora, and
of course StackOverflow and its family are also very useful. 

Besides the above, if you are dealing with a package that is not part of
the "core" OS, such as [Samba](https://www.samba.org/samba/) for setting up
CIFS shares on Linux, you should always look at
[the package site's documentation](https://www.samba.org/samba/docs/) as
well as any specific info you can find about the distro you are running.  
  
