
# Come Out of Your Shell

***`sh` vs. `ash` vs. `bash` vs. everything else, "REPL”, interactive vs. scripts, command history,
tab expansion, environment variables and "A path! A path!"***

> *"If you hold a shell up to your ear, you can hear the OS."* - me

To avoid getting all pedantic, I am just going to define a shell as an environment in which you can
execute commands. People tend to think of a shell as a "command prompt," but you can run a shell
without running a command prompt, but not vice versa - an interactive command prompt is an instance
of a shell environment almost by definition.

Examples of shells:

* [**`CMD.EXE`**](https://technet.microsoft.com/en-us/library/cc754340.aspx)\drshl{CMD.EXE} -
yes, Windows
\drios{Windows}
has a shell.

* [**`PowerShell.exe`**](https://technet.microsoft.com/en-us/library/ms714469%28v=VS.85%29.aspx)
\drshl{Powershell} -
in fact, it has at least two!

In UNIX-land:

* [**`sh`**](https://en.wikipedia.org/wiki/Bourne_shell)\drshl{sh} -
the "original" Bourne shell in UNIX, which spawned:

    * [**`ash`**](https://en.wikipedia.org/wiki/Almquist_shell)\drshl{ash} -
    Almquist shell.

        * **`dash`** - 
        \drshl{dash}
        Debian Almquist shell (replaced `ash` in Debian)

    * [**`bash`**](https://en.wikipedia.org/wiki/Bash_%28Unix_shell%29)\drshl{bash} -
    Bourne-again shell (get it?), the "standard" Linux shell (as much as
    anything is standard across Linux distros).

    * [**`ksh`**](https://en.wikipedia.org/wiki/Korn_shell)\drshl{ksh} -
    Korn shell.

    * [**`zsh`**](https://en.wikipedia.org/wiki/Z_shell)\drshl{zsh} -
    Z shell.

* [**`csh`**](https://en.wikipedia.org/wiki/C_shell)\drshl{csh} - C
shell, historically it is the default shell on BSD systems (although there are arguments on why you
should [***never use it***](http://www.faqs.org/faqs/unix-faq/shell/csh-whynot/)).

* **...and many more!** - [tons, really](https://en.wikipedia.org/wiki/Unix_shell#Shell_categories).

Most Linux distros use `bash`, but the BSDs are all over the place. We're going to assume `bash`
for the rest of this tutorial. With few modifications, anything in the `sh` hierarchy above can
usually run in the other members of the same tree.

## `bash` Built-Ins{.unnumbered}

Every shell has some "built-in" commands that are implemented as part of the shell and not as an
external command or program, and `bash`\drshl{bash} has its share, as shown by running the
[`help`](http://linux.die.net/man/1/help)
\drdoc{help}
command in a `bash` terminal:

\drcap{Built-in commands in \texttt{bash}}
```bash
~ $ help
GNU bash, version 4.3.11(1)-release (x86_64-pc-linux-gnu)
These shell commands are defined internally.  Type `help' to see this list.
Type `help name' to find out more about the function `name'.
Use `info bash' to find out more about the shell in general.
Use `man -k' or `info' to find out more about commands not in this list.

A star (*) next to a name means that the command is disabled.

 job_spec [&]                            history [-c] [-d offset] [n] or hist>
 (( expression ))                        if COMMANDS; then COMMANDS; [ elif C>
 . filename [arguments]                  jobs [-lnprs] [jobspec ...] or jobs >
 :                                       kill [-s sigspec | -n signum | -sigs>
 [ arg... ]                              let arg [arg ...]
 [[ expression ]]                        local [option] name[=value] ...
 alias [-p] [name[=value] ... ]          logout [n]
 bg [job_spec ...]                       mapfile [-n count] [-O origin] [-s c>
 bind [-lpsvPSVX] [-m keymap] [-f file>  popd [-n] [+N | -N]
 break [n]                               printf [-v var] format [arguments]
 builtin [shell-builtin [arg ...]]       pushd [-n] [+N | -N | dir]
 caller [expr]                           pwd [-LP]
 case WORD in [PATTERN [| PATTERN]...)>  read [-ers] [-a array] [-d delim] [->
 cd [-L|[-P [-e]] [-@]] [dir]            readarray [-n count] [-O origin] [-s>
...and so on...
```

Why does this matter? Because if you are in an environment and something as fundamental as
`echo`\drcmd{echo} isn't working, you may not be working in a shell that is going to act like a
"`sh`" shell. ***In general***, `sh`, `ash`, `bash`, `dash` and `ksh` all act similarly enough that
you don't care, but sometimes you may have to care. Knowing if you are on a `csh`\drshl{csh}
variant or even something more esoteric can be key.

Pay attention to the first line in script files, which will typically have a
["shebang"](https://en.wikipedia.org/wiki/Shebang_%28Unix%29)
\index{*@\texttt{\#"!} (shebang)} line that looks like this:

\drcap{\texttt{bash} "shebang"}
```bash
#!/bin/bash
```

In this case we know the script is expecting to be executed by `bash`, and in fact should throw an
error if `/bin/bash` doesn't exist. For example, on the FreeBSD system I have access to, `dash` is
not installed. So consider the following `hello.sh` script:

\drcap{Script with `dash` "shebang"}
```bash
#!/bin/dash
echo Hello, World!
```

When I try to run it on FreeBSD, I get:

\drcap{"Shebang" error}
```bash
% ./hello.sh
./hello.sh: Command not found.
```

This is confusing, because it seems to be saying that `hello.sh` is not found! But in reality it is
complaining about missing `dash`. If I change the script to point to `bash` (which is installed on
that FreeBSD system), it works as expected:

\drcap{Hello, World!}
```bash
% ./hello.sh 
Hello, World!
```

Note that on some systems `#!/bin/sh` points to an alias of `bash`, and on some it is a different
implementation of the original `sh` command, such as `ash` or `dash`. Now you know what to search
for if you hit problems as simple as an expected "built-in" command not being found.

## Everything You Know is (Almost) Wrong{.unnumbered}

`CMD.EXE`\drshl{CMD.EXE} has a lineage that is a mish-mash of CP/M\drios{CP/M} and UNIX excreted
through three decades of backwards compatibility to that devil's spawn we call DOS\drios{DOS}. It
has gotten even muddier over the years as Microsoft has added more commands, PowerShell, POSIX
subsystems, etc.

But even so, there are some similarities between `CMD.EXE` and a Linux shell like
`bash`\drshl{bash}. In both `bash` and `CMD.EXE`\drshl{CMD.EXE} the
[`set`](http://linux.die.net/man/1/set)\drcmd{set}
\index{environment variables!displaying!setcommand@\texttt{set} command} command shows you all environment
variables that have been set. Here's `bash`:

\drcap{\texttt{set} command in \texttt{bash}}
```bash
~ $ set
BASH=/bin/bash
BASHOPTS=checkwinsize:cmdhist:complete_fullquote:expand_aliases:extglob:extquote
:force_fignore:histappend:interactive_comments:login_shell:progcomp:promptvars:s
ourcepath
BASH_ALIASES=()
BASH_ARGC=()
BASH_ARGV=()
BASH_CMDS=()
BASH_COMPLETION_COMPAT_DIR=/etc/bash_completion.d
BASH_LINENO=()
BASH_SOURCE=()
BASH_VERSINFO=([0]="4" [1]="3" [2]="11" [3]="1" [4]="release" [5]="x86_64-pc-lin
ux-gnu")
BASH_VERSION='4.3.11(1)-release'
COLORTERM=gnome-terminal
COLUMNS=80
DIRSTACK=()
DISPLAY=:0
EUID=1003
GROUPS=()
HISTCONTROL=ignoreboth
HISTFILE=/home/myuser/.bash_history
...and so on...
```

And `CMD.EXE`:

\drcap{\texttt{SET} command in \texttt{CMD.EXE}}
```bash
C:\Users\myuser>SET
ALLUSERSPROFILE=C:\ProgramData
APPDATA=C:\Users\myuser\AppData\Roaming
CommonProgramFiles=C:\Program Files\Common Files
CommonProgramFiles(x86)=C:\Program Files (x86)\Common Files
CommonProgramW6432=C:\Program Files\Common Files
COMPUTERNAME=JLEHMER650
ComSpec=C:\Windows\system32\cmd.exe
FP_NO_HOST_CHECK=NO
HOMEDRIVE=C:
HOMEPATH=\Users\myuser
LOCALAPPDATA=C:\Users\myuser\AppData\Local
LOGONSERVER=\\JLEHMER650
NUMBER_OF_PROCESSORS=4
OS=Windows_NT
Path=C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\system32
\config\systemprofile\.dnx\bin;C:\Program Files\Microsoft DNX\Dnvm\;C:\Program F
iles (x86)\nodejs\;C:\Program Files\Microsoft\Web Platform Installer\;C:\Program
 Files\Microsoft SQL Server\130\Tools\Binn\;C:\Program Files (x86)\Microsoft SQL
 Server\130\DTS\Binn\;C:\Program Files\Microsoft SQL Server\120\Tools\Binn\;C:\P
rogram Files (x86)\Microsoft SDKs\Azure\CLI\wbin;C:\Windows\System32\WindowsPowe
rShell\v1.0\
PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC
...and so on...
```

Similarly, the
[`echo`](http://linux.die.net/man/1/echo)\drcmd{echo}
\index{environment variables!displaying!echocommand@\texttt{echo} command}
command can be used to show you the contents of an environment variable like `HOME`\drenv{HOME}{current user's home directory} on
`bash`:

\drcap{\texttt{echo} the \texttt{HOME} environment variable in \texttt{bash}}
```bash
~ $ echo $HOME
/home/myuser
```

Versus the `HOMEPATH` variable under `CMD.EXE`:

\drcap{\texttt{echo} the \texttt{HOMEPATH} environment variable in \texttt{CMD.EXE}}
```bash
C:\> ECHO %HOMEPATH%
\Users\myuser
```

This example shows some valuable differences between shells. Even though both have the concept of
environment variables and displaying their contents using the "same" `echo` command, note that:

1. The syntax for accessing an environment variable is
`$variable`\index{environment variables!syntax} in `bash` and `%variable%` in `CMD.EXE`.

2. `bash` is case-sensitive and so `echo $HOME` works but `echo $home` does not. `CMD.EXE` is
***not*** case-sensitive, so either `echo %homedrive%` or `echo %HOMEDRIVE%` (or `EcHo %hOmEdRiVe%`)
would work.

One final note of caution. You can set up command aliases in `bash` and other shells that allow you
to define a `CMD.EXE`-style `dir` command as a substitute for  the `ls` command in `bash`, or
`copy` for `cp`, `del` for `rm`, and so on. I recommend you don't do this for at least two reasons:

1. It is difficult to get these right in terms of being able to map all the various parameters from
the `bash` command to the appropriate parameters for a `CMD.EXE`-style command. Most people don't
go that far, which means you then end up with a "toy" substitute for the `CMD.EXE` command, and
have to fall back to the native commands anyway.

2. It simply delays you actually learning about the "UNIX" environment. You end up relying on a
crutch that then must be replicated on every system you touch. In my opinion it is better to just
learn the native commands, because then you are instantly productive at any shell window.

## You're a Product of Your Environment (Variables){.unnumbered}

It is much more common to set up environment variables to control run-time execution in Linux than
in Windows. In fact, it is quite common to assign\index{environment variables!assigning} a given
environment variable for the single execution of a program, to the point that `bash` has built-in
"one-line" support for it:

\drcap{Assign \texttt{FOO} environment variable before executing script}
```bash
~ $ FOO=myval /home/myuser/myscript
```

This sets the environment variable `FOO` to "myval" but only for the duration and scope of running
`myscript`.

By convention, environment variables are named all uppercase, whereas all scripts and programs tend
to be named all lowercase. Remember, almost without exception "UNIX" is case-sensitive and Windows
is not.

You can assign multiple variables for a single command or script execution simply by separating
them with spaces:

\drcap{Set multiple environment variables at once}
```bash
~ $ FOO=myval BAR=yourval BAZ=ourvals /home/myuser/myscript
```

Note that passing in values in this way does not safeguard sensitive information from other users
on the system who can see the values at least while the script is running using the
`ps -x`\drcmd{ps} command.

You can also set the value of environment variables to the output of another command by surrounding
it with paired \` ("back ticks", or "grave accents"):

\drcap{Set environment variable to output from a command}
```bash
~ $ FILETYPE=`file --brief --mime-type header.tex`
~ $ echo $FILETYPE
text/plain
```

### Who Am I?{.unnumbered}

When writing scripts that can be run by any user, it may be helpful to know their user name at
run-time. There are at least two different ways to determine that. The first is via the
`USER`\drenv{USER}{current user} environment variable:

\drcap{\texttt{USER} environment variable}
```bash
~ $ echo $USER
myuser
```

The second is with a command with one of the best names, ever -
[`whoami`](http://linux.die.net/man/1/whoami)\drcmd{whoami}:

\drcap{\texttt{whoami} command}
```bash
~ $ whoami
myuser
```

Some environments set the `USER` environment variable, some set a `USERNAME`\drenv{USERNAME}{current user}
variable, and some like Mint set both. I think it is better to use `whoami`, which tends to be on
almost all systems.

## Paths (a Part of Any Balanced Shrubbery){.unnumbered}

The concept of a "path" for finding executables is almost identical between "UNIX" and Windows, and
Windows lifted it from UNIX (or CP/M\drios{CP/M}, which lifted it from UNIX). Look at the output of
the `PATH`\drenv{PATH}{execution search path} environment variable under `bash`:

\drcap{\texttt{PATH} environment variable in \texttt{bash}}
```bash
~ $ echo $PATH
/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games
```

Echoing the `PATH`\drenv{PATH}{execution search path} environment variable under `CMD.EXE` works, too: 

\drcap{\texttt{PATH} environment variable in \texttt{CMD.EXE}}
```
C:\Users\myuser>ECHO %PATH%
C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\system32\conf
ig\systemprofile\.dnx\bin;C:\Program Files\Microsoft DNX\Dnvm\;C:\Program Files
(x86)\nodejs\;C:\Program Files\Microsoft\Web Platform Installer\;C:\Program File
s\Microsoft SQL Server\130\Tools\Binn\;C:\Program Files (x86)\Microsoft SQL Serv
er\130\DTS\Binn\;C:\Program Files\Microsoft SQL Server\120\Tools\Binn\;C:\Progra
m Files (x86)\Microsoft SDKs\Azure\CLI\wbin;C:\Windows\System32\WindowsPowerShel
l\v1.0\
```

Note the differences and similarities. Both the paths are evaluated left to right. Both use
separators between path components, a `;` for DOS and Windows, a
`:` for Linux. Both delimit their directory names with slashes, with `\` for DOS and Windows and
`/`\index{*@\texttt{/} (path separator)} for Linux. But Linux has no concept of a "drive
letter" like `C:` in Windows, and instead everything is mounted in a single namespace hierarchy
starting at the root `/`. We'll be talking more about directories, paths and file systems in the
next chapter.

Just to muddy the waters further, notice how Cygwin\drunx{Cygwin} under Windows shows the
`PATH`\drenv{PATH}{execution search path} environment variable with `bash` syntax but a combination of both Cygwin and
Windows directories, and Windows drive letters like `C:` mapped to `/cygdrive/c`:

\drcap{\texttt{PATH} environment variable in Cygwin}
```bash
$ echo $PATH
/usr/local/bin:/usr/bin:/cygdrive/c/Windows/system32:/cygdrive/c/Windows:/cygdri
ve/c/Windows/System32/Wbem:/cygdrive/c/Windows/system32/config/systemprofile/.dn
x/bin:/cygdrive/c/Program Files/Microsoft DNX/Dnvm:/cygdrive/c/Program Files (x8
6)/nodejs:/cygdrive/c/Program Files/Microsoft/Web Platform Installer:/cygdrive/c
/Program Files/Microsoft SQL Server/130/Tools/Binn:/cygdrive/c/Program Files (x8
6)/Microsoft SQL Server/130/DTS/Binn:/cygdrive/c/Program Files/Microsoft SQL Ser
ver/120/Tools/Binn:/cygdrive/c/Program Files (x86)/Microsoft SDKs/Azure/CLI/wbin
:/cygdrive/c/Windows/System32/WindowsPowerShell/v1.0
```

## Open Your Shell and Interact{.unnumbered}

The actual "command prompt" is when you run a shell in an "interactive session" in a terminal
window. This might be from logging into the console of a Linux VM, or starting a terminal window in
a X window manager like GNOME or KDE, or `ssh`'ing\drnet{ssh} into an interactive session of a
remote machine, or even running a Cygwin\drunx{Cygwin} command prompt under Windows.

Command prompts allow you to work in a so-called "REPL" environment (Read, Evaluate, Print, Loop).
You can run a series of commands once, or keep refining a command or commands until you get them
working the way you want, then transfer their sequence to a script file to capture it.

Real wizards at using the shell can often show off their magic with an incredible one-liner typed
rom memory with lots of obscure commands piped together and invoked with cryptic options.

I am not a real shell wizard. See [chapter 9](#how-do-you-know-what-you-dont-know-man) for how you
can fake it like I do.

## Getting Lazy{.unnumbered}

Most modern interactive shells like `bash` and `CMD.EXE`\drshl{CMD.EXE} allow for tab expansion and
command history, at least for the current session of the shell.

Tab expansion is "auto-complete" for the command prompt. Let's say you have some files in a
directory:

\drcap{List some files}
```bash
~/Documents $ ls
Disabled User Accounts.csv  elsewhere  LOLcatz.jpg  MyResume.md
```

Without tab expansion, typing out something like this is painful:

\drcap{Lots of typing and escape characters}
```bash
~/Documents $ mv Disabled\ User\ Accounts.csv elsewhere/.
```

But with tab expansion, we can simply type `mv D^t`, where `^t` represents hitting the `Tab` key,
and since there is only one file that starts with a "D", tab expansion will fill in the rest of the
file name for us:

\drcap{Tab expansion magic}
```bash
~/Documents $ mv Disabled\ User\ Accounts.csv
```

Then we can go about our business of finishing our command.

One place tab completion in `bash` is different than `CMD.EXE`\drshl{CMD.EXE} is that in `bash` if
you hit `Tab` and there are multiple candidates, it will expand as far as it can and then show you
a list of files that match up to that point and allow you to type in more characters and hit `Tab`
again to complete it. Whereas in `CMD.EXE` it will "cycle" between the multiple candidates, showing
you each one as the completion option in turn. Both are useful, but each is subtly different and
can give you fits when moving between one environment and another.

**Pro Tip:** Remember, UNIX was built by people on slow, klunky teletypes and terminals, and they
hated to type! Tab expansion is your friend and you should use it as often as possible. It gives at
least three benefits:

1. Saves you typing.

2. Helps eliminate misspellings in a long file or command name.

3. Acts as an error checker, because if the tab doesn't expand, chances are you are specifying
something else (the beginning part of the file name) wrong.

The other thing to remember about the interactive shell is command history. Again, both
`CMD.EXE`\drshl{CMD.EXE} and `bash` give you command history, but `CMD.EXE` only remembers it for
the session, while `bash` stores it in one of your hidden "profile" or "dot" files in your home
directory called `.bash_history`
\index{files and directories!special!bashhistory@\texttt{.bash\_history}},
which you can display with `ls -a`:

\drcap{\texttt{ls} command showing hidden files}
```bash
~ $ ls -a
.              .config    .gconf           .mozilla  Templates
..             .dbus      .gnome2          Music     Videos
.bash_history  Desktop    .gnome2_private  Pictures  .xsession-errors
.bash_logout   .dmrc      .ICEauthority    .profile
.cache         Documents  .linuxmint       Public
.cinnamon      Downloads  .local           .ssh
```

Inside, `.bash_history` is just a text file, with the most recent commands at the bottom.

The `bash` shell supports a rich interactive environment for searching for, editing and saving
command history. However, the biggest thing you need to remember to fake it is simply that the up
and down arrows work in the command prompt and bring back your recent commands so you can update
them and re-execute them.

**Note:** If you start multiple sessions under the same account, the saved history will be of the
last login to successfully write back out `.bash_history`.