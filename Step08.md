  
# Step 8. The Man Behind the Curtain

***`/proc`, `/dev`, `ps`, `/var/log`, `/tmp` and other things under the
covers.***

> *"As always, should any member of your team be caught or killed, the
> Secretary will disavow all knowledge of your actions."* - voice on tape
> (*Mission: Impossible*)

This section will cover some "background" techniques that are valuable for
system monitoring, problem determination and the like. Depending on your
role and access levels, some of these commands may not be available to you,
or may require `sudo` access.

## All Part of the Process

To see what *processes* you are running, use
[`ps`](http://linux.die.net/man/1/ps):

```bash
# ps
  PID TTY          TIME CMD
14691 pts/0    00:00:00 bash
25530 pts/0    00:00:00 ps
```

To show processes from *all* users in a process *hierarchy* (child
processes indented under parents), use `ps -AH`:

```bash
ps -AH
# ps -AH
  PID TTY          TIME CMD
    2 ?        00:00:00 kthreadd
    3 ?        00:05:00   ksoftirqd/0
    5 ?        00:00:00   kworker/u:0
    6 ?        00:02:38   migration/0
    7 ?        00:01:06   watchdog/0
    8 ?        00:02:37   migration/1
   10 ?        00:05:02   ksoftirqd/1
   12 ?        00:00:59   watchdog/1
   13 ?        00:00:00   cpuset
   14 ?        00:00:00   khelper
   15 ?        00:00:00   kdevtmpfs
...and so on...
```

You can *kill* a process using the
[`kill`](http://linux.die.net/man/1/kill) command, which takes a process id
and optionally a "signal". Here is an example looking for any running
instance of `vi` and sending it a `kill` command:

```bash
ps -A | grep vi | kill `cut -f2 -d" "`
```

That's:

* **`ps -A`** - list all running processes.

* **`|`** - pipe `stdout` from `ps` to next command.

* **`grep vi`** - find all instances of `vi` (be careful, because that
would include `view` and anything else containing the string `vi`, too).

* **`|`** - pipe `stdout` from `grep` to next command.

* **`kill`** - send a `SIGINT` signal to a process specified by:

* **`` `cut -f2 -d" "` ``** - execute the
[`cut`](http://linux.die.net/man/1/cut) command and take the second
space-delimited field (in this case the process id - the first "field" is
just leading spaces), and place the results of the command execution as
the parameter to the `kill` command.

To monitor the ongoing CPU, memory and other resource utilization of the
*top* processes, you use the [`top`](http://linux.die.net/man/1/top)
command, which unlike most in this book updates dynamically every second
by default:

```bash
top - 14:11:26 up 106 days,  5:24,  2 users,  load average: 0.11, 0.05, 0.05
Tasks:  95 total,   1 running,  94 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.2 us,  0.8 sy,  0.0 ni, 99.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem:   2061136 total,  1909468 used,   151668 free,   151632 buffers
KiB Swap:  4191228 total,   287620 used,  3903608 free,   654900 cached

  PID USER      PR  NI  VIRT  RES  SHR S  %CPU %MEM    TIME+  COMMAND
 9715 git       20   0  525m 230m 4376 S   0.7 11.4  10:11.44 ruby
 9171 git       20   0  520m 229m 4672 S   0.3 11.4  10:27.97 ruby
22899 root      20   0     0    0    0 S   0.3  0.0   0:30.16 kworker/1:0
    1 root      20   0 10648  584  560 S   0.0  0.0   1:02.60 init
    2 root      20   0     0    0    0 S   0.0  0.0   0:00.00 kthreadd
    3 root      20   0     0    0    0 S   0.0  0.0   0:38.05 ksoftirqd/0
    5 root      20   0     0    0    0 S   0.0  0.0   0:00.00 kworker/u:0
    6 root      rt   0     0    0    0 S   0.0  0.0   0:12.23 migration/0
    7 root      rt   0     0    0    0 S   0.0  0.0   0:24.83 watchdog/0
    8 root      rt   0     0    0    0 S   0.0  0.0   0:13.01 migration/1
   10 root      20   0     0    0    0 S   0.0  0.0   0:34.55 ksoftirqd/1
   12 root      rt   0     0    0    0 S   0.0  0.0   0:21.38 watchdog/1
   13 root       0 -20     0    0    0 S   0.0  0.0   0:00.00 cpuset
...and so on...
```

**Note:** Use `Q` or `Ctrl-C` to exit `top`.

## When All You Have is a Hammer

Remember that one of the primary UNIX philosophies is that everything is a
file or can be made to look like a file, including network streams, device
output and the like. This is a really powerful concept, because it allows
you to access things with tools that have ***no idea*** what they are
working on, as long as it "looks like" a file (or stream of text).

One of the places this has become really handy is in the `/proc` "file
system." On modern Linux systems, there is typically a `/proc` directory
that looks like directories and files:

```bash
# ls /proc
1     1776  2     2244   2308   2415   2599   2693   5     9171       cmdline      fb           key-users   mpt           swaps          vmstat
10    178   20    2269   2311   2416   26     3      5030  9174       consoles     filesystems  kmsg        mtrr          sys            zoneinfo
12    1781  2052  2287   2333   2417   2611   3120   5032  9715       cpuinfo      fs           kpagecount  net           sysrq-trigger
13    1783  21    22899  2338   2418   2612   31651  560   9718       crypto       interrupts   kpageflags  pagetypeinfo  sysvipc
130   1790  211   2297   2367   2422   2613   3197   570   99         devices      iomem        loadavg     partitions    timer_list
14    18    212   23     23835  2432   2614   32502  5991  acpi       diskstats    ioports      locks       sched_debug   timer_stats
15    180   2165  2304   23841  24426  2615   355    6     asound     dma          irq          meminfo     self          tty
16    181   2191  2305   2395   25     2616   4691   7     buddyinfo  dri          kallsyms     misc        slabinfo      uptime
17    182   22    2306   24     2550   26735  479    8     bus        driver       kcore        modules     softirqs      version
1713  19    2225  2307   2414   2556   26736  480    88    cgroups    execdomains  keys         mounts      stat          vmallocinfo

```

What is all that? Well if we look a little closer:

```bash
# ls -l /proc
total 0
dr-xr-xr-x  8 root       root                     0 Sep 18 11:17 1
dr-xr-xr-x  8 root       root                     0 Oct 23 13:55 10
dr-xr-xr-x  8 root       root                     0 Oct 23 13:55 12
dr-xr-xr-x  8 root       root                     0 Oct 23 13:55 13
dr-xr-xr-x  8 root       root                     0 Oct 23 13:55 130
dr-xr-xr-x  8 root       root                     0 Oct 23 13:55 14
dr-xr-xr-x  8 root       root                     0 Oct 23 13:55 15
dr-xr-xr-x  8 root       root                     0 Oct 23 13:55 16
dr-xr-xr-x  8 root       root                     0 Oct 23 13:55 17
dr-xr-xr-x  8 root       root                     0 Oct 23 13:55 1713
dr-xr-xr-x  8 statd      nogroup                  0 Oct 23 13:55 1776
...and so on...
```

...we can see that the entries with numeric names are directories. Let's
look in one of those directories:

```bash
# ls -l /proc/1
total 0
dr-xr-xr-x 2 root root 0 Oct 23 14:23 attr
-rw-r--r-- 1 root root 0 Oct 23 14:23 autogroup
-r-------- 1 root root 0 Oct 23 14:23 auxv
-r--r--r-- 1 root root 0 Oct 23 14:23 cgroup
--w------- 1 root root 0 Oct 23 14:23 clear_refs
-r--r--r-- 1 root root 0 Oct 23 14:23 cmdline
-rw-r--r-- 1 root root 0 Oct 23 14:23 comm
-rw-r--r-- 1 root root 0 Oct 23 14:23 coredump_filter
-r--r--r-- 1 root root 0 Oct 23 14:23 cpuset
lrwxrwxrwx 1 root root 0 Oct 23 14:23 cwd -> /
-r-------- 1 root root 0 Oct 23 14:23 environ
lrwxrwxrwx 1 root root 0 Oct 23 14:23 exe -> /sbin/init
...and so on...
```

This contains a lot of information on the process with process id (PID) #1.
If the directory listing shows the entry as a file, it can be examined and
holds ***current*** statistics for whatever the file name implies. If it is
a directory it will hold other entries (files or directories) with yet more
statistics.

In addition, there are system-wide statistics, such as `/proc/cpuinfo`:

```bash
# cat /proc/cpuinfo
processor       : 0
vendor_id       : GenuineIntel
cpu family      : 6
model           : 37
model name      : Intel(R) Xeon(R) CPU           X5690  @ 3.47GHz
stepping        : 1
microcode       : 0x15
cpu MHz         : 3458.000
cache size      : 12288 KB
fpu             : yes
fpu_exception   : yes
cpuid level     : 11
...and so on...
```

## Sawing Logs

Many Linux components and subsystems log to `/var/log`. Here is a pretty
standard directory listing for it on a Debian system:

```bash
# ls /var/log
alternatives.log       auth.log.2.gz    debug       dmesg.4.gz     kern.log       mail.info       mail.warn       news         syslog.4.gz    wtmp.1
alternatives.log.1     auth.log.3.gz    debug.1     dpkg.log       kern.log.1     mail.info.1     mail.warn.1     nginx        syslog.5.gz
alternatives.log.2.gz  auth.log.4.gz    debug.2.gz  dpkg.log.1     kern.log.2.gz  mail.info.2.gz  mail.warn.2.gz  postgresql   syslog.6.gz
alternatives.log.3.gz  btmp             debug.3.gz  dpkg.log.2.gz  kern.log.3.gz  mail.info.3.gz  mail.warn.3.gz  rancid       syslog.7.gz
apache2                btmp.1           debug.4.gz  dpkg.log.3.gz  kern.log.4.gz  mail.info.4.gz  mail.warn.4.gz  redis        user.log
apt                    daemon.log       dmesg       dpkg.log.4.gz  lastlog        mail.log        messages        samba        user.log.1
aptitude               daemon.log.1     dmesg.0     exim4          lpr.log        mail.log.1      messages.1      syslog       user.log.2.gz
aptitude.1.gz          daemon.log.2.gz  dmesg.1.gz  faillog        mail.err       mail.log.2.gz   messages.2.gz   syslog.1     user.log.3.gz
auth.log               daemon.log.3.gz  dmesg.2.gz  fsck           mail.err.1     mail.log.3.gz   messages.3.gz   syslog.2.gz  user.log.4.gz
auth.log.1             daemon.log.4.gz  dmesg.3.gz  installer      mail.err.2.gz  mail.log.4.gz   messages.4.gz   syslog.3.gz  wtmp
```

Some, like `samba` are their own subdirectories with log files under that.
Others are log files that get "rotated" from the most current (no suffix)
through ever older ones (increasing suffix number, e.g., `mail.log.2`).

If you are pursuing a problem with a specific subsystem (like `samba`), it
is good to start in its log files. The two files of general interest are
`dmesg`, which holds kernel-level debug messages and usually is useful for
debugging things like device driver issues. The other is `messages`, which
holds more general "system" messages.

Let's look for kernel errors when booting: 

```bash
# cat dmesg | grep -i error
[    2.310161] Error: Driver 'pcspkr' is already registered, aborting...
[    2.754699] EXT4-fs (sda1): re-mounted. Opts: errors=remount-ro
```

## It's All Temporary

By convention, temporary files are written to `/tmp`. You can place your
own temporary or "work" files there, too. It's a great place to unzip
install bits, for example. Just note that the temporariness is enforced in
that when the system reboots, `/tmp` is reset to empty.
  