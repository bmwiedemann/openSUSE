# homeshick for openSUSE

## Target audience

This package contains a single shared installation of homeshick suitable for
users.  It provides the default `homeshick` command ready for use without
configuration.

## Setup

To gain full functionality (the `homeshick cd` command), and maximum comfort of
use (e.g., auto-completion), it is necessary for shell startup scrips to source
a homeshick setup script. The normal installation instructions for homeshick
explain how to do it:

[homeshick installation instructions](https://github.com/andsens/homeshick/wiki/Installation)

When following those instructions, any mention of cloning the homeshick git
repository can be ignored, obviously. Also, the path
`$HOME/.homesick/repos/homeshick` should be substituted with
`/usr/share/homeshick` to access the corresponding files installed by this
package.

For example, when the installation instructions tell you to run

```
printf '\nsource "$HOME/.homesick/repos/homeshick/homeshick.sh"' >> $HOME/.bashrc
```

you should instead run

```
printf '\nsource "/usr/share/homeshick/homeshick.sh"' >> $HOME/.bashrc
```


## Multiple installations

The default method of installing homeshick is for each user to make a private
clone of the upstream repository from Github. For users wanting to modify the
implementation, or to make contributions to homeshick, that remains the way to
go about it.

This package can co-exist with git clone(s) of homeshick. Assuming that a setup
script from this package has been sourced, as instructed above, the environment
variable `HOMESHICK_DIR` can be used to control which instance of homeshick is
run, the default being the instance installed by this package.

