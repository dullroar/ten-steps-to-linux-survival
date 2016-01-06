
# “Just a Series of Pipes”

***`stdin`/`stdout`/`stderr`, redirects and piping between commands.***

> *"Ceci n'est pas une pipe."* - René Magritte

The ["UNIX philosophy"](https://en.wikipedia.org/wiki/Unix_philosophy) tends to be to have a bunch
of small programs that each do one thing very well, and then to combine them together in
interesting ways. The "glue" for combining them together is often the "piping" or redirection of
"streams" of data (typically text) between programs, each doing one small change to the stream
until it is finally emitted on the console or saved to a file or sent over the Internet.

The first thing to note is there are three "file I/O streams" that are open by default in every
"UNIX" process:

* ***stdin*** - input, typically from the console in an interactive session. In the underlying C file system APIs, this is file descriptor 0.
\drstd{stdin}

* ***stdout*** - "normal" output, typically to the console in an interactive session. This is file
descriptor 1.
\drstd{stdout}

* ***stderr*** - "error" output, typically to the console in an interactive session (so it can be
hard to distinguish when intermingled with *stdout* output). This is file descriptor 2.
\drstd{stderr}

**Note:** Those numeric file descriptors will go from being trivia to important in just a bit.

When a program written in C calls `printf`, it is writing to *stdout*. When a `bash` script calls
`echo`, it too is writing to *stdout*. When a command writes an error message, it is writing to
*stderr*. If a command or program accepts input from the console, it is reading from *stdin*.
\drtxt{echo}
\drstd{stdout}

In this example, `cat` is started with no file name, so it will read from *stdin* (a quite common
"UNIX" command convention), and echo each line typed by the user to *stdout* until the "end of
file," which in an interactive session can be emulated with `Ctrl-D`, shown as `^D` in the example
below but not seen on the console in real life:
\drtxt{cat}

\drcap{\textit{stdin} and \textit{stdout}}
```bash
~ $ cat
This shows reading from stdin
This shows reading from stdin
and writing to stdout.
and writing to stdout.
^D
```

In the above I typed in "This shows reading from stdin" and hit `Enter` (which send a linefeed
and hence marks the "end of the line") and `cat` echoed that line to *stdout*. Then I typed "and
writing to stdout." and hit `Enter` and that line was echoed to *stdout* as well. Finally I hit
`Ctrl-D`, which ended the process.
\drstd{stdout}

## All Magic is Redirection{.unnumbered}

One way to string things together in "the UNIX way" is with file redirection. This is a concept
that also works in `CMD.EXE` and even with the same syntax.
\drshl{CMD.EXE}

Let's create a file with a single line of text in it. One way would be to `vi newfilename`, edit
the file, save it, and exit `vi`. A quicker way is to simply use file redirection:
\dreds{vi}

\drcap{Hello, world}
```bash
~ $ echo Hello, world > hw
~ $ ls -l
total 1
-rw-rwxr--+ 1 myuser mygroup 13 Oct 22 10:40 hw
~ $ cat hw
Hello, world
```

In this case the `> hw` tells `bash` to take the output that `echo` sends to *stdout* and send it
to the file `hw` instead.
\drstd{stdout}
\index{*@\texttt{>} (output redirection)}
\index{I/O!redirection!output (\texttt{>})}

As mentioned above many "UNIX" commands are set up to take one or more file names from the command
line as parameters, and if there aren't any, to read from *stdin*. The `cat` command does that.
While it doesn't save us anything over the above example, the following example using `<` is
illustrative of redirecting a file to *stdin* for a command or program:
\drstd{stdin}
\index{*@\texttt{<} (input redirection)}
\index{I/O!redirection!input (\texttt{<})}

\drcap{Redundant redirection}
```bash
~ $ cat < hw
Hello, world
```

Finally, we need to deal with *stderr*. By convention it is sent to the console just like *stdout*,
and that can make output confusing:
\drstd{stderr}

\drcap{Default \textit{stderr} behavior}
```bash
~ $ echo This is a > a
~ $ echo This is b > b
~ $ echo This is c > c
~ $ mkdir d
~ $ echo This is e > d/e
~ $ find . -exec cat \{\} \;
cat: .: Is a directory
This is a
This is b
This is c
cat: ./d: Is a directory
This is e
```

In the above, between echoing the contents of the `a`, `b`, `c` and `e` files, we see two error
messages from `cat` complaining that `.` and `d` are directories. These are being emitted on
*stderr*, but there is no good way of visually telling that. One way to get rid of them would be to
change `find` to filter for only files:

\drcap{Get rid of the errors in the first place}
```bash
~ $ find . -type f -exec cat \{\} \;
This is a
This is b
This is c
This is e
```

But let's say the example is not so trivial, and we want to capture and log the error messages
separately for later analysis. While we've seen `<` used to represent redirecting *stdin* and `>`
used for redirecting *stdout*, how do we tell the shell we want to redirect *stderr*? Remember
the discussion about file handles above? That's where those esoteric numbers come in handy! To
redirect *stderr* we recall it is ***always*** file descriptor 2, and then we can use:
\drstd{stderr}

\drcap{Redirecting \textit{stderr}}
```bash
~ $ find . -exec cat \{\} \; 2>/tmp/finderrors.log
This is a
This is b
This is c
This is e
~ $ cat /tmp/finderrors.log
cat: .: Is a directory
cat: ./d: Is a directory
```

The `2>/tmp/finderrors.log` is the magic that is redirecting file descriptor 2 (*stderr*) to the
log file `/tmp/finderrors.log`.
\index{*@\texttt{2>} (\textit{stderr} redirection)}
\index{I/O!redirection!error (\texttt{2>})}

A very common paradigm is to capture both *stdout* and *stderr* to the same file. Here is how that
is done, again using file descriptors:
\drstd{stderr}
\drstd{stdout}

\drcap{Redirecting both \textit{stdout} and \textit{stderr} to a file}
```bash
~ $ find . -exec cat \{\} \; >/tmp/find.log 2>&1
~ $ cat /tmp/find.log
cat: .: Is a directory
This is a
This is b
This is c
cat: ./d: Is a directory
This is e
```

Now we see *stdout* being redirected to `/tmp/find.log` with `>/tmp/find.log`, and *stderr* (file
descriptor 2) being sent to the same place as *stdout* (file descriptor 1) with `2>&1`. Note that
this works in `CMD.EXE`, too!
\drshl{CMD.EXE}

If we want to send *stdout* to one file and *stderr* to another, you can do it like this:

\drcap{Redirecting \textit{stdout} one way \textit{stderr} another}
```
~ $ find . -exec cat \{\} \; >/tmp/find.log 2>/tmp/finderrors.log
~ $ cat /tmp/find.log
This is a
This is b
This is c
This is e
~ $ cat /tmp/finderrors.log
cat: .: Is a directory
cat: ./d: Is a directory
```

One final note with redirection is the difference between creating or re-writing a file versus
appending. The following creates a new `/tmp/find.log` file every time it runs (there is no need
to `rm` it first):

\drcap{Overwriting a file with redirection}
```bash
~ $ find . -exec cat \{\} \; >/tmp/find.log
```

However, the next sample using `>>` creates a new `/tmp/find.log` file if it doesn't exist, but
otherwise appends to it:
\index{*@\texttt{>>} (output redirection, appending)}
\index{I/O!redirection!output, appending (\texttt{>>})}

\drcap{Appending to a file with redirection}
```bash
~ $ find . -exec cat \{\} \; >>/tmp/find.log
```

**Note:** There is also a variation on input redirection using `<<`, but it is used mostly in
scripting and is outside the scope of this book.

## Everyone Line Up{.unnumbered}

So we can see that we could pass things between programs by redirecting *stdout* to a file and then
redirecting that file to *stdin* on the next program, and so on. But "UNIX" environments take it a
bit further with the concept of a command "pipeline" that allows directly sending *stdout* from one
program into *stdin* of another using the "pipe" (`|`):
\index{*@\texttt{"|} (pipe)}\index{I/O!redirection!pipe (\texttt{"|})}
\drstd{stdin}
\drstd{stdout}

