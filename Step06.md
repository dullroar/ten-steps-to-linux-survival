
# `vi`

***How to stay sane for 10 minutes in `vi`. Navigation, basic editing, find,
change/change-all, cut and paste, undo, saving and canceling. Plus easier
alternatives like `nano`, and why `vi` still matters.***

> *"You're too young to know."* - Vi (*Grease*)

[`vi`](http://linux.die.net/man/1/vi) stands for *visual editor* (as well as the Roman numeral for
6, which is why it is this chapter), and once you use it you will understand what editing from the
command line must've been like for `vi` to seem both "visual" and a step forward.
\dreds{vi}
\index{commands!vi@\texttt{vi}|seealso{\texttt{vi} Commands}}

Many Linux clones don't use `vi` proper, but a port called [`vim`](http://www.vim.org/) ("**vi** i**m**proved"), that is then accessed via the alias `vi`. The differences tend to be minor, with
`vim` being more customizable.
\dreds{vim}

`vi` and a similar editor, [`emacs`](http://linux.die.net/man/1/emacs), both tend to trip up users
from GUI operating systems such as Windows or OS X that have editors like Notepad that are always
ready for user input.
\dreds{emacs}

Instead, `vi` typically starts in "command mode," where keystrokes execute various navigation and
editing commands. To actually insert text requires a keystroke such as `i` while in command mode,
which then causes `vi` to go into "insert mode." Insert mode is what most Windows users expect from
an editor, i.e., when you type the line changes. The `ESC` key exits insert mode.
\drvic{ESC}{exit insert mode}
\drvic{i}{insert mode}

It is as hard to get used to as it sounds, and you ***will*** execute text you were meaning to
insert as commands, and commands that you were meaning to execute you ***will*** insert as text,
and sooner or later you ***will*** enter `vi` commands into Notepad. I guarantee it. That will be
the day you know you've become truly tainted.

We will not even begin to scratch the surface of `vi`, when there are many books and web sites just
on wielding it to its full potential. In the hands of someone who has mastered it, `vi` can do some
really remarkable feats of editing way beyond the capability of most modern GUI programming
environments.

## Command Me{.unnumbered}

Again, when you first open `vi` it is in "command mode." That means any keystrokes you enter will
"do something." The "something" to be done may be navigating around the file, inserting, deleting
or changing text, manipulating lines, "undoing" or "redoing," writing the changes to disk and the
like.

What are commands? Well, for example `d` means "delete." We'll talk about how to specify ***what***
to delete next. `i` tells `vi` to enter "insert mode" at the point where the cursor is. `0` (zero)
navigates to the start of the current line, and so on.
\drvic{d}{delete}
\drvic{i}{insert mode}
\drvic{0}{jump to beginning of line}

Commands can have ***modifiers*** preceding and following them. Consider the "delete" command, `d`.
If we follow with `w` as in `dw` while in command mode, it will delete a whitespace-delimited
"word" starting at where the cursor is through (including) the next whitespace character.
\drvic{dw}{delete word}

If the `|` in the following represents the cursor:

\drcap{Deleting a "word"}
```bash
This is a wo|rd and so is this.
```

Then typing `dw` will delete from the cursor position the characters `r`, `d` and the space,
leaving the following:

\drcap{After deleting the "word"}
```bash
This is a wo|and so is this.
```

We can also specify the number of times we want to perform a command by prefixing it to the
command. So now if we wanted to delete three words from the cursor position in the above, we'd use
`3dw` and end up with:

\drcap{Deleting multiple words}
```bash
This is a wo|this.
```

Again, in all these examples the `|` represents the cursor.

There is a little bit of nuance in using command modifiers. Consider the `r` (*replace*) command.
It is typically used to change the single ***character*** under the cursor. You may be tempted to
think you can do something like `rw` for "replace word," but it is actually going to simply replace
the current character with a `w`, whereas the real command for doing that is `cw` ("change word").
In addition, you can use repeaters as above, just be sure you understand `r` means "replace a
single character," so `3rx` executed on:
\drvic{c}{change}
\drvic{cw}{change word}
\drvic{r}{replace character}

\drcap{Replace three characters with "x"}
```bash
This is a wo|this.
```

...results in:

\drcap{Three "x" characters}
```bash
This is a woxx|xs.
```

To quit without saving enter `:q`. To write any file changes to disk use `:w`. To save ***and***
quit, type `:wq`.
\drvic{:q}{quit without saving}
\drvic{:w}{write to disk}
\drvic{:wq}{write to disk and quit}

## Undo Me{.unnumbered}

`u` is the "undo" command. It "undoes" or reverts the last change. You can undo the last *n*
changes just as you'd expect, e.g., `3u` undoes the last three changes.
\drvic{u}{undo}

If you want to just cancel out of the file without writing any changes to disk, use
`:q!` (the `!` means to force the quit without saving).
\drvic{:q"!}{quit without saving (force)}

If you want to protect yourself from inadvertent changes to a file you can always open it using
[`view`](http://linux.die.net/man/1/view), the alias for `vi` invoked in read-only mode.
\dreds{view}

## Circumnavigating `vi`{.unnumbered}

In modern implementations of `vi` (like `vim`) running under modern shells the arrow and page keys
will work as you expect, ***in general***. However, you may want to be aware that when in insert
mode, while the left and right arrows may work for navigation, often the up and down arrows can
introduce "garbage" characters into the file (since you are in insert mode). This is because the
keymappings for those keys aren't being interpreted correctly. I usually just swear, exit insert
mode, hit `u` and try again.
\drvic{u}{undo}

As an example, under Cygwin I went into `vi`, went into insert mode after the first line, typed in
"This is a new line" and then hit the up arrow five times, yielding this:

\drcap{Garbage characters}
```bash
This is a word and so is this.
A
A
A
A
A
This is a new line
```

When in command mode, there are multiple ways to jump around in the file besides using the arrow
and page keys:

* **`0`** - jumps to the beginning of the current line.
\drvic{0}{jump to beginning of line}

* **`$`** -jumps to the end of the current line.
\drvic{\$}{jump to end of line}
\index{*@\texttt{\$} (\texttt{vi} jump to end of line)}

* **`w`** - jumps forward a whitespace-delimited "word" on the current line (and of course `3w`
would jump forward three "words").
\drvic{w}{jump forward a word}

* **`b`** - jumps back a whitespace-delimited "word" on the current line.
\drvic{b}{jump back a word}

* **`G`** - jumps to end of the file.
\drvic{G}{jump to end of file}

* **`:0`** - jumps to start of the file (note the preceding `:`).
\drvic{:0}{jump to beginning of file}

* **`/foo`** - find "foo" going forward toward the end of the file.
\index{*@\texttt{/} (\texttt{vi} find forward)}
\index{vicommands@\texttt  {vi} commands!\/@\texttt{/} (find forward)}

* **`?foo`** - find "foo" going backward toward the front of the file.
\index{*@\texttt{?} (\texttt{vi} find backward)}
\index{vicommands@\texttt  {vi} commands!\?@\texttt{?} (find backward)}

* **`n`**  - find the next instance of the search text specified by the last `/` or `?`.
\drvic{n}{find next}

## Insert Tab A Into Slot B{.unnumbered}

There are multiple ways to enter insert mode, but only one way to escape it (pun intended - `ESC`,
get it?)

* **`i`** - enters insert mode at the current cursor position.
\drvic{i}{insert mode}

* **`I`** - enters insert mode at the beginning of the current line.
\drvic{I}{insert mode at beginning of line}

* **`A`**  - enters insert mode (appends) at the end of the current line.
\drvic{A}{append at end of line}

* **`o`** - inserts a new line under (lowercase `o` = "lower" or "below") the current line and puts
the cursor on it in insert mode.
\drvic{o}{insert new line under current line}

* **`O`**  - inserts a new line over (uppercase `O` = "upper" or "above") the current line and puts
the cursor on it in insert mode.
\drvic{O}{insert new line above current line}

## Ctrl-X, Ctrl-C, Ctrl-V{.unnumbered}

When you copy or cut/delete it, it goes into a "buffer." There are ways to access multiple buffers,
but mostly you want the very last thing to be put in the buffer, especially for copying (or cutting)
and pasting. Note that "cutting" and "deleting" are synonymous, since deleting puts the deleted
text in the buffer.

Another thing to understand is that a command "doubled" or repeated typically means "the whole
line." So `dd` means "delete the whole line the cursor is currently on."
\drvic{dd}{delete entire line}

So if deleting is synonymous with cutting, and the cursor is on the second line:

\drcap{Deleting a line}
```bash
This is a word and so is this.
This is a new line.|
```

Then executing `dd` leaves:

\drcap{After the line is gone}
```bash
|This is a word and so is this.
```

We know "This is a new line." went into the buffer. We can paste it back above the current line
with `P`(uppercase `P` = "upper" or "above"), which would result in:
\drvic{P}{paste above current line}

\drcap{After pasting the line above the current line}
```bash
|This is a new line.
This is a word and so is this.
```

Here are some more examples:

* **`p`** - paste the buffer into the current line starting after the cursor location.
\drvic{p}{paste after cursor}

* **`3dd`** - delete (cut) three lines into the buffer.

* **`5yw`** - "yank" (copy) five words starting at the current cursor position into the buffer.
\drvic{y}{copy}

## Change Machine{.unnumbered}

The hardest thing to get down in `vi` is the *substitute* (change or replace) command, `:s`. Its
syntax is esoteric, but once you've memorized it, it becomes intuitive.
\drvic{:s}{change}

The most common scenario is the "change all" command. Given the following file:

\drcap{Sample text file}
```bash
This is a new line
This is a word
and so is this
This and thus
This and this and this
```

Let's change all "this" to "that" by using:

\drcap{Changing "this" to "that"}
```bash
:0,$s/this/that/
```

We'll get into the details in a bit, but the results are interesting, and not what we'd expect:

\drcap{What happened?}
```bash
This is a new line
This is a word
and so is that
This and thus
This and that and this
```

It only changed the "that" at the end of the third line, and the middle "that" on the last. Why?
Two reasons:

1. The substitute command is case sensitive, just like everything else in Linux, unless you tell it
to be *insensitive*.

2. The substitute command only makes one change per line unless you tell it to change *globally*.

So let's hit `u` to reset (undo) the change, and try again with this:
\drvic{u}{undo}

\drcap{Changing "this" to "that", redux}
```bash
:0,$s/this/that/i
```

Results in:

\drcap{Closer, but not quite}
```bash
that is a new line
that is a word
and so is that
that and thus
that and this and this
```

That's better. There is at least one "that" on every line that had a "this," so passing the `i`
("insensitive") switch at the end of the `s` (substitute) command helped with that. But we still
didn't get all the "this" words changed, as the last line shows. Hit `u` and try one more time with this:

\drcap{Changing "this" to "that", one more time!}
```bash
:0,$s/this/that/gi
```

Results in:

\drcap{Finally!}
```bash
that is a new line
that is a word
and so is that
that and thus
that and that and that
```

That's what we wanted! Well, sort of. If we wanted to keep the capitalization we'd have more work
to do. See below.

In general, if you are looking for a case insensitive "change all" like in Windows Notepad, the
magic string to remember is:

\drcap{Memorize this - No, really}
```bash
:0,$s/from/to/gi
```

Picking that apart, we have:

* **`:`** - tells `vi` a special command is coming.

* **`0,$`** - specifies a line range, in this case from the first (`0` - zero-relative) line to
last (`$`) line in the file. You can of course use other line numbers to restrict the range, and
there are other ways to create ranges as well (see about marking lines, below).

* **`s`** - substitute (change) command.

* **`/from`** - "from" pattern (regular expression).

* **`/to`** - "to" (results).

* **`/gi`** - optional switches, `g` means "global" (change all instances on a line, not just the
first one), `i` means (case) "insensitive."

Regular expressions you say! "Now we have two problems." But consider where we left off:
\index{regular expressions}

\drcap{But what about capitalization?}
```bash
that is a new line
that is a word
and so is that
that and thus
that and that and that
```

First, let's capitalize all `t` characters, but only where they are at the beginning of the line:

\drcap{Regular expression for the start of a line}
```bash
:0,$s/^t/T/
```

Yields:

\drcap{Voila! Capitals!}
```bash
That is a new line
That is a word
and so is that
That and thus
That and that and that
```

Now let's change all instances of "that" at the end of a line to be "that."

\drcap{Regular expression for the end of a line}
```bash
:0,$s/that$/that./
```

Ends up with:

\drcap{That with a full stop}
```bash
That is a new line
That is a word
and so is that.
That and thus
That and that and that.
```

And finally as a fun exercise for the reader, using the full power of regular expressions see if
you can figure out how this is adding commas to the end of lines that don't already have a period:

\drcap{Say what?}
```bash
:0,$s/\([^.]$\)/\1,/
```

Renders this:

\drcap{Nicely punctuated}
```bash
That is a new line,
That is a word,
and so is that.
That and thus,
That and that and that.
```

**Hint:** While trying to figure that out, search the Internet for regular expression "capturing
groups."

## "X" Marks the Spot{.unnumbered}

You can "mark" lines in `vi` for use in "ranges" like the "substitute" (change) command above.
Let's say you have a file like the following:

\drcap{Simple file}
```bash
This is a line
This is also a line
This, too
This is next
This is last
```

Maybe we want to change the "This" on the first three lines to "That," but not the last two
(imagine this is a much more complex example). We could do it by hand with the `r` command, but
that's tedious and error prone. Instead, we can "mark" a range.

1. Place the cursor on the first line and use the `m` command followed by a one-character "label"
like `x` (I typically use `m` so I don't have to move my fingers, e.g., `mm`).
\drvic{m}{mark}

2. Place the cursor on the third line and again use the `m` command, but ***with a different label
character*** (I usually use `n` so my fingers don't travel far, so `mn`).

3. Now you can use the `'` character followed by a label to denote the beginning and end of the
range in all kinds of `vi` commands. In our case we want to change "This" on the first three lines,
so:
\drvic{'}{reference a mark}

```bash
:'m,'ns/This/That/
```

Try doing that in Notepad!

**Note:** We could have done that with line ranges, too (`:0,2s/This/That/`), but figuring out the
beginning and ending lines in a large range is a pain. It is much easier to just mark them and go.

## Executing External Commands{.unnumbered}

Sometimes in `vi` it would be great to run the contents of the file through an external command
(`sort` is a favorite) without saving and exiting the file, sorting it, and then re-editing it. We
can do that with `!`, which works a lot like the "substitute" (change) command.
\drtxt{sort}
\drvic{"!}{invoke external command}
\index{*@\texttt{"!} (\texttt{vi} invoke external command)}

To sort the whole file in place:

\drcap{Sort a whole file in vi}
```bash
:0,$!sort
```

To sort a marked range:

\drcap{Sorting a range}
```bash
:'m,'n!sort
```

Another handy command to check out for this kind of thing, especially for formatting written text,
is the [`fmt`](http://linux.die.net/man/1/fmt) command.
\drtxt{fmt}

## The Unseen World{.unnumbered}

Any technical person knows that all the binary permutations of possible values for a byte aren't
mapped to visible characters. Some are ["control
characters"](https://en.wikipedia.org/wiki/Control_character) that range back to the teletype days.
For example, a tab character is hexadecimal 9 (`0x09`), but is often represented as `\t` in many
programming languages, regular expressions and the like.

Similarly, the "end of line" is marked by a control character. Or in the case of Windows, ***two***
control characters. And this causes no end of problems when editing files that can be opened on
both "UNIX" systems and Windows.

On "UNIX," the line feed control character (`0x0a`, or `\n`) is all that marks the end of a line.
For historical reasons (CP/M), Windows ends each line with two control characters, carriage return
(`0x0d`, or `\r`) and line feed. The two together are often referred to as "CRLF."
\drios{CP/M}

This difference manifests in two ways:

1. If you've ever opened a file on Windows in Notepad and all the lines "flow" even though they're
supposed to be individual lines, that means it is probably using "UNIX" end-of-lines (`\n`) only.
Use a line feed aware editor such as [Notepad++](https://notepad-plus-plus.org/) instead.

2. If you open a file in `vi` and it has a `^M` at the end of every line and/or at the bottom you
see something like:

        "Agenda.md" [dos format] 16 lines, 1692 characters

    Either of those mean the file lines each end with "CRLF" (`\r\n`). To change it in `vi` you can
    override the `ff` (file format) setting:

        :set ff=unix

Since regular expressions have syntax for expressing control codes in either shorthand (`\t`) or as
hexadecimal, you can alter control codes in `vi` easily. For example, to change all tab characters
to four spaces:

\drcap{Change all tabs to four spaces as God meant them to be}
```bash
:0,$s/\t/    /g
```

## Let's Get Small{.unnumbered}

So, `vi` is the best we can do? No. On many Linux systems an alternative terminal-based editor will
be installed, often several. There may be [`emacs`](http://linux.die.net/man/1/emacs), which ***will*** make you yearn for the simplicity of `vi`.
\dreds{emacs}

Here are two jokes that are only funny once you've used `emacs`:

> *"'emacs' stands for 'escape', 'meta', 'alt', 'control', 'shift'."*

> *"'emacs' is a good operating system, but it could use an editor."*

If those are funny to you, then you have already been infected by `emacs`. The prognosis is grim.

But there may also be others, notably [`pico`](http://linux.die.net/man/1/pico) and its successor,
[`nano`](http://linux.die.net/man/1/nano). You can see the difference the second you see a file open
in `nano` - in this case, the generated Github-flavored Markdown of this document:
\dreds{nano}
\dreds{pico}

\drcap{Editing a file in \texttt{nano}}
```bash
    GNU nano 2.2.6        File: TenStepsToLinuxSurvival.md                        

|![Merv sez, "Don't panic."](./images/Merv.jpg "Merv sez, 'Don't panic.'")
Merv sez, "Don't panic."

By James Lehmer

v0.7

![](./images/cc-by-sa.png "Creative Commons Attribution-ShareAlike 4.0 Internat$
*Jim's Ten Steps to Linux Survival* by James Lehmer is licensed under a [Creati$

**Dedicated to my first three technical mentors** - Jim Proffer, who taught me $

Introduction
============

> *"And you may ask yourself, 'Well, how did I get here?'"* - Talking Heads (*O$

This is my little "Linux and Bash in 10 steps" guide. It's based around what I $

                              [ Read 3627 lines ]
^G Get Help  ^O WriteOut  ^R Read File ^Y Prev Page ^K Cut Text  ^C Cur Pos
^X Exit      ^J Justify   ^W Where Is  ^V Next Page ^U UnCut Text^T To Spell
```

Two things to note about the above:

1. The cursor (represented above by `|`) is already in "insert mode" like you would expect in a
"normal" editor such as Notepad.

2. Those lines at the bottom are commands that can be invoked by shortcuts. For example, `^O` means
`Ctrl-O` and stands for "WriteOut" or "Save." That's probably easier to remember than `:w` in `vi`,
especially since it is reminding you of it right there on the screen!

So why not always use `nano`? Why does this book harp on and on `vi`? Why do I insist on keeping
all this arcane `vi` nonsense loaded in my head (and I do!)? Because often, like in the nightmare
scenario I posed in the *Introduction*, you may not have control over the system, no ability to
install packages - you have to take what the system has. And it's a pretty sure bet it is going to
have `vi`. So if you have `nano` (or `pico`), use it! You can find out simply by typing in `nano
<filename>` on what you want to edit and see if it works. But if `nano` or `pico` aren't installed,
grit your teeth, remember "insert mode" vs. "command mode", and use `vi`.

And if you have the opportunity to use `emacs`...don't.

## Editing on the Command Line

Sometimes you want to script an edit, typically something similar to a "replace all" that needs
to occur on a file without human intervention. The [`sed`](http://linux.die.net/man/1/sed) (stream
editor) command to the rescue! `sed` has a similar syntax to the "substitute" commands in `vi` (in
fact, the latter got its syntax from the former).
\dreds{sed}

Here is a real-world example. A [MySQL](https://www.mysql.com/) database backup is in reality a text
file containing a large number of SQL statements - the `DROP`, `CREATE` and `INSERT` statements
necessary to recreate the database from scratch. Let's say you have two Wordpress sites,
`www.mysite.com` for production, and `dev.mysite.com` for a testing environment. When Wordpress is
configured, it puts its site address, e.g., `www.mysite.com`, in multiple places in the database. If
you want to refresh your dev site from production, you would backup the MySQL database to a file
like `mysqlbak.sql`. But before loading it in the dev site's database, you would like to change all
those `www.mysite.com` references to `dev.mysite.com`. `sed` to the rescue! Behold:

\drcap{Editing a file with \texttt{sed}}
```bash
~ $ cat mysqlbak.sql | sed 's/www.mysite.com/dev.mysite.com/g' > devbak.sql
```

How cool is that? If you remember the "substitute" command examples for `vi`, above, it should be
perfectly clear what is going on here.