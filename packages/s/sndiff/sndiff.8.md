sndiff 8 "February 2025" "System Manager's Manual"
==================================================

# NAME

**sndiff** - Tool for diffing packages and files from snapshots

# SYNOPSIS
**sndiff** [OPTIONS] [OLD_SNAPSHOT] [NEW_SNAPSHOT] [COMMAND]

# DESCRIPTION

**sndiff** is a small utility that reports differences between btrfs snapshots created by snapper(8) and zypper(8).

By default it shows information about packages and files in `/etc`, that can return diff -u output for changelogs and modified files.

# COMMANDS

The following command line verbs are known:

`list`
: List snapshots in the system

`help`
: Print this message or the help of the given subcommand(s)

# ARGUMENTS

`OLD_SNAPSHOT`
: Snapshot to compare with.  If missing will be autodetected.

`NEW_SNAPSHOT`
: Optional reference snapshot.  Usually the current one.  If missing will be autodetected.

# OPTIONS

`--packages`, `-p`
: Report only changes in packages

`--etc`, `-e`
: Report only changes in `/etc`

`--diff`, `-d`
: Include diff output for changes

`--short`, `-s`
: Short and compact summary of changes

`--json`, `-j`
: JSON output

`--no-colors`, `-n`
: Disable colored output

`--verbose`, `-v`
: Verbose output

`--help`, `-h`
: Print help

`--version`, `-V`
: Print version

# EXAMPLES

`sndiff 3`
: Compare the snapshot 3 with the current active one, showing list
  of updated, downgraded, added and removed packages, and changed,
  added and removed files in `/etc`.

`sndiff 3 4`
: Compare snapshots 3 (old) and 4 (new), showing the same information
  than before.

`sndiff`

: Compare the previous snapshot (old) with the current active one
  (new).  The previous snapshot selection depends on the kind of
  distribution (MicroOS or Tumbleweed).

`sndiff --short 3 4`
: Present the information in a compact way.

`sndiff --packages 3 4`
: Only compares packages from snapshots 3 and 4.

`sndiff --etc 3 4`
: Only compares `/etc` files.

`sndiff --diff 3 4`
: Shows diff -u (10 lines max) of changelog for updated or downgraded
  packages, and changed files from `/etc`.

`sndiff --diff --json 3 4`
: Generate JSON output, this time includes the full differences.

`sndiff --no-colors 3 4`
: No colorized output

`sndiff list`
: Print a table of current snapshots.  Mark the snapshot selected as
  `old` and `new`.

`sndiff --json list`
: Shows the same table in JSON format.

# SEE ALSO
**snapper**(8), **transactional-update**(8), **zypper**(8)
