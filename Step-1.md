![Merv sez, "Don't panic."](./images/Merv.jpg "Merv sez, 'Don&apos;t panic.'")

**By Jim Lehmer**

v0.1

<a rel="license"
href="http://creativecommons.org/licenses/by-sa/4.0/"><img
alt="Creative Commons License" style="border-width:0"
src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png"
/></a><br /><span xmlns:dct="http://purl.org/dc/terms/"
property="dct:title"><i>Jim's Ten Steps to Linux Survival</i></span>
by <span xmlns:cc="http://creativecommons.org/ns#"
property="cc:attributionName">James
Lehmer</span> is licensed under a <a rel="license"
href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons
Attribution-ShareAlike 4.0 International License</a>.

**Dedicated to my first three technical mentors** - Jim Proffer, who taught
me digging deeper was fun and let me do so (often in production). Jerry
Wood, who taught me to stop and think. And Kim Manchak, who let me be more
than he hired me to be. Thank you, gentlemen. I've tried to pay it forward.
This book is part of that.

# Step -1. Introduction

> *"And you may ask yourself, 'Well, how did I ***get*** here?'"* -
> Talking Heads (*Once in a Lifetime*)

This is my little "Linux and Bash in 10 steps" guide. It's based around
what I consider the essentials for <strike>floundering around</strike>
acting like I know what I'm doing in Linux, BSD and *IX-flavored
systems and looking impressive among people who have only worked on
Windows in the GUI. Your "10 steps" may be different than mine and that's
fine, but this list is mine.

I said ten things, but I lied, because history is really important, so we
will start at step #0. And since this is before even that I guess that
means this is a 12-step program...

Here is what we'll cover in the rest of this book:

