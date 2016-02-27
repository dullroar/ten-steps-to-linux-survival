
# Finding Meaning

***The `find` command in all its glory. Probably the single most useful command in "UNIX" (I
think)***

> *"If we had bacon, we could have bacon and eggs, if we had eggs."* - old joke

Different people will have different answers to "What is the single most useful "UNIX" command?"
There certainly are many to consider. But I keep coming back to
[`find`](http://linux.die.net/man/1/find). It can be intimidating to figure out from the
documentation, especially at first, but once you start mastering it, you end up using it over and
over again.
\drfnd{find}{find files}

The main concepts of `find` are simple:

1. Starting at location *X*...

2. Recursively find all files or directories (or "file system entries" to be more precise) that
successfully match one or more tests...

3. And for each match execute one or more actions.

The simplest example is "starting in the current directory, recursively list all files you find":

\drcap{Simplest \texttt{find} example}
```bash
~ $ find
.
./Agenda.md
./Bad and Corrupted Test Files
./Bad and Corrupted Test Files/.DS_Store
./Bad and Corrupted Test Files/2008 Letter of Understanding.TIF
./Bad and Corrupted Test Files/3948175.dat
./Bad and Corrupted Test Files/3948176.dat
./Bad and Corrupted Test Files/3948178.dat
./Bad and Corrupted Test Files/3948180.dat
./Bad and Corrupted Test Files/3948182.dat
./Bad and Corrupted Test Files/3948186.dat
./Bad and Corrupted Test Files/3948190.dat
./Bad and Corrupted Test Files/3948193.dat
./Bad and Corrupted Test Files/3948195.dat
./Bad and Corrupted Test Files/3948197.dat
./Bad and Corrupted Test Files/3948259.dat
...and so on...
```

In this case `find` is just shorthand for `find . -true -print`.

That's not really that interesting. Let's poke around and "find" (pun intended) some better
examples of using `find`. It is better to show than tell in this case. Let's dive into a
semi-complicated one and pick it apart:

\drcap{More complicated \texttt{find} example}
```bash
~ $ find //myserver/myshare/logs/000[4-9] -name \*.dat -newer logchecker.csv \
    -exec /home/myuser/Sandbox/FileCheckers/logchecker \{\} \;
```

How does this all work? Remembering the three steps at the beginning:

1. **Starting at location `//myserver/myshare/logs/000[4-9]`** - in this case a CIFS/SMB share
running under Cygwin^[In fact, `find` is one of the main reasons I use Cygwin on Windows.] (this
won't work on Linux). Note the regular expression (which we will cover later), in this case saying
to look only in directories `0004` through `0009`.

2. **Recursively find file system entries that match one or more tests** - the tests in this
example are:

    a. ***All files that have a name that ends in `.dat`*** - the only thing to note here is the
    `\` preceding the wildcard `*`. This prevents "shell expansion," which would allow the `bash`
    process interpreting the command to expand it to the list of files present in the current
    directory only, not recursively across all directories.

    b. ***That are newer (created or modified after) the file `logchecker.csv`*** - presumably this
    file gets created by running `logchecker` or some related process. This is an optimization
    condition check to only look at files that have been updated since the last time the script ran.

3. **For each match, execute `logchecker`** - and pass in the name of the currently found (matching)
file.

## What's With the Backslashes?{.unnumbered}

Reconsider this example:

\drcap{More complicated \texttt{find} example, explained}
```bash
~ $ find //myserver/myshare/logs/000[4-9] -name \*.dat -newer logchecker.csv \
    -exec /home/myuser/Sandbox/FileCheckers/logchecker \{\} \;
```
          
There are five (5) backslash (`\`) characters in the above. In each case, the backslash is 
preventing [shell expansion](http://www.tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_04.html):
\index{*@\texttt{\textbackslash{}} (escape character)}

1. **`\*.dat`** - preserves the `*` for `find` to use as it recursively searches through
directories, instead of the shell expanding it to all files that end in `.dat` in the current directory.
\index{*@\texttt{*} (wildcard)}

2. **`\`** - the `\` at the end of the first line tells the shell that the command continues on the
next line.

3. **`\{\} \;`** - these three prevent the shell from trying to expand the braces into an
environment variable or the semicolon (which is meant to tell `find` when the command being ran via
`-exec` and its parameters end), otherwise `;` is normally used to separate independent commands on
the same line in the shell.
\index{*@\texttt{;} (command separator)}

That last point bears repeating. Any time you `-exec` in a `find` command (which will be a lot),
just get used to typing `\{\} \;` (the space between the ending brace and the `\;` is
***required***).

## Useful `find` Options{.unnumbered}

The [`find`](http://linux.die.net/man/1/find) documentation gives a bewildering number of options.
Here are the ones you may "find" the most useful:
\drfnd{find}{find files}

* **`-executable`** - the file is executable or the directory is searchable (in other words, the
file or directory's `x` mode bit is set true for user, group or other ("ugo"), per the file
permissions discussion above), and the user executing the `find` command falls into one of the
categories for which it is set.

* **`-group <gname>`** - file belongs to group *gname*.

* **`-iname <pattern>`** - case-insensitive name search. Any wildcard characters should be escaped.

* **`-maxdepth <number>`** - limits the number of directory levels to recurse into.

* **`-mindepth <number>`** - sets a starting directory level below the current one to recurse into.

* **`-name <pattern>`** - case-sensitive name search. Any wildcard characters should be escaped.

* **`-newer <file>`** - each file is tested to see if it is newer than *file*.

* **`-size <n>`** - file uses *n* units of space, which can be specified in various measures like
512-byte blocks (`b`) through gigabytes (`G`).

* **`-type <c>`** - file is of type *c*, with the two most common being `d` (directory) or `f`
(file).

* **`-user <uname>`** - file is owned by *uname*.

## Useful `find` Actions{.unnumbered}

Similarly, you are going to keep coming back to just a handful of `find` actions:

* **`-delete`** - deletes any files matched so far. Note that actions are also tests (predicates),
so as the `find` documentation says, "Don't forget that the find command line is evaluated as an
expression, so putting `-delete` first will make find try to delete everything below the starting
points you specified." In other words, placing `-delete` too early in the expression is going to
yield behavior distressingly similar to `rm -r *`.

* **`-exec` and `-execdir`** - executes a command or script, typically passing in the name of the
file or directory found. You will use this ***all*** the time. The difference between the two is
that `-execdir` changes the working directory to that of the item found before invoking the program
or script, whereas `-exec` simply passes in the fully-qualified path of the found item.

* **`-print`** - prints the full path of the found file or directory. This is the default action.

* **`-printf`** - prints a formatted string, useful for reports.

The `-printf` action allows you to do some interesting things when producing output. For example,
if for some reason we wanted a report where for each file we wanted three lines with the name,
owner and created date and time in ISO 8601 format, all followed by a blank line, we could use the
following `find` command:

\drcap{Using \texttt{find} as a simple reporting tool}
```bash
~ $ touch a b c
~ $ ls -l
total 0
-rw-rwxr--+ 1 myuser mygroup 0 Oct 21 11:02 a
-rw-rwxr--+ 1 myuser mygroup 0 Oct 21 11:02 b
-rw-rwxr--+ 1 myuser mygroup 0 Oct 21 11:02 c
~ $ find . -type f -printf "%p\n%u\n%TY-%Tm-%TdT%TT\n\n"
./a
myuser
2015-10-21T11:02:51.7014527000

./b
myuser
2015-10-21T11:02:51.7035423000

./c
myuser
2015-10-21T11:02:51.7048997000
```

That `-printf` format string `"%p\n%u\n%TY-%Tm-%TdT%TT\n\n"` breaks down into:
\index{*@\texttt{\%} (format)}

* **`"`** - prevent shell expansion on the format string.
* **`%p`** - file name.
* **`\n`** - new line.
* **`%u`** - owning user name.
* **`\n`** - new line.
* **`%TY`** - the last modification date of the file expressed as a year.
* **`-`** - a literal hyphen. 
* **`%Tm`** - the last modification date of the file expressed as a month.
* **`-`** - a literal hyphen. 
* **`%Td`** - the last modification date of the file expressed as a day.
* **`T`** - a literal 'T'.
* **`%TT`** - the time expressed in ***hh:mm:ss.hhhhhh*** format.
* **`\n\n`** - two new lines.
* **`"`** - prevent shell expansion on the format string.