
# Step 4

# Grokking `grep`

## `grep`

Finds files based on their ***content***

```
~ $ touch a b c
~ $ echo This sequence of characters is called a \"string\". > d
~ $ cat d
This sequence of characters is called a "string".
~ $ ls
a  b  c  d
~ $ grep is *
d:This sequence of characters is called a "string".
```

## Famous quote

> *"Some people, when confronted with a problem, think 'I know, I'll use regular expressions.' Now they have two problems."* - Jamie Zawinski

## Regular expressions

A "regex" is a pattern for matching strings

> * `dir *.txt` - match zero or more characters
> * `find //myserver/myshare/logs/000[4-9] -print`
> * `grep is *` - find "is" in all files in current directory

## Helpful regexes

* **`one|other`** - find `one` pattern or the `other`.
* **`^`** - pattern for the beginning of a line.
* **`$`** - pattern for the end of a line.
* **`?`** - match exactly one character.
* **`*`** - match zero or more characters.
* **`+`** - match one or more characters.
* **`[A-Z]`** - match any character in a range (such as in this case any uppercase Latin alphabetic character).
* **`[n|y]`** - match one character or another (such as `n` or `y` here).

## Why 2 problems?

What does the following do?

```
(?bhttp://[-A-Za-z0-9+&@#/%?=~_()|!:,.;]*[-A-Za-z0-9+&@f
```

> * Checks a Web URL for validity
> * Are you going to remember that?
> * Are you going to be able to figure it out?