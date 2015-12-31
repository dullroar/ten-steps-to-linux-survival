
# The Whole Wide World

***`curl`, `wget`, `ifconfig`, `ping`, `ssh`, `telnet`, `/etc/hosts` and email before Outlook.***

> *"Gopher, Everett?"* - Delmar O'Donnell (*O Brother, Where Are Thou?*)

If Sun's motto "The network is the computer" is correct, then of course Linux and similar systems
must be able to access the network from the command line and scripts.

For example, our friend [`ping`](http://linux.die.net/man/8/ping)\drnet{ping} is there:

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
`Ctrl-C` (which sends the [`SIGINT` interrupt](https://en.wikipedia.org/wiki/Unix_signal)
\index{signals} to the program). In this way it acts more like `ping -t` in `CMD.EXE`\drshl{CMD.EXE}
Also, be aware that on Cygwin `ping` is still the system (Windows) `ping`.

[`traceroute`](http://linux.die.net/man/8/traceroute)\drnet{traceroute} works, too (although
for once its name is longer than the `CMD.EXE` counterpart).

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

You can do some digging in DNS with [`dig`](http://linux.die.net/man/1/dig)\drnet{dig}:

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

And [`whois`](http://linux.die.net/man/1/whois)\drnet{whois}:

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

One way to run restricted commands is to log in as a "elevated" or privileged user, such as `root`.
But this is frowned on, and many distros today rely on the [`sudo`](http://linux.die.net/man/8/sudo)
\drcmd{sudo} command to act as a way for a normal user to signal they want to escalate their
privileges temporarily, presuming they are allowed to do so, which is usually indicated by being a
member of the `sudo` group or similar.

In a sense, `sudo` is similar to Windows User Access Control (UAC) prompts. They ensure a human is
in control, in the case of `sudo` by prompting for the user's password. If multiple commands are
invoked by `sudo` within a short time period, you will not be reprompted for a password each time,
(unlike UAC).

Here is a really common example on Debian-based systems:

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

## Surfin' the Command Prompt{.unnumbered}

You can browse the web from the command prompt using something like
[`lynx`](http://linux.die.net/man/1/lynx)\drnet{lynx}. A text-based browser isn't too exciting, but
it can have its purposes (like quickly testing network access from a command prompt). For example,
`lynx http://google.com` yields:

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
[`curl`](http://linux.die.net/man/1/curl)\drnet{curl} and [`wget`](http://linux.die.net/man/1/wget)
drnet{wget}. Both support HTTP(S) and FTP, but `curl` supports even more protocols and options and
tends to be the simplest to just "grab a file and go." You see both used often in install scripts
that download bits from the internet and then execute them:

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
look at what the script is doinng first:

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

## You've Got Mail{.unnumbered}

You can send and receive email from the command prompt. Reading email will be rare, but if the
system has [`pine`](http://linux.die.net/man/1/pine)\drnet{pine} installed, that's probably the
most intuitive from a non-UNIX perspective (although it is still obviously a terminal program).
Otherwise look for [`mutt`](http://linux.die.net/man/1/mutt)\drnet{mutt}.

Sending email is more interesting, especially from shell scripts. There are multiple ways, but
[`email`](http://linux.die.net/man/1/email)\drnet{email} is straightforward enough:

\drcap{Sending email from the command line}
```bash
email --blank-mail --subject "Possibly corrupted files found..." \
  --smtp-server smtp --attach badfiles.csv --from-name NoReply \
  --from-addr noreply@mycorp.com alert@mycorp.com
```

## Let's Connect{.unnumbered}

There are two primary ways to get an interactive "shell" session on a remote machine. The first is
the venerable [`telnet`](http://linux.die.net/man/1/telnet)\drnet{telnet} command. It isn't used
very often for actual interactive sessions any more (for one, because it sends credentials in plain
text on the wire). However, because you can specify the port number, it is still handy for testing
and debugging text-based protocols such as SMTP or HTTP. In the following, after opening a `telnet`
connection on port 80 to Google, I simply entered the HTTP protocol sequence `GET / HTTP/1.1`
followed by a blank line to get Google to return its home page:

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

To get a modern, secure shell to a remote machine, use [`ssh`](http://linux.die.net/man/1/ssh)
\drnet{ssh}, passing in the userid and server like this:

\drcap{\texttt{ssh} command}
```bash
ssh myuser@remoteserver
```

You will be prompted for credentials (or you can use certificates, but that is ***way*** beyond
this text's goals). Once logged in, you will be presented with a command prompt to the remote
system.

You can also use the `SSH` protocol to securely transfer files between systems with the
[`scp`](http://linux.die.net/man/1/scp)\drnet{scp} command. It works like this for a recursive
directory copy:

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

## Network Configuration{.unnumbered}

We won't dive too deep into configuring a network, but there are a few things you should know about
right away. The first is the [`ifconfig`](http://linux.die.net/man/8/ifconfig)\drnet{ifconfig}
command (in some ways is similar to `ipconfig` in `CMD.EXE`\drshl{CMD.EXE}. While you can use
`ifconfig` to alter your networking settings, it is most commonly used to get a quick display of
them:

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

To see what DNS servers the system is using, you can look in `/etc/resolv.conf`
\index{files and directories!special!etcresolvconf@\texttt{/etc/resolv.conf}}:

\drcap{DNS servers in \texttt{resolv.conf}}
```bash
# cat /etc/resolv.conf
domain mydomain.com
search mydomain.com
nameserver 10.0.2.1
nameserver 10.0.2.2
```

And to see any local overrides of network names or aliases, look in `/etc/hosts`
\index{files and directories!special!etchosts@\texttt{/etc/hosts}}:

\drcap{\texttt{hosts} file}
```bash
# cat /etc/hosts
127.0.0.1       localhost
```

**Note:** The UNIX `/etc/hosts` file is the basis for the Windows version
located at `C:\Windows\System32\drivers\etc\hosts`, and has similar syntax.