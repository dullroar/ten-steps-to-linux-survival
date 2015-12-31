
# File Under "Directories"

***`ls`, `mv`, `cp`, `rm` (`-rf *`), `cat`, `chmod`/`chgrp`/`chown` and
everyone's favorite, `touch`.***

> *"I'm in the phone book! I'm somebody now!"* - Navin Johnson (*The Jerk*)

Typically in Linux we are scripting and otherwise moving around files. The file system under the
covers may be one of any number of supported formats, including:

* [**btrfs**](https://en.wikipedia.org/wiki/Btrfs)

* [**ext2**](https://en.wikipedia.org/wiki/Ext2)

* [**ext3**](https://en.wikipedia.org/wiki/Ext3)

* [**ext4**](https://en.wikipedia.org/wiki/Ext4),

* [**ReiserFS**](https://en.wikipedia.org/wiki/ReiserFS)

* [**ZFS**](https://en.wikipedia.org/wiki/ZFS)

* **...and so many more!** - NTFS, FAT, CDFS, etc.

Each has its strengths and weaknesses. While Linux tends to treat the ext* file systems as
preferred, it can write to a lot of file systems and can read even more.

As mentioned before, the biggest differences between Linux and Windows
\drios{Windows}
is that the Linux environments do not have a concept of "drive letters." Instead everything is
"mounted" under a single hierarchy that starts at the "root directory" or
`/`:
\index{*@\texttt{/} (root directory)}\index{files and directories!root (\texttt{/})}

\drcap{Listing of the root directory}
```bash
~ $ ls /
bin    dev   home        lib64       mnt    Other  run   sys  var
boot   Docs  initrd.img  lost+found  Music  proc   sbin  tmp  vmlinuz
cdrom  etc   lib         media       opt    root   srv   usr
```

The root file system may be backed by a disk device, memory or even the network. It will have one
or more directories under it. Multiple physical drives and network locations can be "mounted"
virtually anywhere, under any directory or subdirectory in the hierarchy.

**Note:** Dynamically mounted devices like USB drives and DVDs are often mounted automatically
under either a `/mnt` or `/media` directory.

## Looking at Files{.unnumbered}

As we've already seen, the command to *list* the contents of a directory is
[`ls`](http://linux.die.net/man/1/ls):\drfnd{ls}{list directory contents}


\drcap{Listing directory contents}
```bash
~ $ ls
Desktop  Documents  Downloads  Music  Pictures  Public  Templates  Videos
```

Remember, "UNIX" environments think of files that start with a `.` as "hidden." If you want to see
all these
["dotfiles"](https://en.wikipedia.org/wiki/Hidden_file_and_hidden_directory#Unix_and_Unix-like_environments)
\index{files and directories!hidden (dotfiles)},
you can use `ls -a`, in this case on an average "home" directory:

\drcap{Listing a home directory showing hidden "dotfiles"}
```bash
~ $ ls -a
.              .config    .gconf           .mozilla  Templates
..             .dbus      .gnome2          Music     Videos
.bash_history  Desktop    .gnome2_private  Pictures  .xsession-errors
.bash_logout   .dmrc      .ICEauthority    .profile
.cache         Documents  .linuxmint       Public
.cinnamon      Downloads  .local           .ssh
```

Wow! That's a lot of dotfiles!

If you want to see some details for each file, use `ls -l`:

\drcap{Detailed listing of home directory}
```bash
~ $ ls -l
total 32
drwxr-xr-x 2 myuser mygroup 4096 Dec 13 18:18 Desktop
drwxr-xr-x 3 myuser mygroup 4096 Dec 13 18:22 Documents
drwxr-xr-x 2 myuser mygroup 4096 Dec 13 18:18 Downloads
drwxr-xr-x 2 myuser mygroup 4096 Dec 13 18:18 Music
drwxr-xr-x 2 myuser mygroup 4096 Dec 13 18:18 Pictures
drwxr-xr-x 2 myuser mygroup 4096 Dec 13 18:18 Public
drwxr-xr-x 2 myuser mygroup 4096 Dec 13 18:18 Templates
drwxr-xr-x 2 myuser mygroup 4096 Dec 13 18:18 Videos
```

And of course parameters can be combined, as with the two above:

\drcap{Detailed listing of home directory with "dotfiles"}
```bash
~ $ ls -al
total 112
drwxr-xr-x 21 myuser mygroup 4096 Dec 13 18:19 .
drwxr-xr-x  6 root   root    4096 Dec 13 14:24 ..
-rw-------  1 myuser mygroup  287 Dec 13 18:19 .bash_history
-rw-r--r--  1 myuser mygroup  220 Dec 13 14:24 .bash_logout
drwx------  5 myuser mygroup 4096 Dec 13 18:18 .cache
drwxr-xr-x  3 myuser mygroup 4096 Dec 13 18:18 .cinnamon
drwxr-xr-x 12 myuser mygroup 4096 Dec 13 18:18 .config
drwx------  3 myuser mygroup 4096 Dec 13 18:18 .dbus
drwxr-xr-x  2 myuser mygroup 4096 Dec 13 18:18 Desktop
-rw-------  1 myuser mygroup   29 Dec 13 18:18 .dmrc
drwxr-xr-x  3 myuser mygroup 4096 Dec 13 18:22 Documents
drwxr-xr-x  2 myuser mygroup 4096 Dec 13 18:18 Downloads
drwx------  3 myuser mygroup 4096 Dec 13 18:18 .gconf
drwx------  3 myuser mygroup 4096 Dec 13 18:18 .gnome2
drwx------  2 myuser mygroup 4096 Dec 13 18:18 .gnome2_private
-rw-------  1 myuser mygroup  668 Dec 13 18:18 .ICEauthority
drwxr-xr-x  3 myuser mygroup 4096 Dec 13 18:18 .linuxmint
drwxr-xr-x  3 myuser mygroup 4096 Dec 13 18:18 .local
drwxr-xr-x  4 myuser mygroup 4096 Dec 13 18:18 .mozilla
drwxr-xr-x  2 myuser mygroup 4096 Dec 13 18:18 Music
drwxr-xr-x  2 myuser mygroup 4096 Dec 13 18:18 Pictures
...and so on...
```

## A Brief Detour Around Parameters{.unnumbered}

In `bash` and many Linux commands in general, there are old, "short" (terse) parameter names, like
`ls -a`, and newer, longer, descriptive parameter names like `ls --all` that mean the same thing.
It is typically good to use the shorter version during interactive sessions and testing, but I
prefer long parameter names in scripts, because when I come back and look at it in two years, I may
not remember what `rm -rf *`\drfnd{rm}{remove file} means (in the "UNIX" world it means you're toast if you run
it by mistake), thus `rm --recursive --force *` seems a bit more "intuitive."

> ***The behind you save in the future by describing things well today may well be your own.*** -
> me

The older style parameters are typically preceded by a single hyphen or "switch" character:

\drcap{Short parameter}
```bash
~ $ ls -r
```

Some commands support parameters with no "switch" character at all, as with `xvf` (e***X***tract,
***V***erbose, input ***F***ile name) in the following `tar`\drcmd{tar} example:

\drcap{Alternate short parameter syntax}
```bash
~ $ tar xvf backup.tar
```

The newer "GNU-style" parameters are preceded by two hyphens and usually are quite "verbose":

\drcap{Long parameters}
```bash
~ $ ls --recursive --almost-all --ignore-backups
```

Again, it is ***highly recommended*** that you take the time to use the GNU-style parameters in
scripts as self-documenting code.

## More Poking at Files{.unnumbered}

If we suspect the file is a text file, we can echo it to the console with the
[`cat`](http://linux.die.net/man/1/cat)\drcmd{cat}
\index{files and directories!display (\texttt{cat} command)}
(*concatenate*) command:

\drcap{\texttt{cat} command}
```bash
~ $ cat installrdp
#!/bin/bash
sudo apt-get -y install git
cd ~
git clone git://github.com/FreeRDP/FreeRDP.git
cd FreeRDP
sudo apt-get -y install build-essential git-core cmake libssl-dev libx11-dev lib
xext-dev libxinerama-dev \
  libxcursor-dev libxdamage-dev libxv-dev libxkbfile-dev libasound2-dev libcups2
  -dev libxml2 libxml2-dev \
  libxrandr-dev libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev libxi-dev
   libgstreamer-plugins-base1.0-dev
sudo apt-get -y install libavutil-dev libavcodec-dev
sudo apt-get -y install libcunit1-dev libdirectfb-dev xmlto doxygen libxtst-dev
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

In this example when we `cat installrdp` we can determine it is a `bash` shell script (because the
"shebang"\index{*@\texttt{\#"!} (shebang)} is pointing to `bash`\drshl{bash}) that looks to install and configure
[FreeRDP](https://github.com/FreeRDP/FreeRDP)\drnet{xfreerdp} on a Debian-style system:

1. **`apt-get`**\drpkg{apt-get} -
Debian-style package manager.

2. **`git clone`**\drcmd{git} - cloning package from [GitHub](http://github.com).

3. **`cmake`**\drcmd{cmake} and **`make`**\drcmd{make} - configuring and building software from
source.

A better way to display a longer file is to use the
[`less`](http://linux.die.net/man/1/less)\drcmd{less}
\index{files and directories!paginate!less@\texttt{less} command}\index{pagination!\texttt{less} command}
command (which is a derivative of the original
[`more`](http://linux.die.net/man/1/more)\drcmd{more}
\index{files and directories!paginate!more@\texttt{more} command}\index{pagination!\texttt{more} command},
hence the name). `less` is a paginator, where the `Space`, `Page Down` or down arrow keys scroll
down and the `Page Up` or up arrow keys scrolls up. `Q` quits.

**Note:** The `vi`\dreds{vi} search (`/`, `?`, `n` and `p`) and navigation (`G`, `0`) keys work
within `less`, too. In general `less` is a great lightweight way to motor around in a text file
without editing it.

We can also look at just the end or *tail* of a file (often the most interesting when looking at
log files and troubleshooting a current problem) with the
[`tail`](http://linux.die.net/man/1/tail)\drcmd{tail}
\index{files and directories!display (\texttt{tail} command)}
command. The next example shows the last 10 lines of the kernel
`dmesg`
\index{files and directories!special!varlogdmesg@\texttt{/var/log/dmesg}}
\index{varlogdmesg@\texttt{/var/log/dmesg} (kernel log)}
log:

\drcap{\texttt{tail} command}
```bash
/var/log $ tail dmesg
[    3.913318] Bluetooth: BNEP socket layer initialized
[    3.914888] Bluetooth: RFCOMM TTY layer initialized
[    3.914895] Bluetooth: RFCOMM socket layer initialized
[    3.914900] Bluetooth: RFCOMM ver 1.11
[    3.935772] init: failsafe main process (732) killed by TERM signal
[    4.046700] init: cups main process (896) killed by HUP signal
[    4.046710] init: cups main process ended, respawning
[    4.186239] init: samba-ad-dc main process (919) terminated with status 1
[    4.328999] r8169 0000:02:00.0 eth0: link down
[    4.329037] IPv6: ADDRCONF(NETDEV_UP): eth0: link is not ready
```

To show a specific number of lines use the `-n` parameter with `tail`:

\drcap{Display last 15 lines of a file with \texttt{tail -n}}
```bash
/var/log $ tail -n 15 dmesg
[    3.899169] Bluetooth: HCI socket layer initialized
[    3.899170] Bluetooth: L2CAP socket layer initialized
[    3.899179] Bluetooth: SCO socket layer initialized
[    3.913306] Bluetooth: BNEP (Ethernet Emulation) ver 1.3
[    3.913309] Bluetooth: BNEP filters: protocol multicast
[    3.913318] Bluetooth: BNEP socket layer initialized
[    3.914888] Bluetooth: RFCOMM TTY layer initialized
[    3.914895] Bluetooth: RFCOMM socket layer initialized
[    3.914900] Bluetooth: RFCOMM ver 1.11
[    3.935772] init: failsafe main process (732) killed by TERM signal
[    4.046700] init: cups main process (896) killed by HUP signal
[    4.046710] init: cups main process ended, respawning
[    4.186239] init: samba-ad-dc main process (919) terminated with status 1
[    4.328999] r8169 0000:02:00.0 eth0: link down
[    4.329037] IPv6: ADDRCONF(NETDEV_UP): eth0: link is not ready
```

You can also use `tail` to with the `-f` parameter to *follow* an open file and continuously display
any new output at the end, which is useful for monitoring log files in real time:

\drcap{\texttt{tail -f} command}
```bash
/var/log $ tail -f syslog
Dec 13 19:23:40 MtLindsey dhclient: DHCPACK of 192.168.0.8 from 192.168.0.1
Dec 13 19:23:40 MtLindsey dhclient: bound to 192.168.0.8 -- renewal in 1423 seco
nds.
Dec 13 19:23:40 MtLindsey NetworkManager[960]: <info> (eth0): DHCPv4 state chang
ed renew -> renew
Dec 13 19:23:40 MtLindsey NetworkManager[960]: <info>   address 192.168.0.8
Dec 13 19:23:40 MtLindsey NetworkManager[960]: <info>   prefix 24 (255.255.255.0
)
Dec 13 19:23:40 MtLindsey NetworkManager[960]: <info>   gateway 192.168.0.1
Dec 13 19:23:40 MtLindsey NetworkManager[960]: <info>   nameserver '97.64.168.12
'
Dec 13 19:23:40 MtLindsey NetworkManager[960]: <info>   nameserver '192.119.194.
131'
Dec 13 19:23:40 MtLindsey dbus[689]: [system] Activating service name='org.freed
esktop.nm_dispatcher' (using servicehelper)
Dec 13 19:23:40 MtLindsey dbus[689]: [system] Successfully activated service 'or
g.freedesktop.nm_dispatcher'
```

Use `Ctrl-C` to cancel following the file.

If we know nothing about a *file*, we can use the
[`file`](http://linux.die.net/man/1/file)\drfnd{file}{detect file type}
command to help
us guess:

\drcap{\texttt{file} command}
```bash
~ $ file installrdp 
installrdp: Bourne-Again shell script, ASCII text executable
```

That's straightforward enough! The `file` command isn't always 100% accurate, but it is pretty good
and uses an interesting set of heuristics and a text file "database" of ["magic" number
definitions](http://linux.die.net/man/5/magic) to define how it figures out what type of file it is
examining.

**Remember:** File extensions have no real meaning per se in Linux (although some are used
especially for media and document formats), so a file name with no extension like `installrdp` is
perfectly valid. Hence the utility of the `file` command.

## Sorting Things Out{.unnumbered}

Let's say we have three files, and want to display the contents of one of them. We know we can do
that with `cat`\drcmd{cat}:

\drcap{Show contents of one file}
```bash
~ $ cd Invoices/
~/Invoices $ ls
ElevatorTrucks  FarmCombines  FarmTractors
~/Invoices $ cat ElevatorTrucks 
Truck   brakes  200
Truck   tires   400
Truck   tires   400
Truck   tires   400
Truck   winch   100
```

But what if we wanted to process all the lines in all the files in alphabetical order? Just
directing the files into a program won't do it, because the file names will be sorted by the shell
and the lines will be processed in file name order, not the ultimate sorted order of all the file
contents.

\drcap{Show contents of all three files}
```bash
~/Invoices $ cat *
Truck   brakes  200
Truck   tires   400
Truck   tires   400
Truck   tires   400
Truck   winch   100
Combine motor   1500
Combine brakes  400
Combine tires   2500
Tractor motor   1000
Tractor brakes  300
Tractor tires   2000
```

The [`sort`](http://linux.die.net/man/1/sort)\drcmd{sort}\index{sorting!\texttt{sort} command}
command to the rescue! We will see that the `sort` command can be used to not just *sort* files,
but also to merge them and remove duplicates.

\drcap{\texttt{sort} command}
```bash
~/Invoices $ sort *
Combine brakes  400
Combine motor   1500
Combine tires   2500
Tractor brakes  300
Tractor motor   1000
Tractor tires   2000
Truck   brakes  200
Truck   tires   400
Truck   tires   400
Truck   tires   400
Truck   winch   100
```

What if we want to sort by the parts column? Well, it is the second "key" field delimited by
whitespace, so:

\drcap{Sort by the second "key" column}
```bash
~/Invoices $ sort -k 2 *
Truck   brakes  200
Tractor brakes  300
Combine brakes  400
Tractor motor   1000
Combine motor   1500
Tractor tires   2000
Combine tires   2500
Truck   tires   400
Truck   tires   400
Truck   tires   400
Truck   winch   100
```

What about by the third column, the amount?

\drcap{Sort by the third column}
```bash
~/Invoices $ sort -k 3 *
Truck   winch   100
Tractor motor   1000
Combine motor   1500
Truck   brakes  200
Tractor tires   2000
Combine tires   2500
Tractor brakes  300
Combine brakes  400
Truck   tires   400
Truck   tires   400
Truck   tires   400
```

That's not what we expected because it is sorting numbers alphabetically. Let's fix that by telling
it to sort numerically:

\drcap{Sort by third column, numerically}
```bash
~/Invoices $ sort -k 3 -n *
Truck   winch   100
Truck   brakes  200
Tractor brakes  300
Combine brakes  400
Truck   tires   400
Truck   tires   400
Truck   tires   400
Tractor motor   1000
Combine motor   1500
Tractor tires   2000
Combine tires   2500
```

Maybe we care about the top three most expensive items. We haven't talked about
`pipes`\index{*@\texttt{"|} (pipe)}\index{files and directories!redirection} yet, but check
this out:

\drcap{Top three most expensive items}
```bash
~ $ sort -k 3 -n * | tail -n 3
Combine motor   1500
Tractor tires   2000
Combine tires   2500
```

Finally, what if we want only unique rows?

\drcap{Sort and show only unique rows}
```bash
~/Invoices $ sort -k 3 -n -u *
Truck   winch   100
Truck   brakes  200
Tractor brakes  300
Truck   tires   400
Tractor motor   1000
Combine motor   1500
Tractor tires   2000
Combine tires   2500
```

Just to reinforce long parameters, the last example is equivalent to:

\drcap{Sort unique rows using long parameter names}
```bash
~/Invoices $ sort --key 3 --numeric-sort --unique *
Truck   winch   100
Truck   brakes  200
Tractor brakes  300
Truck   tires   400
Tractor motor   1000
Combine motor   1500
Tractor tires   2000
Combine tires   2500
```

If you read that command in a script file, there would be little confusion as to what it was doing.

## Rearranging Deck Chairs{.unnumbered}

We can copy, move (or rename - same thing) and delete files and directories. To *copy*, simply use
the [`cp`](http://linux.die.net/man/1/cp)\drfnd{cp}{copy}
command:

\drcap{\texttt{cp} command}
```bash
~ $ cp diary.txt diary.bak
```

You can copy entire directories recursively:

\drcap{Copying directories recursively}
```bash
~ $ cp -r thisdir thatdir
```

Or, if we want to be self-documenting in a script, we can use those long parameter names again:

\drcap{\texttt{cp} command with long parameter names}
```bash
~ $ cp --recursive thisdir thatdir
```

To *move* use
[`mv`](http://linux.die.net/man/1/mv):\drfnd{mv}{move files}

\drcap{\texttt{mv} command}
```bash
~ $ mv thismonth.log lastmonth.log
```

**Note:** There is no semantic difference between "move" and "rename." However, there are some
really cool renaming scenarios that the [`rename`](http://linux.die.net/man/1/rename)\drfnd{rename}{rename file}
command can take care of beyond `mv`, like renaming all file extensions from `.htm` to `.html`.

## Making Files Disappear{.unnumbered}

To delete or *remove* a file you use
[`rm`](http://linux.die.net/man/1/rm):\drfnd{rm}{remove file}

\drcap{\texttt{rm} command}
```bash
~ $ rm desktop.ini
```

**Pro Tip:** There is no "Are you sure?" prompt when removing a single file specified with no
wildcards, or even ***all*** files with a wildcard, and there is no "Recycle Bin" or "Trash Can"
when working from the command prompt, so ***BE CAREFUL!***

The following scenario can happen ***way*** too often, even to experienced system administrators.
Note the accidental space between `*` and `.bak` on the `rm` command:

\drcap{Oops!}
```bash
~ $ cd MyDissertation/
~/MyDissertation $ ls
Bibliography.bak  Bibliography.doc  Dissertation.bak  Dissertation.doc
~/MyDissertation $ rm * .bak
rm: cannot remove ‘.bak’: No such file or directory
~/MyDissertation $ ls
~/MyDissertation $ 
```

So, in order, our hapless user:

1. Changed to directory `MyDissertation`.

2. Listed the directory contents with `ls`, saw the combination of `.doc` and `.bak` files.

3. Decided to delete the `.bak` files with `rm`, but accidentally typed in a space between the
wildcard `*` and the `.bak`. Note ominous warning message.

4. Presto! `ls` shows ***everything*** is gone, not just the backup files! The user's priorities
just got rearranged as they go hunting for another copy of their dissertation.

So be careful out there! This is an example where tab completion can be an extra error check. Many
times I use command history in these cases by changing the `ls` to look for just the files I want
to delete:

\drcap{First make sure we are dealing with the right files}
```bash
~ $ ls *.bak
Citations.bak  Dissertation.bak
```

Then I use the "up arrow" to bring back the `ls` command and change `ls` to `rm` before running it.
Safer that way.

## `touch` Me{.unnumbered}

We just learned how to make a file disappear. We can also make a file magically appear, just by
[`touch`](http://linux.die.net/man/1/touch):\drfnd{touch}{change modified date or create file}

\drcap{\texttt{touch} command}
```bash
~ $ touch NewEmptyDissertation.doc
~ $ ls -l
total 0
-rw-rwxr--+ 1 myuser mygroup 0 Oct 19 14:12 NewEmptyDissertation.doc
```

Notice the newly created file is zero bytes long.

Interestingly enough, we can also use `touch` just to update the "last modified date" of an
existing file, as you can see in time change in the following listing after running
`touch`\drfnd{touch}{change modified date or create file} on the same
file again:

\drcap{A second \texttt{touch}}
```bash
~ $ touch NewEmptyDissertation.doc
~ $ ls -l
total 0
-rw-rwxr--+ 1 myuser mygroup 0 Oct 19 14:14 NewEmptyDissertation.doc
```

It can be useful (but also distressing from a forensics point of view) to set the last modified
date of a file to a specific date and time, which
`touch`\index{files and directories!set last modified date (\texttt{touch} command)} also allows
you to do, in this case to the night before Christmas:

\drcap{Set file modified date to a specific date and time}
```bash
~ $ touch -t 201412242300 NewEmptyDissertation.doc
~ $ ls -l
total 0
-rw-rwxr--+ 1 myuser mygroup 0 Dec 24  2014 NewEmptyDissertation.doc
```

To *make a directory* you use
[`mkdir`](http://linux.die.net/man/1/mkdir):\drfnd{mkdir}{make directory}

\drcap{\texttt{mkdir} command}
```bash
~ $ cd Foo
~/Foo $ ls -l
total 4
-rw-r--r-- 1 myuser mygroup    0 Dec 14 05:49 a
-rw-r--r-- 1 myuser mygroup    0 Dec 14 05:49 b
-rw-r--r-- 1 myuser mygroup    0 Dec 14 05:49 c
drwxr-xr-x 2 myuser mygroup 4096 Dec 14 05:49 d
~/Foo $ mkdir Bar
~/Foo $ ls -l
total 8
-rw-r--r-- 1 myuser mygroup    0 Dec 14 05:49 a
-rw-r--r-- 1 myuser mygroup    0 Dec 14 05:49 b
drwxr-xr-x 2 myuser mygroup 4096 Dec 14 14:49 Bar
-rw-r--r-- 1 myuser mygroup    0 Dec 14 05:49 c
drwxr-xr-x 2 myuser mygroup 4096 Dec 14 05:49 d
```

Typically you need to create all intervening directories before creating a "child" directory:

\drcap{\texttt{mkdir} error}
```bash
~ $ mkdir Xyzzy/Something
mkdir: cannot create directory ‘Xyzzy/Something’: No such file or directory
```

But of course you can override that behavior:

\drcap{Make multiple intervening directories at once}
```bash
~/Foo $ mkdir --parents Xyzzy/Something
~/Foo $ ls 
a  b  Bar  c  d  Xyzzy
~/Foo $ ls Xyzzy
Something
```

## Navigating Through Life{.unnumbered}

Ever notice that "life" is an anagram for "file"? Spooky, eh?

Given that the UNIX-style file systems are hierarchical in nature they are similar to navigate as
with `CMD.EXE`\drshl{CMD.EXE}. The biggest difference is the absense of drive letters and the
direction of the slashes.

To *change directories*, simply use
[`cd`](http://linux.die.net/man/1/cd)\drfnd{cd}{change directory}
much like in Windows:

\drcap{\texttt{cd} command}
```bash
~ $ cd /etc
~ $ pwd
/etc
```

[`pwd`](http://linux.die.net/man/1/pwd)\drfnd{pwd}{print working directory}
simply *prints the working (current) directory*. If `whoami` tells you who you are, `pwd` tells you
***where*** you are.

In Linux, users can have "home"\index{files and directories!home (\texttt{\~{}})}
directories (similar to Windows profiles), typically located under `/home/<username>` for normal
users, and `/root` for the "root" (admin) id. To change to a user's "home" directory, simply use
`cd`\drfnd{cd}{change directory} with no parameters:

\drcap{Change to home directory}
```bash
/etc $ cd
~ $ pwd
/home/myuser
```

The tilde
(`~`)\index{*@\texttt{\~{}} (home directory)}
\index{files and directories!home (\texttt{\~{}})}
character is an alias for the current user's home directory. The following example is equivalent to
above:

\drcap{Alternative way to change to home directory}
```bash
/etc $ cd ~
~ $ pwd
/home/myuser
```

More useful is that the tilde can be combined with a user name to specify the home directory of
***another*** user:

\drcap{Change to the home directory of another user}
```bash
~ # cd ~myuser
myuser # pwd
/home/myuser
```

**Note:** The above assumes you have permissions to `cd`\drfnd{cd}{change directory} into `/home/myuser`. See the upcoming
section on file permissions for more info.

In addition, you need to know the difference between "absolute" and
"relative" paths:

* **Absolute path**\index{files and directories!absolute path} - ***always*** "goes through" or
specifies the "root"
(`/`)\index{*@\texttt{/} (root directory)}\index{files and directories!root (\texttt{/})}
directory, e.g. regardless of the current working directory, `cd /etc` will change it to `/etc`.

* **Relative path**\index{files and directories!relative path} - does ***not*** specify the root
directory, and expects to start the navigation at the current directory with all path components
traversed from there, e.g., `cd Dissertations` changes the current directory to a subdirectory
called `Dissertations`.

Windows inherited the concept of `.`
\index{*@\texttt{.} (current directory)}\index{files and directories!current directory (\texttt{.})}
for the current directory and `..`
\index{*@\texttt{..} (parent directory)}\index{files and directories!parent directory (\texttt{..})}
for the parent directory directly from UNIX. Consider the following examples that combine all of
the above about relative paths and see if it makes sense:

\drcap{Relative paths exercise}
```bash
~/Foo $ ls
~/Foo $ mkdir Bar Baz
~/Foo $ ls
Bar  Baz
~/Foo $ cd Bar
~/Foo/Bar $ touch a b c
~/Foo/Bar $ ls
a  b  c
~/Foo/Bar $ cd ../Baz
~/Foo/Baz $ touch d e f
~/Foo/Baz $ ls
d  e  f
~/Foo/Baz $ ls ..
Bar  Baz
~/Foo/Baz $ ls ../Bar
a  b  c
```

Did you notice how both `mkdir`\drfnd{mkdir}{make directory} and `touch`\drfnd{touch}{change modified date or create file} allow for specifying multiple
directory and file names in the same command?

## May I?{.unnumbered}

Most "UNIX" file systems come with a set of nine
permissions
\index{files and directories!permissions}
that can be thought of as a "grid" of 3x3 showing "who has what?" The "who" is known as "UGO":

* **User** - the user that is the "owner" of the file or directory.

* **Group** - the group that is the "owner" of the file or directory.

* **Other** - everyone else.

The "what" is:

* **Read**

* **Write**

* **Execute** - for files, for directories this means "navigate" or "list contents".

The combination of "who has what?" is usually shown in detailed directory
listings by a set of ten characters, with the first one determining
whether an entry is a directory (`d`) or a file (`-`):
\drbsd{FreeBSD}

\drcap{Another \texttt{ls -l} example, this time on FreeBSD}
```bash
% ls -l /etc
total 1876
drwxr-xr-x   2 root  wheel        512 Jan 15  2009 X11
-rw-r--r--   1 root  wheel          0 Sep  3  2013 aliases
-rw-r--r--   1 root  wheel      16384 Sep  3  2013 aliases.db
-rw-r--r--   1 root  wheel        210 May  6  2009 amd.map
-r--r--r--   1 root  wheel        233 Feb 15  2007 amd.map.snap
-rw-r--r--   1 root  wheel       1234 May  6  2009 apmd.conf
-rw-r--r--   1 root  wheel        231 May  6  2009 auth.conf
drwxr-xr-x   2 root  wheel        512 May  6  2009 bluetooth
-rw-r--r--   1 root  wheel        737 Mar 19  2015 crontab
-rw-r--r--   1 root  wheel        108 May  6  2009 csh.cshrc
-rw-r--r--   1 root  wheel        617 Apr 15  2009 csh.login
-rw-r--r--   1 root  wheel        110 May  6  2009 csh.logout
-rw-r--r--   1 root  wheel        565 May  6  2009 ddb.conf
drwxr-xr-x   2 root  wheel        512 May  6  2009 defaults
-rw-r--r--   1 root  wheel       9779 May  6  2009 devd.conf
-rw-r--r--   1 root  wheel       2071 May  6  2009 devfs.conf
-rw-r--r--   1 root  wheel        267 May  6  2009 dhclient.conf
-rw-r--r--   1 root  wheel       5704 May  6  2009 disktab
-rw-rw-r--   1 root  operator       0 Nov  3  2005 dumpdates
drwxr-xr-x   6 root  staff        512 Nov 12  2014 fail2ban
-rw-r--r--   1 root  wheel        142 May  6  2009 fbtab
...and so on...
```

In the above, for example, we can see that the user `root` owns the file `aliases` while the
`wheel` group is the primary group for it. `root` can both read and write the file (`rw-`) while
any user in the `wheel` group can only read it (`r--`). Any other id will also have read access
(`r--`).

Similarly we see that `defaults` is a directory (`d`) that can be read, written (new files created)
and listed by `root` (`rwx`), and read and listed by the group `wheel` and all other ids (`r-xr-x`).

Back on Linux, if we look in `/etc/init.d`\index{files and directories!special!etcinitd@\texttt{/etc/init.d/}}
where many services store their startup scripts we see:

\drcap{Listing the \texttt{/etc/init.d} directory}
```bash
~ $ ls -l /etc/init.d
total 276
-rwxr-xr-x 1 root root 2243 Apr  3  2014 acpid
-rwxr-xr-x 1 root root 2014 Feb 19  2014 anacron
-rwxr-xr-x 1 root root 4596 Apr 24  2015 apparmor
-rwxr-xr-x 1 root root 2401 Dec 30  2013 avahi-daemon
-rwxr-xr-x 1 root root 1322 Mar 30  2014 binfmt-support
-rwxr-xr-x 1 root root 4474 Sep  4  2014 bluetooth
-rwxr-xr-x 1 root root 2125 Mar 13  2014 brltty
-rwxr-xr-x 1 root root 4651 Apr  9  2014 casper
-rwxr-xr-x 1 root root  425 Jun 26 09:11 cinnamon
-rwxr-xr-x 1 root root 1919 Jan 18  2011 console-setup
-rwxr-xr-x 1 root root 2489 May  6  2012 cpufrequtils
lrwxrwxrwx 1 root root   21 Sep  7 04:00 cron -> /lib/init/upstart-job
-rwxr-xr-x 1 root root  938 Nov  1  2013 cryptdisks
-rwxr-xr-x 1 root root  896 Nov  1  2013 cryptdisks-early
-rwxr-xr-x 1 root root 3184 Apr  3  2014 cups
-rwxr-xr-x 1 root root 1961 Apr  7  2014 cups-browsed
-rwxr-xr-x 1 root root 2813 Nov 25  2014 dbus
-rwxr-xr-x 1 root root 1217 Mar  7  2013 dns-clean
lrwxrwxrwx 1 root root   21 Sep  7 04:00 friendly-recovery -> /lib/init/upstart-
job
-rwxr-xr-x 1 root root 1105 May 13  2015 grub-common
...and so on...
```

In this case all the scripts are readable, writable and executable (`rwx`) by the `root` user, and
readable and executable by the `root` group and all other users (`r-xr-x`). Later on I will explain
linked files (those that start with an `l` instead of a `-` in the detailed listing above).

To *change* the *owning* user of a file or directory (assuming you have permissions to do so), use
the [`chown`](http://linux.die.net/man/1/chown)\drcmd{chown}
\index{files and directories!permissions!\texttt{chown} command} command:

\drcap{Change file ownership}
```bash
# ls -l
total 4
-rwxr--r-- 1 root root 17 Oct 20 10:07 foo
# chown git foo
# ls -l
total 4
-rwxr--r-- 1 git root 17 Oct 20 10:07 foo
```

To *change* the primary *group*, use the
[`chgrp`](http://linux.die.net/man/1/chgrp)\drcmd{chgrp}
\index{files and directories!permissions!\texttt{chgrp} command} command:

\drcap{\texttt{chgrp} command}
```bash
# chgrp git foo
# ls -l
total 4
-rwxr--r-- 1 git git 17 Oct 20 10:07 foo
```

To *change* the various permissions or *mode* bits, you use the
[`chmod`](http://linux.die.net/man/1/chmod)\drcmd{chmod}
\index{files and directories!permissions!\texttt{chmod} command} command. It uses mnemonics of
"ugo" for user, group and "other," respectively. It also uses mnemonics of "rwx" for read, write
and execute, and `+` to add a permission and `-` to remove it. For example, to add the execute
permission for the group and remove read permission for "other":

\drcap{\texttt{chmod} command}
```bash
# chmod g+x,o-r foo
# ls -l
total 4
-rwxr-x--- 1 git git 17 Oct 20 10:07 foo
```

**Pro Tip:** To look like an old-hand UNIX hacker, you can also convert any set of "rwx"
permissions into an octal number from 0 (no permissions) to 7 (all permissions). It helps to think
of the three permissions as "binary places":

* **`r`** `= 2`^`2`^` = 4`
* **`w`** `= 2`^`1`^` = 2`
* **`x`** `= 2`^`0`^` = 1`
* **`-`** `= 0`

Some examples:

* **`---`** `= 0 + 0 + 0 = 0`
* **`r--`** `= 2`^`2`^` + 0 + 0 = 4`
* **`r-x`** `= 2`^`2`^` + 0 + 2`^`0`^` = 5`
* **`rw-`** `= 2`^`2`^` + 2`^`1`^` + 0 = 6`
* **`rwx`** `= 2`^`2`^` + 2`^`1`^` + 2`^`0`^` = 7`

Now to use octal with `chmod`, we think of the overall result we want for a file. For example, if
we want the `foo` file to be readable, writable and executable by both its owning user and group,
and not accessible at all by anyone else, we could use:

\drcap{\texttt{chmod} with lots of typing}
```bash
# chmod u+rwx,g+rwx,o- foo
# ls -l
total 4
-rwxrwx--- 1 git git 17 Oct 20 10:07 foo
```

Or we could simply convert those permissions into octal in our head and:

\drcap{\texttt{chmod} with octal like a boss}
```bash
# chmod 770 foo
# ls -l
total 4
-rwxrwx--- 1 git git 17 Oct 20 10:07 foo
```

Now you know the answer to that "How will we ever use octal in real life?" question you asked in
school!

For a script or executable file to be allowed to run, it ***must*** be marked as executable for one
of the user, group or other entries. The following should be insightful:

\drcap{Marking a file as executable}
```bash
# echo "echo Hello world" > foo
# ls -l
total 4
-rw-r--r-- 1 root root 17 Oct 20 10:07 foo
# ./foo
-bash: ./foo: Permission denied
# chmod u+x foo
# ls -l
total 4
-rwxr--r-- 1 root root 17 Oct 20 10:07 foo
# ./foo
Hello world
```

## "I'll Send You a Tar Ball"{.unnumbered}

In the Windows world, we are used to compressing and sending directories around as `.zip` files. In
Linux you can also deal with `.zip`\index{files and directories!zipfiles@\texttt{.zip} files}
\index{compression!zipfiles@\texttt{.zip} files} files,
although they don't tend to be the most common, using the
[`zip`](http://linux.die.net/man/1/zip)\drcom{zip} and
[`unzip`](http://linux.die.net/man/1/unzip)\drcom{unzip} commands:

\drcap{\texttt{zip} command}
```bash
~ $ cd Foo
~/Foo $ touch a b c
~/Foo $ mkdir d
~/Foo $ touch d/e
~/Foo $ cd ..
~ $ zip -r Foo Foo
  adding: Foo/ (stored 0%)
  adding: Foo/c (stored 0%)
  adding: Foo/b (stored 0%)
  adding: Foo/d/ (stored 0%)
  adding: Foo/d/e (stored 0%)
  adding: Foo/a (stored 0%)
~ $ ls -l Foo.zip
-rw-r--r-- 1 myuser mygroup 854 Dec 14 15:31 Foo.zip
```

\drcap{\texttt{unzip} command}
```bash
~ $ unzip Foo
Archive:  Foo.zip
replace Foo/c? [y]es, [n]o, [A]ll, [N]one, [r]ename: A
 extracting: Foo/c
 extracting: Foo/b                   
 extracting: Foo/d/e                 
 extracting: Foo/a
```

Not too exciting, but you get the drift. There is typically support for other compression
algorithms, such as the [`gzip`](http://linux.die.net/man/1/gzip)\drcom{gzip},
[`bzip2`](http://linux.die.net/man/1/bzip2)\drcom{bzip2} and
[`7z`](http://linux.die.net/man/1/7z)\drcom{7z} (7-zip) commands.

However, the "native" way to "archive" a directory's contents in "UNIX" is with
[`tar`](http://linux.die.net/man/1/tar)\drcmd{tar}, which is so old that `tar` stands for "tape
archive." Its purpose is to take virtually any directory structure and create a single output
"stream" or file of it. That is then typically ran through a compression command and the result is
called a "tarball":

\drcap{Creating a tarball}
```bash
~ $ tar cvf Foo.tar Foo/*
Foo/a
Foo/b
Foo/c
Foo/d/
Foo/d/e
~ $ ls -l Foo.tar 
-rw-r--r-- 1 myuser mygroup 10240 Dec 19 07:52 Foo.tar
~ $ gzip Foo.tar 
~ $ ls -l Foo.tar.gz 
-rw-r--r-- 1 myuser mygroup 193 Dec 19 07:52 Foo.tar.gz
```

In the `tar` command above, the parameters are `c` (create a new archive), `v` (turn on "verbose"
output) and `f` followed by the file name of the new
`.tar`\index{files and directories!tararchivefiles@\texttt{.tar} archive files} file.

**Note:** `tar` supports POSIX-style parameters (`-c`), GNU-style (`--create`), as well as the
older style (`c` with no hyphens at all), as shown in these examples. So both of the following are
also equivalent to the above:

\drcap{\texttt{tar} parameter styles}
```bash
~ $ tar -c -v -f Foo.tar Foo/*
~ $ tar --create --verbose --file=Foo.tar Foo/*
```

The use of compression commands along with `tar` is so prevalent that they've been built into `tar`
itself now as optional parameters:

\drcap{One-step tarball}
```bash
~ $ tar cvzf Foo.tgz Foo
Foo/
Foo/c
Foo/b
Foo/d/
Foo/d/e
Foo/a
~ $ ls -l Foo.tgz 
-rw-r--r-- 1 myuser mygroup 197 Dec 19 07:54 Foo.tgz
```

In this case the `z` parameter says to use `gzip`\drcom{gzip} compression, and the
`.tgz`\index{files and directories!tgzarchivefiles@\texttt{.tgz} archive files}
\index{compression!tgzfiles@\texttt{.tgz} files} file suffix means
basically "tarred and gzipped", or the equivalent to `.tar.gz` in the first example.

`tar` is used to both create and read `.tar` files. So to extract something like the above, you can
change the create (`c`) parameter to extract (`x`), like this:

\drcap{Extracting a tarball}
```bash
~ $ tar xvf Foo.tgz 
Foo/
Foo/c
Foo/b
Foo/d/
Foo/d/e
Foo/a
```

## Let's `link` Up!{.unnumbered}

In Windows there are "shortcuts," which are simply special files that the OS knows to interpret as
"go open this other file over there." There are also "hard links" that allow for different
directory entries ***in the same file system*** to point to the same physical file.

UNIX file systems also have both these types of links (which isn't surprising, given that Microsoft
got the ideas from UNIX). Both are created with the
[`ln`](http://linux.die.net/man/1/ln)\drfnd{ln}{link} command. A "soft
link"\index{files and directories!soft links} is equivalent to a Windows shortcut, and can point
to a file or a directory, and can point to anything on any mounted file system:

\drcap{Soft links example}
```bash
~ $ ls -l
total 4
-rw-r--r-- 1 myuser mygroup    0 Oct 24 15:53 a
-rw-r--r-- 1 myuser mygroup    0 Oct 24 15:53 b
-rw-r--r-- 1 myuser mygroup    0 Oct 24 15:53 c
drwxr-xr-x 2 myuser mygroup 4096 Oct 24 16:00 d
~ $ cd d
~ $ pwd
/tmp/foo/d
~ $ cd ..
~ $ ln -s a MyThesis.doc
~ $ ln -s d Dee
~ $ ls -l
total 4
-rw-r--r-- 1 myuser mygroup    0 Oct 24 15:53 a
-rw-r--r-- 1 myuser mygroup    0 Oct 24 15:53 b
-rw-r--r-- 1 myuser mygroup    0 Oct 24 15:53 c
drwxr-xr-x 2 myuser mygroup 4096 Oct 24 16:00 d
lrwxrwxrwx 1 myuser mygroup    1 Oct 24 16:40 Dee -> d
lrwxrwxrwx 1 myuser mygroup    1 Oct 24 16:40 MyThesis.doc -> a
~ $ cd Dee
~ $ pwd
/tmp/foo/Dee
```

The things to notice about this example:

1. The `-s` parameter indicates "create a *soft* link."

2. Instead of a `-` or `d`, a soft link is shown in a `ls` listing as `l` regardless of whether the
target is a file or directory. This is because a soft link doesn't "know" ***what*** the target
is - it is just a file in a directory pointing to another location. ***What*** that location is
will be determined after the link is traversed.

A "hard link"\index{files and directories!hard links} is a bit different. It can only be made
between *files* and the two files ***must be on the same file system***. That is because hard links
are actually directory entries (as opposed to files in directories) that point to the same
["inode"](https://en.wikipedia.org/wiki/Inode)\index{files and directories!inodes} on disk. From
within a single directory it is impossible to tell if there are other directories with pointers to
the same files (inodes) on disk.

\drcap{Hard links example}
```bash
~ $ ls
a  b  c  d  Dee  MyThesis.doc
~ $ ln b B
~ $ cd d
~ $ ln ../b .
~ $ ls -l
total 0
-rw-r--r-- 3 myuser mygroup 0 Oct 24 15:53 b
-rw-r--r-- 1 myuser mygroup 0 Oct 24 15:54 e
~ $ cd ..
~ $ ls -l
total 4
-rw-r--r-- 1 myuser mygroup    0 Oct 24 15:53 a
-rw-r--r-- 3 myuser mygroup    0 Oct 24 15:53 b
-rw-r--r-- 3 myuser mygroup    0 Oct 24 15:53 B
-rw-r--r-- 1 myuser mygroup    0 Oct 24 15:53 c
drwxr-xr-x 2 myuser mygroup 4096 Oct 24 16:49 d
lrwxrwxrwx 1 myuser mygroup    1 Oct 24 16:40 Dee -> d
lrwxrwxrwx 1 myuser mygroup    1 Oct 24 16:40 MyThesis.doc -> a
```

The "net net" of all the above is that now `b`, `B` and `d/b` all point to exactly the same inode,
or disk location, i.e., the exact same physical file.

### I Said "Go Away!", Dammit!{.unnumbered}

So what can possibly go wrong with links? With soft links the answer is easy - the "remote"
location being pointed to goes away or is renamed:

\drcap{Broken soft links example}
```bash
~ $ ls -l
total 4
-rw-r--r-- 1 myuser mygroup    0 Oct 24 15:53 a
-rw-r--r-- 3 myuser mygroup    0 Oct 24 15:53 b
-rw-r--r-- 3 myuser mygroup    0 Oct 24 15:53 B
-rw-r--r-- 1 myuser mygroup    0 Oct 24 15:53 c
drwxr-xr-x 2 myuser mygroup 4096 Oct 24 16:49 d
lrwxrwxrwx 1 myuser mygroup    1 Oct 24 16:40 Dee -> d
lrwxrwxrwx 1 myuser mygroup    1 Oct 24 16:40 MyThesis.doc -> a
~ $ rm a
~ $ ls -l
total 4
-rw-r--r-- 3 myuser mygroup    0 Oct 24 15:53 b
-rw-r--r-- 3 myuser mygroup    0 Oct 24 15:53 B
-rw-r--r-- 1 myuser mygroup    0 Oct 24 15:53 c
drwxr-xr-x 2 myuser mygroup 4096 Oct 24 16:49 d
lrwxrwxrwx 1 myuser mygroup    1 Oct 24 16:40 Dee -> d
lrwxrwxrwx 1 myuser mygroup    1 Oct 24 16:40 MyThesis.doc -> a
~ $ cat MyThesis.doc 
cat: MyThesis.doc: No such file or directory
```

So even though the soft link `MyThesis.doc` is still in the directory, the actual underlying file
`a` is now gone, and trying to access it via the soft link leads to the somewhat confusing "No such
file or directory" error message (*splutter* "I can see it! ***It's right there!***")

With hard links, it isn't so much a problem because of the nature of the beast. Since each hard
link is a directory (metadata) entry pointing to an inode, deleting one simply deletes that
directory entry. As long as the file has other hard links pointing to it, it "exists." Only when
the last remaining hard link is removed has it been "deleted." Let's play:

\drcap{Many hard linkes, one inode}
```bash
~ $ echo "This is b." > b
~ $ cat b
This is b.
~ $ cat B
This is b.
~ $ cat d/b
This is b.
```

So, that makes sense. We created an original file `b` by placing "This is b." in it, and then
created two hard links to it, `B` and `d/b`. We see that it has the same contents no matter how we
access it, because it is pointing to the same inode.

Can you guess how many `rm`\drfnd{rm}{remove file} commands it will take to delete the file containing "This is
b."?

\drcap{Deleting a file with many hard links}
```bash
~ $ rm b
~ $ cat b
cat: b: No such file or directory
~ $ cat B
This is b.
~ $ cat d/b
This is b.
~ $ rm B
~ $ cat d/b
This is b.
~ $ rm d/b
```

Ultimately, it takes a `rm` for every hard link to permanently delete a file.

### `mount` It? I Don't Even Know It's Name!{.unnumbered}

With all this talk that a hard link can only be on the same file system, how do you know whether
two directories are on the same file system? In Windows it's easy - that's exactly what the drive
letters are telling you. But in Linux, where everything is "mounted" under a single hierarchy
starting at `/`\index{*@\texttt{/} (root directory)}
\index{files and directories!root (\texttt{/})}, how do I know that `/var/something` and
`var/or/other` are on the same file system?

There are multiple ways to tell, actually. The easiest is with the
[`df`](http://linux.die.net/man/1/df)\drfnd{df}{display file system disk space} command:

\drcap{\texttt{df} command}
```bash
~ $ df
Filesystem                1K-blocks     Used Available Use% Mounted on
/dev/mapper/mint--vg-root 118647068 28847464  83749608  26% /
none                              4        0         4   0% /sys/fs/cgroup
udev                        1965068        4   1965064   1% /dev
tmpfs                        396216     1568    394648   1% /run
none                           5120        0      5120   0% /run/lock
none                        1981068      840   1980228   1% /run/shm
none                         102400       24    102376   1% /run/user
/dev/sda1                    240972    50153    178378  22% /boot
```

The ones of interest are the `/dev` entries, and we see that everything mounted under `/` is on one
file system, except for whatever happens to be on the file system mounted under `/boot`. So outside
of `/boot`, on this system we could hard link away to our heart's content.

**Note:** - It is (barely) beyond the scope of this book to cover the
[`mount`](http://linux.die.net/man/8/mount)\drsys{mount}{mount file system} command. I wanted to, really bad, but with
all the different file systems and device types and all the options for both it can get so complex
so fast that I decided not to. Maybe if you ask, real nice...

### I'm Seeing Double{.unnumbered}

So, both hard\index{files and directories!hard links} and soft
links\index{files and directories!soft links} can have some interesting side effects if you think
about them. For one, if you are backing things up, then you may get duplicates in your backup set.
In fact, with hard links you will, by definition, unless the backup software is very smart and
doing things like de-duplication.

But even with soft links if everything just blindly followed them you could also get duplicates
where you didn't want them, or even circular references. Also, the pointers in the soft link files
are not evaluated until a command references them. Note that the following is perfectly legal with
soft links, but may not give the results you expect - think about the current working directory
shown by `pwd`\drfnd{pwd}{print working directory} in the following, and the effects of the ***relative paths*** as the
sample progresses:

\drcap{Soft links and relative paths}
```bash
~ $ cd Foo
~/Foo $ rm -rf *
~/Foo $ cd ..
~ $ cd Foo
~/Foo $ pwd
/home/myuser/Foo
~/Foo $ rm -rf *
~/Foo $ mkdir d
~/Foo $ touch a b c d/e
~/Foo $ ln -s . d/f
~/Foo $ ls d/f
e  f
~/Foo $ ln -s .. d/g
~/Foo $ ls d/g
a  b  c  d
```

Many commands that deal with files and file systems, like `find`\drfnd{find}{find files}, have parameters
specifically telling the command whether to follow soft links or not (by default, `find` does
not - see the next chapter for more).

## What's the `diff`?{.unnumbered}

Most people think of [`diff`](http://linux.die.net/man/1/diff)\drfnd{diff}{show differences between files}
\index{files and directories!compare files (\texttt{diff} command)} as a tool only programmers find
useful, but that is short-sighted. The whole purpose of `diff` is to show differences between
files. For example, I backed up this document (which is a text file) before starting this section,
then typed this introduction to `diff`. This is what `diff` showed after I added the new paragraph:

\drcap{\texttt{diff} example}
```bash
~ $ diff Step02.bak Step02.md
1285a1286,1291
> Most people think of [`diff`](http://linux.die.net/man/1/diff) as a tool
> only programmers find useful, but that is short-sighted. The whole purpose
> of `diff` is to show differences between files. For example, I backed up
> this document (which is a text file) before starting this chapter, then
> typed this introduction to `diff`. This is what `diff` shows:
```

In other words, the "arrows" are pointing to the "new" file (by convention the file specified on
the left is the "old" file and the file on the right is the "new" file), showing five lines were
inserted, starting at line 1285. Pretty meta, but not real exciting.

Let's look at something else, say a configuration file for an application. We have an original file,
`orig.conf`:

\drcap{\texttt{orig.conf} file}
```bash
~ $ cat orig.conf
FOO=1

SOME=THINGS
STAY=THE
SAME=ALWAYS

BAR=Xyzzy
```

Then we have a new file, `new.conf`:

\drcap{\texttt{new.conf} file}
```bash
~ $ cat new.conf
FOO=2

SOME=THINGS
STAY=THE
SAME=ALWAYS
```

Now if we `diff` them:

\drcap{Using \texttt{diff} on config files}
```bash
~ $ diff orig.conf new.conf
1c1
< FOO=1
---
> FOO=2
7d6
< BAR=Xyzzy
```

Now we can more easily see that line #1 changed (`1c1`) from `FOO=1` on the "left" file to `FOO=2`
on the "right," and that line #7 was deleted (`7d6`) from the "left" file to form the "right."
Again, not too interesting, but imagine that both files were thousands of lines long, and there
were only a few changes, and you were trying to detect and recover an accidentally-deleted line.
Now you can see why `diff` can be handy, as long as you keep around a prior version either in a
backup file or version control system to compare against.

`diff` is your friend. It really comes into play with a version control system like
[`git`](http://linux.die.net/man/1/git)\drcmd{git}, but again, that is beyond the scope of this
book.