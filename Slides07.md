
# Step 7

# The Whole Wide World

## Network commands

> * `ping yahoo.com` - works like `ping -t` in `CMD.EXE`
> * `traceroute yahoo.com`
> * `dig yahoo.com`
> * `whois yahoo.com`

## `sudo` make me a sandwich

> * Many commands require "super-user" privileges
> * One way to get it is to log-in as "root"
>     * Not recommended in general
> * `sudo` - allows a pre-authorized user to run privileged commands
> * `sudo apt-get update`

## Surfin' the command prompt

> * `lynx` - command-line browser
> * `wget` - get files over HTTP, FTP, etc.
> * `curl` - alternative to `wget`

## Sending mail

```
~ $ email --blank-mail --subject "Possibly corrupted files found..." \
  --smtp-server smtp --attach badfiles.csv --from-name NoReply \
  --from-addr noreply@mycorp.com alert@mycorp.com
```

## Logging in elsewhere

> * `ssh` - secure shell
>     * `ssh myuser@remoteserver`
> * `scp` - secure copy (over `ssh`)
>     * `scp -r myfiles/* myuser@remoteserver:/home/myuser/myfiles/.`

## Network configuration

> * `ifconfig` - display current network settings
> * `cat /etc/resolv.conf` - display current DNS settings
> * `cat /etc/hosts` - display local network aliases