\drcap{Piping output between programs}
```bash
~ $ cat *.txt | tr '\\' '/' | while read line ; do ./mycmd "$line" ; done
```

This little one-liner starts showing off the usefulness of chaining several small programs,
each doing one thing. In this case:

1. `cat` echos the contents of all `.txt` files in alphabetical order by their file name to
*stdout*, which is piped to...

2. [`tr`](http://linux.die.net/man/1/tr) "translates" (replaces) any backslash characters (here
"escaped" as `'\\'` because the backslash character is a special character) to forward slashes (`/`)
before sending it into...
\drtxt{tr}

3. A `while` loop that reads each line into a variable called `$line` and then calls...
\drscr{while}

4. Some custom script or program called `./mycmd` passing in the value of each `$line`.

Think about the power of that. `cat` didn't know there were multiple `.txt` files or not - the
shell expansion of the `*.txt` wildcard did that. It read all those files and echoed them to
*stdout* which in this case was a pipeline sending each line in order to another command to
transform the data, before sending each line to the custom code in `mycmd`, that only expects a
single line or value each time it is run. It has no idea about the `.txt` files or the
transformation or the pipeline!

***That*** is the "UNIX philosophy" at work.

There are some nice performance benefits for this approach, too. In general Linux & Co. will
overlap the processing by starting all the commands in the pipeline, with the ones on the right
getting data from the ones further "upstream" to the left as soon as it is written, instead of
using file redirection where one program would have to finish completely running and writing out to
a file before the next program could start and read in that file as input.

Finally, if you want to capture something to a file ***and*** see it on the console at the same
time, that is where the [`tee`](http://linux.die.net/man/1/tee) command comes in:
\drtxt{tee}

```bash
~ $ find . -name error.log | tee > errorlogs.txt
```

This would write the results of finding all files names `error.log` to the console and also to
`errorlogs.txt`. This is useful when you are manually running things and want to see the results
immediately, but also want a log of what you did.