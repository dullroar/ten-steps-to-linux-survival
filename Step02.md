  
# Step 2. File Under "Directories"

***`ls`, `mv`, `cp`, `rm` (`-rf *`), `cat`, `chmod`/`chgrp`/`chown` and
everyone's favorite, `touch`.***

> *"I'm in the phone book! I'm somebody now!"* - Navin Johnson (*The Jerk*)

Typically in Linux we are scripting and otherwise moving around files. The
file system under the covers may be one of any number of supported
formats, including:

* [**ext2**](https://en.wikipedia.org/wiki/Ext2)

* [**ext3**](https://en.wikipedia.org/wiki/Ext3)

* [**ext4**](https://en.wikipedia.org/wiki/Ext4),

* [**ReiserFS**](https://en.wikipedia.org/wiki/ReiserFS)

* **...and so much more!** - NTFS, FAT, etc.

Each has its strengths and weaknesses.  While Linux tends to treat the ext*
file systems as preferred, it can write to a lot of file systems and
can read even more.

As mentioned above, the biggest differences between Linux and Windows
is that the Linux environments tend not to have a concept of "drive
letters." Instead everything is "mounted" under a single hierarchy that
starts at the "root directory" or `/`.

```bash
$ ls /
bin   etc         lib         media  proc  sbin     sys  var
boot  home        lib64       mnt    root  selinux  tmp  vmlinuz
dev   initrd.img  lost+found  opt    run   srv      usr
```

The root file system may be backed by a disk device, LUN, memory or even
the network. It will have one or more directories under it. Multiple
physical drives and network locations can be "mounted" virtually anywhere,
under any directory or subdirectory in the hierarchy.

**Note:** Dynamically mounted devices like USB drives and DVDs are often
mounted automatically under either a `/mnt` or `/media` directory.

## Looking at Files

The command to *list* the contents of a directory is the
[`ls`](http://linux.die.net/man/1/ls) command:

```bash
$ ls
Desktop    Downloads  FreeRDP     Music     Public  Temp       Videos
Documents  Dropbox    installrdp  Pictures  rdp     Templates
```

Remember, UNIX environments think of files that start with a `.` as
"hidden." If you want to see all these
["dotfiles"](https://en.wikipedia.org/wiki/Hidden_file_and_hidden_directory#Unix_and_Unix-like_environments),
you can use `ls -a`:

```bash
$ ls -a
.              Desktop        .gksu.lock       .mozilla   .themes
..             .dmrc          .gnome2          Music      .thumbnails
.adobe         Documents      .gnome2_private  Pictures   .thunderbird
.atom          Downloads      .hugin           .pki       Videos
.bash_history  .dropbox       .ICEauthority    .profile   .wine
.bash_logout   Dropbox        .icons           .ptbt1     .Xauthority
.cache         .dropbox-dist  installrdp       Public     .xinputrc
.cinnamon      .face          .lastpass        rdp        .xsession-errors
.cmake         FreeRDP        .linuxmint       .sbd
.config        .gconf         .local           Temp
.dbus          .gimp-2.8      .macromedia      Templates
```

Wow! That's a lot of dotfiles!

If you want to see some details of each file, use `ls -l`:

```bash
$ ls -l
total 92
drwxr-xr-x  2 myuser mygroup      4096 Sep  7 04:16 Desktop
drwxr-xr-x  2 myuser mygroup      4096 Oct 13 10:02 Documents
drwxr-xr-x  2 myuser mygroup      4096 Oct 14 09:45 Downloads
drwx------  8 myuser mygroup      4096 Oct 16 19:58 Dropbox
drwxr-xr-x 19 myuser mygroup      4096 Oct 12 09:48 FreeRDP
-rwxr-x---  1 myuser sambashare    883 Oct 12 11:34 installrdp
drwxr-xr-x  5 myuser mygroup      4096 Oct 16 10:47 LightTable
drwxr-xr-x  2 myuser mygroup      4096 Sep  7 04:16 Music
drwxr-xr-x  3 myuser mygroup     36864 Oct 12 17:29 Pictures
drwxr-xr-x  2 myuser mygroup      4096 Sep  7 04:16 Public
-rwxr-xr-x  1 myuser mygroup       816 Oct 15 18:00 rdp
...and so on...
```

And of course parameters can be combined, as with the two above:

```bash
$ ls -al
total 344
drwxr-xr-x 40 myuser mygroup      4096 Oct 17 07:14 .
drwxr-xr-x  3 root   root         4096 Sep  7 04:09 ..
drwx------  3 myuser mygroup      4096 Sep  7 09:33 .adobe
drwxr-xr-x  5 myuser mygroup      4096 Oct 12 15:48 .atom
-rw-------  1 myuser mygroup      6428 Oct 17 06:11 .bash_history
-rw-r--r--  1 myuser mygroup       220 Sep  7 04:09 .bash_logout
drwx------ 18 myuser mygroup      4096 Oct 13 07:31 .cache
drwxr-xr-x  5 myuser mygroup      4096 Oct 16 19:57 .cinnamon
drwxr-xr-x  3 myuser mygroup      4096 Oct 12 09:45 .cmake
drwxr-xr-x 26 myuser mygroup      4096 Oct 15 10:23 .config
drwx------  3 myuser mygroup      4096 Sep  7 04:16 .dbus
...and so on...
```

## A Brief Detour Around Parameters

In `bash` and many Linux commands in general, there are old, "short"
(terse) parameter names, like `ls -a`, and newer, longer, descriptive
parameter names like `ls --all` that mean the same thing. It is typically
good to use the shorter version during interactive sessions and testing,
but I prefer long parameter names in scripts, because when I come back
and look at it in two years, I may not remember what `rm -rf *` means
(in the *IX world it means you're toast if you run it in the wrong
directory by mistake), thus `rm --recursive --force *` seems a bit more
"intuitive."

> ***The behind you save in the future by describing things well today
> may well be your own.*** - me

The older style parameters are typically preceded by a single hyphen
"switch" character:

```bash
ls -r
```

Or even no "switch" character at all, as with `xvf` (e***X***tract,
***V***erbose, input ***F***ile name) in the following:

```bash
tar xvf backup.tar
```

The newer "GNU-style" parameters are preceded by two hyphens and usually
are quite "verbose":

```bash
ls --recursive --almost-all --ignore-backups
```

Again, it is ***highly recommended*** that you take the time to use the
GNU-style parameters in scripts as self-documenting code.

## More Poking at Files

If we suspect the file is a text file, we can echo it to the console
with the [`cat`](http://linux.die.net/man/1/cat) (*concatenate*) command:

```bash
$ cat installrdp 
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

We can determine from the above that `installrdp` is a `bash` shell script
that looks to install and configure
[FreeRDP](https://github.com/FreeRDP/FreeRDP) on a Debian-style system:

1. **`apt-get`** - Debian-style package manager.

2. **`git clone`** - cloning package from [GitHub](http://github.com).

3. **`cmake`** and **`make`** - configuring and building software from
source.

A better way to display a longer file is to use the
[`less`](http://linux.die.net/man/1/less) command (which is a derivative of
the original [`more`](http://linux.die.net/man/1/more), hence the name).
`less` is a paginator, where the `Space`, `Page Down` or down arrow keys
scroll down and the `Page Up` or up arrow keys scrolls up. `Q` quits.

**Note:** The `vi` search (`/`, `?`, `n` and `p`) and navigation (`G`, `0`)
keys work within `less`, too. In general `less` is a great lightweight way
to motor around in a text file without editing it.

We can also look at just the end or *tail* of a file (often the most
interesting when looking at log files and troubleshooting a current
problem) with the [`tail`](http://linux.die.net/man/1/tail) command. To
show the last 10 lines of the kernel `dmesg` log:

```bash
# tail dmesg
[    2.774931] loop: module loaded
[    3.349880] eth0: intr type 3, mode 0, 3 vectors allocated
[    3.351331] eth0: NIC Link is Up 10000 Mbps
[    3.422647] RPC: Registered named UNIX socket transport module.
[    3.422649] RPC: Registered udp transport module.
[    3.422650] RPC: Registered tcp transport module.
[    3.422651] RPC: Registered tcp NFSv4.1 backchannel transport module.
[    3.432437] FS-Cache: Loaded
[    3.443980] FS-Cache: Netfs 'nfs' registered for caching
[    3.449794] Installing knfsd (copyright (C) 1996 okir@monad.swb.de).
```

To show the last 20 lines:

```bash
# tail -n 20 dmesg
[    2.317838] [drm] Fifo max 0x00040000 min 0x00001000 cap 0x0000077f
[    2.318843] [drm] Supports vblank timestamp caching Rev 1 (10.10.2010).
[    2.318845] [drm] No driver support for vblank timestamp query.
[    2.318914] [drm] Screen objects system initialized
[    2.318917] [drm] Detected no device 3D availability.
[    2.323011] [drm] Initialized vmwgfx 2.4.0 20120209 for 0000:00:0f.0 ...
[    2.486733] input: ImPS/2 Generic Wheel Mouse as /devices/platform/i8...
[    2.655694] Adding 4191228k swap on /dev/sda5.  Priority:-1 extents:1...
[    2.666714] EXT4-fs (sda1): re-mounted. Opts: (null)
[    2.754699] EXT4-fs (sda1): re-mounted. Opts: errors=remount-ro
[    2.774931] loop: module loaded
[    3.349880] eth0: intr type 3, mode 0, 3 vectors allocated
[    3.351331] eth0: NIC Link is Up 10000 Mbps
[    3.422647] RPC: Registered named UNIX socket transport module.
[    3.422649] RPC: Registered udp transport module.
[    3.422650] RPC: Registered tcp transport module.
[    3.422651] RPC: Registered tcp NFSv4.1 backchannel transport module.
[    3.432437] FS-Cache: Loaded
[    3.443980] FS-Cache: Netfs 'nfs' registered for caching
[    3.449794] Installing knfsd (copyright (C) 1996 okir@monad.swb.de).
```

You can also use `tail` to *follow* an open file and continuously display
any new output at the end, which is useful for monitoring log files in real
time:

```bash
# tail -f dmesg
[    2.774931] loop: module loaded
[    3.349880] eth0: intr type 3, mode 0, 3 vectors allocated
[    3.351331] eth0: NIC Link is Up 10000 Mbps
[    3.422647] RPC: Registered named UNIX socket transport module.
[    3.422649] RPC: Registered udp transport module.
[    3.422650] RPC: Registered tcp transport module.
[    3.422651] RPC: Registered tcp NFSv4.1 backchannel transport module.
[    3.432437] FS-Cache: Loaded
[    3.443980] FS-Cache: Netfs 'nfs' registered for caching
[    3.449794] Installing knfsd (copyright (C) 1996 okir@monad.swb.de).
...new lines will appear here over time...
```

If we know nothing about a *file*, we can use the
[`file`](http://linux.die.net/man/1/file) command to help us guess:

```bash
$ file installrdp 
installrdp: Bourne-Again shell script, ASCII text executable
```

That's straightforward enough! The `file` command isn't always 100%
accurate, but it is pretty good and uses an interesting set of heuristics
and a text file "database" of
["magic" number definitions](http://linux.die.net/man/5/magic) to define
how it figures out what type of file it is examining.

**Remember:** File extensions have no real meaning per se in Linux
(although some are used, especially for media and document formats), so
a file name with no extension like `installrdp` is perfectly valid. Hence
the utility of the `file` command.

## Sorting Things Out

The [`sort`](http://linux.die.net/man/1/sort) command can be used to not
just *sort* files, but also to merge them and remove duplicates.

Let's say we have three files:

```bash
$ ls
ElevatorTrucks  FarmCombines  FarmTractors
```

Here are the contents of each:

```bash
$ cat ElevatorTrucks
Truck   brakes  200
Truck   tires   400
Truck   tires   400
Truck   tires   400
Truck   winch   100

$ cat FarmCombines
Combine motor   1500
Combine brakes  400
Combine tires   2500

$ cat FarmTractors
Tractor motor   1000
Tractor brakes  300
Tractor tires   2000
```

But what if we wanted to process all the lines in all the files in a single
alphabetical order? Just redirecting the files into a program won't do it,
because the file names will be sorted by the shell and the lines will be
processed in file name order, not the ultimate sorted order of all the file
contents:

```bash
$ cat *
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

The `sort` command to the rescue!

```bash
$ sort *
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

What if we want to sort by the parts column? Well, it is the second "key"
field delimited by whitespace, so:

```bash
$ sort -k 2 *
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

```bash
$ sort -k 3 *
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

That's not what we expected because it is sorting numbers alphabetically.
Let's fix that by telling it to sort numerically:

```bash
$ sort -k 3 -n *
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

Maybe we care about the top three most expensive items. We haven't talked
about pipes yet, but check this out:

```bash
$ sort -k 3 -n * | tail -n 3
Combine motor   1500
Tractor tires   2000
Combine tires   2500
```

Finally, what if we want only unique rows?

```bash
$ sort -k 3 -n -u *
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

```bash
$ sort --key 3 --numeric-sort --unique *
Truck   winch   100
Truck   brakes  200
Tractor brakes  300
Truck   tires   400
Tractor motor   1000
Combine motor   1500
Tractor tires   2000
Combine tires   2500
```

## Rearranging Deck Chairs

We can copy, move or rename (same thing) and delete files and
directories. To *copy*, simply use the
[`cp`](http://linux.die.net/man/1/cp) command:

```bash
$ cp diary.txt diary.bak
```

You can copy entire directories recursively:

```bash
$ cp -r thisdir thatdir
```

Or, if we want to be self-documenting in a script, we can use those long
parameter names:

```bash
$ cp --recursive thisdir thatdir
```

To *move* use [`mv`](http://linux.die.net/man/1/mv):

```
$ mv thismonth.log lastmonth.log
```

**Note:** There is no semantic difference between "move" and "rename."
However, there are some really cool renaming scenarios that the
[`rename`](http://linux.die.net/man/1/rename) command can take care of
beyond `mv`, like renaming all file extensions from `.htm` to `.html`.

## Making Files Disappear

To delete or *remove* a file you use [`rm`](http://linux.die.net/man/1/rm):

```bash
$ rm desktop.ini
```

**Pro Tip:** There is no "Are you sure?" prompt when removing a single file
specified with no wildcards, or even all files with a wildcard, and there
is no "Recycle Bin" or "Trash Can" when working from the command prompt, so
be careful!

This kind of scenario can happen ***way*** too often, even to experienced
system administrators (note the space between `*` and `.bak`):

```bash
$ cd MyDissertation

$ ls
Citations.bak  Citations.doc  Dissertation.bak  Dissertation.doc  Notes.doc

$ rm * .bak
rm: cannot remove ‘.bak’: No such file or directory

$ ls

```

So, in order, our hapless user:

1. Changed to directory `MyDissertation`.

2. Listed the directory contents with `ls`, saw the combination of `.doc`
and `.bak` files.

3. Decided to delete the `.bak` files with `rm`, but accidentally typed in
a space between the wildcard `*` and the `.bak`. Note ominous warning
message.

4. Presto! `ls` shows ***everything*** is gone, not just the backup
files! Yay! The user's day's priorities just got rearranged as they go
hunting for another backup of their dissertation.

So be careful out there! This is an example where tab completion can be an
extra error check. Or a lot of times I use command history in these cases
by changing the `ls` to look for just the files I want to delete:

```bash
$ ls *.bak
Citations.bak  Dissertation.bak
```

Then using the "up arrow" to bring back up the `ls` command and changing
`ls` to `rm` and re-executing it. Safer that way.

## Touch Me

We just learned how to make a file disappear. We can also make a file
magically appear, just by [`touch`](http://linux.die.net/man/1/touch):

```bash
$ touch NewEmptyDissertation.doc

$ ls -l
total 0
-rw-rwxr--+ 1 myuser mygroup 0 Oct 19 14:12 NewEmptyDissertation.doc

```

Notice the newly created file is zero bytes long.

Interestingly enough, we can also use touch just to update the "last
modified date" of an existing file, as you can see in time change in the
following listing after running `touch` on the same file again:

```bash
$ touch NewEmptyDissertation.doc

$ ls -l
total 0
-rw-rwxr--+ 1 myuser mygroup 0 Oct 19 14:14 NewEmptyDissertation.doc
```

It can be useful (but also distressing from a forensics point of view) to
sometimes set the last modified date of a file to a specific date and time,
which `touch` also allows you to do, in this case to the night before
Christmas:

```bash
$ touch -t 201412242300 NewEmptyDissertation.doc

$ ls -l
total 0
-rw-rwxr--+ 1 myuser mygroup 0 Dec 24  2014 NewEmptyDissertation.doc
```

To *make a directory* you use [`mkdir`](http://linux.die.net/man/1/mkdir):

```bash
$ mkdir Bar

$ ls
Bar
```

Typically you need to create all intervening directories before creating a
"child" directory:

```bash
$ mkdir Xyzzy/Something
mkdir: cannot create directory ‘Xyzzy/Something’: No such file or directory
```

But of course you can override that behavior:

```bash
$ mkdir --parents Xyzzy/Something

$ ls
Bar  Xyzzy

$ ls Xyzzy
Something
```

## Navigating Through Life

Ever notice that "life" is an anagram for "file"? Spooky, eh?

Given that the UNIX-style file systems are hierarchical in nature they are
similar to navigate as with `CMD.EXE`. The biggest difference is the
absense of drive letter and the direction of the slashes.

To *change directories*, simply use [`cd`](http://linux.die.net/man/1/cd)
much like in Windows:

```bash
$ cd /etc

$ pwd
/etc
```

[`pwd`](http://linux.die.net/man/1/pwd) simply *prints the working
(current) directory*.

In Linux, users can have "home" directories (similar to Windows profiles),
typically located under `/home/username` for normal users and `/root` for
the "root" id. To change to a user's "home" directory, simply use `cd`:

```bash
$ cd

$ pwd
/home/myuser
```

The tilde (`~`) character is an alias for the current user's home
directory. The following example is equivalent to above:

```bash
$ cd ~

$ pwd
/home/myuser
```

More useful is that the tilde can be combined with a user name to specify
the home directory of ***another*** user:

```bash
$ cd ~git

$ pwd
/home/git
```

**Note:** The above assumes you have permissions to `cd` into `/home/git`.
See the section on file permissions for more info.

In addition, you need to know the difference between "absolute" and
"relative" paths:

* **Absolute path** - ***always*** "goes through" or specifies the "root"
(`/`) directory, e.g. `cd /etc`.

* **Relative path** - does ***not*** specify the root directory, expects
to start the navigation at the current directory with all path components
existing from there, e.g., `cd Dissertations`.

Windows inherited the concept of `.` for the current directory and `..`
for the parent directory directly from UNIX. Consider the following
examples that combine all of the above about relative paths and see if it
all makes sense:

```bash
$ mkdir Bar Baz

$ ls
Bar  Baz

$ cd Bar

$ touch a b c

$ ls
a  b  c

$ cd ../Baz

$ ls

$ touch d e f

$ ls
d  e  f

$ ls ..
Bar  Baz

$ ls ../Bar
a  b  c
```

Did you notice how both `mkdir` and `touch` allow for specifying multiple
directory and file names in the same command?

## May I?

Most UNIX-style file systems come with a set of nine permissions that can
be thought of as a "grid" of 3x3 showing "who has what?" The "who" is
"UGO":

* **User** - the user that is the "owner" of the file or directory.

* **Group** - the group that is the "owner" of the file or directory.

* **Other** - everyone else.

The "what" is:

* **Read**

* **Write**

* **Execute** - for files, for directories this means "navigate" or "list
contents".

The combination of "who has what?" is usually shown in detailed directory
listings by a set of ten characters, with the first one determining
whether an entry is a directory or a file:

```bash
# ls -l /etc
total 844
drwxr-xr-x 3 root root    4096 Feb 25  2015 acpi
-rw-r--r-- 1 root root    2981 Apr 23  2014 adduser.conf
-rw-r--r-- 1 root root      45 Jul  9 08:46 adjtime
-rw-r--r-- 2 root root     621 May 22  2014 aliases
-rw-r--r-- 1 root root   12288 May 22  2014 aliases.db
drwxr-xr-x 2 root root   20480 Feb 25  2015 alternatives
-rw-r--r-- 1 root root    4185 Dec 28  2011 analog.cfg
drwxr-xr-x 7 root root    4096 Feb 25  2015 apache2
drwxr-xr-x 6 root root    4096 Feb 25  2015 apt
-rw-r----- 1 root daemon   144 Jun  9  2012 at.deny
-rw-r--r-- 1 root root    1895 Dec 29  2012 bash.bashrc
-rw-r--r-- 1 root root      45 Jun 17  2012 bash_completion
drwxr-xr-x 2 root root    4096 Feb 25  2015 bash_completion.d
...and so on...
```

In the above, for example, we can see that the user `root` owns the file
`at.deny` while the `daemon` group is the primary group for it. `root`
can both read and write the file (`rw-`) while any user in the `daemon`
group can only reade it (`r--`). No other id will have any access to the
file at all (`---`).

Similarly we see that `acpi` is a directory (`d`) that can be read, written
(new files created) and listed by `root` (`rwx`), and read and listed by 
the group `root` and all other ids (`r-xr-x`).

If we look in `/etc/init.d` where many services store their startup scripts
we see:

```bash
# ls -l /etc/init.d
total 332
-rwxr-xr-x 1 root root  2227 Apr 15  2013 acpid
-rwxr-xr-x 1 root root  7820 Jan 31  2014 apache2
-rwxr-xr-x 1 root root  1071 Jun 25  2011 atd
-rwxr-xr-x 1 root root  1276 Oct 15  2012 bootlogs
-rwxr-xr-x 1 root root  1281 Jul 14  2013 bootmisc.sh
-rwxr-xr-x 1 root root  3816 Jul 14  2013 checkfs.sh
-rwxr-xr-x 1 root root  1099 Jul 14  2013 checkroot-bootclean.sh
-rwxr-xr-x 1 root root  9673 Jul 14  2013 checkroot.sh
-rwxr-xr-x 1 root root  1379 Dec  8  2011 console-setup
-rwxr-xr-x 1 root root  3033 Jul  3  2012 cron
-rwxr-xr-x 1 root root  2813 Feb  5  2015 dbus
-rwxr-xr-x 1 root root  6435 Jan  2  2013 exim4
...and so on...
```

In this case all the scripts are readable, writable and executable (`rwx`)
by the `root` user, and readable and executable by the `root` group and all
other users (`r-xr-x`).

To *change* the *owning* user of a file or directory (assuming you have
permissions to do so), use the [`chown`](http://linux.die.net/man/1/chown)
command:

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
[`chgrp`](http://linux.die.net/man/1/chgrp) command:

```bash
# chgrp git foo

# ls -l
total 4
-rwxr--r-- 1 git git 17 Oct 20 10:07 foo
```

To *change* the various permissions or *mode* bits, you use the
[`chmod`](http://linux.die.net/man/1/chmod) command. It uses mnemonics of
"ugo" for (owning) user, group and "other," respectively. It also uses
mnemonics of "rwx" for read, write and execute, and `+` to add
a permission and `-` to remove it. For example, to add execute permission
for the group and remove read permission for "other":

```bash
# chmod g+x,o-r foo

# ls -l
total 4
-rwxr-x--- 1 git git 17 Oct 20 10:07 foo
```

**Pro Tip:** To look like an old hand UNIX hacker, you can also convert
any set of "rwx" permissions into an octal number from 0 (no permissions)
to 7 (all permissions). It helps to think of the three permissions as
"binary places":

* **r** - 2^2 = 4
* **w** - 2^1 = 2
* **x** - 2^0 = 1
* **-** - 0

Some examples:

* **---** - 0 + 0 + 0 = 0
* **r--** - 2^2 + 0 + 0 = 4
* **r-x** - 2^2 + 0 + 2^0 = 5
* **rw-** - 2^2 + 2^1 + 0 = 6
* **rwx** - 2^2 + 2^1 + 2^0 = 7

Now to use octal with `chmod`, we think of the overall result we want for
a file. For example, if we want the `foo` file to be readable, writable
and executable by both its owning user and group, and not accessible at all
by anyone else, we could use:

```bash
# chmod u+rwx,g+rwx,o- foo

# ls -l
total 4
-rwxrwx--- 1 git git 17 Oct 20 10:07 foo

```

Or we could simply convert those permissions into octal in our head and:

```bash
# chmod 770 foo

# ls -l
total 4
-rwxrwx--- 1 git git 17 Oct 20 10:07 foo

```

Now you know the answer to that "How will we ever use octal in real life?"
question you asked in school!

**Note:** For a script or executable file to be allowed to run, it
***must*** be marked as executable for one of the user, group or other
entries. The following should be insightful:

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

## "I'll Send You a Tar Ball"

In the Windows world, we are used to compressing and sending directories
around as `.zip` files. In Linux you can also deal with `.zip` files,
although they don't tend to be the most common, using the
[`zip`](http://linux.die.net/man/1/zip) and
[`unzip`](http://linux.die.net/man/1/unzip) commands:

```bash
$ mkdir foo

$ cd foo

$ touch a b c

$ mkdir d

$ touch d/e

$ cd ..

$ zip -r foo foo
updating: foo/ (stored 0%)
  adding: foo/c (stored 0%)
  adding: foo/b (stored 0%)
  adding: foo/d/ (stored 0%)
  adding: foo/d/e (stored 0%)
  adding: foo/a (stored 0%)

$ ls -l foo.zip
-rw-r--r-- 1 myuser mygroup 854 Oct 24 15:56 foo.zip

$ unzip foo
Archive:  foo.zip
replace foo/c? [y]es, [n]o, [A]ll, [N]one, [r]ename: A
 extracting: foo/c                   
 extracting: foo/b                   
 extracting: foo/d/e                 
 extracting: foo/a                   
```

Not too exciting, but you get the drift. There is typically support for
other compression algorithms, too, using
[`bzip2`](http://linux.die.net/man/1/bzip2) and
[`7z`](http://linux.die.net/man/1/7z) (7-zip) commands.

However, the "native" way to "archive" a directory's contents in *IX is
with [`tar`](http://linux.die.net/man/1/tar), which is so old that `tar`
stands for "tape archive." Its purpose is to take virtually any directory
structure and create a single output "stream" or file of it. That is
then typically ran through a compression command and the result is called
a "tarball":

```bash
$ tar cvf foo.tar foo/*
foo/a
foo/b
foo/c
foo/d/
foo/d/e

$ ls -l foo.tar
-rw-r--r-- 1 myuser mygroup 10240 Oct 24 16:14 foo.tar

$ gzip foo.tar

$ ls -l foo.tar.gz 
-rw-r--r-- 1 myuser mygroup 187 Oct 24 16:14 foo.tar.gz
```

In the `tar` command above, the parameters are `c` (create a new archive),
`v` (turn on "verbose" output) and `f` followed by the file name of the
new `.tar` file.

**Note:** `tar` supports POSIX-style parameters (`-c`), GNU-style
(`--create`), and the old BSD-style (`c` with no hyphens at all), as shown
in these examples. So both of the following are also equivalent to the
above:

```bash
$ tar -c -v -f foo.tar foo/*

$ tar --create --verbose --file=foo.tar foo/*
```

The use of compression commands along with `tar` is so prevalent that
they've been built into `tar` itself now as optional parameters:

```bash
$ tar cvzf foo.tgz foo
foo/
foo/c
foo/b
foo/d/
foo/d/e
foo/a

$ ls -l foo.tgz
-rw-r--r-- 1 myuser mygroup 191 Oct 24 16:19 foo.tgz
```

In this case the `z` parameter says to use `gzip` compression, and the
`.tgz` file suffix means basically "tarred and gzipped", or the equivalent
to `.tar.gz` in the first example.

`tar` is used to both create and read `.tar` files. So to extract something
like the above, you can change the create (`c`) parameter to extract
(`x`), like this:

````bash
$ tar xvf foo.tgz
foo/
foo/c
foo/b
foo/d/
foo/d/e
foo/a
```

## Let's Link Up!

In Windows there are "shortcuts," which are simply special files that the
OS knows to interpret as "go open this other file over there." There are
also "hard links" that allow to different directory entries *in the same
file system* to point to the same physical file.

UNIX file systems also have both these types of links (which isn't
surprising, given that Microsoft got the ideas from UNIX). A "soft link" is
equivalent to a Windows shortcut, and can point to a file or a directory,
and can point to anything on any mounted file system:

```bash
$ ls -l
total 4
-rw-r--r-- 1 myuser mygroup    0 Oct 24 15:53 a
-rw-r--r-- 1 myuser mygroup    0 Oct 24 15:53 b
-rw-r--r-- 1 myuser mygroup    0 Oct 24 15:53 c
drwxr-xr-x 2 myuser mygroup 4096 Oct 24 16:00 d

$ cd d

$ pwd
/tmp/foo/d

$ cd ..

$ ln -s a MyThesis.doc

$ ln -s d Dee

$ ls -l
total 4
-rw-r--r-- 1 myuser mygroup    0 Oct 24 15:53 a
-rw-r--r-- 1 myuser mygroup    0 Oct 24 15:53 b
-rw-r--r-- 1 myuser mygroup    0 Oct 24 15:53 c
drwxr-xr-x 2 myuser mygroup 4096 Oct 24 16:00 d
lrwxrwxrwx 1 myuser mygroup    1 Oct 24 16:40 Dee -> d
lrwxrwxrwx 1 myuser mygroup    1 Oct 24 16:40 MyThesis.doc -> a

$ cd Dee

$ pwd
/tmp/foo/Dee
```

The things to notice about this example:

1. The `-s` parameter indicates "create a *soft* link."

2. Instead of a `-` or `d`, a soft link is shown in a `ls` listing as `l`
regardless of whether the target is a file or directory. This is because
a soft link doesn't "know" ***what*** the target is - it is just a file
with a name in a directory pointing to another location. ***What*** that
location is will be determine after the link is traversed.

A "hard link" is a bit different. It can only be made between files and the
two files must be on the same file system. That is because hard links are
actually directory entries (as opposed to files in directories) that point
to the same ["inode"](https://en.wikipedia.org/wiki/Inode) on disk. From
within a single directory it is impossible to tell if there are other
directories with pointers to the same files (inodes) on disk.

```bash
$ ls
a  b  c  d  Dee  MyThesis.doc

$ ln b B

$ cd d

$ ln ../b .

$ ls -l
total 0
-rw-r--r-- 3 myuser mygroup 0 Oct 24 15:53 b
-rw-r--r-- 1 myuser mygroup 0 Oct 24 15:54 e

$ cd ..

$ ls -l
total 4
-rw-r--r-- 1 myuser mygroup    0 Oct 24 15:53 a
-rw-r--r-- 3 myuser mygroup    0 Oct 24 15:53 b
-rw-r--r-- 3 myuser mygroup    0 Oct 24 15:53 B
-rw-r--r-- 1 myuser mygroup    0 Oct 24 15:53 c
drwxr-xr-x 2 myuser mygroup 4096 Oct 24 16:49 d
lrwxrwxrwx 1 myuser mygroup    1 Oct 24 16:40 Dee -> d
lrwxrwxrwx 1 myuser mygroup    1 Oct 24 16:40 MyThesis.doc -> a
```

The "net net" of all the above is that now `b`, `B` and `d/b` all point to
exactly the same inode, or disk location, i.e., the exact same physical
file.

### I Said "Go Away!", Dammit!

So what can possibly go wrong with links? With soft links the answer is
easy - the "remote" location being pointed to goes away or is renamed:

```bash
$ ls -l
total 4
-rw-r--r-- 1 myuser mygroup    0 Oct 24 15:53 a
-rw-r--r-- 3 myuser mygroup    0 Oct 24 15:53 b
-rw-r--r-- 3 myuser mygroup    0 Oct 24 15:53 B
-rw-r--r-- 1 myuser mygroup    0 Oct 24 15:53 c
drwxr-xr-x 2 myuser mygroup 4096 Oct 24 16:49 d
lrwxrwxrwx 1 myuser mygroup    1 Oct 24 16:40 Dee -> d
lrwxrwxrwx 1 myuser mygroup    1 Oct 24 16:40 MyThesis.doc -> a

$ rm a

$ ls -l
total 4
-rw-r--r-- 3 myuser mygroup    0 Oct 24 15:53 b
-rw-r--r-- 3 myuser mygroup    0 Oct 24 15:53 B
-rw-r--r-- 1 myuser mygroup    0 Oct 24 15:53 c
drwxr-xr-x 2 myuser mygroup 4096 Oct 24 16:49 d
lrwxrwxrwx 1 myuser mygroup    1 Oct 24 16:40 Dee -> d
lrwxrwxrwx 1 myuser mygroup    1 Oct 24 16:40 MyThesis.doc -> a

$ cat MyThesis.doc 
cat: MyThesis.doc: No such file or directory
```

So even though the soft link `MyThesis.doc` was still in the directory,
the actual underlying file `a` is now gone, and trying to access it via
the soft link leads to the somewhat confusing "No such file or directory"
error message ("I can see it! It's right there!")

With hard links, it isn't so much a problem as just the nature of the
beast. Because each hard link is a directory (metadata) entry pointing to
an inode, deleting one simply deletes that directory entry. As long as the
file has other hard links pointing to it, it "exists." Only when the last
remaining hard link is removed has it been "deleted." Let's play:

```bash
$ echo "This is b." > b

$ cat b
This is b.

$ cat B
This is b.

$ cat d/b
This is b.
```

So, that makes sense. Above we had an original file `b` and created to
hard links to it, `B` and `d/b`. When we edit `b` by placing "This is b."
in it, we see that it has the same contents no matter how we access it,
because it is pointing to the same inode.

Can you guess how many `rm` commands it will take to delete the file
containing "This is b."?

```bash
$ rm b

$ cat b
cat: b: No such file or directory

$ cat B
This is b.

$ cat d/b
This is b.

$ rm B

$ cat d/b
This is b.

$ rm d/b

$ ls
c  d  Dee  MyThesis.doc
```

So, ultimately, it takes a `rm` for every hard link to permanently delete
a file.

### Mount It? I Don't Even Know It's Name!

With all this talk that a hard link can only be on the same file system,
how do you know whether two directories are on the same file system? In
Windows it's easy - that's exactly what the drive letters are telling you.
But in Linux, where everything is "mounted" under a single hierarchy
starting at `/`, how do I know that `/var/something` and `var/or/other`
are on the same file system?

There are multiple ways to tell, actually. The easiest is with the
[`df`](http://linux.die.net/man/1/df) command:

```bash
$ df
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

The ones of interested are the `/dev` entries, and we see that everything
mounted under `/` is on one file system, except for whatever happens to be
on the file system mounted under `/boot`. So outside of `/boot`, on this
system we could hard link away to our heart's content.

**Note:** - It is (barely) beyond the scope of this book to cover the
[`mount`](http://linux.die.net/man/8/mount) command. I wanted to, really
bad, but it can get so complex so fast that I decided not to. Maybe if you
ask, real nice...

### I'm Seeing Double

So, both hard and soft links can have some interesting side effects if you
think about them, yes? For one, if you are backing things up, then
you may get duplicates in your backup set. In fact, with hard links you
will, by definition, unless the backup software is very smart and doing
things like de-duplication.

But even with soft links if everything just blindly followed them you could
also get duplicates where you didn't want them, or even circular
references. Also, the pointers in the soft link files are not evaluated
until the a command references them. Note that the following is perfectly
legal with soft links, but may not give the results you expect - think
about current working directory shown by `pwd` in the following, and what
the effects of the relative paths shown are as the sample progresses:

```bash
$ pwd
/tmp/foo

$ rm -rf *

$ touch a b c

$ mkdir d

$ touch d/e

$ ln -s . d/f

$ ls d/f
e  f

$ ln -s .. d/g

$ ls d/g
a  b  c  d
```

Many commands that deal with files and file systems, like `find`, have
parameters specifically telling the command whether to follow soft links
or not (by default, `find` does not).

## What's the `diff`?

Most people think of [`diff`](http://linux.die.net/man/1/diff) as a tool
only programmers find useful, but that is short-sighted. The whole purpose
of `diff` is to show differences between files. For example, I backed up
this document (which is a text file) before starting this chapter, then
typed this introduction to `diff`. This is what `diff` shows:

```bash
$ diff Agenda.bak Agenda.md
1285a1286,1291
> Most people think of [`diff`](http://linux.die.net/man/1/diff) as a tool
> only programmers find useful, but that is short-sighted. The whole purpose
> of `diff` is to show differences between files. For example, I backed up
> this document (which is a text file) before starting this chapter, then
> typed this introduction to `diff`. This is what `diff` shows:
```

In other words, the "arrows" are pointing to the "new" file (by convention
the file specified on the left is the "old" file and the file on the right
is the "new" file), showing five lines were inserted, starting at line
1285. Pretty meta, but not real exciting.

Let's look at something else, say a configuration file for an application.
We have an original file, `orig.conf`:

```bash
$ cat orig.conf
FOO=1

SOME=THINGS
STAY=THE
SAME=ALWAYS

BAR=Xyzzy
```

Then we have a new file, `new.conf`:

```bash
$ cat new.conf
FOO=2

SOME=THINGS
STAY=THE
SAME=ALWAYS
```

Now if we `diff` them:

```bash
$ diff orig.conf new.conf
1c1
< FOO=1
---
> FOO=2
7d6
< BAR=Xyzzy
```

Now we can more easily see that line #1 changed (`1c1`) from `FOO=1` on
the "left" file to `FOO=2` on the "right," and that line #7 was deleted
(`7d6`) from the "left" file to form the "right." Again, not too
interesting, but imagine that both files were thousands of lines long, and
there were only a few changes, and you were trying to detect and recover an
accidentally-deleted line. Now you can see why `diff` can be handy, as long
as you keep around a prior version either in a backup file or source code
control to compare against.

`diff` is your friend. It really comes into play with a version control
system like `git`, but again, that is beyond the scope of this book.
  