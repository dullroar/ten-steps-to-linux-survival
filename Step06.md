  
# `vi`

***How to stay sane for 10 minutes in `vi`. Navigation, basic editing, find,
change/change-all, cut and paste, undo, saving and canceling. Plus easier
alternatives like `nano`, and why `vi` still matters.***

> *"You're too young to know."* - Vi (*Grease*)

[`vi`](http://linux.die.net/man/1/vi) stands for *visual editor* (as well
as the Roman numeral for 6, which is why it is this chapter), and once
you use it you will understand what editing from the command line
must've been like for `vi` to seem both "visual" and a step forward.

Many Linux clones don't use `vi` proper, but a port called
[`vim`](http://www.vim.org/) ("**vi** i**m**proved") "that can then be
accessed via the alias `vi`. The differences tend to be minor, with `vim`
being more customizable.

`vi` and a similar editor, [`emacs`](http://linux.die.net/man/1/emacs),
both tend to trip up users from GUI operating systems such as Windows or
OS X that have editors like Notepad that are always ready for user input.

Instead, `vi` typically starts in "command mode," where keystrokes
execute various navigation and editing commands. To actually insert text
requires a keystroke such as `i` while in command mode, which then
causes `vi` to go into "insert mode." Insert mode is what most Windows
users expect from an editor, i.e., when you type the line changes. The
`ESC` key exits insert mode.

It is as hard to get used to as it sounds, and you ***will*** execute text
you were meaning to insert as commands, and commands that you were meaning
to execute as text you ***will*** insert as text, and sooner or later you
***will*** enter `vi` commands into Notepad. That will be the day you know
you've become truly tainted.

This will not even begin to scratch the surface of `vi`, when there are
many, many books and web sites just on wielding it to its full potential.
In the hands of someone who has mastered it, `vi` can do some really
remarkable feats of editing way beyond the capability of most modern GUI
programming environments.

## Command Me

Again, when you first open `vi` it is in "command mode." That means any
keystrokes you enter will "do something." The "something" to be done may
be navigating around the file, inserting, deleting or changing text,
manipulating lines, "undo", writing the changes to disk and the like.

What are commands? Well, for example `d` means "delete." We'll talk about
how to specify ***what*** to delete next. `i` tells `vi` to enter "insert
mode" at the point where the cursor is. `0` navigates to the start of the
current line, and so on.

Commands can have ***modifiers*** preceding and following them. Consider
the "delete" command, `d`. If we follow with `w` as in `dw` while in
command mode, it will delete a whitespace-delimited "word" starting at
where the cursor is through (including) the next whitespace character.

If the `|` in the following represents the cursor:

```
This is a wo|rd and so is this.
```

Then typing `dw` will delete from the cursor position the characters `r`,
`d` and the space, leaving the following:

```
This is a wo|and so is this.
```

We can also specify a number of times we want to perform a command before
the command. So now if we wanted to delete three words from the cursor
position in the above, we'd use `3dw` and end up with:

```
This is a wo|this.
```

Again, in all these examples the `|` represents the cursor.

There is a little bit of nuance in using command modifiers. Consider the
`r` (*replace*) command. It is typically used to change the single
***character*** under the cursor. You may be tempted to think you can do
something like `rw` for "replace word," but it is actually going to simply
replace the current character with a `w`, whereas the real command for
doing that is `cw` ("change word"). In addition, you can use repeaters as
above, just be sure you understand `r` means "replace a single character,"
so `3rx` executed on:

```
This is a wo|this.
```

...results in:

```
This is a woxx|xs.

```

To quit without saving enter `:q`. To write any file changes to disk use
`:w`. To save and quit, type `:wq`.

## Undo Me

`u` is the "undo" command. It "undoes" or reverts the last change. You can
undo the last *n* changes just as you'd expect, e.g., `3u` undoes the last
three changes.

If you want to just cancel out of the file without writing any changes to
disk, use `:q!` (the `!` means to force the quit without saving).

If you want to protect yourself from inadvertent changes to a file you can
always open it using [`view`](http://linux.die.net/man/1/view), the alias
for `vi` invoked in read-only mode.

## Circumnavigating `vi`

In modern implementations of `vi` (like `vim`) running under modern shells
the arrow and page keys will work as you expect, ***in general***. However,
you may want to be aware that when in insert mode, while the left and right
arrows may work for navigation, often the up and down arrows can introduce
"garbage" characters into the file (since you are in insert mode). This is
because the keymappings for those keys aren't being interpreted correctly.
I usually just swear, exit insert mode, hit `u` and try again.

As an example, under Cygwin I went into `vi`, went into insert mode after
the first line, typed in "This is a new line" and then hit the up arrow
five times, yielding this:

```
This is a word and so is this.
A
A
A
A
A
This is a new line
```

When in command mode, there are multiple ways to jump around in the file
besides using the arrow and page keys:

* **`0`** - jumps to the beginning of the current line.

* **`$`** - jumps to the end of the current line.

* **`w`** - jumps forward a whitespace-delimited "word" on the current
line (and of course `3w` would jump forward three "words").

* **`b`** - jumps back a whitespace-delimited "word" on the current line.

* **`G`** - jumps to end of file.

* **`:0`** - jumps to start of file.

* **`/foo`** - find "foo" going forward toward the end of the file.

* **`?foo`** - find "foo" going backward toward the front of the file.

* **`n`** - find the next instance of the search text specified by the last
`/` or `?`.

* **`p`** - find the previous instance of the search text specified by the
last `/` or `?`.

## Insert Tab A Into Slot B

There are multiple ways to enter insert mode, but only one way to escape it
(pun intended - `ESC`, get it?)

* **`i`** - enters insert mode at the current cursor position.

* **`I`** - enters insert mode at the beginning of the current line.

* **`A`** - enters insert mode (appends) at the end of the current line.

* **`o`** - inserts a new line under (lowercase `o` = "lower" or "below")
the current line and puts the cursor on it in insert mode.

* **`O`** - inserts a new line over (uppercase `O` = "upper" or "above")
the current line and puts the cursor on it in insert mode.

## Ctrl-X, Ctrl-C, Ctrl-V

When you copy or cut/delete it, it goes into a "buffer." There are ways to
access multiple buffers, but mostly you want the very last thing to be put
in the buffer, especially for copying (or cutting) and pasting. Note that
"cutting" and "deleting" are synonymous, since deleting puts the deleted
text in the buffer.

Another thing to understand is that a command "doubled" or repeated
typically means "the whole line." So `dd` means "delete the whole line the
cursor is currently on."

So if deleting is synonymous with cutting, and the cursor is on the second
line:

```
This is a word and so is this.
This is a new line.|
```

Then executing `dd` leaves:

```
|This is a word and so is this.
```

We know "This is a new line." went into  the buffer. We can paste it back
above the current line with `P`, which would result in:

```
|This is a new line.
This is a word and so is this.
```

Here are some more examples:

* **`p`** - paste the buffer into the current line starting after the
cursor location.

* **`3dd`** - delete (cut) three lines into the buffer.

* **`5yw`** - "yank" (copy) five words starting at the current cursor
position into the buffer.

## Change Machine

The hardest thing to get down in `vi` is the *substitute* (change) command.
Its syntax is esoteric, but once you've memorized it, it becomes
intuitive.

The most common scenario is the "change all" command. Given the following
file:

```
This is a new line
This is a word
and so is this
This and thus
This and this and this

```

Let's change all "this" to "that" by using:

```
:1,$s/this/that/
```

We'll get into the details in a bit, but the results are interesting, and
not what we'd expect:

```
This is a new line
This is a word
and so is that
This and thus
This and that and this
```

It only changed the "that" at the end of the third line, and the middle
"that" on the last. Why? Two reasons:

1. The substitute command is case sensitive, just like everything else in
Linux, unless you tell it to be *insensitive*.

2. The substitute command only makes one change per line unless you tell
it to change *globally*.

So let's hit `u` to reset (undo) the file, and try again with this:

```
:1,$s/this/that/i
```

Results in:

```
that is a new line
that is a word
and so is that
that and thus
that and this and this
```

That's better. There is at least one "that" on every line that had a
"this," so passing the `i` ("insensitive") switch at the end of the
`s` (substitute) command helped with that. But we still didn't get all
the "this" words changed, as the last line shows. Hit `u` and try one more
time with this:

```
:1,$s/this/that/gi
```

Results in:

```
that is a new line
that is a word
and so is that
that and thus
that and that and that
```

That's what we wanted! In general, if you are looking for a Windows
Notepad-like, case insensitive "change all," the magic string to remember
is:

```
:1,$s/from/to/gi
```

Picking that apart, we have:

* **`:`** - tells `vi` a special command is coming.

* **`1,$`** - specifies a line range, in this case from the first (`1`) to
last (`$`) lines in the file. You can of course use other lines numbers to
restrict the range, and there are other ways to create ranges as well.

* **`s`** - substitute (change) command.

* **`/from`** - "from" pattern (regular expression).

* **`/to`** - "to" (results).

* **`/gi`** - optional switches, `g` means "global" (change all instances
on a line, not just the first one), `i` means (case) "insensitive."

Regular expressions you say! Now we have two problems! But consider:

```
that is a new line
that is a word
and so is that
that and thus
that and that and that
```

First, let's capitalize all `t` characters, but only where they are at the
beginning of the line:

```
:1,$s/^t/T/
```

Yields:

```
That is a new line
That is a word
and so is that
That and thus
That and that and that
```

Now let's change all instances of "that" at the end of a line to be "that."

```
:1,$s/that$/that./
```

Ends up with:

```
That is a new line
That is a word
and so is that.
That and thus
That and that and that.
```

And finally as a fun exercise for the reader, using the full power of
regular expressions see if you can figure out how this is adding commas
to the end of lines that don't already have a period:

```
:1,$s/\([^.]$\)/\1,/
```

Like this:

```
That is a new line,
That is a word,
and so is that.
That and thus,
That and that and that.
```

## "X" Marks the Spot

You can "mark" lines in `vi` for use in "ranges" like the "substitute"
(change) command above. Let's say you have a file like the following:

```
This is a line
This is also a line
This, too
This is next
This is last
```

Maybe we want to change the "This" on the first three lines to "That," but
not the last two (imagine this is a much more complex example). We could do
it by hand, but that's tedious and error prone. Instead, we can "mark" a
range.

1. Place the cursor on the first line and use the `m` command followed by
a one-character "label" like `x` (I typically use `m` so I don't have to
move my fingers).

2. Place the cursor on the third line and again use the `m` command, but
***with a different label character*** (I usually use `n` so my fingers
don't travel far).

3. Now you can use the `'` character followed by a label to denote the
beginning and end of the range in all kinds of `vi` commands. In our case
we want to change "This" on the first three lines, so:

```
:'m,'ns/This/That/
```

Try doing that in Notepad!

## Executing External Commands

Sometimes in `vi` it would be great to run the contents of the file through
an external command (`sort` is a favorite) without saving and exiting the
file, sorting it, and then re-editing it. We can do that with `!`, which
works a lot like the "substitute" (change) command.

To sort the whole file in place:

```
:1,$!sort
```

To sort a marked range:

```
:'m,'n!sort
```

Another handy command to check out for this kind of thing, especially for
code or written text, is the [`fmt`](http://linux.die.net/man/1/fmt)
command.

## The Unseen World

Any technical person knows that all the binary permutations of possible
values for a byte aren't mapped to visible characters. Some are
["control characters"](https://en.wikipedia.org/wiki/Control_character)
that range back to the teletype days. For example, a tab character is
hexadecimal 9 (`0x09`), but is often represented as `\t` in many
programming languages, regular expressions and the like.

Similarly, the "end of line" is marked by a control character. Or in the
case of Windows, ***two*** control characters. And this causes no end of
problems when editing files that can be opened on both "UNIX" systems and
Windows.

On "UNIX," the line feed control character (`0x0a`, or `\n`) is all that
marks the end of a line. For historical reasons (CP/M), Windows ends each
line with two control characters, carriage return (`0x0d`, or `\r`) and
line feed. The two together are often referred to as "CRLF."

This difference manifests in two ways:

1. If you've ever opened a file on Windows in Notepad and all the lines
"flow" even though they're supposed to be individual lines, that means it
is probably using "UNIX" end-of-lines (`\n`) only. Use a line feed aware
editor such as Notepad++ instead.

2. If you open a file in `vi` and it has a `^M` at the end of every
line and/or at the bottom you see something like:

        "Agenda.md" [dos format] 16 lines, 1692 characters

    Either of those mean the file lines each end with "CRLF" (`\r\n`). To
    change it in `vi` you can use the following command (`ff` means
    "file format":

        :set ff=unix

Since regular expressions have syntax for expressing control codes in
either shorthand (`\t`) or as hexadecimal, you can alter control codes in
`vi` easily. For example, to change all tab characters to four spaces:

```
:1,$s/\t/    /g
```

## Let's Get Small

So, `vi` is the best we can do? No. On many Linux systems an alternative
terminal-based editor will be installed, often several. There may be
[`emacs`](http://linux.die.net/man/1/emacs), which will make you yearn for
the simplicity of `vi`.

Here are two jokes that are only funny once you've used `emacs`:

> *"'emacs' stands for 'escape', 'meta', 'alt', 'control', 'shift'."*

> *"'emacs' is a good operating system, but it could use an editor."*

If those are funny to you, then you have already been infected by `emacs`.
May God have mercy on your soul.

But there may also others, notably
[`pico`](http://linux.die.net/man/1/pico) and its successor,
[`nano`](http://linux.die.net/man/1/nano). You can see the difference the
second you see a file open in `nano`:

```
  GNU nano 2.2.6                 File: Title.md                                        

|[author]: # (Jim Lehmer)
[title]: # (Jim's Ten Steps to Linux Survival)

# Jim's Ten Steps to Linux Survival

**By Jim Lehmer**

<a rel="license"
href="http://creativecommons.org/licenses/by-sa/4.0/"><img
alt="Creative Commons License" style="border-width:0"
src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png"
/></a><br /><span xmlns:dct="http://purl.org/dc/terms/"
property="dct:title">Jim's Ten Steps to Linux Survival</span>
by <span xmlns:cc="http://creativecommons.org/ns#"
property="cc:attributionName">James
Lehmer</span> is licensed under a <a rel="license"
href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons
Attribution-ShareAlike 4.0 International License</a>.
                                   [ Read 18 lines ]
^G Get Help   ^O WriteOut   ^R Read File  ^Y Prev Page  ^K Cut Text   ^C...
^X Exit       ^J Justify    ^W Where Is   ^V Next Page  ^U UnCut Text ^T...
```

Two things to note about the above:

1. The cursor (represented above by `|`) is already in "insert mode" like
you would expect in a "normal" editor like Notepad.

2. Those lines at the bottom are commands that can be invoked by shortcuts.
For example, `^O` means `Ctrl-O` and stands for "WriteOut" or "Save."
That's probably easier to remember than `:w` in `vi`, especially since it
is reminding you of it right there on the screen!

So why not always use `nano`? Why does this book harp on and on `vi`?
Why do I insist on keeping all this arcane `vi` nonsense loaded in my head
(and I do!)? Because often, like in the nightmare scenario I posed in the
*Introduction*, you may not have control over the system, no ability to
install packages - you have to take what the system has. And it's a pretty
sure bet it is going to have `vi`. So if you have `nano` (or `pico`), use
it! But if you don't, grit your teeth, remember "insert mode" vs.
"command mode", and use `vi`.

And if you have the opportunity to use `emacs`...don't.
  
