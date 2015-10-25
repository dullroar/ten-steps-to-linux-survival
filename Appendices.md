  
# Appendices

> *"That rug really tied the room together, did it not?"* - Walter Sobchak
> (*The Big Lebowski*)

## Cheat Sheet

This list outlines all the commands, files and other UNIX items of interest
brought up in this book. Use `man` or other methods outlined in the book
to find more information on them.

### Environment Variables

* [**`$?`**](http://linux.die.net/abs-guide/exit-status.html) - the exit
code for the last command or program executed.
* [**`$PATH`**](http://linux.die.net/Bash-Beginners-Guide/sect_03_02.html) -
the execution search path.

### Conditional Execution

See ["logical operators."](http://linux.die.net/abs-guide/ops.html)

* **`&&`** - execute the second
command only if the first command succeeds.
* **`||`** - execute the secon
command even if the first command fails.

### Redirection

See ["I/O Redirection."](http://linux.die.net/abs-guide/io-redirection.html)

* **`stderr`** - file descriptor 2, always open for writing from a
process, defaults to the screen on a terminal session.
* **`stdin`** - file descriptor 0, always open for reading in a
process, defaults to the keyboard input on a terminal session.
* **`stdout`** - file descriptor 1, always open for writing from a
process, defaults to the screen on a terminal session.
* **`<`** - redirect a file to `stdin`.
* **`>`** - redirect `stdout` to a file.
* **`2>`** - redirect `stderr` to a file.
* **`|`** - pipe `stdout` from one process into `stdin` in another
process.

### Special Files and Directories

* [**`~`**](http://linux.die.net/Bash-Beginners-Guide/sect_03_04.html) -
shortcut for current user's home directory.
* **`.bash_history`** - history of commands entered at the command
prompt (also a nice example of a hidden "dotfile").

### System Directories

See
[Important System Directories.](http://linux.die.net/abs-guide/systemdirs.html)

* **`/etc`** - configuration files location.
* **`/home`** - "home" or user profile directories.
* **`/proc`** - system run-time information.
* **`/root`** - "home" directory for "root" user (system admin).
* **`/tmp`** - temporary files location.
* **`/var/log`** - log files location.

### Commands

These are "section 1" commands, i.e., normal user commands that typically
don't require any special privileges beyond permissions to access files and
the like.

* [**`7z`**]*http://linux.die.net/man/1/7z) - compress and uncompress files
and directories using the 7-zip algorithm.
* [**`apropos`**](http://linux.die.net/man/1/apropos) - search for help on
commands by pattern.
* [**`awk`**](http://linux.die.net/man/1/awk) - language for processing
streams of data.
* [**`bash`**](http://linux.die.net/man/1/bash) - the Bourne-again shell.
* [**`bzip2`**](http://linux.die.net/man/1/bzip2) - compress and uncompress
files using the `bzip2` algorithm.
* [**`cat`**](linux.die.net/man/1/cat) - concatenate the input files to
`stdout`.
* [**`cd`**](linux.die.net/man/1/cd) - change the current directory.
* [**`chgrp`**](linux.die.net/man/1/chgrp) - change the primary group of a
file or directory.
* [**`chmod`**](linux.die.net/man/1/chmod) - change the permissions (mode
bits) of a file or directory.
* [**`chown`**](linux.die.net/man/1/chown) - change the owner of a file or
directory.
* [**`cp`**](linux.die.net/man/1/cp) - copy files or directories.
* [**`crontab`**](linux.die.net/man/1/crontab) - display or edit tasks to
be run by `cron`.
* [**`curl`**](http://linux.die.net/man/1/curl) - download files from the
internet.
* [**`df`**](http://linux.die.net/man/1/df) - show space utilization by
file system.
* [**`diff`**](linux.die.net/man/1/diff) - show the differences between
files.
* [**`dig`**](http://linux.die.net/man/1/dig) - look up DNS info on an address.
* [**`dpkg`**](http://linux.die.net/man/1/dpkg) - package manager for
Debian flavors.
* [**`echo`**](linux.die.net/man/1/echo) - display passed parameters to
`stdout`.
* [**`email`**](http://linux.die.net/man/1/email) - send email.
* [**`false`**](linux.die.net/man/1/false) - do nothing, unsuccessfully.
* [**`file`**](linux.die.net/man/1/file) - give best guess as to type of
file.
* [**`find`**](http://linux.die.net/man/1/find) - find files based on
various conditions and execute actions against the results.
* [**`grep`**](linux.die.net/man/1/grep) - search for a pattern (regular
expression) in files.
* [**`help`**](linux.die.net/man/1/help) - help for built-in commands in
`bash`.
* [**`info`**](http://linux.die.net/man/1/info) - an alternative for `man`,
especially for GNU programs. Remember `q` quits.
* [**`less`**](linux.die.net/man/1/less) - display the file one page at a
time on `stdout`.
* [**`ln`**](linux.die.net/man/1/ln) - create hard or soft (shortcut)
links.
* [**`ls`**](linux.die.net/man/1/ls) - list directory contents.
* [**`man`**](linux.die.net/man/1/man) - display manual pages. Remember `q`
quits.
* [**`mkdir`**](linux.die.net/man/1/mkdir) - make a new directory.
* [**`mutt`**](linux.die.net/man/1/mutt) - email client.
* [**`mv`**](linux.die.net/man/1/mv) - move files or directories.
* [**`pine`**](linux.die.net/man/1/pine) - email client.
* [**`ps`**](linux.die.net/man/1/ps) - list running processes.
* [**`pwd`**](linux.die.net/man/1/pwd) - print the current (working)
directory name.
* [**`rename`**](linux.die.net/man/1/rename) - rename files in more complex
ways than `mv` can.
* [**`rm`**](linux.die.net/man/1/rm) - delete (remove) files or
directories.
* [**`set`**](linux.die.net/man/1/set) - set an environment variable, or
display all environment variables.
* [**`sort`**](linux.die.net/man/1/sort) - sort `stdin` or a file to
`stdout`.
* [**`ssh`**](http://linux.die.net/man/1/ssh) - secure shell termina
progam and protocol.
* [**`tail`**](http://linux.die.net/man/1/tail) - display the last lines of
a file.
* [**`tar`**](http://linux.die.net/man/1/tar) - "tape archive", a way to
combine directories into a single flat file.
* [**`tee`**](http://linux.die.net/man/1/tee) - write to a file and
`stdout` at the same time.
* [**`telnet`**](http://linux.die.net/man/1/telnet) - ancient terminal
program and protocol.
* [**`touch`**](http://linux.die.net/man/1/touch) - create an empty file or
change the last-modified time of an existing file.
* [**`true`**](http://linux.die.net/man/1/true) - do nothing, successfully.
* [**`uname`**](http://linux.die.net/man/1/uname) - print system info.
* [**`unzip`**](http://linux.die.net/man/1/unzip) - uncompress `.zip`
files.
* [**`vi`**](http://linux.die.net/man/1/vi) - "visual" editor, a file
editor.
* [**`wget`**](http://linux.die.net/man/1/wget) - download files from the
internet.
* [**`whoami`**](http://linux.die.net/man/1/whoami) - the answer to life's
most existential question.
* [**`whois`**](http://linux.die.net/man/1/whois) - look up DNS ownership
info on an address.
* [**`zip`**](http://linux.die.net/man/1/zip) - compress files and
directories using the PKZip algorithm.

### System Commands

These are "section 8" commands, and ***may*** require special privileges
such as `sudo` to run, depending on the system. Yes, some systems restrict
the use of `ping`!

* [**`apt-get`**](http://linux.die.net/man/8/apt-get) - package manager for
Debian flavors.
* [**`cron`**](http://linux.die.net/man/8/cron) - system for running
"scheduled tasks."
* [**`dmesg`**](http://linux.die.net/man/8/dmesg) - display kernel log
messages.
* [**`ifconfig`**](http://linux.die.net/man/8/ifconfig) - display network
(interface) configuration.
* [**`mount`**](http://linux.die.net/man/8/mount) - mount a file system to
a specific location.
* [**`ping`**](http://linux.die.net/man/8/ping) - test for network
connectivity to an IP address.
* [**`reboot`**](http://linux.die.net/man/8/reboot) - restart the system.
* [**`rpm`**](http://linux.die.net/man/8/rpm) - package manager for Fedora
flavors.
* [**`shutdown`**](http://linux.die.net/man/8/shutdown) - shutdown or
restart the system.
* [**`sudo`**](http://linux.die.net/man/8/sudo) - execute a command with
elevated privileges.
* [**`traceroute`**](http://linux.die.net/man/8/traceroute) - trace the
route to an IP address.

## Examples

The following are meant to be simple, mostly "one-liner" type samples to
reinforce the concepts here and continue to show you "the UNIX philosophy"
of approaching solutions in multiple small steps.

### Keep It Simple, Stupid

Here's a good example. During the debugging of this book I kept having
problems with internal links to other parts of the generated PDF not
working. Some did, some didn't. And they ***all*** worked in epub and HTML
outputs.

I had a suspicion it was because I was wrapping links from one line to the
next in Markdown (trying to keep below a certain column count), so I wanted
to find all lines that had an opening square bracket but ***not*** a
closing one, e.g., I wanted to catch the first line in the following:

```markdown
See [Important System
Directories.](http://linux.die.net/abs-guide/systemdirs.html)
```

Now you could spend a long time with regular expressions trying to figure
out how to do negative matching on that closing `]`. Good luck!

Or you could do something as simple as this, which shows the source files
now, after I've cleaned them all up (the only remnants are now in
examples):

```bash
$ grep '\[' *.md | grep -v ']'
Step01.md: (( expression ))           if COMMANDS; then COMMANDS; [ elif C>
Step01.md: :                          kill [-s sigspec | -n signum | -sigs>
Step04.md:./FileCheckers/otschecker:  [ $rc != 0 -a "$pdfinfo" != "Comma...
Step04.md:./FileCheckers/pdfpwdchecker: if [ $rc != 0 -a "$pdfinfo" = "C...
```

What makes this simple? Finding `[` with the first `grep` and then simply
piping it to a second `grep` and inverting the match logic (`-v`) on `]`.

**Note:** For what it's worth, it doesn't look like the wrapped links in
Markdown were the issue. In fact, now that I generate Markdown as an output
format for the `README.md` file, I've noticed it does the same thing.
So I still haven't figured it out! Ideas welcome.

### Chain Gangs

Remembering that `&&` only executes the next command if the prior one is
successful, we can do things like set up a sample directory and (empty)
files for playing around with files and directories in one fell swoop:

```bash
$ mkdir -p /tmp/foo/d && cd /tmp/foo && touch a b c d/e

$ ls
a  b  c  d
```

That is roughly equivalent to:

```bash
$ cd /tmp

$ mkdir -p foo

$ cd foo

$ mkdir -p d

$ touch a b c d/e

$ ls
a  b  c  d
```

### Simple Scripts

I said I wasn't going to cover scripting, especially logical constructs
like `if`/`fi`. But simple scripts that just "do things" in a certain
order are within scope, and the following, which installs
[`freerdp`](https://github.com/freerdp/freerdp), is a good example of
simply taking the guesswork out of doing something repetitive across
multiple machines. I keep this `installrdp` script in Dropbox so I can run
it on any new machine I set up quickly and easily (once I get Dropbox set
up on the machine!)

```bash
#!/bin/bash
sudo apt-get -y install git
cd ~
git clone git://github.com/FreeRDP/FreeRDP.git
cd FreeRDP
sudo apt-get -y install build-essential git-core cmake libssl-dev \
  libx11-dev libxext-dev libxinerama-dev libxcursor-dev libxdamage-dev \
  libxv-dev libxkbfile-dev libasound2-dev libcups2-dev   libxml2 \
  libxml2-dev libxrandr-dev libgstreamer0.10-dev \
  libgstreamer-plugins-base0.10-dev libxi-dev \
  libgstreamer-plugins-base1.0-dev libavutil-dev libavcodec-dev \
  libcunit1-dev libdirectfb-dev xmlto doxygen libxtst-dev
cmake -DCMAKE_BUILD_TYPE=Debug -DWITH_SSE2=ON .
make
sudo make install
sudo echo "/usr/local/lib/freerdp" > /etc/ld.so.conf.d/freerdp.conf
sudo echo "/usr/local/lib64/freerdp" >> /etc/ld.so.conf.d/freerdp.conf
sudo echo "/usr/local/lib" >> /etc/ld.so.conf.d/freerdp.conf
sudo ldconfig
which xfreerdp
xfreerdp --version
```

You should be able to understand all of the above now, or know where to
look to figure it out. The only nuance we may not have covered is that at
the shell prompt and in scripts both you can put a `\` at the end of a line
and it will "escape" the newline (`\r`) so you can continue the same
command on the next line. This is useful because some interactive
terminals don't "wrap" well, and it makes more readable script files, too.

And yes, in the section on package management I talked about the dangers
of installing packages directly from source. In this case, though,
`freerdp` in the Mint repositories is lagging far enough behind the new
RDP protocol version 8 support that I want to use the latest and greatest
`freerdp` from GitHub for performance reasons. But now it's up to me to
track and update the software (if I care).

  