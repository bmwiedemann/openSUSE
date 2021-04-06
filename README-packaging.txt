!!! DO NOT SUBMIT CEPH.SPEC MODIFICATIONS TO OBS !!!
!!! CEPH.SPEC IS MAINTAINED UPSTREAM !!!

So you have an idea for how to improve ceph.spec and are preparing to submit it
to the Factory devel project. You might also intend to test your patch in the
OBS, first. Please read this before proceeding!

Instructions for submitting
---------------------------

The ceph.spec file is maintained upstream at https://github.com/ceph/ceph

To patch it, use the following procedure:

1. find out the current Factory ceph maintainer(s) (e.g. by examining the
   most recent entries in the ceph.changes file)
2. open PR targeting the master branch at https://github.com/ceph/ceph
   Make sure to sign your commit ("git commit --signoff") using your real name
   and real email address. If this is a problem, contact the current Factory
   maintainers: they can act as a proxy.
3. ping the Factory ceph maintainers about your PR

The Factory ceph maintainers will take care of getting your upstream PR
reviewed, tested, merged and, if necessary, backported. They will also take care
of submitting the patch to Factory.

Caveat for testing
------------------

If you want to test your patch (e.g. in your home project), please read the
following CAVEAT:

The ceph.spec file is maintained upstream. As a consequence of that, we cannot
simply run the downstream spec file cleaner on it. (If you are now asking
"why?", here is one reason: the spec file cleaner changes the copyright notice!
Another reason is: the spec file cleaner has been known to munge ceph.spec so
badly that it breaks the build!)

Now, if special action is not taken, the spec file cleaner will run on the
server each time you commit. That must be avoided at all costs. Fortunately, it
is easy to avoid it by passing the "--noservice" option to "osc commit", e.g.:

    osc commit --noservice

