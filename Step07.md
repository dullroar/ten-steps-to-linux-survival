  
# The Whole Wide World

***`curl`, `wget`, `ifconfig`, `ping`, `ssh`, `telnet`, `/etc/hosts` and
email before Outlook.***

> *"Gopher, Everett?"* - Delmar O'Donnell (*O Brother, Where Are Thou?*)

If Sun's motto, "The network is the computer" is correct, then of course
Linux and similar systems must be able to access the network from the
command line and scripts.

For example, our friend [`ping`](http://linux.die.net/man/8/ping) is there:

```
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

One difference with `ping` is that by default in Linux `ping` doesn't stop
until the user presses `Ctrl-C` (which sends the
[`SIGINT` interrupt](https://en.wikipedia.org/wiki/Unix_signal) to the
program). In this way it acts more like `ping -t` in `CMD.EXE`. Also, be
aware that on Cygwin `ping` is still the system (Windows) `ping`.

[`traceroute`](http://linux.die.net/man/8/traceroute) works, too (although
for once its name is longer than the `CMD.EXE` counterpart).

```
# traceroute www.yahoo.com
traceroute to www.yahoo.com (98.138.252.30), 30 hops max, 60 byte packets
 1  10.208.3.254 (10.208.3.254)  0.720 ms  0.706 ms  0.693 ms
 2  10.208.6.53 (10.208.6.53)  0.808 ms  0.896 ms  0.943 ms
 3  10.208.6.46 (10.208.6.46)  2.632 ms  2.636 ms  2.634 ms
 4  kcm-priv-20.inet.qwest.net (63.159.159.185)  30.786 ms  30.852 ms  3...
 5  * * *
 6  67.134.114.230 (67.134.114.230)  30.441 ms  29.811 ms  30.372 ms
 7  67.130.10.174 (67.130.10.174)  32.267 ms  32.700 ms  32.789 ms
 8  67.130.10.103 (67.130.10.103)  32.416 ms  32.421 ms  32.420 ms
 9  min-edge-13.inet.qwest.net (67.130.30.21)  33.878 ms  31.719 ms  34....
10  chp-brdr-03.inet.qwest.net (67.14.8.194)  45.668 ms  55.177 ms  45.6...
11  63.146.27.18 (63.146.27.18)  46.371 ms  46.333 ms  47.234 ms
...and so on...
```

You can do some digging in DNS with `dig`:

```
# dig yahoo.com

; <<>> DiG 9.8.4-rpz2+rl005.12-P1 <<>> yahoo.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 18148
;; flags: qr rd ra; QUERY: 1, ANSWER: 3, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;yahoo.com.                     IN      A

;; ANSWER SECTION:
yahoo.com.              1705    IN      A       206.190.36.45
yahoo.com.              1705    IN      A       98.139.183.24
yahoo.com.              1705    IN      A       98.138.253.109

;; Query time: 17 msec
;; SERVER: 10.208.2.4#53(10.208.2.4)
;; WHEN: Fri Oct 23 13:16:51 2015
;; MSG SIZE  rcvd: 75
```

And `whois`:

```
# whois yahoo.com

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
...and so on...
```

## `sudo` Make Me a Sandwich

It may not be the best place to discuss it, but we've finally come to a
point where your normal user account may not have access to these tools.
On many systems network commands are considered "system" or privileged
commands and are restricted.

One way to run restricted commands is to log in as a "elevated" or
privileged user, such as `root`. But this is frowned on, and many distros
today rely on the [`sudo`](http://linux.die.net/man/8/sudo) command to
act as a way for a normal user to signal they want to escalate their
privileges temporarily (presuming they are allowed to do so, which is
usually indicated by being a member of the `sudo` group or similar.

In a sense, `sudo` is similar to Windows User Access Control (UAC, or "Are
you sure?") prompts. They ensure a human is in control, in the case of
`sudo` by prompting for the user's password (if multiple commands are
invoked by `sudo` within a short time period, you will not be reprompted
for a password each time).

Here is a really common example on Debian-based systems:

```
$ apt-get update
E: Could not open lock file /var/lib/apt/lists/lock - open (13: Permissi...
E: Unable to lock directory /var/lib/apt/lists/
E: Could not open lock file /var/lib/dpkg/lock - open (13: Permission de...
E: Unable to lock the administration directory (/var/lib/dpkg/), are you...
```

The error message, especially the last line, is pretty clear. Let's try it
again with `sudo`:

```
$ sudo apt-get update
[sudo] password for myuser: 
Ign http://extra.linuxmint.com rafaela InRelease
Ign http://packages.linuxmint.com rafaela InRelease                            
Hit http://security.ubuntu.com trusty-security InRelease                       
Hit http://extra.linuxmint.com rafaela Release.gpg                             
Hit http://packages.linuxmint.com rafaela Release.gpg                          
Hit http://security.ubuntu.com trusty-security/main amd64 Packages             
Ign http://archive.ubuntu.com trusty InRelease                                 
Ign http://archive.canonical.com trusty InRelease                              
Hit http://security.ubuntu.com trusty-security/restricted amd64 Packages       
Hit http://extra.linuxmint.com rafaela Release                
...and so on...
```

Now you should get the punchline to [this comic](https://xkcd.com/149/),
and hence the title of this section.

## Surfin' the Command Prompt

You can browse the web from the command prompt using something like
[`lynx`](http://linux.die.net/man/1/lynx). A text-based browser isn't too
exciting, but it can have its purposes (like quickly testing network access
from a command prompt). For example, `lynx http://google.com` yields:

```
   Search Images Maps Play YouTube News Gmail Drive More »
   Web History | Settings | Sign in

   Google

   _______________________________________________________
   Google Search  I'm Feeling Lucky                          Advanced search

   Advertising Programs     Business Solutions     +Google     About Google

   © 2015 - Privacy - Terms

```

There are two other commands that are used to pull down web resources and
save them locally - [`curl`](http://linux.die.net/man/1/curl) and
[`wget`](http://linux.die.net/man/1/wget). Both support HTTP(S) and FTP,
but `curl` supports even more protocols and options, while `curl` tends
to be the simplest to just "grab a file and go." You see both used often in
install scripts that then download more bits from the internet:

```
wget -O - http://foocorp.com/installs/install.sh | bash
```

Or:

```
curl http://foocorp.com/installs/install.sh | bash
```

**Note:** As always, you should be cautious when downloading and executing
arbitrary bits, and this technique doesn't lessen your responsibility
there.

## You've Got Mail

You can send and receive email from the command prompt. Reading email will
be rare, but if the system has [`pine`](http://linux.die.net/man/1/pine)
installed, that's probably the most intuitive from a non-UNIX perspective
(although it is still obviously a command line program). Otherwise look for
[`mutt`](http://linux.die.net/man/1/mutt).

Sending email is more interesting, especially from shell scripts. There are
multiple ways, but [`email`](http://linux.die.net/man/1/email) is
straightforward enough:

```
email --blank-mail --subject "Possibly corrupted files found..." \
  --smtp-server smtp --attach badfiles.csv --from-name NoReply \
  --from-addr noreply@mycorp.com alert@mycorp.com
```

## Let's Connect

There are two primary ways to get an interactive "shell" session on a
remote machine. The first is the venerable
[`telnet`](http://linux.die.net/man/1/telnet) command. It isn't used very
often for actual interactive sessions any more (for one, because it sends
credentials in plain text on the wire). However, because you can specify
the port number, it is still handy for testing and debugging text-based
protocols such as SMTP or HTTP. In the following, after opening a `telnet`
connection on port 80 to Google, I simply entered the HTTP protocol
sequence `GET / HTTP/1.1` followed by a blank line to get Google to return
its home page:

```
# telnet google.com 80
Trying 216.58.216.110...
Connected to google.com.
Escape character is '^]'.
GET / HTTP/1.1

HTTP/1.1 200 OK
Date: Fri, 23 Oct 2015 18:26:04 GMT
Expires: -1
Cache-Control: private, max-age=0
Content-Type: text/html; charset=ISO-8859-1
P3P: CP="This is not a P3P policy! See http://www.google.com/support/acc...
Server: gws
X-XSS-Protection: 1; mode=block
X-Frame-Options: SAMEORIGIN
Set-Cookie: PREF=ID=1111111111111111:FF=0:TM=1445624764:LM=1445624764:V=...
Set-Cookie: NID=72=HLgGubMnO1ThhvhOAmvehue96EKTh9D6F19zidZQU-E9AibEg2Op6...
Accept-Ranges: none
Vary: Accept-Encoding
Transfer-Encoding: chunked

8000
<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage"...
...and so on...
```

To get a modern, secure shell to a remote machine, use
[`ssh`](http://linux.die.net/man/1/ssh), passing in the userid and server
like this:

```
ssh myuser@remoteserver
```

You will be prompted for credentials (or you can use certificates, but that
is ***way*** beyond this text's goals).

You can also use the `SSH` protocol to securely transfer files between
systems with the [`scp`](http://linux.die.net/man/1/scp) command. It works
like this for a recursive directory copy:

```
scp -r myfiles/* myuser@remoteserver:/home/myuser/.
```

In this case we are copying the files in `myfiles` and its subdirectories
to `/home/myuser/` on `remoteserver` logged in as `myuser`.

**Note:** The first time you log into a remote server with `ssh` or `scp`
you will be asked to accept the remote server's "fingerprint." You can
usually just say "yes":

```
~# ssh myuser@remotehost
The authenticity of host '[remotehost] ([10.0.2.3]:22)' can't be established.
ECDSA key fingerprint is 98:70:17:38:db:d0:16:ee:b2:93:08:3e:30:25:14:70.
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

## Network Configuration

We won't dive too deep into configuring a network, but there are a few
things you should know about right away. The first is the
[`ifconfig`](http://linux.die.net/man/8/ifconfig). While you can use
`ifconfig` to alter your networking settings, it is most commonly used
to get a quick display of them:

```
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

To see what DNS servers the system is using:

```
# cat /etc/resolv.conf
domain mydomain.com
search mydomain.com
nameserver 10.0.2.1
nameserver 10.0.2.2
```

And to see any local overrides of network names or aliases:

```
# cat /etc/hosts
127.0.0.1       localhost
```

**Note:** The UNIX `/etc/hosts` file is the basis for the Windows version
located at `C:\Windows\System32\drivers\etc\hosts`, and has similar syntax.

  