0. [**Some History**](#step-0.-some-history) – UNIX vs. BSD, System V vs. 
BSD, Linux vs. BSD, POSIX, “UNIX-like,” Cygwin, and why any of this matters
now, “Why does this script off the internet work on this system and not on
that one?”

1. [**Come Out of Your Shell**](#step-1.-come-out-of-your-shell) – `sh` vs.
`ash` vs. `bash` vs. everything else, "REPL”, interactive vs. scripts,
command history, tab expansion, environment variables and "A path! A path!" 

2. [**File Under "Directories"**](#step-2.-file-under-directories) – `ls`,
`mv`, `cp`, `rm` (`-rf *`), `cat`, `chmod`/`chgrp`/`chown` and everyone's
favorite, `touch`.
    
3. [**Finding Meaning**](#step-3.-finding-meaning) – the `find` command in
all its glory. Probably the single most useful command in *IX (I think).

4. [**Grokking `grep`**](#step-4.-grokking-grep) – and probably gawking at
`awk` while we are at it, which means regular expressions, too. Now we have
two problems.

5. [**“Just a Series of Pipes”**](#step-5.-just-a-series-of-pipes) –
`stdin`/`stdout`/`stderr`, redirects, piping between commands.

6. [**`vi`**](#step-6.-vi) (had to be #6, if you think about it) – how to
stay sane for 10 minutes in `vi`. Navigation, basic editing, find,
change/change-all, cut and paste, undo, saving and canceling. Plus easier
alternatives like `nano`, and why `vi` still matters.

7. [**The Whole Wide World**](#step-7.-the-whole-wide-world) – `curl`,
`wget`, `ifconfig`, `ping`, `ssh`, `telnet`, `/etc/hosts` and email before
Outlook.

8. [**The Man Behind the Curtain**](#step-8.-the-man-behind-the-curtain) -
`/proc`, `/dev`, `ps`, `/var/log`, `/tmp` and other things under the
covers.

9. [**How Do You Know What You Don’t Know, 
`man`?**](#step-9.-how-do-you-know-what-you-dont-know-man) –
`man`, `info`, `apropos`, Linux Documentation Project, Debian and Arch
guides, StackOverflow and the dangers of searching for “`man find`” or
“`man touch`” on the internet.

10. [**And So On**](#step-10.-and-so-on) - `/etc`, starting and
stopping services, `apt-get`/`rpm`/`yum`, and more.

Plus [some stuff](#appendices) at the end to tie the whole room
together.

## Batteries Not Included

It should be obvious that there is ***plenty*** that is not covered:

* **System initialization** - besides, the whole *IX world is in flux
right now over system initialization architecture and the shift from
["init"](https://en.wikipedia.org/wiki/Init) scripts to
[`systemd`](https://en.wikipedia.org/wiki/Systemd).

* **Scripting logic** - scripting, logic constructs (`if`/`fi`,
`while`/`done`, and the like).

* **Desktops** - X Windows and the plethora of desktop environments like
GNOME, KDE, Cinnamon, Mate, Unity and on and on. This is where *IX systems
get the farthest apart in terms of interoperability, settings and
customization.

* **Servers** - setting up or configuring web servers like Apache or node,
email servers like dovecot, Samba servers for file shares, and so on.

* **Security** - other than the simple basics of the file system security
model.

Plus so much more. Again, this is not meant to be exhaustive, but to help
someone whose system administration experience has been limited to
"Next-Next-Next-Finish" installs and filling in text boxes in wizards on
Windows.

## Please, Give Generously

That said, if you find something amiss in here - a typo, a misconception or
mistake, or a command or parameter you ***really, really, really*** think
should be in here even though I said I am not trying to be exhaustive, feel
free to [clone it from
GitHub](https://github.com/dullroar/ten-steps-to-linux-survival.git), make
your changes and send me a `git pull` request. Or you can try to [file it
as an issue](https://github.com/dullroar/ten-steps-to-linux-survival/issues?q=is%3Aopen+is%3Aissue)
and I'll see how I feel that day.

## Why?

Because I work in a primarily Windows-oriented shop, and I seem to be "the
guy" that everyone comes to when they need help on a Linux or related
system. I don't count myself a Linux guru (***at all***), but I have been
running it since 1996 (Slackware on a laptop with 8MB of memory!), and have
worked on or run at home various ports and flavors and and versions and
distros of "*IX" over the years, including:

* **AIX**

* **FreeBSD**

* **HP/UX**

* **Linux** - literally more distros than I can count or remember, but at
least Debian, Fedora, Yellow Dog, Ubuntu/Kubuntu/Xubuntu, Mint,
Raspbian, Gentoo, Red Hat and of course the venerable Slackware.

* **Solaris**

* **SunOS**

...on various machines and machine architectures from mighty Sun servers to
generic "Intel" VMs down to Raspberry Pis (plus an original "wedge"
iMac running as a kitchen kiosk long after its "Best by" date and OS/9's
demise, thanks to Yellow Dog Linux).

All that while also working on MVS, VSE, OS/2, DOS since 3.x, Windows since
1.x, etc., etc. I don't think I am special when I list all that - there are
lots of people with my level of experience ***and better***, especially in
commercial software engineering. I am just one of them.

But for some reason there are many places, especially in small and medium
business (SMB) environments, where the "stack" tends to be more purely
Microsoft because it keeps things simpler and cheaper for the (smaller)
staff. I work in such a place. The technical staff is quite competent, but
when they bump up against systems whose primary "user interface"
for system administration is a command prompt and some scripts, they panic.

This is my attempt to help my co-workers by saying:

> *"Don't panic."* - Douglas Adams (*Hitchhiker's Guide to the Galaxy*)

It started out as a proposal I made a few weeks ago to develop a "lunch and
learn" session of about 60-90 minutes of what I considered to be "a Linux
survival guide." The list in the *Introduction* above is based on my
original email proposal. The audience would be entirely technical,
primarily "IT" (Windows/Cisco/VMWare/Exchange/SAN admins).

My goal is not to get into scripting or system setup and hardening or the
thousand different ways to slice a file. Instead, the scenario I see in my
head is for one of the participants in that "lunch and learn," armed with
that discussion and having glanced through this book, to be better able to
survive if dropped into the jungle with:

> *"The main www site is down, and all the people who know about it are
> out. It's running on some sort of Linux, I think, and the credentials and
> IP address are scrawled on this sticky note. Can you get in and poke
> around and see if you can figure it out?"* - your boss (next Tuesday
> morning)

Well, as I started to type out my notes of what I considered to be
"essential," they just kept growing and growing. And now, some nights,
weekends and lunch hours gone, this is what you see as the result. I figure
the slides will be easier to prepare for that "lunch and learn," now that I
have the "notes"!

## Caveat Administrator

Even so, anything like this is incomplete. Anyone knowledgable of Linux
will probably splutter their coffee into their neckbeard at least once a
chapter because I don't mention a parameter on a command or an entire
subject at all! And that's right - because this "survival guide" is already
long enough.

This book is not meant to be an authoritative source, but instead a ["fake
book"](https://en.wikipedia.org/wiki/Fake_book) for getting up and running
***quickly*** with the sheer basics, plus knowing where to go for help. It
is not a replacement for reading the real documentation and doing research
and testing, especially in production! But hopefully it will help get you
through that "Can you get in and poke around and see if you can figure it
out?" scenario, above. And if Linux should start becoming more of your job,
maybe this will help as a gentle push toward "RTFM" along with thinking in
"The UNIX Way."
