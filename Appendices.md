
\renewcommand{\chaptername}{}
\renewcommand{\thechapter}{A}

# Appendices

> *"That rug really tied the room together, did it not?"* - Walter Sobchak (*The Big Lebowski*)

## Cheat Sheet{.unnumbered}

This list outlines all the commands, files and other UNIX items of interest brought up in this
book. Use `man` or other methods outlined in the book to find more information on them.

### Environment Variables{.unnumbered}

* [**`$?`**](http://linux.die.net/abs-guide/exit-status.html) - the exit code for the last command
or program executed.
\index{*@\texttt{?} (exit status environment variable)}
\index{environment variables!\?@\texttt{\$}\texttt{?} (exit status code)}

* [**`$HISTIGNORE`**](http://linux.die.net/man/1/sh) - a colon-separated list of patterns to keep
from being recorded in the command history file.
\drenv{HISTIGNORE}{commands to ignore in command history}

* [**`$PATH`**](http://linux.die.net/Bash-Beginners-Guide/sect_03_02.html) - the execution search
path.
\drenv{PATH}{execution search path}

### Conditional Execution{.unnumbered}

See ["logical operators"](http://linux.die.net/abs-guide/ops.html).

* **`&&`** - execute the second command only if the first command succeeds.
\index{*@\texttt{\&}\texttt{\&} (logical "and" operator)}

* **`||`** - execute the second command even if the first command fails.
\index{*@\texttt{"|"|} (logical "or" operator)}

### Redirection{.unnumbered}

See ["I/O Redirection"](http://linux.die.net/abs-guide/io-redirection.html).

* ***stderr*** - file descriptor 2, always open for writing from a process, defaults to the screen
on a terminal session.
\drstd{stderr}

* ***stdin*** - file descriptor 0, always open for reading in a process, defaults to the keyboard
input on a terminal session.
\drstd{stdin}

* ***stdout*** - file descriptor 1, always open for writing from a process, defaults to the screen
on a terminal session.
\drstd{stdout}

* **`<`** - redirect a file to *stdin*.
\drstd{stdin}
\index{*@\texttt{<} (input redirection)}
\index{I/O!redirection!input (\texttt{<})}

* **`>`** - redirect *stdout* to a file.
\drstd{stdout}
\index{*@\texttt{>} (output redirection)}
\index{I/O!redirection!output (\texttt{>})}

* **`2>`** - redirect *stderr* to a file.
\drstd{stderr}
\index{*@\texttt{2>} (\textit{stderr} redirection)}
\index{I/O!redirection!error (\texttt{2>})}

* **`|`** - pipe *stdout* from one process into *stdin* in another process.
\drstd{stdin}
\drstd{stdout}
\index{*@\texttt{"|} (pipe)}
\index{I/O!redirection!pipe (\texttt{"|})}

### Special Files and Directories{.unnumbered}

* [**`~`**](http://linux.die.net/Bash-Beginners-Guide/sect_03_04.html) - shortcut for current
user's home directory.
\index{files and directories!home (\texttt{\~{}})}

* **`.bash_history`** - history of commands entered at the command prompt (also a nice example of a
hidden "dotfile").
\index{files and directories!special!bashhistory@\texttt{.bash\_history}}

### System Directories{.unnumbered}

See [Important System Directories](http://linux.die.net/abs-guide/systemdirs.html).

* **`/etc`** - configuration files location.
\index{files and directories!special!etc@\texttt{/etc/}}

* **`/home`** - "home" or user profile directories.
\index{files and directories!home (\texttt{/home/})}

* **`/proc`** - system run-time information.
\index{files and directories!special!proc@\texttt{/proc/}}

* **`/root`** - "home" directory for "root" user (system admin).
\index{files and directories!root "home" (\texttt{/root/})}

* **`/tmp`** - temporary files location.
\index{files and directories!special!tmp@\texttt{/tmp/}}

* **`/var/log`** - log files location.
\index{files and directories!special!varlog@\texttt{/var/log/}}

### Commands{.unnumbered}

These are "section 1" commands, i.e., normal user commands that typically don't require any special
privileges beyond permissions to access files and the like.

* [**`7z`**](http://linux.die.net/man/1/7z) - compress and uncompress files and directories using
the 7-zip algorithm.
\drcom{7z}

* [**`apropos`**](http://linux.die.net/man/1/apropos) - search for help on commands by pattern.
\drdoc{apropos}

* [**`awk`**](http://linux.die.net/man/1/awk) - language for processing streams of data.
\drscr{awk}

* [**`bash`**](http://linux.die.net/man/1/bash) - the Bourne-again shell.
\drscr{bash}

* [**`bzip2`**](http://linux.die.net/man/1/bzip2) - compress and uncompress files using the `bzip2`
algorithm.
\drcom{bzip2}

* [**`cat`**](http://linux.die.net/man/1/cat) - concatenate the input files to *stdout*.
\drtxt{cat}
\drstd{stdout}

* [**`cd`**](http://linux.die.net/man/1/cd) - change the current directory.
\drfnd{cd}{change directory}

* [**`chgrp`**](http://linux.die.net/man/1/chgrp) - change the primary group of a file or directory.
\drprm{chgrp}

* [**`chmod`**](http://linux.die.net/man/1/chmod) - change the permissions (mode bits) of a file or
directory.
\drprm{chmod}

* [**`chown`**](http://linux.die.net/man/1/chown) - change the owner of a file or directory.
\drprm{chown}

* [**`cmake`**](http://linux.die.net/man/1/cmake) - configure makefiles.
\drcmd{cmake}{configure makefiles}

* [**`cp`**](http://linux.die.net/man/1/cp) - copy files or directories.
\drfnd{cp}{copy}

* [**`crontab`**](http://linux.die.net/man/1/crontab) - display or edit tasks to be run by `cron`.
\drsys{crontab}{edit scheduled jobs}

* [**`curl`**](http://linux.die.net/man/1/curl) - download files from the internet.
\drnet{curl}

* [**`cut`**](http://linux.die.net/man/1/cut) - remove (cut) sections from lines.
\drtxt{cut}

* [**`df`**](http://linux.die.net/man/1/df) - show space utilization by file system.
\drfnd{df}{display file system disk space}

* [**`diff`**](http://linux.die.net/man/1/diff) - show the differences between files.
\drfnd{diff}{show differences between files}

* [**`dig`**](http://linux.die.net/man/1/dig) - look up DNS info on an address.
\drnet{dig}

* [**`dpkg`**](http://linux.die.net/man/1/dpkg) - package manager for Debian flavors.
\drpkg{dpkg}

* [**`du`** ](http://linux.die.net/man/1/du) - estimate disk usage.
\drfnd{du}{disk use by directory}

* [**`echo`**](http://linux.die.net/man/1/echo) - display passed parameters to *stdout*.
\drtxt{echo}
\drstd{stdout}

* [**`emacs`**](http://linux.die.net/man/1/emacs) - great operating system, but it could use an
editor.
\dreds{emacs}

* [**`email`**](http://linux.die.net/man/1/email) - send email.
\drnet{email}

* [**`false`**](http://linux.die.net/man/1/false) - do nothing, unsuccessfully.
\drscr{false}

* [**`file`**](http://linux.die.net/man/1/file) - give best guess as to type of file.
\drfnd{file}{detect file type}

* [**`find`**](http://linux.die.net/man/1/find) - find files based on various conditions and
execute actions against the results.
\drfnd{find}{find files}

* [**`fmt`**](http://linux.die.net/man/1/fmt) - simple text formatter.
\drtxt{fmt}

* [**`grep`**](http://linux.die.net/man/1/grep) - search for a pattern (regular expression) in
files.
\drfnd{grep}{search files}

* [**`gzip`**](http://linux.die.net/man/1/gzip) - compression program.
\drcom{gzip}

* [**`help`**](http://linux.die.net/man/1/help) - help for built-in commands in `bash`.
\drdoc{help}

* [**`if`**](http://linux.die.net/man/1/if) - conditionally execute a program.
\drscr{if}

* [**`info`**](http://linux.die.net/man/1/info) - an alternative for `man`, especially for GNU
programs. Remember `q` quits.
\drdoc{info}

* [**`latex`**](http://linux.die.net/man/1/latex) - process LaTeX document markup.
\drtxt{latex}

* [**`less`**](http://linux.die.net/man/1/less) - display the file one page at a time on *stdout*.
\drtxt{less}
\drstd{stdout}
\index{files and directories!paginate!less@\texttt{less} command}
\index{pagination!\texttt{less} command}

* [**`ln`**](http://linux.die.net/man/1/ln) - create hard or soft (shortcut) links.
\drfnd{ln}{link}

* [**`locate`**](http://linux.die.net/man/1/locate) - locate files by name.
\drfnd{locate}{locate files}

* [**`ls`**](http://linux.die.net/man/1/ls) - list directory contents.
\drfnd{ls}{list directory contents}

* [**`lynx`**](http://linux.die.net/man/1/lynx) - command line web browser.
\drnet{lynx}

* [**`make`**](http://linux.die.net/man/1/make) - run programs according to "recipes" in makefiles.
\drcmd{make}{build by recipes}

* [**`man`**](http://linux.die.net/man/1/man) - display manual pages. Remember `q` quits.
\drdoc{man}

* [**`mkdir`**](http://linux.die.net/man/1/mkdir) - make a new directory.
\drfnd{mkdir}{make directory}

* [**`more`**](http://linux.die.net/man/1/more) - display the file one page at a time on *stdout*.
\drtxt{more}
\drstd{stdout}
\index{files and directories!paginate!more@\texttt{more} command}
\index{pagination!\texttt{more} command}

* [**`mutt`**](http://linux.die.net/man/1/mutt) - email client.
\drnet{mutt}

* [**`mv`**](http://linux.die.net/man/1/mv) - move files or directories.
\drfnd{mv}{move files}

* [**`nano`**](http://linux.die.net/man/1/nano) - small, intuitive text editor.
\dreds{nano}

* [**`pandoc`**](http://pandoc.org/README.html) - markup converter. The primary tool used to create
this book in multiple formats including PDF, EPUB, HTML and Markdown.
\drcmd{pandoc}{markup converter}

* [**`pdflatex`**](http://linux.die.net/man/1/pdflatex) - create PDF files.
\drcmd{pdflatex}{create PDF files}

* [**`pico`**](http://linux.die.net/man/1/pico) - small, intuitive text editor.
\dreds{pico}

* [**`pine`**](http://linux.die.net/man/1/pine) - email client.
\drnet{pine}

* [**`ps`**](http://linux.die.net/man/1/ps) - list running processes.
\drsys{ps}{list processes}

* [**`pwd`**](http://linux.die.net/man/1/pwd) - print the current (working) directory name.
\drfnd{pwd}{print working directory}

* [**`rename`**](http://linux.die.net/man/1/rename) - rename files in more complex ways than `mv`
can.
\drfnd{rename}{rename file}

* [**`rm`**](http://linux.die.net/man/1/rm) - delete (remove) files or directories.
\drfnd{rm}{remove file}

* [**`rsync`**](http://linux.die.net/man/1/rsync) - efficiently and securely "mirror" directories
between local and remote locations.
\drnet{rsync} 

* [**`scp`**](http://linux.die.net/man/1/scp) - file copy over secure shell protocol.
\drnet{scp}

* [**`sed`**](http://linux.die.net/man/1/sed) - stream editor for editing from the command line.
\dreds{sed}

* [**`set`**](http://linux.die.net/man/1/set) - set an environment variable, or display all
environment variables.
\drcmd{set}{set shell options}

* [**`smbclient`**](http://linux.die.net/man/1/smbclient) - copy files to and from Windows using the
SMB/CIFS (Windows file share) protocol.
\drnet{smbclient}

* [**`sort`**](http://linux.die.net/man/1/sort) - sort *stdin* or a file to *stdout*.
\drtxt{sort}
\drstd{stdin}
\drstd{stdout}

* [**`ssh`**](http://linux.die.net/man/1/ssh) - secure shell terminal progam and protocol.
\drnet{ssh}

* [**`tail`**](http://linux.die.net/man/1/tail) - display the last lines of a file.
\drtxt{tail}

* [**`tar`**](http://linux.die.net/man/1/tar) - "tape archive", a way to combine directories into a
single flat file.
\drcmd{tar}{archive files}

* [**`tee`**](http://linux.die.net/man/1/tee) - write to a file and *stdout* at the same time.
\drtxt{tee}
\drstd{stdout}

* [**`telnet`**](http://linux.die.net/man/1/telnet) - ancient terminal program and protocol.
\drnet{telnet}

* [**`top`**](http://linux.die.net/man/1/top) - list processes by resource utilization (CPU).
\drsys{top}{list processes by resource use}

* [**`touch`**](http://linux.die.net/man/1/touch) - create an empty file or change the
last-modified time of an existing file.
\drfnd{touch}{change modified date or create file}

* [**`tr`**](http://linux.die.net/man/1/tr) - translate (map, convert) characters.
\drtxt{tr}

* [**`true`**](http://linux.die.net/man/1/true) - do nothing, successfully.
\drscr{true}

* [**`uname`**](http://linux.die.net/man/1/uname) - print system info.
\drsys{uname}{system info}

* [**`unzip`**](http://linux.die.net/man/1/unzip) - uncompress `.zip` files.
\drcom{unzip}

* [**`vi`**](http://linux.die.net/man/1/vi) - "visual" editor, a file editor.
\dreds{vi}

* [**`view`**](http://linux.die.net/man/1/view) - read-only version of `vim`.
\dreds{view}

* [**`vim`**](http://linux.die.net/man/1/vim) - `vi` Improved, another implementation of `vi`
allowing more customization.
\dreds{vim}

* [**`wget`**](http://linux.die.net/man/1/wget) - download files from the internet.
\drnet{wget}

* [**`which`**](http://linux.die.net/man/1/which) - determine the path of a program.
\drcmd{which}{find program}

* [**`while`**](http://linux.die.net/man/1/while) - perform a command multiple times.
\drscr{while}

* [**`whoami`**](http://linux.die.net/man/1/whoami) - the answer to life's most existential
question.
\drcmd{whoami}{existential question}

* [**`whois`**](http://linux.die.net/man/1/whois) - look up DNS ownership info on an address.
\drnet{whois}

* [**`xfreerdp`**](http://linux.die.net/man/1/xfreerdp) - RDP protocol client.
\drnet{xfreerdp}

* [**`zip`**](http://linux.die.net/man/1/zip) - compress files and directories using the PKZip
algorithm.
\drcom{zip}

### System Commands{.unnumbered}

Most of these are "section 8" commands, and ***may*** require special privileges such as `sudo` to
run, depending on the system. Yes, some systems restrict the use of `ping`!

* [**`apt-get`**](http://linux.die.net/man/8/apt-get) - package manager for Debian flavors.
\drpkg{apt-get}

* [**`aptitude`**](http://linux.die.net/man/8/aptitude) - package manager for Debian flavors.
\drpkg{aptitude}

* [**`cron`**](http://linux.die.net/man/8/cron) - system for running "scheduled tasks."
\drsys{cron}{run scheduled jobs}

* [**`dmesg`**](http://linux.die.net/man/8/dmesg) - display kernel log messages.
\drsys{dmesg}{display kernel log}

* [**`ifconfig`**](http://linux.die.net/man/8/ifconfig) - display network (interface) configuration.
\drnet{ifconfig}

* [**`kill`**](http://linux.die.net/man/1/kill) - terminate a process.
\drsys{kill}{terminate process}

* [**`mount`**](http://linux.die.net/man/8/mount) - mount a file system to a specific location.
\drsys{mount}{mount file system}

* [**`pacman`**](https://www.archlinux.org/pacman/pacman.8.html) - package manager for Arch Linux.
^[Not to be confused with the game. <http://linux.die.net/man/1/pacman>]
\drpkg{pacman}

* [**`passwd`**](http://linux.die.net/man/1/passwd) - change password.
\drsys{passwd}{change password}

* [**`ping`**](http://linux.die.net/man/8/ping) - test for network connectivity to an IP address.
\drnet{ping}

* [**`reboot`**](http://linux.die.net/man/8/reboot) - restart the system.
\drsys{reboot}{reboot system}

* [**`rpm`**](http://linux.die.net/man/8/rpm) - package manager for Fedora flavors.
\drdis{Fedora}
\drdis{Red Hat}
\drpkg{rpm}

* [**`shutdown`**](http://linux.die.net/man/8/shutdown) - shutdown or restart the system.
\drsys{shutdown}{shutdown or reboot system}

* [**`sudo`**](http://linux.die.net/man/8/sudo) - execute a command with elevated privileges.
\drsys{sudo}{execute as another user}

* [**`traceroute`**](http://linux.die.net/man/8/traceroute) - trace the route to an IP address.
\drnet{traceroute}

* [**`yum`**](https://www.centos.org/docs/4/html/yum/) - package manager for CentOS, originally
created for Yellow Dog Linux ("Yellow dog Updater, Modified").
\drdis{CentOS}
\drdis{Yellow Dog}
\drpkg{yum}

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

Remembering that `&&` only executes the next command if the prior one is successful, we can do
things like set up a sample directory and (empty) files for playing around with files and
directories in one fell swoop:
\index{*@\texttt{\&}\texttt{\&} (logical "and" operator)}

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

I said I wasn't going to cover scripting, especially logical constructs like `if`/`fi`. But simple
scripts that just "do things" in a certain order are within scope, and the following, which installs [`freerdp`](https://github.com/freerdp/freerdp), is a good example of simply taking the
guesswork out of doing something repetitive across multiple machines. I keep this `installrdp`
script in Dropbox so I can run it quickly and easily on any new machine I set up (once I get
Dropbox set up on the machine!)
\drscr{if}
\drnet{xfreerdp}

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