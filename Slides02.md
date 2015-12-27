
# Step 2

## File under "Directories"

----

## `ls` - list files

```
~ $ ls
Audiobooks  Downloads  KindleGen  Podcasts  Templates
Desktop     Dropbox    Music      Public    Videos
Documents   FreeRDP    Pictures   Temp      VSCode-linux-x64
```

## "Dotfiles"

```
~ $ ls -a
.              .dmrc          .gnome2_private  Pictures    .themes
..             Documents      .hplip           .pki        .thumbnails
.adobe         Downloads      .hugin           Podcasts    .thunderbird
.atom          .dropbox       .ICEauthority    .profile    Videos
Audiobooks     Dropbox        .icons           .ptbt1      .vscode
.bash_history  .dropbox-dist  KindleGen        Public      VSCode-linux-x64
.bash_logout   .face          .lastpass        .sbd        .wine
.cache         FreeRDP        .lesshst         .ssh        .Xauthority
.cinnamon      .gconf         .linuxmint       .swp        .xinputrc
.cmake         .gimp-2.8      .local           Temp        .xsession-errors
.config        .gitconfig     .macromedia      Templates
.dbus          .gksu.lock     .mozilla         .texmf-var
Desktop        .gnome2        Music            .TeXworks
```

## List details

```
~ $ ls -l
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

## Combining parameters

```
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

## Parameter types

> * **Short**
>     * `rm -rf *`
>     * Easier to type
> * **Long**
>     * `rm --recursive --force *`
>     * Easier to understand

## `cat` - concatenate files

```
~ $ cat installrdp 
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
...and so on...
```

## `tail` - show end of files

```
~ # tail dmesg
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

## "Follow" a file

```
~ # tail -f dmesg
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

## `sort` - sorting files

```
~ $ sort -k 3 -n * | tail -n 3
Combine motor   1500
Tractor tires   2000
Combine tires   2500
```

## `cp` - copy files

```
~ $ cp diary.txt diary.bak
~ $ cp -r thisdir thatdir
~ $ cp --recursive thisdir thatdir
```

## `mv` - move files

```
~ $ mv thismonth.log lastmonth.log
```

> * `mv` is simple rename
> * `rename` offers more options  

## `rm` - remove files

```
~ $ rm desktop.ini
```

## Danger, Will Robinson!

```
~ $ cd MyDissertation
~ $ ls
Citations.bak  Citations.doc  Dissertation.bak  Dissertation.doc  Notes.doc
~ $ rm * .bak
rm: cannot remove ‘.bak’: No such file or directory
~ $ ls
```

## And all was null and void...

```
~ $ rm -rf *
```

## `touch` - update file time

```
~ $ touch NewEmptyDissertation.doc
~ $ ls -l
total 0
-rw-rwxr--+ 1 myuser mygroup 0 Oct 19 14:12 NewEmptyDissertation.doc
```

## Reset file time

```
~ $ touch -t 201412242300 NewEmptyDissertation.doc
~ $ ls -l
total 0
-rw-rwxr--+ 1 myuser mygroup 0 Dec 24  2014 NewEmptyDissertation.doc
```

## `mkdir` - make directory

```
~ $ mkdir Bar
~ $ ls
Bar
```

## `cd` - change directory

```
~ $ cd /etc
~ $ pwd
/etc
```

## Absolute paths

> * Always includes the root, `/`
> * `cd /etc`

## Relative paths

> * Starts from current directory, `.`
> * Parent directory is `..`
> * `cd child`
> * `cd ../sibling`

## `.` and `..`

> * `.` - current directory
>     * - we will see why this is useful later
> * `..` - parent directory
>     * - useful to navigate "up and out"

## May I?

> * **3x3 "grid"** - who by what?
> * **UGO** - who?
> * **RWX** - what?

## Who?

> * **U** - primary *user* or "owner"
> * **G** - primary *group*
> * **O** - other (everyone else)

## What?

> * **R** - *read* permission
> * **W** - *write* permission
> * **X** - *execute* permission
>     * - "list directory" permission

## `ls -l`, again

```
~ $ ls -l
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

## `-rwxr-xr-x`

> * `-` - file
> * `rwx` - `myuser` can read, write and execute
> * `r-x` - `mygroup` and anyone else can read and execute

## `drwx------`

> * `d` - directory
> * `rwx` - `myuser` can read, write and list contents
> * `---` - no one else can do anything

## Changing owners

> * `chown myuser foo` - change owner of `foo` to user `myuser`
> * `chgrp mygroup bar` - change group for `bar` to `mygroup`

## Changing access

> * `chmod u+rw foo` - give primary owner read/write to `foo`
> * `chmod o-x bar` - remove execute permission for "others" from `bar`

## Will this be on the test?

If `rwx` were octal:

> * `r` == 2^2^ (4)
> * `w` == 2^1^ (2)
> * `x` == 2^0^ (1)
> * `-` == 0

## Olde Skool `chmod`

Then `chmod 754 foo`:

> * `7` = `rwx` for user
> * `5` = `r-x` for group
> * `4` = `r--` for other

Quicker than `chmod u=rwx,g=rx,o=r foo`

## Why won't it run?

```
~ # echo "echo Hello world" > foo
~ # ls -l
total 4
-rw-r--r-- 1 root root 17 Oct 20 10:07 foo
~ # ./foo
-bash: ./foo: Permission denied
~ # chmod u+x foo
~ # ls -l
total 4
-rwxr--r-- 1 root root 17 Oct 20 10:07 foo
~ # ./foo
Hello world
```

## Compressing files

```
~ $ zip -r foo foo
updating: foo/ (stored 0%)
  adding: foo/c (stored 0%)
  adding: foo/b (stored 0%)
  adding: foo/d/ (stored 0%)
  adding: foo/d/e (stored 0%)
  adding: foo/a (stored 0%)
~ $ ls -l foo.zip
-rw-r--r-- 1 myuser mygroup 854 Oct 24 15:56 foo.zip
~ $ unzip foo
Archive:  foo.zip
 extracting: foo/c                   
 extracting: foo/b                   
 extracting: foo/d/e                 
 extracting: foo/a                   
```

## tarballs

```
~ $ tar cvzf foo.tgz foo
foo/
foo/c
foo/b
foo/d/
foo/d/e
foo/a
~ $ ls -l foo.tgz
-rw-r--r-- 1 myuser mygroup 191 Oct 24 16:19 foo.tgz
~ $ tar xvf foo.tgz
foo/
foo/c
foo/b
foo/d/
foo/d/e
foo/a
```

## Soft links

```
~ $ ln -s d Dee
```

> * Equivalent to a shortcut
> * Target can be directory or file
> * Target can be any file system
> * Deleting link doesn't affect target
> * Deleting target breaks link, doesn't remove it

## Hard links

```
~ $ ln d Dee
```

> * `Equivalent to NTFS junction point
> * Target can be only files
> * Target must be on same file system
> * File not deleted until ***ALL*** hard links deleted

## File systems

```
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

## What's the `diff`?

```
~ $ diff orig.conf new.conf
1c1
< FOO=1
---
> FOO=2
7d6
< BAR=Xyzzy
```