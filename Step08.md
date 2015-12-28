
# The Man Behind the Curtain

***`/proc`, `/dev`, `ps`, `/var/log`, `/tmp` and other things under the covers.***

> *"As always, should any member of your team be caught or killed, the Secretary will disavow all
> knowledge of your actions."* - voice on tape (*Mission: Impossible*)

This section will cover some "background" techniques that are valuable for system monitoring,
problem determination and the like. Depending on your role and access levels, some of these
commands may not be available to you, or may require `sudo` access.

## All Part of the Process{.unnumbered}

To see what *processes* you are running, use [`ps`](http://linux.die.net/man/1/ps)\drcmd{ps}:

\drcap{\texttt{ps} command}
```bash
# ps
  PID TTY          TIME CMD
14691 pts/0    00:00:00 bash
25530 pts/0    00:00:00 ps
```

To show processes from *all* users in a process *hierarchy* (child processes indented under parents)
use `ps -AH`:

\drcap{Showing all processes}
```bash
~ $ ps -AH
  PID TTY          TIME CMD
    2 ?        00:00:00 kthreadd
    3 ?        00:00:00   ksoftirqd/0
    5 ?        00:00:00   kworker/0:0H
    7 ?        00:00:06   rcu_sched
    8 ?        00:00:02   rcuos/0
    9 ?        00:00:01   rcuos/1
   10 ?        00:00:03   rcuos/2
   11 ?        00:00:01   rcuos/3
   12 ?        00:00:00   rcuos/4
   13 ?        00:00:00   rcuos/5
   14 ?        00:00:00   rcuos/6
   15 ?        00:00:00   rcuos/7
   16 ?        00:00:00   rcu_bh
   17 ?        00:00:00   rcuob/0
   18 ?        00:00:00   rcuob/1
   19 ?        00:00:00   rcuob/2
   20 ?        00:00:00   rcuob/3
   21 ?        00:00:00   rcuob/4
   22 ?        00:00:00   rcuob/5
   23 ?        00:00:00   rcuob/6
   24 ?        00:00:00   rcuob/7
...and so on...
```

You can *kill* a process using the [`kill`](http://linux.die.net/man/1/kill)\drcmd{kill} command,
which takes a process id and optionally a "signal"\index{Signals}. Here is an example looking for
any running instance of `vi` and sending it a `kill` command:

\drcap{Hunting down and killing \texttt{vi} sessions}
```bash
ps -A | grep vi | kill `cut -f2 -d" "`
```

That's:

* **`ps -A`** - list all running processes.

* **`|`** - pipe `stdout`\index{stdout} from `ps` to next command.

* **`grep vi`** - find all instances of `vi` (be careful, because that would include `view` and
anything else containing the string `vi`, too).

* **`|`** - pipe `stdout` from `grep`\drcmd{grep} to next command.

* **`kill`** - send a `SIGINT` signal\index{Signals} to a process specified by:

* **`` `cut -f2 -d" "` ``** - execute the [`cut`](http://linux.die.net/man/1/cut)\drcmd{cut}
command and take the second space-delimited field (in this case the process id - the first "field"
is just leading spaces), and place the results of the command execution as the parameter to the
`kill` command.

To monitor the ongoing CPU, memory and other resource utilization of the *top* processes, you use
the [`top`](http://linux.die.net/man/1/top)\drcmd{top} command, which unlike most in this book
updates dynamically every second by default:

\drcap{\texttt{top} command}
```bash
top - 14:11:26 up 106 days,  5:24,  2 users,  load average: 0.11, 0.05, ...
Tasks:  95 total,   1 running,  94 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.2 us,  0.8 sy,  0.0 ni, 99.0 id,  0.0 wa,  0.0 hi,  0.0 si, ...
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

## When All You Have is a Hammer{.unnumbered}

Remember that one of the primary UNIX philosophies is that everything is a file or can be made to
look like a file, including network streams, device output and the like. This is a really powerful
concept, because it allows you to access things with tools that have ***no idea*** what they are
working on, as long as it "looks like" a file (or stream of text).

One of the places this has become really handy is in the `/proc`
\index{Files and Directories!Special!\texttt{/proc/}} "file system." On modern Linux systems, there
is typically a `/proc` directory that looks like directories and files:

\drcap{\texttt{/proc} file system}
```bash
~ $ ls /proc
1     1566  2607  299   4549  53    75         cmdline      mtrr
10    1587  2617  3     4579  54    754        consoles     net
100   16    2627  300   4589  55    760        cpuinfo      pagetypeinfo
1022  17    2629  301   46    56    762        crypto       partitions
1030  18    2699  3029  4602  575   764        devices      sched_debug
1035  1803  27    31    4612  61    77         diskstats    schedstat
1038  19    2712  3111  47    6146  79         dma          scsi
11    2     2799  3112  48    6153  8          driver       self
12    20    28    3116  49    6199  8167       execdomains  slabinfo
1295  2073  2802  3117  4955  62    8168       fb           softirqs
1297  2077  2811  3150  4958  6212  8200       filesystems  stat
13    21    2815  32    4960  63    822        fs           swaps
1304  22    2820  324   4976  640   8296       interrupts   sys
1305  23    2823  326   5     642   9          iomem        sysrq-trigger
1306  2324  2825  329   50    645   9266       ioports      sysvipc
1308  2349  2829  33    5005  6463  927        irq          timer_list
1311  2356  2831  330   5012  647   939        kallsyms     timer_stats
14    24    2836  34    5033  649   9465       kcore        tty
1408  2494  2846  36    5045  661   9613       keys         uptime
1468  25    2847  37    51    665   9796       key-users    version
147   2507  2848  3713  511   676   9850       kmsg         version_signature
148   2518  2850  374   5122  686   99         kpagecount   vmallocinfo
...and so on...
```

What is all that? Well, look a little closer:

\drcap{Detailed listing of the \texttt{/proc} file system}
```bash
~ $ ls -l /proc
total 0
dr-xr-xr-x  9 root       root                     0 Dec 22 06:06 1
dr-xr-xr-x  9 root       root                     0 Dec 22 06:06 10
dr-xr-xr-x  9 root       root                     0 Dec 22 06:06 100
dr-xr-xr-x  9 myuser     mygroup                  0 Dec 22 10:17 10035
dr-xr-xr-x  9 root       root                     0 Dec 22 06:06 1022
dr-xr-xr-x  9 root       root                     0 Dec 22 06:06 1030
dr-xr-xr-x  9 root       root                     0 Dec 22 06:06 1035
dr-xr-xr-x  9 root       root                     0 Dec 22 06:06 1038
dr-xr-xr-x  9 root       root                     0 Dec 22 06:06 11
dr-xr-xr-x  9 root       root                     0 Dec 22 06:06 12
dr-xr-xr-x  9 root       root                     0 Dec 22 06:06 1295
dr-xr-xr-x  9 root       root                     0 Dec 22 06:06 1297
dr-xr-xr-x  9 root       root                     0 Dec 22 06:06 13
dr-xr-xr-x  9 root       root                     0 Dec 22 06:06 1304
dr-xr-xr-x  9 root       root                     0 Dec 22 06:06 1305
dr-xr-xr-x  9 root       root                     0 Dec 22 06:06 1306
dr-xr-xr-x  9 root       root                     0 Dec 22 06:06 1308
dr-xr-xr-x  9 root       root                     0 Dec 22 06:06 1311
dr-xr-xr-x  9 root       root                     0 Dec 22 06:06 14
dr-xr-xr-x  9 root       root                     0 Dec 22 06:06 1408
dr-xr-xr-x  9 root       root                     0 Dec 22 06:06 1468
...and so on...
```

We can see that the entries with numeric names are directories. Let's look in one of those
directories:

\drcap{Looking inside one of the \texttt{/proc} process directories}
```bash
~ # ls -l /proc/1
total 0
dr-xr-xr-x 2 root root 0 Dec 22 10:18 attr
-rw-r--r-- 1 root root 0 Dec 22 10:18 autogroup
-r-------- 1 root root 0 Dec 22 10:18 auxv
-r--r--r-- 1 root root 0 Dec 22 06:06 cgroup
--w------- 1 root root 0 Dec 22 10:18 clear_refs
-r--r--r-- 1 root root 0 Dec 22 06:06 cmdline
-rw-r--r-- 1 root root 0 Dec 22 10:18 comm
-rw-r--r-- 1 root root 0 Dec 22 10:18 coredump_filter
-r--r--r-- 1 root root 0 Dec 22 10:18 cpuset
lrwxrwxrwx 1 root root 0 Dec 22 10:18 cwd -> /
-r-------- 1 root root 0 Dec 22 06:06 environ
lrwxrwxrwx 1 root root 0 Dec 22 06:06 exe -> /sbin/init
dr-x------ 2 root root 0 Dec 22 10:18 fd
dr-x------ 2 root root 0 Dec 22 10:18 fdinfo
-rw-r--r-- 1 root root 0 Dec 22 10:18 gid_map
-r-------- 1 root root 0 Dec 22 10:18 io
-r--r--r-- 1 root root 0 Dec 22 06:06 limits
-rw-r--r-- 1 root root 0 Dec 22 10:18 loginuid
dr-x------ 2 root root 0 Dec 22 10:18 map_files
-r--r--r-- 1 root root 0 Dec 22 10:18 maps
-rw------- 1 root root 0 Dec 22 10:18 mem
...and so on...
```

This contains a lot of information on the process with process id (PID) #1. If the directory
listing shows the entry as a file, it can be examined and holds ***current*** statistics for
whatever the file name implies:

\drcap{How much I/O has process 1 done?}
```bash
~ # cat /proc/1/io
rchar: 803882767
wchar: 152731542
syscr: 201510
syscw: 57855
read_bytes: 663872512
write_bytes: 113012736
cancelled_write_bytes: 3072000
```

If it is a directory it will hold other entries (files or directories) with yet more statistics.

In addition, there are system-wide statistics, such as `/proc/cpuinfo`:

\drcap{Looking at CPU info in \texttt{/proc/cpuinfo}}
```bash
~ # cat /proc/cpuinfo 
processor	: 0
vendor_id	: GenuineIntel
cpu family	: 6
model		: 69
model name	: Intel(R) Core(TM) i5-4200U CPU @ 1.60GHz
stepping	: 1
microcode	: 0x14
cpu MHz		: 895.023
cache size	: 3072 KB
physical id	: 0
siblings	: 4
core id		: 0
cpu cores	: 2
apicid		: 0
initial apicid	: 0
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov 
pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pd
pe1gb rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopol
ogy nonstop_tsc ap
...and so on...
```

## Sawing Logs{.unnumbered}

Many Linux components and subsystems log to `/var/log`.
\index{Files and Directories!Special!\texttt{/var/log/}} Here is a pretty standard directory
listing for it on a Linux Mint system:

\drcap{Looking at logs}
```bash
~ # ls /var/log
alternatives.log       dmesg.4.gz             pm-suspend.log.1
alternatives.log.1     dpkg.log               pm-suspend.log.2.gz
alternatives.log.2.gz  dpkg.log.1             pm-suspend.log.3.gz
alternatives.log.3.gz  dpkg.log.2.gz          pycentral.log
apt                    dpkg.log.3.gz          samba
aptitude               faillog                speech-dispatcher
aptitude.1.gz          fontconfig.log         syslog
aptitude.2.gz          fsck                   syslog.1
auth.log               gpu-manager.log        syslog.2.gz
auth.log.1             hp                     syslog.3.gz
auth.log.2.gz          installer              syslog.4.gz
auth.log.3.gz          kern.log               syslog.5.gz
auth.log.4.gz          kern.log.1             syslog.6.gz
boot.log               kern.log.2.gz          syslog.7.gz
bootstrap.log          kern.log.3.gz          udev
btmp                   kern.log.4.gz          unattended-upgrades
btmp.1                 lastlog                upstart
ConsoleKit             mdm                    wtmp
cups                   mintsystem.log         wtmp.1
dmesg                  pm-powersave.log       Xorg.0.log
dmesg.0                pm-powersave.log.1     Xorg.0.log.old
dmesg.1.gz             pm-powersave.log.2.gz  Xorg.20.log
...and so on...
```

Some, like `samba` are their own subdirectories with log files under that. Others are log files
that get "rotated" from the most current (no suffix) through ever older ones (increasing suffix
number, e.g., `mail.log.2`).

If you are pursuing a problem with a specific subsystem (like `samba`), it is good to start in its
log files. The two log files of general interest are `dmesg`\index{dmesg}
\index{Files and Directories!Special!\texttt{/var/log/dmesg}}, which holds kernel-level debug
messages and usually is useful for debugging things like device driver issues. The other is
`messages`\index{Files and Directories!Special!\texttt{/var/log/messages}}, which holds more
general "system" messages.

Let's look for kernel errors when booting: 

\drcap{Kernel errors when booting}
```bash
~ # cat /var/log/dmesg | grep -i error
[   15.828463] EXT4-fs (dm-1): re-mounted. Opts: errors=remount-ro
```

## It's All Temporary{.unnumbered}

By convention, temporary files are written to `/tmp`
\index{Files and Directories!Special!\texttt{/tmp/}}. You can place your own temporary or "work"
files there, too. It's a great place to unzip install bits, for example. Just note that the
temporariness is enforced in that when the system reboots, `/tmp` is reset to empty.