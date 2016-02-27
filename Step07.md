
# The Whole Wide World

***`curl`, `wget`, `ifconfig`, `ping`, `ssh`, `telnet`, `/etc/hosts` and email before Outlook.***

> *"Gopher, Everett?"* - Delmar O'Donnell (*O Brother, Where Are Thou?*)

If Sun's motto "The network is the computer" is correct, then of course Linux and similar systems
must be able to access the network from the command line and scripts.

For example, our friend [`ping`](http://linux.die.net/man/8/ping) is there:
\drnet{ping}

\drcap{ping command}
```bash
# ping www.yahoo.com
PING fd-fp3.wg1.b.yahoo.com (98.138.253.109) 56(84) bytes of data.
64 bytes from ir1.fp.vip.ne1.yahoo.com (98.138.253.109): icmp_req=1 ttl=...
64 bytes from ir1.fp.vip.ne1.yahoo.com (98.138.253.109): icmp_req=2 ttl=...
64 bytes from ir1.fp.vip.ne1.yahoo.com (98.138.253.109): icmp_req=3 ttl=...
64 bytes from ir1.fp.vip.ne1.yahoo.com (98.138.253.109): icmp_req=4 ttl=...
64 bytes from ir1.fp.vip.ne1.yahoo.com (98.138.253.109): icmp_req=5 ttl=...
64 bytes from ir1.fp.vip.ne1.yahoo.com (98.138.253.109): icmp_req=6 ttl=...
64 bytes from ir1.fp.vip.ne1.yahoo.com (98.138.253.109): icmp_req=7 ttl=...
64 bytes from ir1.fp.vip.ne1.yahoo.com (98.138.253.109): icmp_req=8 ttl=...
64 bytes from ir1.fp.vip.ne1.yahoo.com (98.138.253.109): icmp_req=9 ttl=...
64 bytes from ir1.fp.vip.ne1.yahoo.com (98.138.253.109): icmp_req=10 ttl...
^C
--- fd-fp3.wg1.b.yahoo.com ping statistics ---
10 packets transmitted, 10 received, 0% packet loss, time 9004ms
rtt min/avg/max/mdev = 59.933/62.581/70.935/3.191 ms
```

One difference with `ping` is that by default in Linux `ping` doesn't stop until the user presses
`Ctrl-C` (which sends the [`SIGINT` interrupt](https://en.wikipedia.org/wiki/Unix_signal) to the
program). In this way it acts more like `ping -t` in `CMD.EXE` Also, be aware that on Cygwin `ping`
is still the system (Windows) `ping`.
\drshl{CMD.EXE}
\index{signals}

[`traceroute`](http://linux.die.net/man/8/traceroute) works, too (although for once its name is
longer than the `CMD.EXE` counterpart).
\drnet{traceroute}

\drcap{traceroute command}
```bash
~ $ traceroute google.com
traceroute to google.com (216.58.216.78), 30 hops max, 60 byte packets
 1  192.168.0.1 (192.168.0.1)  3.623 ms  3.978 ms  7.231 ms
 2  * * *
 3  * * *
 4  * * *
 5  * * *
 6  * * *
 7  72.14.215.212 (72.14.215.212)  26.205 ms  27.502 ms  27.648 ms
 8  209.85.242.133 (209.85.242.133)  31.547 ms  31.550 ms  31.548 ms
 9  72.14.237.231 (72.14.237.231)  29.516 ms  29.556 ms  29.657 ms
10  ord30s21-in-f78.1e100.net (216.58.216.78)  30.313 ms  33.138 ms  28.092 ms
```

You can do some digging in DNS with [`dig`](http://linux.die.net/man/1/dig):
\drnet{dig}

\drcap{dig command}
```bash
~ $ dig yahoo.com

; <<>> DiG 9.9.5-3ubuntu0.6-Ubuntu <<>> yahoo.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 46478
;; flags: qr rd ra; QUERY: 1, ANSWER: 3, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;yahoo.com.			IN	A

;; ANSWER SECTION:
yahoo.com.		605	IN	A	98.138.253.109
yahoo.com.		605	IN	A	206.190.36.45
yahoo.com.		605	IN	A	98.139.183.24

;; Query time: 23 msec
;; SERVER: 127.0.1.1#53(127.0.1.1)
;; WHEN: Tue Dec 22 09:46:26 CST 2015
;; MSG SIZE  rcvd: 86
```

And [`whois`](http://linux.die.net/man/1/whois):
\drnet{whois}

```bash
~ $ whois yahoo.com

Whois Server Version 2.0

Domain names in the .com and .net domains can now be registered
with many different competing registrars. Go to http://www.internic.net
for detailed information.

   Server Name: YAHOO.COM.ACCUTAXSERVICES.COM
   IP Address: 98.136.43.32
   IP Address: 66.196.84.168
   Registrar: WILD WEST DOMAINS, LLC
   Whois Server: whois.wildwestdomains.com
   Referral URL: http://www.wildwestdomains.com

   Server Name: YAHOO.COM.ANGRYPIRATES.COM
   IP Address: 8.8.8.8
   Registrar: NAME.COM, INC.
   Whois Server: whois.name.com
   Referral URL: http://www.name.com

   Server Name: YAHOO.COM.AU
   Registrar: WILD WEST DOMAINS, LLC
...and so on...
```

## sudo Make Me a Sandwich{.unnumbered}

It may not be the best place to discuss it, but we've finally come to a point where your normal
user account may not have access to these tools. On many systems network commands are considered
"system" or privileged commands and are restricted.

One way to run restricted commands is to log in as an "elevated" or privileged user, such as `root`.
But this is frowned on, and many distros today rely on the [`sudo`](http://linux.die.net/man/8/sudo)
command to act as a way for a normal user to signal they want to escalate their privileges
temporarily, presuming they are allowed to do so, which is usually indicated by being a member of
the `sudo` group or similar.
\drsys{sudo}{execute as another user}

In a sense, `sudo` is similar to Windows User Access Control (UAC) prompts. They ensure a human is
in control, in the case of `sudo` by prompting for the user's password. If multiple commands are
invoked by `sudo` within a short time period, you will not be reprompted for a password each time,
(unlike UAC).

Here is a really common example on Debian-based systems:
\drpkg{apt-get}

\drcap{Make me a sandwich}
```bash
~ $ apt-get update
E: Could not open lock file /var/lib/apt/lists/lock - open (13: Permission denie
d)
E: Unable to lock directory /var/lib/apt/lists/
E: Could not open lock file /var/lib/dpkg/lock - open (13: Permission denied)
E: Unable to lock the administration directory (/var/lib/dpkg/), are you root?
```

The error message, especially the last line, is pretty clear. Let's try it again with `sudo`:

\drcap{sudo Make me a sandwich}
```bash
~ $ sudo apt-get update
Ign http://packages.linuxmint.com rafaela InRelease
Ign http://extra.linuxmint.com rafaela InRelease                               
Hit http://extra.linuxmint.com rafaela Release.gpg                             
Hit http://packages.linuxmint.com rafaela Release.gpg                          
Ign http://archive.ubuntu.com trusty InRelease                                 
Hit http://security.ubuntu.com trusty-security InRelease                       
Hit http://packages.linuxmint.com rafaela Release                              
Hit http://extra.linuxmint.com rafaela Release                                 
Hit http://archive.ubuntu.com trusty-updates InRelease                         
Hit http://security.ubuntu.com trusty-security/main amd64 Packages             
Hit http://packages.linuxmint.com rafaela/main amd64 Packages                  
Hit http://extra.linuxmint.com rafaela/main amd64 Packages                     
Ign http://archive.canonical.com trusty InRelease                              
Hit http://archive.ubuntu.com trusty Release.gpg                               
Hit http://security.ubuntu.com trusty-security/restricted amd64 Packages       
Hit http://extra.linuxmint.com rafaela/main i386 Packages                      
Hit http://packages.linuxmint.com rafaela/upstream amd64 Packages              
Hit http://security.ubuntu.com trusty-security/universe amd64 Packages         
Hit http://archive.ubuntu.com trusty-updates/main amd64 Packages               
Hit http://packages.linuxmint.com rafaela/import amd64 Packages                
Hit http://security.ubuntu.com trusty-security/multiverse amd64 Packages       
Hit http://archive.canonical.com trusty Release.gpg                            
...and so on...         
```

Now you should get the punchline to [this comic](https://xkcd.com/149/), and hence the title of
this section.

**NOTE:** The first time you ever run `sudo` on a machine, you will probably see the following.
They are good words to live by:

\drcap{Words to live by}
```
We trust you have received the usual lecture from the local System
Administrator. It usually boils down to these three things:

    #1) Respect the privacy of others.
    #2) Think before you type.
    #3) With great power comes great responsibility.
```

## Surfin' the Command Prompt{.unnumbered}

You can browse the web from the command prompt using something like
[`lynx`](http://linux.die.net/man/1/lynx). A text-based browser isn't too exciting, but it can have
its purposes (like quickly testing network access from a command prompt). For example, `lynx
http://google.com` yields:
\drnet{lynx}

\drcap{Browsing like it's 1994}
```bash
                                                                          Google

   Search Images Maps Play YouTube News Gmail Drive More »
   Web History | Settings | Sign in

   Google

     _______________________________________________________
     Google Search  I'm Feeling Lucky                          Advanced search
                                                               Language tools

   Advertising Programs     Business Solutions     +Google     About
   Google

                          © 2015 - Privacy - Terms






(NORMAL LINK) Use right-arrow or <return> to activate.
  Arrow keys: Up and Down to move.  Right to follow a link; Left to go back.
 H)elp O)ptions P)rint G)o M)ain screen Q)uit /=search [delete]=history list 
```

There are two other commands that are used to pull down web resources and save them locally -
[`curl`](http://linux.die.net/man/1/curl) and [`wget`](http://linux.die.net/man/1/wget). Both
support HTTP(S) and FTP, but `curl` supports even more protocols and options and tends to be the
simplest to just "grab a file and go." You see both used often in install scripts that download
bits from the internet and then execute them by piping them to `bash`:
\drscr{bash}
\drnet{curl}
\drnet{wget}

\drcap{\texttt{wget} in an install script}
```bash
wget -O - http://foocorp.com/installs/install.sh | bash
```

Or:

\drcap{\texttt{curl} in an install script}
```bash
curl http://foocorp.com/installs/install.sh | bash
```

**Note:** As always, you should be cautious when downloading and executing arbitrary bits, and this
technique doesn't lessen your responsibility there. It is often better to use something like `curl`
to download the script but instead of piping it to `bash` to be executed, redirect it to a file and
look at what the script is doing first:

\drcap{Check out what that script is doing first!}
```bash
~ $ curl http://foocorp.com/installs/install.sh > install.sh
~ $ cat install.sh
#!/bin/bash
# I'm a script from a bad guy, check out the next line!
rm -rf /*
```

Now, aren't you glad you didn't just execute that without checking?

But if the script looks right, then you can `chmod` it and run it:

\drcap{Got a good script, so execute it}
```bash
~ $ curl http://foocorp.com/installs/install.sh > install.sh
~ $ cat install.sh
#!/bin/bash
# I'm a script from a good guy.
# Do some stuff...
~ $ chmod 770 install.sh
~ $ ./install.sh
```

## It's Nice to Share

Linux boxes can be set up to share files to Windows machines using the SMB/CIFS protocols via a
system called [Samba](https://www.samba.org/). However, that is beyond the scope of this book,
since the intended audience will not likely need to do that.

However, there is often a need in the scenarios I envision the reader has been thrust into, where
they have to share files back and forth between a local *IX box and a Windows machine. Maybe it's
to pull files over to Windows to be backed up by the shop's normal backup mechanisms. Or it could
be to bring over log files for forensics. It could even be to copy files from Windows to the Linux
machine.

For example, in my company we keep copies of our Windows servers application configuration
files (such as various `web.config` files) in Git, specifically on a
[GitLab](https://about.gitlab.com/) server. There is a `cron` job (coming up later) that copies
the files every day from the Windows servers and then commits them to GitLab if there are any
changes. It's a nice way to keep track of environment changes over time.

How do you copy files from Windows to Linux or vice versa? With the
[`smbclient`](http://linux.die.net/man/1/smbclient) command. It works somewhat similarly to the
[`ftp`](http://linux.die.net/man/1/ftp) (but again, if you're going to copy using the FTP protocol,
I think `curl` or `wget` are better). Here is an example of `smbclient` to get you started.
\drnet{ftp}
\drnet{smbclient}

\drcap{Copying multiple files from a Windows machine with `mget`}
```bash
~ $ smbclient //winbox/myshare -U myuser%mypassword -W mywindomain \
-c "prompt;cd configs;mget *.config;exit"
```

To understand the above:

* **`//winbox/myshare`** - is the Windows share. Note in this case you use forward slashes (`/`),
not the typical backslashes (`\`) that Windows uses.

* **`-U myuser%mypassword`** - userid and password. If you don't specify them, you will be prompted,
but if you are using this command in a script you either have to specify them or have the share set
up with guest permissions. It is a good idea to make sure the script file is locked down, and that
the `smbclient` command is not recorded in your `.bash_history` file (covered later).

* **`-W mywindomain`** - the Active Directory domain the Windows machine is a member of (or often
`WORKGROUP` if it is a standalone machine).

* **`-c "prompt;cd configs;mget *.config;exit"`** - the remote commands to execute, in this case
turning the `smbclient` prompting off (useful for scripts), changing to the `settings`
directory on the remote Windows machine with `cd`, then getting multiple (`mget`) files using the
wildcard `*.config`, and then `exit` to end the command sequence and disconnect.

**Note:** You can send files ***to*** a Windows machine by using `mput` rather than `mget`.

## You've Got Mail{.unnumbered}

You can send and receive email from the command prompt. Reading email will be rare, but if the
system has [`pine`](http://linux.die.net/man/1/pine) installed, that's probably the most intuitive
from a non-UNIX perspective (although it is still obviously a terminal program). Otherwise look for
[`mutt`](http://linux.die.net/man/1/mutt).
\drnet{mutt}
\drnet{pine}

Sending email is more interesting, especially from shell scripts. There are multiple ways, but
[`email`](http://linux.die.net/man/1/email) is straightforward enough:
\drnet{email}

\drcap{Sending email from the command line}
```bash
~ $ email --blank-mail --subject "Possibly corrupted files found..." \
  --smtp-server smtp --attach badfiles.csv --from-name NoReply \
  --from-addr noreply@mycorp.com alert@mycorp.com
```

## Let's Connect{.unnumbered}

There are two primary ways to get an interactive "shell" session on a remote machine. The first is
the venerable [`telnet`](http://linux.die.net/man/1/telnet) command. It isn't used very often for
actual interactive sessions any more (for one, because it sends credentials in plain text on the
wire). However, because you can specify the port number, it is still handy for testing and
debugging text-based protocols such as SMTP or HTTP. In the following, after opening a `telnet`
connection on port 80 to Google, I simply entered the HTTP protocol sequence `GET / HTTP/1.1`
followed by a blank line to get Google to return its home page:
\drnet{telnet}

\drcap{Using \texttt{telnet} to diagnose HTTP}
```bash
~ $ telnet google.com 80
Trying 216.58.216.78...
Connected to google.com.
Escape character is '^]'.
GET / HTTP/1.1

HTTP/1.1 200 OK
Date: Tue, 22 Dec 2015 15:58:47 GMT
Expires: -1
Cache-Control: private, max-age=0
Content-Type: text/html; charset=ISO-8859-1
P3P: CP="This is not a P3P policy! See https://www.google.com/support/accounts/a
nswer/151657?hl=en for more info."
Server: gws
X-XSS-Protection: 1; mode=block
X-Frame-Options: SAMEORIGIN
Set-Cookie: NID=74=nqD9y_pSQudbaw6obB94Ngw6lsn4t_S8Z3NbZcUJ5HB4qUXCpu988A5QG3EQD
kwqgOdGapsUSmsi91yHAa9_LU9JeP4pKop-1p5w7LlrdMyGrGojwoaX58ML6PSH5nGLsdZV0Z5vBqNTh
A; expires=Wed, 22-Jun-2016 15:58:47 GMT; path=/; domain=.google.com; HttpOnly
Accept-Ranges: none
Vary: Accept-Encoding
Transfer-Encoding: chunked

...and so on...
```

The `SMTP` protocol can also be diagnosed this way:

\drcap{Using \texttt{telnet} to diagnose SMTP}
```bash
~ $ telnet smtp 25
Trying 10.1.1.8...
Connected to mail.mydomain.com.
Escape character is '^]'.
220 MAIL.MYDOMAIN.COM
HELO
250 MAIL.MYDOMAIN.COM Hello [10.1.1.8]
MAIL FROM:<myuser@mydomain.com>
250 2.1.0 Sender OK
RCPT TO:<youruser@yourdomain.com>
250 2.1.5 Recipient OK
DATA
354 Start mail input; end with <CRLF>.<CRLF>
This is an email. A single period terminates it.
.
250 2.6.0 <ea43bfd5-5f3f-4335-9c3e-e739f196c56f@MAIL.MYDOMAIN.COM>
Queued mail for delivery
```

In the above, after entering `telnet smtp 25` (our internal email DNS CNAME is `smtp`), I entered:

* **`HELO`** - the starting command for the protocol.

* **`MAIL FROM:<myuser@mydomain.com>`** - the "from" email address.

* **`RCPT TO:<youruser@yourdomain.com>`** - the "to" email address.

* **`DATA`** - indicating I am ready to start the email body, which is `This is an email, a single
period terminates it.` And you will notice there is a single period on the following line, which
tells the SMTP server the body is done and to send the email. If all is successful, then an email
should shortly show up in the inbox of `youruser@yourdomain.com`.

**NOTE:** - diagnosing SMTP connectivity like this can be ***very*** handy sometimes. It is a good
tool to have in your toolchest, and you can do it under Cygwin or a PuTTY Telnet session on a
Windows box just as easily as from a Linux machine.

To get a modern, *secure shell* to a remote machine over an encrypted connection, use
[`ssh`](http://linux.die.net/man/1/ssh), passing in the userid and server like this:
\drnet{ssh}

\drcap{\texttt{ssh} command}
```bash
ssh myuser@remoteserver
```

You will be prompted for credentials (or you can use certificates, but that is ***way*** beyond
this text's goals). Once logged in, you will be presented with a command prompt to the remote
system.

You can also use the `SSH` protocol to *securely copy* files between systems with the
[`scp`](http://linux.die.net/man/1/scp) command. It works like this for a recursive directory copy:
\drnet{scp}

\drcap{\texttt{scp} command}
```bash
scp -r myfiles/* myuser@remoteserver:/home/myuser/.
```

In this case we are copying the files in `myfiles` and its subdirectories to `/home/myuser/` on
`remoteserver` logged in as `myuser`.

**Note:** The first time you log into a remote server with `ssh` or `scp` you will be asked to
accept the remote server's "fingerprint." You can usually just say "yes":

\drcap{Sample \texttt{ssh} session}
```bash
~# ssh myuser@remotehost
The authenticity of host '[remotehost] ([10.0.2.3]:22)' can't be established.
ECDSA key fingerprint is 98:bb:17:38:ee:d0:16:ee:b2:93:08:4e:30:25:14:70.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '[remotehost],[10.0.2.3]:22' (ECDSA) to the list
of known hosts.
myuser@remotehost's password:
Linux remotehost 3.2.0-4-amd64 #1 SMP Debian 3.2.65-1+deb7u2 x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Tue Oct 20 09:37:10 2015 from otherhost
$
```

The `scp` command does a naive copy, that is, it simply copies everything from the source to the
target. But what if you want to "mirror" the source to the target, meaning that if you delete
something on the source side, it will get deleted on the target as well? `scp` won't help you with
that. You could delete the target directory completely each time before copying, but that may not
be safe (what happens if the copy fails after you've deleted the target?) Another problem with `scp`
is it copies every byte of every file every time, even if the files haven't changed. That can be
really slow and inefficient when copying a large, complex directory containing gigabytes of files
over the Internet.

This is where the [`rsync`](http://linux.die.net/man/1/rsync) command comes in handy. `rsync` does
three things well:
\drnet{rsync}

1. It copies using the `ssh` protocol by default, just like `scp`, so it is secure. And it uses
the `scp` commands compression capabilities by default to increase efficiency. You can turn that
behavior off via a parameter when copying files that are already compressed, such as JPEGs.

2. It copies only the ***changed blocks*** (not even just the changed files), which means if there
are no or few changes, it is very fast.

3. It deletes files on the target if they've been deleted from the source, which allows you to
mirror all changes between the two servers or sites.

**NOTE**: For `rsync` to work, it has to be installed on both servers.

\drcap{Using \texttt{rsync} to mirror directories between servers}
```bash
~ $ rsync --delete --progress --recursive --verbose --exclude '.git' \
--exclude '.bak' ~/dev/website/ myuser@mysite.com:public_html
```

This invokes `rsync` as follows:

* **`--delete`** - deletes files on the target server.

* **`--progress`** - shows progress as it copies.

* **`--recursive`** - does a recursive copy.

* **`--verbose`** - shows verbose output.

* **`--exclude '.git'`** - exclude any directory or file named `.git`.

* **`--exclude '.bak'`** - also exclude any directory or file named `.bak`.

* **`~/dev/website/`** - copy from this directory on the local machine, including all files under
it (trailing slash).

* **`myuser@mysite.com:public_html`** - copy to the `public_html` directory under the home directory
of `myuser` on the `mysite.com` server.

**NOTE:** `rsync` can be used to efficiently mirror directories even on the local server. If there
are two large and complex directories on a single server you want to keep synchronized, you can
simply use local addresses for both directories:

\drcap{Using \texttt{rsync} to mirror local directories}
```bash
~ $ rsync --delete --progress --recursive --verbose --exclude '.git' \
--exclude '.bak' ~/dev/website/ /var/nginx/staging/website
```

## Network Configuration{.unnumbered}

We won't dive too deep into configuring a network, but there are a few things you should know about
right away. The first is the [`ifconfig`](http://linux.die.net/man/8/ifconfig) command. In some
ways is similar to `ipconfig` in `CMD.EXE`. While you can use `ifconfig` to alter your networking
settings, it is most commonly used to get a quick display of them:
\drnet{ifconfig}
\drshl{CMD.EXE}

\drcap{\texttt{ifconfig} command}
```bash
# ifconfig
eth0      Link encap:Ethernet  HWaddr 00:00:56:a3:35:fe
          inet addr:10.0.2.3  Bcast:10.0.2.255  Mask:255.255.252.0
          inet6 addr: fe80::255:56ff:fea3:35fe/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:364565022 errors:0 dropped:386406 overruns:0 frame:0
          TX packets:35097654 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:34727642861 (32.3 GiB)  TX bytes:195032017498 (181.6 GiB)

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:16436  Metric:1
          RX packets:111207 errors:0 dropped:0 overruns:0 frame:0
          TX packets:111207 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:6839306 (6.5 MiB)  TX bytes:6839306 (6.5 MiB)
```

To see what DNS servers the system is using, you can look in `/etc/resolv.conf`:
\index{files and directories!special!etcresolvconf@\texttt{/etc/resolv.conf}}

\drcap{DNS servers in \texttt{resolv.conf}}
```bash
# cat /etc/resolv.conf
domain mydomain.com
search mydomain.com
nameserver 10.0.2.1
nameserver 10.0.2.2
```

And to see any local overrides of network names or aliases, look in `/etc/hosts`:
\index{files and directories!special!etchosts@\texttt{/etc/hosts}}

\drcap{\texttt{hosts} file}
```bash
# cat /etc/hosts
127.0.0.1       localhost
```

**Note:** The UNIX `/etc/hosts` file is the basis for the Windows version
located at `C:\Windows\System32\drivers\etc\hosts`, and has similar syntax.