\cleardoublepage
![Merv sez, "Don't panic."](./images/MervBW.jpg "Merv sez, 'Don&apos;t panic.'")\ \
<br/>
Merv sez, "Don't panic."
\clearpage
\ \
\ \
<br/>
<br/>
By James Lehmer
\ \
\ \
<br/>
<br/>
v0.7
\ \
\ \
<br/>
<br/>
![](./images/cc-by-sa.png "Creative Commons Attribution-ShareAlike 4.0 International")\
*Ten Steps to Linux Survival - Bash for Windows People* by James Lehmer is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International
License](http://creativecommons.org/licenses/by-sa/4.0/).
\ \
\ \
<br/>
<br/>
**Dedicated to my first three technical mentors**

* Jim Proffer, who taught me digging deeper was fun and let me do so, often in production!

* Jerry Wood, who taught me to stop and think, and once called me an "inveterate toolmaker" in a
review, a badge I still wear with pride.

* Kim Manchak, who allowed me to be more than he hired me to be, and continues to be a great chess
opponent.

Thank you, gentlemen. I've tried to pay it forward. This book is part of that.

\pagestyle{fancy}
\fancyhead{}
\fancyhead[LE]{\slshape TEN\ STEPS\ TO\ LINUX\ SURVIVAL}
\fancyhead[RO]{\slshape \leftmark}
\renewcommand{\headrulewidth}{0.4pt}

# Introduction

> *"And you may ask yourself, 'Well, how did I get here?'"* - Talking Heads (*Once in a Lifetime*)

This is my little "Linux and Bash in 10 steps" guide. It's based on what I consider the essentials
for ~~floundering around~~ acting like I know what I'm doing in Linux, BSD and "UNIX-flavored"
systems and looking impressive among people who have only worked on Windows in the GUI. Your "10
steps" may be different than mine and that's fine, but this list is mine.

I said ten things, but I lied, because history is really important, so we will start at step #0.
And since this is before even that I guess that means this is a 12-step program...

Here is what we'll cover in the rest of this book:

0. [**Some History**](#some-history) – UNIX vs. BSD, System V vs. BSD, Linux vs. BSD, POSIX,
“UNIX-like,” Cygwin, and why any of this matters now, “Why does this script off the internet work
on this system and not on that one?”

1. [**Come Out of Your Shell**](#come-out-of-your-shell) – `sh` vs. `ash` vs. `bash` vs. everything
else, "REPL”, interactive vs. scripts, command history, tab expansion, environment variables and "A
path! A path!"

2. [**File Under "Directories"**](#file-under-directories) – `ls`, `mv`, `cp`, `rm` (`-rf *`),
`cat`, `chmod`/`chgrp`/`chown` and everyone's favorite, `touch`.

3. [**Finding Meaning**](#finding-meaning) – the `find` command in all its glory. Probably the
single most useful command in "UNIX" (I think).

4. [**Grokking `grep`**](#grokking-grep) – and probably gawking at `awk` while we are at it, which
means regular expressions, too. Now we have two problems.

5. [**“Just a Series of Pipes”**](#just-a-series-of-pipes) – `stdin`/`stdout`/`stderr`, redirects,
piping between commands.

6. [**`vi`**](#vi) (had to be #6, if you think about it) – how to stay sane for 10 minutes in `vi`.
Navigation, basic editing, find, change/change-all, cut and paste, undo, saving and canceling. Plus
easier alternatives like `nano`, and why `vi` still matters.

7. [**The Whole Wide World**](#the-whole-wide-world) – `curl`, `wget`, `ifconfig`, `ping`, `ssh`,
`telnet`, `/etc/hosts` and email before Outlook.

8. [**The Man Behind the Curtain**](#the-man-behind-the-curtain) - `/proc`, `/dev`, `ps`,
`/var/log`, `/tmp` and other things under the covers.

9. [**How Do You Know What You Don’t Know, `man`?**](#how-do-you-know-what-you-dont-know-man) –
`man`, `info`, `apropos`, Linux Documentation Project, Debian and Arch guides, StackOverflow and
the dangers of searching for “`man find`” or “`man touch`” on the internet.

10. [**And So On**](#and-so-on) - `/etc`, starting and stopping services, `apt-get`/`rpm`/`yum`,
and more.

Plus [some stuff](#appendices) at the end to tie the whole room together.

The most current release of the book should always be available for download in different formats on
[GitHub](https://github.com/dullroar/ten-steps-to-linux-survival/releases).

## Batteries Not Included{.unnumbered}

It should be obvious that there is ***plenty*** that is not covered:

* **System initialization** - besides, the whole "UNIX" world is in flux right now over system
initialization architecture and the shift from ["init"](https://en.wikipedia.org/wiki/Init) scripts
to [`systemd`](https://en.wikipedia.org/wiki/Systemd).

* **Scripting logic** - scripting, logic constructs (`if`/`fi`, `while`/`done`, and the like).

* **Desktops** - X Windows and the plethora of desktop environments like GNOME, KDE, Cinnamon, Mate,
Unity and on and on. This is where "UNIX" systems get the farthest apart in terms of
interoperability, settings and customization.

* **Servers** - setting up or configuring web servers like Apache or node, email servers like
dovecot, Samba servers for file shares, and so on.

* **Security** - other than the simple basics of the file system security model.

Plus so much more. Again, this is not meant to be exhaustive, but to help someone whose system
administration experience has been limited to Windows.

## Please, Give (Suggestions) Generously{.unnumbered}

That said, if you find something amiss in here - a typo, a misconception or mistake, or a command
or parameter you ***really, really, really*** think should be in here even though I said
I am not trying to be exhaustive, feel free to [clone it from
GitHub](https://github.com/dullroar/ten-steps-to-linux-survival), make your changes and send me a
`git pull` request. Or you can try to [file it as an
issue](https://github.com/dullroar/ten-steps-to-linux-survival/issues) and I'll see how I feel that
day.

## Why?{.unnumbered}

Because I work in a primarily Windows-oriented shop, and I seem to be "the guy" that everyone comes
to when they need help on a Linux or related system. I don't count myself a Linux guru (***at
all***), but I have been running it since 1996 (Slackware on a laptop with 8MB of memory!), and
have worked on or run at home various ports and flavors and and versions and distros of "UNIX" over
the years, including:

* **AIX**

* **FreeBSD**

* **HP/UX**

* **Linux** - literally more distros than I can count or remember, but at least Debian, Fedora,
Yellow Dog, Ubuntu/Kubuntu/Xubuntu, Mint, Raspbian, Gentoo, Red Hat and of course the venerable
Slackware.

* **Solaris**

* **SunOS**

All on various machines and machine architectures from mighty Sun servers to generic "Intel" VMs
down to Raspberry Pis, plus an original "wedge" iMac running as a kitchen kiosk long after its
"Best by" date and OS/9's demise, thanks to Yellow Dog Linux.

All that while also working on MVS, VSE, OS/2, DOS since 3.x, Windows since 1.x, etc., etc. I don't
think I am special when I list all that - there are lots of people with my level of experience
***and better***, especially in commercial software engineering. I am just one of them.

But for some reason there are many places, especially in small and medium business (SMB)
environments, where the "stack" tends to be more purely Microsoft because it keeps things simpler
and cheaper for the smaller staff. I work in such a place. The technical staff is quite competent,
but when they bump up against systems whose primary "user interface" for system administration is a
`bash` command prompt and some scripts, they panic.

This is my attempt to help my co-workers by saying:

> *"Don't panic."* - Douglas Adams (*Hitchhiker's Guide to the Galaxy*)

It started out as a proposal I made a while ago to develop a "lunch and learn" session of about
60-90 minutes of what I considered to be "a Linux survival guide." The list in the
[*Introduction*](#introduction) above is based on my original email proposal. The audience is
entirely technical, primarily "IT" (Windows/Cisco/VMWare/Exchange/SAN admins).

My goal is not to get into scripting, or system setup and hardening, or the thousand different ways
to slice a file. Instead, the scenario I see in my head is for one of the participants in that
"lunch and learn," armed with that discussion and having glanced through this book, to be
better able to survive if dropped into the jungle with:

> *"The main www site is down, and all the people who know about it are out. It's running on some
> sort of Linux, I think, and the credentials and IP address are scrawled on this sticky note. Can
> you get in and poke around and see if you can figure it out?"* - your boss (next Tuesday morning)

As I started to type out my notes of what I considered to be "essential," they just kept growing
and growing. Many nights, weekends and lunch hours later, this is the result. The slides were much
easier to prepare now that I have the "notes"!

**Note:** - The slides are included in [the same GitHub repository as this
book](https://github.com/dullroar/ten-steps-to-linux-survival/releases).

## Caveat Administrator{.unnumbered}

Even so, anything like this is incomplete. Anyone truly knowledgable of Linux will splutter their
coffee into their neckbeard^[Stereotype intentional.] at least once a chapter because I don't
mention a parameter on a command or an entire subject at all! And that's right - because this
"survival guide" is already long enough.

This book is not meant to be an authoritative source, but instead a ["fake
book"](https://en.wikipedia.org/wiki/Fake_book) for getting up and running ***quickly*** with the
sheer basics, plus knowing where to go for help. I modeled it explicitly after "short and
opinionated" tech books such as Douglas Crockford's [*Javascript: The Good
Parts*](http://shop.oreilly.com/product/9780596517748.do) and especially those licensed under
[Creative Commons](http://creativecommons.org/licenses/by-sa/4.0/), such as the books from [Green
Tea Press](http://greenteapress.com/). If you like those big tech books that are priced by the
kilogram, this is not the book for you.

It is also not a replacement for reading the real documentation and doing research and testing,
especially in production! But hopefully it will help get you through that "Can you get in and poke
around and see if you can figure it out?" scenario above. And if Linux should start becoming more
of your job, maybe this will help as a gentle push toward "RTFM" along with thinking in "The UNIX
Way."

**WARNING:** ***Many of the commands in this book can alter your system and possibly damage it.***

Obvious candidates include the file system commands like `rm`\drcmd{rm}
\index{Files and Directories!Delete (\texttt{rm} command)}, the
`vi`\drcmd{vi}\index{Editors!vi@\texttt{vi}} editor (obviously), and some of the "system admin"
commands mentioned later, including system and service restarts. Use your common sense plus the
various resources for documentation mentioned in this book to make sure you aren't doing anything
destructive to your system, especially in production.

***YOU HAVE BEEN WARNED!***

## Conventions{.unnumbered}

If a command, file name or other "computer code" is shown in-line in a sentence, it will appear in
a fixed-width font, e.g., `ls --recursive *.txt`.

If a command and its output, script code or something else is shown in a block, it will appear like
this:

\drcap{Sample command}
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

All such blocks have been normalized to only show a maximum of 80x24 characters. This is
intentional. While most modern "UNIX" systems and terminal windows like `ssh`\drcmd{ssh} can handle
any geometry, there are still systems and situations where you get the same terminal size that your
grandfather would've used. It is best to learn how to deal with these by using `less`\drcmd{less},
redirection and the like.

The examples in this book typically show something like `~ $` before the command, or `~ #` (when
logged in as root) or `%` (when running under `csh`\drshl{csh}). These "command prompts" are set in
`bash`\drshl{bash} via the [`PS1` environment
variable](https://www.linux.com/learn/docs/ldp/443-bash-prompt-howto)\drenv{PS1}
and are not meant to be typed in as part of the command.

In the few places where a "UNIX" command is shown in comparison to a "DOS" command run under
`CMD.EXE`\drshl{CMD.EXE}, the latter is shown in all uppercase to help distinguish it from the
"UNIX" equivalent, even though `CMD.EXE` is case-insensitive. In other words, `set` will be shown
for `bash` and `SET` for `CMD.EXE`.

## Acknowledgments{.unnumbered}

Thanks to Ken Astl for reading an early draft of this book. Thanks to my wife Leslie for putting up
with me while I obsessed over it.