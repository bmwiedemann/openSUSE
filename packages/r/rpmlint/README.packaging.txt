= rpmlint-checks, rpmlint-tests =

The files from rpmlint-checks and rpmlint-tests managed in git. If
you need to make changes, you have the following options:
* Make them in git and update the package from git (you can file
  pull requests if you don't have write access)
* Create a patch, add the patch to the package and let one of the
  maintainers commit it for you

The online repos are at:
https://github.com/openSUSE/rpmlint-checks
https://github.com/openSUSE/rpmlint-tests

For building the package from git run the service directly:
osc service disabledrun

The services may mess up versions and changes files a bit. Needs
some manual tweaking.
