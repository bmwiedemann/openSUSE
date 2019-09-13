This package should use just the content of the git tree. If you need
to make changes, you have the following options:
* Make them in git and update the package from git (you can send merge
  request if you don't have write access)
* Create a patch, add the patch to the package and let one of the
  aaa_base packagers commit it for you

The online repository is at:
http://github.com/openSUSE/aaa_base

For building the package from git run the service directly:
osc service disabledrun

Note that aaa_base.spec and aaa_base.changes are not part of the git
repo.
