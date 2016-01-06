
# And So On

***`/etc`, starting and stopping services, `apt-get`/`rpm`/`yum`, and more.***

> *"Et cetera, et cetera, et cetera!"* - The King (*The King and I*)

This step is a grab bag of stuff that didn't seem to directly belong anywhere else, but I still
think needs to be known, or at least brushed up against.

## One-Stop Shopping{.unnumbered}

In UNIX-like systems, most (not all) system configuration is stored in directories and text files
under `/etc`.
\index{files and directories!special!etc@\texttt{/etc/}}

**Note:** In Linux `/etc` is almost universally pronounced "slash-et-see," ***not*** "forward slash
et cetera."

\drcap{\texttt{/etc} directory}
```bash
~ $ ls /etc
acpi                    hosts                 pki
adduser.conf            hosts.allow           pm
adjtime                 hosts.deny            pnm2ppa.conf
alternatives            hp                    polkit-1
anacrontab              icedtea-web           ppp
apg.conf                ifplugd               printcap
apm                     ImageMagick           profile
apparmor                init                  profile.d
apparmor.d              init.d                protocols
apport                  initramfs-tools       pulse
apt                     inputrc               purple
at-spi2                 insserv               python
avahi                   insserv.conf          python2.7
bash.bashrc             insserv.conf.d        python3
bash_completion         inxi.conf             python3.4
bash_completion.d       iproute2              rc0.d
bindresvport.blacklist  issue                 rc1.d
blkid.conf              issue.dpkg-old        rc2.d
blkid.tab               issue.net             rc3.d
bluetooth               issue.net.dpkg-old    rc4.d
bonobo-activation       java-7-openjdk        rc5.d
brlapi.key              kbd                   rc6.d
...and so on...
```

Depending on what you are trying to configure, you may need to be in one or many files in `/etc`.
This is a ***very short*** list of files and directories you may need to examine there:

* **`fstab`** - a listing of the file systems currently mounted and their types.
\index{files and directories!special!etcfstab@\texttt{/etc/fstab}}

* **`group`** - the security groups on the system.
\index{files and directories!special!etcgroup@\texttt{/etc/group}}

* **`hosts`** - network aliases (overrides DNS, takes effect immediately).
\index{files and directories!special!etchosts@\texttt{/etc/hosts}}

* **`init.d`** - startup and shutdown scripts for "services."
\index{files and directories!special!etcinitd@\texttt{/etc/init.d/}}

* **`mtab`** - list of current "mounts."
\index{files and directories!special!etcmtab@\texttt{/etc/mtab}}

* **`passwd`** - "shadow" file containing all the user accounts on the system.
\index{files and directories!special!etcpasswd@\texttt{/etc/passwd}}

* **`resolv.conf`** - DNS settings.
\index{files and directories!special!etcresolvconf@\texttt{/etc/resolv.conf}}

* **`samba`** - file sharing settings for CIFS-style shares.
\index{files and directories!special!etcsamba@\texttt{/etc/samba/}}

There are lots of other interesting files under `/etc`, but I keep returning to the above again and
again. On most of them you can run the `man` command against section 5 to see their format and
documentation, e.g., `man 5 hosts`.

## Service Station{.unnumbered}

We are going to ignore system initialization and "stages," and assume most of the time you are
running on a well-functioning system. Even so sometimes you want to restart a specific system
service without rebooting the whole system, often to force re-reading changed configuration files.
First check if the service has a script in `/etc/init.d`:
\index{files and directories!special!etcinitd@\texttt{/etc/init.d/}}

\drcap{init.d directory}
```bash
~ $ ls /etc/init.d
acpid             dbus               ondemand     single
anacron           dns-clean          pppd-dns     skeleton
apparmor          friendly-recovery  procps       smbd
avahi-daemon      grub-common        pulseaudio   speech-dispatcher
binfmt-support    halt               rc           sudo
bluetooth         hddtemp            rc.local     udev
brltty            irqbalance         rcS          umountfs
casper            kerneloops         README       umountnfs.sh
cinnamon          killprocs          reboot       umountroot
console-setup     kmod               resolvconf   unattended-upgrades
cpufrequtils      lm-sensors         rsync        urandom
cron              loadcpufreq        rsyslog      virtualbox-guest-utils
cryptdisks        mdm                samba        virtualbox-guest-x11
cryptdisks-early  mintsystem         samba-ad-dc  x11-common
cups              networking         saned
cups-browsed      nmbd               sendsigs
```

