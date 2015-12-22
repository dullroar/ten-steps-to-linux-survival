
# Step 10

# And So On...

## `/etc`

```
~ # ls -l /etc
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
...and so on...
```

Most system configuration information is here

## Some helpful `/etc` files

* **`fstab`** - file systems currently mounted
* **`group`** - security groups
* **`hosts`** - network aliases
* **`init.d`** - startup and shutdown scripts for "services."
* **`mtab`** - list of current "mounts."
* **`passwd`** - "shadow" file containing all the user accounts
* **`resolv.conf`** - DNS settings.
* **`samba`** - file sharing settings for CIFS-type shares

## May I be of service?

> * "Services" (or "daemons") are long-running processes
> * Typically controlled via `/etc/init.d` scripts
>     * `/etc/init.d/samba stop`
>     * `/etc/init.d/samba start`
>     * `/etc/init.d/samba restart` - the above two commands combined

## Package management

> * Most Linux distros have a package manager
>     * `dpkg` and `apt-get` on Debian flavors
>     * `rpm` on Fedora flavors
> * Package managers are like "Add/Remove Programs" - can install, update
or delete applications
> * Package managers are like "Windows Update" - can update and upgrade the
OS

## Package management on Debian

(...and Ubuntu, Mint and others)

> * `apt-get update` - pull down latest package definitions
> * `apt-get upgrade` - upgrade all packages
> * `apt-get install curl` - install package "curl"
> * `apt-get` is an admin command and usually requires `sudo`
> * `dpkg -i somesoftware.deb` - install a package file downloaded from the
web

## Which `which` is which?

> * `which curl` - show which `curl` will execute
> * `locate curl` - show all files on system with "curl" in the path
> * `./curl` - regardless of `$PATH`, execute `curl` that is in current
directory

## Over and over and over

> * `cron` - service that runs "cron jobs" (scheduled task)
> * `crontab` - show cron jobs for current user
> * `crontab -e` - edit cron jobs for current user
>     * `sudo crontab -e -u otheruser` - edit cron jobs for another user

## Start me up

> * `reboot` - reboot the system (typically requires `sudo`)
> * `shutdown -h now` - shut down system now

## Turn on your signals

> * `kill` - send a signal to a process
>     * Most "signals" allow process to cleanup
>     * `kill -9` - does ***NOT*** allow process to cleanup, may corrupt
data

## Exit smiling

> * `echo $?` - show "return code" or exit code for last command or program
> * `a && b` - execute `a` and if it is successful execute `b`
> * `a || b` - execute `a` and then execute `b` regardless of `a`