# Step 1. Come Out of Your Shell

***`sh` vs. `ash` vs. `bash` vs. everything else, "REPL”, interactive vs.
scripts, command history, tab expansion, environment variables and "A path!
A path!"***

> *"If you hold a shell up to your ear, you can hear the OS."* - me

To avoid getting all pedantic, I am just going to define a shell as an
environment in which you can execute commands. People tend to think of
a shell as a "command prompt," but you can run a shell without running
a command prompt, but not vice versa - an interactive command prompt is
an instance of a shell environment almost by definition.

Examples of shells:

* [**`CMD.EXE`**](https://technet.microsoft.com/en-us/library/cc754340.aspx) -
yes, Windows has a shell.

* [**`PowerShell.exe`**](https://technet.microsoft.com/en-us/library/ms714469%28v=VS.85%29.aspx) -
in fact, it has at least two!

In UNIX-land:

* [**`sh`**](https://en.wikipedia.org/wiki/Bourne_shell) - the "original"
Bourne shell in UNIX, which spawned:

    * [**`ash`**](https://en.wikipedia.org/wiki/Almquist_shell) - Almquist
    shell.

        * **`dash`** - Debian Almquist shell (replaced `ash` in Debian)

    * [**`bash`**](https://en.wikipedia.org/wiki/Bash_%28Unix_shell%29) -
    Bourne-again shell (get it?), the "standard" Linux shell.

    * [**`ksh`**](https://en.wikipedia.org/wiki/Korn_shell) - Korn shell.

    * [**`zsh`**](https://en.wikipedia.org/wiki/Z_shell) - Z shell.

* [**`csh`**](https://en.wikipedia.org/wiki/C_shell) - C shell,
historically it is the default shell on BSD systems (although there are
arguments on why you should [***never use
it***](http://www.faqs.org/faqs/unix-faq/shell/csh-whynot/)).

* **...and many more!** - [tons,
really](https://en.wikipedia.org/wiki/Unix_shell#Shell_categories).

Most Linux distros use `bash`, but the BSDs are all over the place. We're
going to assume `bash` for the rest of this tutorial. With few
modifications, anything in the `sh` hierarchy above can usually run in the
other members of the same tree.

## `bash` Built-Ins

Every shell has some "built-in" commands that are implemented as part
of the shell and not as an external command or program, and `bash` has its
share, as shown by running the [`help`](http://linux.die.net/man/1/help)
command in a `bash` terminal:

```bash
$ help
GNU bash, version 4.3.42(4)-release (x86_64-unknown-cygwin)
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
...and so on...
```

The above was run in `bash` under Cygwin, but identical output is shown
when running `help` under `bash` on Linux, too.

Why does this matter? Because if you are in an environment and something
as fundamental as `echo` isn't working, you may not be working in a shell
that is going to act like a "`sh`" shell. ***In general***, `sh`, `ash`,
`bash`, `dash` and `ksh` all act similarly enough that you don't care,
but sometimes you may have to care. Knowing if you are on a `csh` variant
or even something more esoteric can be key.

Pay attention to the first line in script files, which will typically
have a ["shebang"](https://en.wikipedia.org/wiki/Shebang_%28Unix%29) line
that looks like this:

```bash
#!/bin/bash
```

In this case we know the script is expecting to be executed by `bash`,
and in fact should throw an error if `/bin/bash` doesn't exist. Note
that on some systems:

```bash
#!/bin/sh
```

...is pointing to an alias of `bash`, and on some it is a different
implementation of the original `sh` command, such as `ash` or `dash`. Now
you know what to google if you hit problems as simple as an expected
built-in command not being found.

## Everything You Know is (Almost) Wrong

`CMD.EXE` has a lineage that is a mish-mash of CP/M and UNIX excreted
through three decades of backwards compatibility via that devil spawn
we call DOS. It has gotten even muddier over the years as Microsoft has
added more commands, PowerShell, POSIX subsystems, etc.

But even so, there are some similarities. In both `bash` and `CMD.EXE`,
the [`set`](http://linux.die.net/man/1/set) command shows you all
environment variables that have been set:

***bash***

[Under Cygwin]

```bash
$ set
ALLUSERSPROFILE='C:\ProgramData'
APPDATA='C:\Users\myuser\AppData\Roaming'
BASH=/bin/bash
BASHOPTS=cmdhist:complete_fullquote:expand_aliases:extglob:extquote:for...
BASH_ALIASES=()
BASH_ARGC=()
BASH_ARGV=()
BASH_CMDS=()
BASH_COMPLETION=/etc/bash_completion
BASH_COMPLETION_COMPAT_DIR=/etc/bash_completion.d
BASH_COMPLETION_DIR=/etc/bash_completion.d
BASH_LINENO=()
...and so on...
```

***CMD.EXE***

```
C:\> set
ALLUSERSPROFILE=C:\ProgramData
APPDATA=C:\Users\myuser\AppData\Roaming
CLIENTNAME=JLEHMER650
CommandPromptType=Native
CommonProgramFiles=C:\Program Files\Common Files
CommonProgramFiles(x86)=C:\Program Files (x86)\Common Files
CommonProgramW6432=C:\Program Files\Common Files
COMPUTERNAME=JCAPPDEV
ComSpec=C:\Windows\system32\cmd.exe
ExtensionSdkDir=C:\Program Files (x86)\Microsoft SDKs\Windows\v8.0\Exten...
FP_NO_HOST_CHECK=NO
Framework35Version=v3.5
...and so on...
```

Similarly, the [`echo`](http://linux.die.net/man/1/echo) command can be
used to show you the contents of an environment variable (among other
things):

***bash***

```bash
$ echo $HOMEDRIVE
C:
```

***CMD.EXE***

```
C:\> echo %homedrive%
C:
```

This example shows some valuable differences between shells, though.
Even though both have the concept of environment variables and echoing
out their contents using the "same" command, note that:

1. The syntax for accessing an environment variable is `$variable` in
`bash` and `%variable%` in `CMD.EXE`.

2. `bash` is case-sensitive and so `echo $HOMEDRIVE` works but `echo
$homedrive` does not. `CMD.EXE` is ***not*** case-sensitive, so either
`echo %homedrive%` or `echo %HOMEDRIVE%` (or `EcHo %hOmEdRiVe%`)
would work.

## You're a Product of Your Environment (Variables)

It is much more common to set up environment variables to control
execution in Linux than in Windows. In fact, it is quite common to
override a given environment variable for the single execution of a
program, to the point that `bash` has built-in "one-line" support for it:

```bash
FOO=myval /home/lehmer/myscript
```

This sets the environment variable `FOO` to "myval" but only for the
duration and scope of running `myscript`.

By convention, environment variables are named all uppercase, whereas all
scripts and programs tend to be named all lowercase. Remember, almost
without exception Linux and company are case-sensitive and Windows is not.

You can set or override multiple variables for a single command or script
execution simply by separating them with spaces:

```bash
FOO=myval BAR=yourval BAZ=ourvals /home/lehmer/myscript
```

Note that passing in values in this way does not safeguard sensitive
information from other users on the system who can see the values at
least while the script is running using the `ps -x` command.

You can also set the value of environment variables to the output of a
command using \`:

```bash
$ filetype=`file --print --mime-type --no-pad --print0 otschecker.csv`

$ echo $filetype
otschecker.csv: text/plain
```

## Paths (a Part of Any Balanced Shrubbery)

The concept of a "path" for finding executables is almost identical, and
Windows lifted it from UNIX (or CP/M, which lifted it from UNIX). You
can tell how similar they are by looking at the output of the `PATH`
environment variable under `CMD.EXE` and `bash` running under Cygwin
for the same user on the same machine:

***CMD.EXE***

[Formatted for readability]

```
C:\> echo %path%
C:\Program Files (x86)\Microsoft Visual Studio 11.0\Common7\IDE\CommonEx...
C:\Program Files (x86)\Microsoft Visual Studio 11.0\VC\BIN\amd64;
C:\Windows\Microsoft.NET\Framework64\v4.0.30319;
C:\Windows\Microsoft.NET\Framework64\v3.5;
C:\Program Files (x86)\Microsoft Visual Studio 11.0\VC\VCPackages;
C:\Program Files (x86)\Microsoft Visual Studio 11.0\Common7\IDE;
C:\Program Files (x86)\Microsoft Visual Studio 11.0\Common7\Tools;
...and so on...
```

***bash***

[Formatted for readability]

```bash
$ echo $PATH
/usr/local/bin:/usr/bin:/cygdrive/c/Windows/system32:/cygdrive/c/Windows...
/cygdrive/c/Windows/System32/Wbem:/cygdrive/c/Windows/System32/WindowsPo...
/cygdrive/c/Program Files/SourceGear/Common/DiffMerge:
/cygdrive/c/Program Files/TortoiseHg:
/cygdrive/c/Program Files (x86)/Microsoft SQL Server/100/Tools/Binn:
/cygdrive/c/Program Files/Microsoft SQL Server/100/Tools/Binn:
/cygdrive/c/Program Files/Microsoft SQL Server/100/DTS/Binn:
...and so on...
```

Note the differences and similarities. Both the paths are evaluated
left to right. Both use separators between path components, a `;` for
DOS and Windows, a `:` for Linux. Both delimit their directory names
with slashes, with `\` for DOS and Windows and `/` for Linux. But Linux
has no concept of a "drive letter" like `C:`, and instead everything is
rooted in a single namespace hierarchy starting at the root `/`. We'll be
talking more about directories in the next chapter.

## Open Your Shell and Interact

The actual "command prompt" is when you bring up a shell in an "interactive
session" in a terminal window.  This might be from logging into the console
of a Linux VM, or starting a terminal window in a X window manager like
GNOME or KDE, or `ssh`'ing into an interactive session of a remote
machine, or even running a Cygwin command prompt under Windows.

Command prompts allow you to work in a so-called "REPL" environment
(Read, Evaluate, Print, Loop). You can run a series of commands once,
or keep refining a command or commands until you get them working the
way you want, then transfer their sequence to a script file to capture it.

Real shell wizards can often show off their magic in an incredible
one-liner typed from memory with lots of obscure commands piped together
and invoked with cryptic options.

I am not a real shell wizard. See [chapter 9](#HowDoYouKnowWhatYouDontKnow)
for how you can fake it like I do.

## Getting Lazy

Most modern interactive shells like `bash` and `CMD.EXE` allow for
tab expansion and command history, at least for the current session of
the shell.

Tab expansion is "auto-complete" for the command prompt. Let's say you
have the following files in a directory:

```bash
$ ls -l
total 764
-rwxrwx---+ 1 myuser mygroup  18554 Oct  9 15:01 Agenda.md
drwxrwx---+ 1 myuser mygroup      0 Oct  9 08:50 Bad and Corrupted Test
Files
drwxrwx---+ 1 myuser mygroup      0 Sep 22 15:35 CheckMD5sLog
-rw-rwxr--+ 1 myuser mygroup   1431 Oct  9 14:58 CygwinPath.txt
-rwxrwx---+ 1 myuser mygroup  22461 Oct  7 14:19 Disabled Active Directory Accounts.xlsx
-rwxrwx---+ 1 myuser mygroup  55647 Sep 18 08:31 filtered.txt
drwxrwx---+ 1 myuser mygroup      0 Sep 15 15:59 FLOCK
-rwxrwx---+ 1 myuser mygroup  11185 Feb 24  2015 GitLab Upgrade Info.txt
...and so on...
```

Without tab expansion, typing out something like:

```bash
mv Disabled\ Active\ Directory\ Accounts.xlsx
```

...is painful. But with tab expansion, we can simply:

```bash
mv D^t
```

...where `^t` represents hitting the `Tab` key, and since there is only
one file that starts with a "D" tab expansion will fill in the rest of
the file name:

```bash
mv Disabled\ Active\ Directory\ Accounts.xlsx
```

...and we can go about our business of finishing our command.

One place the tab completion in `bash` is different than `CMD.EXE`
is that in `bash` if you hit `Tab` and there are multiple candidates,
it will expand as far as it can and then show you a list of files that
match up to that point and allow you to type in more characters and hit
`Tab` again to complete it. Whereas in `CMD.EXE` it will "cycle" between
the multiple candidates, showing you each one as the completion option
in turn. Both are useful, but each is subtly different and can give you
fits when moving between one environment and another.

**Pro Tip:** Remember, UNIX was built by people on slow, klunky teletypes
and terminals, and they hated to type! Tab expansion is your friend and
you should use it as often as possible. It gives at least three benefits:

1. Saves you typing.

2. Helps eliminate misspellings in a long file or command name.

3. Acts as an error checker, because if the tab doesn't expand, chances
are you are specifying something else (the beginning path of the file)
wrong.

The other thing to remember about the interactive shell is command
history. Again, both `CMD.EXE` and `bash` give you command history, but
`CMD.EXE` only remembers it for the session, while `bash` stores it in
one of your hidden "profile" or "dot" files in your home directory called
`.bash_history`:

```bash
$ ls -a
.              .bash_profile  .gitignore  .minttyrc  Dropbox      Sandbox
..             .bashrc        .inputrc    .profile   fast-export  Shared
.bash_history  .gitconfig     .lesshst    .ssh       myuser      Temp

```

Inside, `.bash_history` is just a text file, with the most recent commands
at the bottom.

The `bash` shell supports a rich interactive environment for searching for,
editing and saving command history. However, the biggest thing you needf
to remember to fake it is simply that the up and down arrows work in
the command prompt and bring back your recent commands so you can update
them and re-execute them.

**Note:** If you start multiple sessions under the same account,
the saved history will be of the last login to successfully write back out
`.bash_history`.
