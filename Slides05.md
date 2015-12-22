
# Step 5

# A Series of Pipes

## `stdin`, `stdout`, `stderr`

* **stdin** - input, file descriptor 0
* **stdout** - output, file descriptor 1
* **stderr** - "error" output, file descriptor 2
* All three use the console in interactive mode by default

## Output redirection

```
~ $ echo Hello, world > hw
~ $ ls -l
total 1
-rw-rwxr--+ 1 myuser mygroup 13 Oct 22 10:40 hw
~ $ cat hw
Hello, world
```

## Input redirection


```
~ $ cat < hw
Hello, world
```

Equivalent to:

```
~ $ cat hw
Hello, world
```

## Errors

```
~ $ find . -exec cat \{\} \;
cat: .: Is a directory
This is a
This is b
This is c
cat: ./d: Is a directory
This is e
```

"Is a directory" is an error message

## Error redirection

```
~ $ find . -exec cat \{\} \; 2>/tmp/finderrors.log
This is a
This is b
This is c
This is e
~ $ cat /tmp/finderrors.log
cat: .: Is a directory
cat: ./d: Is a directory
```

This is where those "file descriptors" come in

## Logging ALL output to file

```
~ $ find . -exec cat \{\} \; >/tmp/find.log 2>&1
~ $ cat /tmp/find.log
cat: .: Is a directory
This is a
This is b
This is c
cat: ./d: Is a directory
This is e
```

The `2>&1` trick works in `CMD.EXE`, too!

## Rewrite vs. append

```
~ $ find . -exec cat \{\} \; >/tmp/find.log
```

vs.

```
~ $ find . -exec cat \{\} \; >>/tmp/find.log
```

## Everyone line up

```
~ $ cat *.txt | tr '\\' '/' | while read line ; do ./mycmd "$line" ; done
```

1.  `cat` echos all `.txt` files to `stdout`, piped to...
2.  [`tr`](http://linux.die.net/man/1/tr) translates any backslash characters before sending it into...
3.  A `while` loop that reads each line into a variable called `$line` and then calls...
4.  Some custom script or program called `./mycmd` passing in the value of each `$line`.

## Two places at once

```
~ $ find . -name error.log | tee > errorlogs.txt
```

> * Log output to `error.log`
> * Monitor its progress on the console at the same time