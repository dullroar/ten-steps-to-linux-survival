
\renewcommand{\chaptername}{}
\renewcommand{\thechapter}{A}

# Appendices

> *"That rug really tied the room together, did it not?"* - Walter Sobchak (*The Big Lebowski*)

## Cheat Sheet{.unnumbered}

This list outlines all the commands, files and other UNIX items of interest brought up in this
book. Use `man` or other methods outlined in the book to find more information on them.

### Environment Variables{.unnumbered}

* [**`$?`**](http://linux.die.net/abs-guide/exit-status.html)
\index{environment variables!\?@\texttt{\$}\texttt{?} (exit status code)}
\index{*@\texttt{?} (exit status environment variable)} - the exit code for the last
command or program executed.

* [**`$PATH`**](http://linux.die.net/Bash-Beginners-Guide/sect_03_02.html)\drenv{PATH}{execution search path} - the
execution search path.

### Conditional Execution{.unnumbered}

See ["logical operators"](http://linux.die.net/abs-guide/ops.html).

* **`&&`**\index{*@\texttt{\&}\texttt{\&} (logical "and" operator)} - execute the second
command only if the first command succeeds.

* **`||`**\index{*@\texttt{"|"|} (logical "or" operator)} - execute the second command even
if the first command fails.

### Redirection{.unnumbered}

See ["I/O Redirection"](http://linux.die.net/abs-guide/io-redirection.html).

* ***stderr***\drstd{stderr} - file descriptor 2, always open for
writing from a process, defaults to the screen on a terminal session.

* ***stdin***\drstd{stdin} - file descriptor 0, always open for reading
in a process, defaults to the keyboard input on a terminal session.

* ***stdout***\drstd{stdout} - file descriptor 1, always open for
writing from a process, defaults to the screen on a terminal session.

* **`<`**\index{*@\texttt{<} (input redirection)}
\index{I/O!redirection!input (\texttt{<})} - redirect a file to *stdin*.
\drstd{stdin}

* **`>`**\index{*@\texttt{>} (output redirection)}
\index{I/O!redirection!output (\texttt{>})} - redirect *stdout* to a file.
\drstd{stdout}

* **`2>`**\index{*@\texttt{2>} (\textit{stderr} redirection)}
\index{I/O!redirection!error (\texttt{2>})} - redirect *stderr* to a file.
\drstd{stderr}

* **`|`**\index{*@\texttt{"|} (pipe)}\index{I/O!redirection!pipe (\texttt{"|})} - pipe
*stdout* from one process into *stdin* in another process.
\drstd{stdin}
\drstd{stdout}

### Special Files and Directories{.unnumbered}

* [**`~`**](http://linux.die.net/Bash-Beginners-Guide/sect_03_04.html)
\index{files and directories!home (\texttt{\~{}})} - shortcut for current user's home directory.

* **`.bash_history`**\index{files and directories!special!bashhistory@\texttt{.bash\_history}} - history of
commands entered at the command prompt (also a nice example of a hidden "dotfile").

### System Directories{.unnumbered}

See [Important System Directories](http://linux.die.net/abs-guide/systemdirs.html).

* **`/etc`**\index{files and directories!special!etc@\texttt{/etc/}} - configuration files location.

* **`/home`**\index{files and directories!home (\texttt{/home/})} - "home" or user profile
directories.

* **`/proc`**\index{files and directories!special!proc@\texttt{/proc/}} - system run-time information.

* **`/root`**\index{files and directories!root "home" (\texttt{/root/})} - "home" directory for
"root" user (system admin).

* **`/tmp`**\index{files and directories!special!tmp@\texttt{/tmp/}} - temporary files location.

* **`/var/log`**\index{files and directories!special!varlog@\texttt{/var/log/}} - log files location.

### Commands{.unnumbered}

These are "section 1" commands, i.e., normal user commands that typically don't require any special
privileges beyond permissions to access files and the like.

* [**`7z`**](http://linux.die.net/man/1/7z)\drcmd{7z} - compress and uncompress files and
directories using the 7-zip algorithm.

* [**`apropos`**](http://linux.die.net/man/1/apropos)\drdoc{apropos} - search for help on commands
by pattern.

* [**`awk`**](http://linux.die.net/man/1/awk)\drcmd{awk} - language for processing streams of data.

* [**`bash`**](http://linux.die.net/man/1/bash)\drcmd{bash} - the Bourne-again shell.

* [**`bzip2`**](http://linux.die.net/man/1/bzip2)\drcmd{bzip2} - compress and uncompress files
using the `bzip2` algorithm.

* [**`cat`**](http://linux.die.net/man/1/cat)\drcmd{cat} - concatenate the input files to *stdout*.
\drstd{stdout}

* [**`cd`**](http://linux.die.net/man/1/cd)\drcmd{cd} - change the current directory.

* [**`chgrp`**](http://linux.die.net/man/1/chgrp)\drcmd{chgrp} - change the primary group of a file
or directory.

* [**`chmod`**](http://linux.die.net/man/1/chmod)\drcmd{chmod} - change the permissions (mode bits)
of a file or directory.

* [**`chown`**](http://linux.die.net/man/1/chown)\drcmd{chown} - change the owner of a file or
directory.

* [**`cp`**](http://linux.die.net/man/1/cp)\drcmd{cp} - copy files or directories.

* [**`crontab`**](http://linux.die.net/man/1/crontab)\drcmd{crontab} - display or edit tasks to be
run by `cron`.

* [**`curl`**](http://linux.die.net/man/1/curl)\drnet{curl} - download files from the internet.

* [**`df`**](http://linux.die.net/man/1/df)\drcmd{df} - show space utilization by file system.

* [**`diff`**](http://linux.die.net/man/1/diff)\drcmd{diff} - show the differences between files.

* [**`dig`**](http://linux.die.net/man/1/dig)\drnet{dig} - look up DNS info on an address.

* [**`dpkg`**](http://linux.die.net/man/1/dpkg)\drpkg{dpkg} - package manager for Debian flavors.

* [**`echo`**](http://linux.die.net/man/1/echo)\drcmd{echo} - display passed parameters to *stdout*.
\drstd{stdout}

* [**`email`**](http://linux.die.net/man/1/email)\drnet{email} - send email.

* [**`false`**](http://linux.die.net/man/1/false)\drcmd{false} - do nothing, unsuccessfully.

* [**`file`**](http://linux.die.net/man/1/file)\drcmd{file} - give best guess as to type of file.

* [**`find`**](http://linux.die.net/man/1/find)\drcmd{find} - find files based on various
conditions and execute actions against the results.

* [**`grep`**](http://linux.die.net/man/1/grep)\drcmd{grep} - search for a pattern (regular
expression) in files.

* [**`help`**](http://linux.die.net/man/1/help)\drdoc{help} - help for built-in commands in `bash`.

* [**`info`**](http://linux.die.net/man/1/info)\drdoc{info} - an alternative for `man`, especially
for GNU programs. Remember `q` quits.

* [**`less`**](http://linux.die.net/man/1/less)\drcmd{less}\index{files and directories!paginate!less@\texttt{less} command}\index{pagination!\texttt{less} command} - display the file one page at a time
on *stdout*.
\drstd{stdout}

* [**`ln`**](http://linux.die.net/man/1/ln)\drcmd{ln} - create hard or soft (shortcut) links.

* [**`ls`**](http://linux.die.net/man/1/ls)\drcmd{ls} - list directory contents.

* [**`lynx`**](http://linux.die.net/man/1/lynx)\drnet{lynx} - command line web browser.

* [**`man`**](http://linux.die.net/man/1/man)\drdoc{man} - display manual pages. Remember `q` quits.

* [**`mkdir`**](http://linux.die.net/man/1/mkdir)\drcmd{mkdir} - make a new directory.

* [**`more`**](http://linux.die.net/man/1/more)\drcmd{more}\index{files and directories!paginate!more@\texttt{more} command}\index{pagination!\texttt{more} command} - display the file one page at a time on
*stdout*.
\drstd{stdout}

* [**`mutt`**](http://linux.die.net/man/1/mutt)\drnet{mutt} - email client.

* [**`mv`**](http://linux.die.net/man/1/mv)\drcmd{mv} - move files or directories.

* [**`pine`**](http://linux.die.net/man/1/pine)\drnet{pine} - email client.

* [**`ps`**](http://linux.die.net/man/1/ps)\drcmd{ps} - list running processes.

* [**`pwd`**](http://linux.die.net/man/1/pwd)\drcmd{pwd} - print the current (working) directory
name.

* [**`rename`**](http://linux.die.net/man/1/rename)\drcmd{rename} - rename files in more complex
ways than `mv` can.

* [**`rm`**](http://linux.die.net/man/1/rm)\drcmd{rm} - delete (remove) files or directories.

* [**`scp`**](http://linux.die.net/man/1/scp)\drnet{scp} - file copy over secure shell protocol.

* [**`set`**](http://linux.die.net/man/1/set)\drcmd{set} - set an environment variable, or display
all environment variables.

* [**`sort`**](http://linux.die.net/man/1/sort)\drcmd{sort} - sort *stdin* or a file to *stdout*.
\drstd{stdin}
\drstd{stdout}

* [**`ssh`**](http://linux.die.net/man/1/ssh)\drnet{ssh} - secure shell terminal progam and
protocol.

* [**`tail`**](http://linux.die.net/man/1/tail)\drcmd{tail} - display the last lines of a file.

* [**`tar`**](http://linux.die.net/man/1/tar)\drcmd{tar} - "tape archive", a way to combine
directories into a single flat file.

* [**`tee`**](http://linux.die.net/man/1/tee)\drcmd{tee} - write to a file and *stdout* at the same
time.
\drstd{stdout}

* [**`telnet`**](http://linux.die.net/man/1/telnet)\drnet{telnet} - ancient terminal program and
protocol.

* [**`touch`**](http://linux.die.net/man/1/touch)\drcmd{touch} - create an empty file or change the
last-modified time of an existing file.

* [**`true`**](http://linux.die.net/man/1/true)\drcmd{true} - do nothing, successfully.

* [**`uname`**](http://linux.die.net/man/1/uname)\drcmd{uname} - print system info.

* [**`unzip`**](http://linux.die.net/man/1/unzip)\drcmd{unzip} - uncompress `.zip` files.

* [**`vi`**](http://linux.die.net/man/1/vi)\dreds{vi} - "visual" editor, a file editor.

* [**`wget`**](http://linux.die.net/man/1/wget)\drnet{wget} - download files from the internet.

* [**`whoami`**](http://linux.die.net/man/1/whoami)\drcmd{whoami} - the answer to life's most
existential question.

* [**`whois`**](http://linux.die.net/man/1/whois)\drnet{whois} - look up DNS ownership info on an
address.

* [**`xfreerdp`**](http://linux.die.net/man/1/xfreerdp)\drnet{xfreerdp} - RDP protocol client.

* [**`zip`**](http://linux.die.net/man/1/zip)\drcmd{zip} - compress files and directories using the
PKZip algorithm.

### System Commands{.unnumbered}

These are "section 8" commands, and ***may*** require special privileges such as `sudo` to run,
depending on the system. Yes, some systems restrict the use of `ping`!

* [**`apt-get`**](http://linux.die.net/man/8/apt-get)\drpkg{apt-get} - package manager for Debian
flavors.

* [**`aptitude`**](http://linux.die.net/man/8/aptitude)\drpkg{aptitude} - package manager for
Debian flavors.

* [**`cron`**](http://linux.die.net/man/8/cron)\drcmd{cron} - system for running "scheduled tasks."

* [**`dmesg`**](http://linux.die.net/man/8/dmesg)\drcmd{dmesg} - display kernel log messages.

* [**`ifconfig`**](http://linux.die.net/man/8/ifconfig)\drnet{ifconfig} - display network
(interface) configuration.

* [**`mount`**](http://linux.die.net/man/8/mount)\drcmd{mount} - mount a file system to a specific
location.

* [**`ping`**](http://linux.die.net/man/8/ping)\drnet{ping} - test for network connectivity to an
IP address.

* [**`reboot`**](http://linux.die.net/man/8/reboot)\drcmd{reboot} - restart the system.

* [**`rpm`**](http://linux.die.net/man/8/rpm)\drpkg{rpm} - package manager for Fedora flavors.

* [**`shutdown`**](http://linux.die.net/man/8/shutdown)\drcmd{shutdown} - shutdown or restart the
system.

* [**`sudo`**](http://linux.die.net/man/8/sudo)\drcmd{sudo} - execute a command with elevated
privileges.

* [**`traceroute`**](http://linux.die.net/man/8/traceroute)\drnet{traceroute} - trace the route to
an IP address.

## Examples{.unnumbered}

The following are meant to be simple, mostly "one-liner" type samples to reinforce the concepts
here and continue to show you "the UNIX philosophy" of approaching solutions in multiple small
steps.

### Keep It Simple, Stupid{.unnumbered}

Here's a good example. During the debugging of this book I kept having problems with internal links
to other parts of the generated PDF not working. Some did, some didn't. And they ***all*** worked
in epub and HTML outputs.

I had a suspicion it was because I was wrapping links from one line to the next in Markdown (trying
to keep below a certain column count), so I wanted to find all lines that had an opening square
bracket but ***not*** a closing one, e.g., I wanted to catch the first line in the following:

\drcap{Some Markdown}
```bash
See [Important System
Directories.](http://linux.die.net/abs-guide/systemdirs.html)
```

Now you could spend a long time with regular expressions trying to figure out how to do negative
matching on that closing `]`. Good luck!

Or you could do something as simple as this:

\drcap{Searching through the Markdown for mismatched brackets}
```bash
$ grep '\[' *.md | grep -v ']'
Step01.md: (( expression ))           if COMMANDS; then COMMANDS; [ elif C>
Step01.md: :                          kill [-s sigspec | -n signum | -sigs>
Step04.md:./FileCheckers/otschecker:  [ $rc != 0 -a "$pdfinfo" != "Comma...
Step04.md:./FileCheckers/pdfpwdchecker: if [ $rc != 0 -a "$pdfinfo" = "C...
```

What makes this simple? Finding `[` with the first `grep` and then simply piping it to a second
`grep` and inverting the match logic (`-v`) on `]`.

### Chain Gangs{.unnumbered}

Remembering that `&&`\index{*@\texttt{\&}\texttt{\&} (logical "and" operator)} only
executes the next command if the prior one is successful, we can do things like set up a sample
directory and (empty) files for playing around with files and directories in one fell swoop:

\drcap{Make a bunch of files and directories at once}
```bash
~ $ mkdir -p /tmp/foo/d && cd /tmp/foo && touch a b c d/e
~ $ ls
a  b  c  d
```

That is roughly equivalent to:

\drcap{Make a bunch of files the long way}
```bash
~ $ cd /tmp
~ $ mkdir -p foo
~ $ cd foo
~ $ mkdir -p d
~ $ touch a b c d/e
~ $ ls
a  b  c  d
```

### Simple Scripts{.unnumbered}

I said I wasn't going to cover scripting, especially logical constructs like `if`/`fi`\drcmd{if}.
But simple scripts that just "do things" in a certain order are within scope, and the following,
which installs [`freerdp`](https://github.com/freerdp/freerdp)\drnet{xfreerdp}, is a good example of
simply taking the guesswork out of doing something repetitive across multiple machines. I keep this
`installrdp` script in Dropbox so I can run it quickly and easily on any new machine I set up (once
I get Dropbox set up on the machine!)

\drcap{A simple install script}
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

You should be able to understand all of the above now, or know where to look to figure it out. The
only nuance we may not have covered is that at the shell prompt and in scripts both you can put a
`\` at the end of a line and it will "escape" the newline (`\r`) so you can continue the same
command on the next line. This is useful because some interactive terminals don't "wrap" well, and
it makes more readable script files, too.

And yes, in the section on package management I talked about the dangers of installing packages
directly from source. In this case, though, `freerdp` in the Mint repositories is lagging far
enough behind the new RDP protocol version 8 support that I want to use the latest and greatest
`freerdp` from GitHub for performance reasons. But now it's up to me to track and update the
software (if I care).