
# Step 8

# The Man Behind the Curtain

## View running processes

> * `ps` - shows running processes
>     * `ps -A` - shows ***all*** running processes
>     * `ps -A | grep bash` - show all running bash processes
> * `top` - show "top" processes by CPU, memory and other criteria

## /proc file system

```
~ # cat /proc/cpuinfo
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

> * Many live system metrics, presented as "files"

## Sawing logs

```
~ # ls /var/log
alternatives.log       auth.log.2.gz    debug       dmesg.4.gz     kern....
alternatives.log.1     auth.log.3.gz    debug.1     dpkg.log       kern....
alternatives.log.2.gz  auth.log.4.gz    debug.2.gz  dpkg.log.1     kern....
alternatives.log.3.gz  btmp             debug.3.gz  dpkg.log.2.gz  kern....
apache2                btmp.1           debug.4.gz  dpkg.log.3.gz  kern....
apt                    daemon.log       dmesg       dpkg.log.4.gz  lastlog
aptitude               daemon.log.1     dmesg.0     exim4          lpr.log
aptitude.1.gz          daemon.log.2.gz  dmesg.1.gz  faillog        mail.err
auth.log               daemon.log.3.gz  dmesg.2.gz  fsck           mail....
auth.log.1             daemon.log.4.gz  dmesg.3.gz  installer      mail....
```

## It's all temporary

> * `/tmp` - standard location for temp files
> * Cleared at reboot