If so, then chances are it will respond to a fairly standard set of commands, such as the following
samples with `samba`:

\drcap{Stopping and starting services}
```bash
~ # /etc/init.d/samba stop
[ ok ] Stopping Samba daemons: nmbd smbd.
~ # /etc/init.d/samba start
[ ok ] Starting Samba daemons: nmbd smbd.
~ # /etc/init.d/samba restart
[ ok ] Stopping Samba daemons: nmbd smbd.
[ ok ] Starting Samba daemons: nmbd smbd.
```

**Note:** The above examples were run as `root`, otherwise they would probably have required
execution using `sudo`.

## Package Management{.unnumbered}

Almost all Linux distros have the concept of "packages" which are used to install, update and
uninstall software. There are different package managers, including `dpkg` and `apt-get` on
Debian-based distros, `rpm` on Fedora descendants, etc. For the rest of this section we will use
Debian tools, but in general the concepts and problems are similar for the other toolsets.
\drpkg{apt-get}
\drpkg{dpkg}
\drpkg{rpm}

One of the nicest things about Linux-style package managers (as opposed to traditional Windows
installers) is that they can satisfy all a packages "dependencies" (other packages that are
required for a package to run) and automatically detect and install those, too. See
[Chocolately](https://chocolatey.org/) for an attempt to build a similar ecosystem in Windows.

One thing Linux distros do is define the "repositories" (servers and file structures) that serve
the various packages. In addition, there are usually multiple versions of packages, typically
matching different releases of the distro. We won't go into setting up a system to point to
these here.

In Debian flavors, [`apt-get`](http://linux.die.net/man/8/apt-get) is usually the tool of choice
for package management. Another option is [`aptitude`](http://linux.die.net/man/8/aptitude).
\drpkg{apt-get}
\drpkg{aptitude}

There are three common `apt-get` commands that get used over and over. The first downloads and
*updates* the local metadata cache for the repositories:

\drcap{\texttt{apt-get update}}
```bash
~ $ sudo apt-get update
[sudo] password for myuser:
Ign http://packages.linuxmint.com rafaela InRelease
Ign http://extra.linuxmint.com rafaela InRelease
Hit http://extra.linuxmint.com rafaela Release.gpg                             
Hit http://packages.linuxmint.com rafaela Release.gpg                          
Hit http://security.ubuntu.com trusty-security InRelease                       
Hit http://extra.linuxmint.com rafaela Release
Hit http://packages.linuxmint.com rafaela Release
Hit http://security.ubuntu.com trusty-security/main amd64 Packages
Hit http://packages.linuxmint.com rafaela/main amd64 Packages
Hit http://extra.linuxmint.com rafaela/main amd64 Packages
Hit http://security.ubuntu.com trusty-security/restricted amd64 Packages
Hit http://extra.linuxmint.com rafaela/main i386 Packages
Hit http://packages.linuxmint.com rafaela/upstream amd64 Packages
Ign http://archive.canonical.com trusty InRelease
Ign http://archive.ubuntu.com trusty InRelease
Hit http://security.ubuntu.com trusty-security/universe amd64 Packages
Hit http://packages.linuxmint.com rafaela/import amd64 Packages
Hit http://security.ubuntu.com trusty-security/multiverse amd64 Packages
Hit http://packages.linuxmint.com rafaela/main i386 Packages
Hit http://archive.canonical.com trusty Release.gpg
Hit http://archive.ubuntu.com trusty-updates InRelease
...and so on...
```

**Note:** `apt-get` is an administrative command and usually requires `sudo`.

The second common command *upgrades* all the packages in the system to the latest release in the
repository (which may not be the latest and greatest release of the package):

\drcap{Upgrading installed packages}
```bash
~ $ sudo apt-get dist-upgrade
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Calculating upgrade... Done
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
```

In this case there was nothing to upgrade.

**Note:** In the example above I used `apt-get dist-upgrade`. There is also an `apt-get upgrade`
command. `apt-get dist-upgrade` will resolve any new dependencies and download new packages if
needed, but ***it may also remove packages it considers no longer needed.*** `apt-get upgrade`
simply performs an in-place upgrade of already-installed packages and in no case will install new
or remove unneeded packages. Which is appropriate for you will depend on your circumstances. You
can use the `--simulate` parameter with either to have `apt-get` show you what it would do without
actually doing it.
\drpkg{apt-get}

And the final common command is obviously to install a package:

\drcap{Installing a package}
```bash
~ $ sudo apt-get install traceroute
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following NEW packages will be installed:
  traceroute
0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
Need to get 0 B/45.0 kB of archives.
After this operation, 176 kB of additional disk space will be used.
Selecting previously unselected package traceroute.
(Reading database ... 307895 files and directories currently installed.)
Preparing to unpack .../traceroute_1%3a2.0.20-0ubuntu0.1_amd64.deb ...
Unpacking traceroute (1:2.0.20-0ubuntu0.1) ...
Processing triggers for man-db (2.6.7.1-1ubuntu1) ...
Setting up traceroute (1:2.0.20-0ubuntu0.1) ...
update-alternatives: using /usr/bin/traceroute.db to provide /usr/bin/traceroute
 (traceroute) in auto mode
update-alternatives: using /usr/bin/lft.db to provide /usr/bin/lft (lft) in auto
 mode
update-alternatives: using /usr/bin/traceproto.db to provide /usr/bin/traceproto
 (traceproto) in auto mode
update-alternatives: using /usr/sbin/tcptraceroute.db to provide /usr/sbin/tcptr
aceroute (tcptraceroute) in auto mode
```

You can also `apt-get remove` or `apt-get purge` packages. See the `apt-get` `man` page for details.
\drpkg{apt-get}

This all looks very convenient, and it is. The problems arise because some distros are better at
tracking current versions of packages in their repositories than others. In fact, some distros
purposefully stay behind cutting edge for system stability purposes. Debian itself is a good example
of this, as are many "LTS" (long term support) releases in other distros.

## Other Sources{.unnumbered}

Besides the distribution's repositories, you can install packages and other software from a variety
of places. It may be an "official" site for the package, GitHub, a "personal package archive" (PPA)
or whatever. The package may be in a binary installable format (`.deb` files for Debian systems),
in source format requiring it to be built, in a zipped "tarball," and more.
\index{files and directories!debpackagefiles@\texttt{.deb} package files}

If you want the latest and greatest version of a package you often have to go to its "official"
site or GitHub repository. There, you may find a `.deb` file, in which case you could install it
with `dpkg`:
\drpkg{dpkg}

\drcap{Installing a package with \texttt{dpkg}}
```bash
sudo dpkg -i somesoftware.deb
```

There is, however, a problem. You now have to remember that you installed that package by hand and
keep it up to date by hand (or not). `apt-get upgrade` isn't going to help you here. This is true
no matter what way you get the alternative package - `.deb` file, tarball, source code, or 
whatever (although `apt-get` can work with PPAs in a more automated manner).
\drpkg{apt-get}

The second problem with third-party package sources is how do you know whether to trust them or
not? If something is in an "official" distro repository, chances are it has been vetted to a
certain degree. But otherwise, it is caveat administrator.

The final problem with package managers is that they're such a good idea that ***everything*** has
them now. Not just the operating systems like Linux, but languages like Python have
[`pip`](https://pypi.python.org/pypi/pip/) and execution environments like node have
[`npm`](https://www.npmjs.com/). So now you end up with having to keep track of what you have
installed on a system across two or three or more package managers at different levels of abstraction. It can be a mess!

Add into this that many of these language and environment package managers allow setting up
"global" (system-wide) or "local" (current directory) versions of a package to allow different
versions of the same package to exist on the same system, where different applications may be
relying on the different versions to work. Do you keep good notes? You'd better!

## Which `which` is Which?{.unnumbered}

Now that we've seen that we can have multiple versions of the same command or executable on the
system, an interesting question arises. *Which* `foo` command am I going to call if I just type
`foo` at the command prompt? In other words, after taking the `$PATH` variable into
consideration and searching for the program through that from left to right, which version in which
directory is going to be called?
\drenv{PATH}{execution search path}

Luckily we have the [`which`](http://linux.die.net/man/1/which) command for just that!
\drcmd{which}{find program}

\drcap{\texttt{which} command}
```bash
~ $ which curl
/usr/bin/curl
```

How can you tell if you have multiple versions of something installed? One way is with the
[`locate`](http://linux.die.net/man/1/locate) command:
\drfnd{locate}{locate files}

\drcap{\texttt{locate} command}
```bash
~ $ locate md5
/boot/grub/i386-pc/gcry_md5.mod
/lib/modules/3.16.0-38-generic/kernel/drivers/usb/gadget/amd5536udc.ko
/usr/bin/md5pass
/usr/bin/md5sum
/usr/bin/md5sum.textutils
/usr/include/libavutil/md5.h
/usr/include/openssl/md5.h
/usr/lib/casper/casper-md5check
/usr/lib/grub/i386-pc/gcry_md5.mod
/usr/lib/i386-linux-gnu/sasl2/libcrammd5.so
/usr/lib/i386-linux-gnu/sasl2/libcrammd5.so.2
/usr/lib/i386-linux-gnu/sasl2/libcrammd5.so.2.0.25
/usr/lib/i386-linux-gnu/sasl2/libdigestmd5.so
/usr/lib/i386-linux-gnu/sasl2/libdigestmd5.so.2
/usr/lib/i386-linux-gnu/sasl2/libdigestmd5.so.2.0.25
/usr/lib/python2.7/md5.py
/usr/lib/python2.7/md5.pyc
/usr/lib/ruby/1.9.1/x86_64-linux/digest/md5.so
/usr/lib/x86_64-linux-gnu/sasl2/libcrammd5.so
/usr/lib/x86_64-linux-gnu/sasl2/libcrammd5.so.2
/usr/lib/x86_64-linux-gnu/sasl2/libcrammd5.so.2.0.25
/usr/lib/x86_64-linux-gnu/sasl2/libdigestmd5.so
...and so on...
```

The `locate` command, if installed, is basically a database of all of the file names on the system
(collected periodically - not in real time). You are simply searching the database for a pattern.
It is a quicker way to look than `find / -name \*pattern*\`.

One final note on which thing gets executed. Unlike in Windows, "UNIX" environments do not consider
the local directory (the current directory you are sitting at the command prompt, i.e., what
[`pwd`](http://linux.die.net/man/1/pwd) shows) as part of the path unless `.` is explicitly listed
in `$PATH` (and that is typically a bad idea). This is for security purposes. So it can be a bit
unnerving to try and execute `foo` in the current directory and get:
\drfnd{pwd}{print working directory}

\drcap{Command not found - but it's right there!}
```bash
~ $ ls -l foo
-rwxrwx--- 1 myuser mygroup 16 Oct 23 19:03 foo
~ $ foo
No command 'foo' found, did you mean:
 Command 'fgo' from package 'fgo' (universe)
 Command 'fop' from package 'fop' (main)
 Command 'fog' from package 'ruby-fog' (universe)
 Command 'fox' from package 'objcryst-fox' (universe)
 Command 'fio' from package 'fio' (universe)
 Command 'zoo' from package 'zoo' (universe)
 Command 'xoo' from package 'xoo' (universe)
 Command 'goo' from package 'goo' (universe)
foo: command not found
```

Instead, to invoke `foo`, you can either fully qualify the path as shown by `pwd`:

\drcap{Using a fully qualified path to execute a command}
```bash
~ $ /home/myuser/foo
```

Or you can prepend the `./` relative path to it, to indicate "the `foo` in the current directory
(`.`)":

\drcap{Specifying the command in the current directory}
```bash
~ $ ./foo
```

## Over and Over and Over{.unnumbered}

The function of scheduled tasks in Windows is performed by [`cron`](http://linux.die.net/man/8/cron)
in Linux. It reads in the various [`crontab(5)`](http://linux.die.net/man/5/crontab) files on the
system and executes the commands in them at the specified times. You use the
[`crontab(1)`](http://linux.die.net/man/1/crontab) command to view and edit the `crontab` files for your user (and other users if you have admin privileges).
\drsys{cron}{run scheduled jobs}
\drsys{crontab}{edit scheduled jobs}
\index{crontab@\texttt{crontab} (file)}
\index{files and directories!special!crontab@\texttt{crontab}}

The sample given in the comments of the `crontab` when initially opened using `crontab -e` give a
fine example of the syntax of the `crontab` file:

\drcap{Looking at default \texttt{crontab} file}
```bash
# Edit this file to introduce tasks to be run by cron.
#
# Each task to run has to be defined through a single line
# indicating with different fields when the task will be run
# and what command to run for the task
#
# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any').#
# Notice that tasks will be started based on the cron's system
# daemon's notion of time and timezones.
#
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
#
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
#
# For more information see the manual pages of crontab(5) and cron(8)
#
# m h  dom mon dow   command
```

If you have `sudo` privileges you can edit the `crontab` file for another user with:

\drcap{Editing another user's \texttt{crontab} file}
```bash
$ sudo crontab -e -u otheruser
```

This can be useful to do things like run backup jobs as the user that is running the web server,
say, so it has access rights to all the necessary files to back up the web server installation by
definition.

The only other thing I have to add about `cron` is when it runs the commands from each `crontab`,
they are typically not invoked with that particular user's environment settings, so it is best to
fully specify the paths to files both in the `crontab` file itself and in any scripts or parameters
to scripts it calls. Depending on the system and whether `$PATH` is set at all when a "`cron` job"
runs, you may have to specify the full paths to binaries in installed packages or even what you
would consider "system" libraries! The `which` command comes in handy here for finding out where
each command is installed.
\drenv{PATH}{execution search path}

## Start Me Up{.unnumbered}

If you need to reboot the system the quickest way is with the
[`reboot`](http://linux.die.net/man/8/reboot) command:
\drsys{reboot}{reboot system}

\drcap{\texttt{reboot} command}
```bash
$ sudo reboot
```

You can also use the [`shutdown`](http://linux.die.net/man/8/shutdown) command with the `-r` option,
but why? The handier use for `shutdown` is to tell a system to halt and power off after shutting
down:
\drsys{shutdown}{shutdown or reboot system}

\drcap{Shutdown and power off}
```bash
$ sudo shutdown -h now
```

## Turn on Your Signals{.unnumbered}

One of the basic concepts in UNIX program is that of
["signals"](https://en.wikipedia.org/wiki/Unix_signal). You are probably already familiar with one
way to send signals to a program, which is via `Ctrl-C` at the command prompt, which sends the
`SIGINT` ("interrupt") signal to the program. Typically this will cause a program to terminate.
\index{signals}

However, most signals can be "caught" by a program and coded around. There is one "uninterruptable"
signal, however - `SIGKILL`. We can send `SIGKILL` to a process and cause it to terminate
immediately with:

\drcap{Terminating a process with extreme prejudice}
```bash
kill -s 9 14302
```

The `-s 9` is for signal #9, which is the `SIGKILL` signal (it is the tenth signal in the signal
list, which is 0-relative, hence #9).

You can also use the following "shorthand" for `SIGKILL`:

\drcap{Even shorter way to \texttt{kill} the process}
```bash
kill -9 14302
```

Or if you want to get all verbose:

\drcap{A more verbose killer}
```bash
kill -s SIGKILL 14302
```

**Note:** `SIGKILL` should be used as a last resort, because a program is not allowed to catch it
or be notified of it and hence can perform no closing logic or cleanup and that may lead to data
corruption. It is for getting rid of "hung" processes when nothing else will work. Always try to 
stop a program with a more "normal" method, which can include sending `SIGINT` to it first.

## Exit, Smiling{.unnumbered}

Sometimes a command runs and there isn't a good way to tell if it worked or not. "UNIX" programs are
supposed to set an "exit status" when they end that by convention is `0` if the program exited
successfully and a non-zero, (typically) positive number if there was an error. The exit status for
the last executed command or program can be shown at the command line using the `$?` environment
variable. Consider if the file `foo` exists and `bar` does not:
\index{*@\texttt{?} (exit status environment variable)}
\index{environment variables!\?@\texttt{\$}\texttt{?} (exit status code)}

\drcap{Examining exit codes}
```bash
~ $ ls foo
foo
~ $ echo $?
0
~ $ ls bar
ls: cannot access bar: No such file or directory
~ $ echo $?
2
```

**Note:** In many cases the exit codes come from the ANSI Standard C library's [`errno.h`
file](http://mazack.org/unix/errno.php). All of this is much handier when handling errors in
scripts, but we're not going to go into script logic here.

However, sometimes even at the command line we want to be able to conditionally control a sequence
of commands, and continue (or not) based on the success (or failure) of a previous command. In
`bash` we have `&&` and `||` to the rescue!
\index{*@\texttt{\&}\texttt{\&} (logical "and" operator)}
\index{*@\texttt{"|"|} (logical "or" operator)}

* **`a && b`** - execute `a` ***and*** `b`, i.e., execute `b` only if `a` is successful.

* **`a || b`** - execute `a` ***or*** `b`, that is execute `b` whether ***or*** not `a` is
successful.

Our example of file `foo` (which exists) and file `bar` (which does not) and the effect on the exit
code of `ls` can be illustrative here, too:

\drcap{Using \texttt{\&}\texttt{\&} to chain commands together}
```bash
~ $ ls foo && ls bar
foo
ls: cannot access bar: No such file or directory
~ $ echo $?
2
```

Both `ls` commands execute because the first successfully found `foo`, but the second emits its
error and sets the exit code to `2` (failure).

\drcap{Using \texttt{||} to execute the first and possibly the second command}
```bash
~ $ ls foo || ls bar
foo
~ $ echo $?
0
```

Note in this case the `ls bar` command ***did not*** execute because the logical "or" condition was
already satisfied by the successful execution of the first `ls`. The exit code is obviously `0`
(success).

\drcap{With \texttt{\&}\texttt{\&} the second command won't execute if the first fails}
```bash
~ $ ls bar && ls foo
ls: cannot access bar: No such file or directory
~ $ echo $?
2
```

Obviously if the first command fails, the "and" condition as a whole fails and the expression exits
with a code of `2`. And finally, while the first command failed the second still can execute
because of the "or", and the whole expression returns `0`.

\drcap{One more example with \texttt{||}}
```bash
~ $ ls bar || ls foo
ls: cannot access bar: No such file or directory
foo
~ $ echo $?
0
```

**Note:** There is actually a [`true`](http://linux.die.net/man/1/true) command whose purpose is to
"do nothing, successfully." All it does is return a `0` (success) exit code. This can be useful in
scripting and also sometimes when building "and" and "or" clauses like above.
\drscr{true}

And yes, of course, that means there is also a [`false`](http://linux.die.net/man/1/false) command
to "do nothing, unsuccessfully!"
\drscr{false}

\drcap{\texttt{true} and \texttt{false} commands}
```bash
~ $ true
~ $ echo $?
0
~ $ false
~ $ echo $?
1
```

## The End{.unnumbered}

Now you know what I know. Or at least what I keep loaded in my head vs. what I simply search for
when I need to know it, and you know how to do that searching, too.

Good luck, citizen!