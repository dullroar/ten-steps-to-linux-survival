
# Grokking `grep`

***And probably gawking at `awk` while we are at it, which means regular
expressions, too. Now we have two problems.***

> *"Some people, when confronted with a problem, think 'I know, I'll use
> regular expressions.' Now they have two problems."* - Jamie Zawinski 

If the `file` command is useful for finding file system entries based
on their attributes, the [`grep`](http://linux.die.net/man/1/grep)\drcmd{grep}
command is good for finding files whose ***contents*** match a [regular
expression](https://en.wikipedia.org/wiki/Regular_expression)\index{regular expression}.
You already know at least one regular expression, the wildcard `*`
character from the `CMD.EXE`\drshl{CMD.EXE} prompt and Windows Explorer. It means
"match zero or more characters." We'll cover more on regular expressions,
or "regexes," in a moment.

First, an example of `grep`, showing all files in a directory with the
pattern "is" in them:

\drcap{grep example}
```bash
~ $ touch a b c
~ $ echo This sequence of characters is called a \"string\". > d
~ $ cat d
This sequence of characters is called a "string".
~ $ ls
a  b  c  d
~ $ grep is *
d:This sequence of characters is called a "string".
```

## Expressing Yourself Regularly{.unnumbered}

So what are "regular expressions?" Simply, they are patterns for matching
"strings," which are sequences of "characters," e.g.:

\drcap{A string}
```bash
This sequence of characters is called a "string".
```

That is a string. So is, "That is a string." And "That" and "T" and so
on. ***In general*** (with many exceptions), the UNIX world view is that
everything is composed of text (or "strings"), and that creating, changing,
finding and passing around text is the primary mode of operation.

In the `grep` example, we can see a regular expression can be as
simple as "is". It can also be as complicated as:

\drcap{Complex regular expression}
```bash
(?bhttp://[-A-Za-z0-9+&@#/%?=~_()|!:,.;]*[-A-Za-z0-9+&@f
```

That shows at least one attempt at being [a very complete parser of valid
HTTP URLs](http://blog.codinghorror.com/the-problem-with-urls/).
Wow! What's all that? Now you see why you have two problems. Even if you
get that all figured out, or if you actually sit and create something like
that from scratch yourself (and it works!), imagine coming back six months
later and trying to decipher it again.

There are literally [whole web sites](http://www.regular-expressions.info/)
and books on just regular expressions. With variations they are used in all
"UNIX" shells, Perl, Python, Javascript, Java, C# and more. So obviously
(a) they are really useful, and (b) we're not going to cover all of regexes
here.

There are so many things you can do, the only thing to remember is "regular
expressions" when you think "I need to find things based on a pattern" and
then research what it will take to define the pattern you want.

In the mean time, following are a few ***simple*** regex examples. Consider
the file `invoices`:

\drcap{Invoices file}
```bash
~ $ cat invoices
Combine brakes  400
Combine motor   1500
Combine tires   2500
Tractor brakes  300
Tractor motor   1000
Tractor tires   2000
Truck   brakes  200
Truck   tires   400
Truck   tires   400
Truck   tires   400
Truck   winch   100
```

Let's find all lines with "tractor":

\drcap{Trying to find tractors}
```bash
~ $ grep tractor invoices
```

Huh, nothing was found. But this is UNIX-land, so we know it is sensitive -
about case anyway:

\drcap{Trying to find tractors, part two}
```bash
~ $ grep Tractor invoices
Tractor brakes  300
Tractor motor   1000
Tractor tires   2000
```

Or we could just tell `grep` we are insensitive (to case, anyway):

\drcap{Let's be insensitive}
```bash
~ $ grep -i tractor invoices
Tractor brakes  300
Tractor motor   1000
Tractor tires   2000
```

And just to remind you about long-style parameters:

\drcap{Spelling out our insensitivity}
```bash
~ $ grep --ignore-case tractor invoices
Tractor brakes  300
Tractor motor   1000
Tractor tires   2000
```

But what ***lines*** are those on?

\drcap{Print the line numbers of matches}
```bash
~ $ grep -i -n tractor invoices
1:Tractor       motor   1000
2:Tractor       brakes  300
3:Tractor       tires   2000
```

To get more complicated, we can pass the `-E` parameter (for *extended*
regular expressions) and start doing some really fun stuff. Let's look for
lines with either "Tractor" or "Truck":

\drcap{Extended regular expressions}
```bash
~ $ grep -E "Tractor|Truck" invoices
Tractor brakes  300
Tractor motor   1000
Tractor tires   2000
Truck   brakes  200
Truck   tires   400
Truck   tires   400
Truck   tires   400
Truck   winch   100
```

For me, the following keep coming up when using regular expressions:

* **`one|other`** - find `one` pattern or the `other`.
* **`^`** - pattern for the beginning of a line.
* **`$`** - pattern for the end of a line.
* **`?`** - match exactly one character.
* **`*`** - match zero or more characters.
* **`+`** - match one or more characters.
* **`[A-Z]`** - match any character in a range (such as in this case any
uppercase Latin alphabetic character).
* **`[n|y]`** - match one character or another (such as `n` or `y` here).

For example, to find the lines that end in `400`:

\drcap{Find lines ending with 400}
```bash
$ grep  -E "^*400$" invoices
Combine brakes  400
Truck   tires   400
Truck   tires   400
Truck   tires   400
```

## Groveling With `grep`{.unnumbered}

To recursively find all files that contain the string "pdfinfo":

\drcap{Recursive grep}
```bash
~ $ grep -R -i pdfinfo *
./FileCheckers/otschecker:# pdfinfo, too. If pdfinfo thinks it's junk, ...
./FileCheckers/otschecker:        pdfinfo=`pdfinfo -opw foo "$1" 2>&1 1...
./FileCheckers/otschecker:        if [ $rc != 0 -a "$pdfinfo" != "Comma...
./FileCheckers/pdfchecker:        # pdfinfo, too. If pdfinfo thinks it'...
./FileCheckers/pdfchecker:                pdfinfo=`pdfinfo "$1" > /dev/...
./FileCheckers/pdfpwdchecker:# pdfinfo, too. If pdfinfo thinks it's jun...
./FileCheckers/pdfpwdchecker:        pdfinfo=`pdfinfo -opw foo "$1" 2>&...
./FileCheckers/pdfpwdchecker:        if [ $rc != 0 -a "$pdfinfo" = "Com...
./FileCheckers/README.md:* ***[pdfinfo(1)](http://linux.die.net/man/1/p...
```

The above is functionally equivalent but ***much*** quicker than:

\drcap{Recursive grep is faster than find plus grep}
```bash
~ $ find . -type f -exec grep -H -i pdfinfo \{\} \; 
```

**Note:** In general, if a command has its own "recursive" option (such as
`-R` with `grep`), it is quicker to use that rather than to invoke the
command repeatedly using `find`\drcmd{find} instead.

However, sometimes you can use `find` to filter down files to be checked
before having `grep` read through them, and have that result in much
quicker results.

For example, if you only wanted to check files that contain "pdfinfo" that
have been created or modified since the last time you checked, it ***could
be*** quicker to run something like:

\drcap{A better example of when to use find plus grep}
```bash
~ $ find . ! -name pdfinfo.log -newer pdfinfo.log -type f -exec grep -H \
    -i pdfinfo \{\} \; > pdfinfo.log
```

This says to ignore files named "pdfinfo.log" (`! -name pdfinfo.log`) and
otherwise look for files (`-type f`) containing "pdfinfo" (`-exec grep
...`) that haven't been checked since the last time "pdfinfo.log" was
modified (`-newer pdfinfo.log`). In my tests the first run (which initially
creates the "pdfinfo.log" file) ran in 30 seconds but subsequents runs took
just a few seconds. This was because the number of files to be searched
through all directories was big enough it paid to pre-filter the results
before handing them to `grep`.

## Gawking at `awk`{.unnumbered}

I don't have much to say about [`awk`](http://linux.die.net/man/1/awk)\drcmd{awk}
other than:

1. It is named after its three authors,
[Aho, Weinberger and Kernighan](https://en.wikipedia.org/wiki/AWK), all
three of whom are computer science greats from Bell Labs. The GNU version
is called `gawk`, of course!

2. It is a "data driven scripting language." That's a fancy way of saying
it was written specifically with slicing and dicing text in mind.

3. It generally is broken out when the typical "UNIX" commands and shell
features like pipes and redirection aren't enough.

4. Usually, if I start thinking of `awk`, I start thinking of a way to
program the answer in another language, or reframe the question to get an
answer not requiring `awk`.

That said, it is a powerful knife in the tool belt, and you should be
aware it exists.

To whet your taste, here is the type of "one-liner" for which `awk` is
famous, in this case [formatting and printing a report on user
ids](http://www.ibm.com/developerworks/library/l-awk1/) from `/etc/passwd`:

\drcap{awk example}
```bash
~ $ awk -F":" '{ print "username: " $1 "\t\tuid:" $3 }' /etc/passwd
username: root		uid:0
username: daemon		uid:1
username: bin		uid:2
username: sys		uid:3
username: sync		uid:4
username: games		uid:5
username: man		uid:6
username: lp		uid:7
username: mail		uid:8
username: news		uid:9
username: uucp		uid:10
...and so on...
```