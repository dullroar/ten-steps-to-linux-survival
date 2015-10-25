  
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

  