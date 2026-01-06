Libbytesize 2.12
----------------

Vojtech Trefny (8):

- packit: Bump release only for daily Copr builds
- tests: Split locale tests into multiple test cases
- misc: Separate Ansible tasks into a different file
- misc: Add build and test dependecies for CentOS
- misc: Use --break-system-packages for pip on Debian
- misc: Do not use "with_items" when installing packages
- HACKING: Update directions for updating documentation
- Fix compilation with C23

dependabot[bot] (3):

- infra: bump actions/checkout from 4 to 5
- infra: bump actions/upload-artifact from 4 to 5
- infra: bump actions/checkout from 5 to 6

Libbytesize 2.11
----------------

Alexandre Detiste (1):

- remove dependency on python3-six and python2 crumbs

Vojtech Trefny (8):

- dist: Fix release number in spec
- Squashed 'translation-canary/' changes from 4d4e65b..5bb8125
- ci: Bump actions/checkout from v3 to v4
- Rename 'master' branch to 'main'
- New version - 2.10
- ci: Set custom release number for Packit
- ci: Update CentOS Stream repositories for Packit
- ci: Add dependabot to automatically update GH actions

Weblate (1):

- Update translation files

Weblate Translation Memory (1):

- Translated using Weblate (Sinhala)

dependabot[bot] (1):

- infra: bump actions/upload-artifact from 3 to 4

triallax (1):

- tests: remove unnecessary bash dependency

김인수 (4):

- Translated using Weblate (Korean)
- Added translation using Weblate (Japanese)
- Translated using Weblate (Japanese)
- Translated using Weblate (Korean)

Libbytesize 2.10
----------------

Alexandre Detiste (1):

- remove dependency on python3-six and python2 crumbs

Vojtech Trefny (4):

- dist: Fix release number in spec
- Squashed 'translation-canary/' changes from 4d4e65b..5bb8125
- ci: Bump actions/checkout from v3 to v4
- Rename 'master' branch to 'main'

Libbytesize 2.9
---------------

Tomas Bzatek (1):

- build: Exit before AC_OUTPUT on error

Vojtech Trefny (1):

- ci: Manually prepare spec file for Packit

Weblate (1):

- Update translation files

triallax (1):

- tests: fix locale tests on musl

김인수 (1):

- Translated using Weblate (Korean)

Libbytesize 2.8
---------------

Baurzhan Muftakhidinov (2):

- Added translation using Weblate (Kazakh)
- Translated using Weblate (Kazakh)

Temuri Doghonadze (2):

- Added translation using Weblate (Georgian)
- Translated using Weblate (Georgian)

Vojtech Trefny (24):

- Sync spec with downstream
- README: Remove the Travis CI badge
- Add a GitHub action for running csmock static analysis
- ci: Run rpmbuild tests in GitHub actions
- ci: Update the csmock GitHub actions configuration
- ci: Rename csmock.Dockerfile to ci.Dockerfile
- ci: Update Fedora versions for RPM build tests
- spec: Change license string to the SPDX format required by Fedora
- misc: Remove "warn: false" from Ansible "command"
- ci: Update chroots for RPM builds
- configure.ac: Remove invalid email address for bug reports
- ci: Add Packit configuration for RPM builds on pull requests
- ci: Remove GitHub action for RPM builds
- ci: Use Packit for daily builds in Copr
- spec: Bump release to 21 for Packit daily builds
- ci: Add Packit automation for downstream builds
- spec: Fix source archive URL
- Make use of error optional
- Replace C++ style comments with C style
- Various docstring fixes
- docs: Remove information about Python 2 support
- Remove unused test dependencies variables from Makefile
- Do not hardcode pylint executable name in Makefile
- ci: Do not use release descriptions for Packit builds

Weblate (1):

- Update translation files

김인수 (1):

- Translated using Weblate (Korean)

Libbytesize 2.7
---------------

Gogo Gogsi (2):

- Added translation using Weblate (Croatian)
- Translated using Weblate (Croatian)

Sam James (1):

- build: avoid bashisms in configure

Vojtech Trefny (6):

- Do not use distutils to get Python library path
- Revert "Translations update from Weblate"
- Fix warnings dicovered by the GCC analyzer
- Fix some warnings and typos in docstrings and comments
- Remove Travis CI configuration
- Fix skipping tests when required locale is missing

Weblate (2):

- Update translation files
- Update translation files

Libbytesize 2.6
---------------

Hela Basa (1):

- Added translation using Weblate (Sinhala)

Ricky Tigg (1):

- Translated using Weblate (Finnish)

Vojtech Trefny (3):

- Sync spec with downstream
- Squashed 'translation-canary/' changes from fccbb1b..4d4e65b
- Make sure Size can be interpreted as integer in Python 3.10

Weblate (1):

- Update translation files

simmon (2):

- Added translation using Weblate (Korean)
- Translated using Weblate (Korean)

Libbytesize 2.5
---------------

Adolfo Jayme Barrientos (2):

- Translated using Weblate (Spanish)
- Translated using Weblate (Asturian)

Ricky Tigg (1):

- Translated using Weblate (Finnish)

Vojtech Trefny (6):

- Sync spec with downstream
- travis: Add --nogpgcheck when using dnf on Fedora
- bscalc: Add option to print only single "human readable" result
- tests: Run pylint and pycodestyle on bscalc
- travis: Print logs after failed tests
- tools: Read input from stdin when not running in a tty

Weblate (1):

- Update translation files

Yaron Shahrabani (2):

- Added translation using Weblate (Hebrew)
- Translated using Weblate (Hebrew)

gururajrkatti (1):

- Add support to ppc64le for debian build

Libbytesize 2.4
---------------

Adam Duskett (1):

- remove msgcat dependency

Akarshan Biswas (2):

- Added translation using Weblate (Bengali (India))
- Translated using Weblate (Bengali (India))

Vojtech Trefny (4):

- Fix library version in pkgconfig file
- Add ansible playbook for installing test dependencies
- Add Travis CI config and Dockerfiles for running tests
- Add Travis build status badge

Weblate (1):

- Update translation files


Libbytesize 2.3
---------------

Jean-Baptiste (1):

- add translation platform widget

Oğuz Ersen (1):

- Translated using Weblate (Turkish)

Vojtech Trefny (5):

- Sync spec with downstream
- Add PO files to git
- Remove Zanata from our build and release processes
- Do not regenerate POT file during 'make release'
- Fix memory leak in bs_size_new_from_str

Weblate (1):

- Update translation files


Libbytesize 2.2
---------------

Giulio Benetti (1):

- src/gettext: fix warning if gettext is already present

Tim Biermann (1):

- fix build on shells where test == fails

Vojtech Trefny (2):

- Add POT file to git and do not rebuild it during every build
- New version - 2.2

Vratislav Podzimek (2):

- Update README.md
- Require the same version of python3-bytesize in libbytesize-tools

Libbytesize 2.1
---------------

New minor release of the libbytesize library. There are only two bugfixes in
this release.

**Full list of changes**

Hongxu Jia (1):

- fix out of tree build failure

Vojtech Trefny (1):

- Fix return value for round_to_nearest when using Size

Libbytesize 2.0
---------------

New major release of the libbytesize library. There are no API or ABI changes
but we made some changes in dependencies and behavior.

**Notable changes**

- New bytesize calculator `bssize` has been added.
- Code has been ported from PCRE to PCRE2.
- Python 2 support has been removed.

**Full list of changes**

Vojtech Trefny (5):

- Run all libbytesize tests from one script
- Add all "public" python API  symbols to __init__.py
- Allow running tests using installed library
- Remove Python 2 support
- Port to pcre2

Vratislav Podzimek (10):

- Add support for floor division by a non-integer number in Python
- Add a simple bytesize calculator tool
- Add tools to autotools and packaging
- Exit with 1 from configure if there were failures
- Add a summary to the end of ./configure output
- Only support modulo between two Size instances
- Fix parsing of exponential representations of real numbers
- Add the '--version' option to bs_calc.py
- Add a man page for the bscalc tool
- Assume the given expression is in bytes if no unit is given


Libbytesize 1.4
---------------

New minor release of the libbytesize library. There are only small changes in
this release.

**Full list of changes**

Vojtech Trefny (6):

- Use new ldconfig_scriptlets macro in spec
- Do not use rpm to check for Zanata client
- Fix licence header for "gettext.h"
- Do not try to run python2 tests without python2 support
- Make sure the test script fails if one of the test runs fail
- Squashed 'translation-canary/' changes from 840c2d6..fccbb1b

Thanks to all our contributors.

Vojtech Trefny, 2018-08-02

Libbytesize 1.3
---------------

New minor release of the libbytesize library. There are only small changes in
this release. Most notable change is new configure option `--without-python2`
that allows building libbytesize without Python 2 support.


**Full list of changes**

Vojtech Trefny (5):

- Do not segfault when trying to bs_size_free NULL
- Fix links for documentation and GH project
- Add gcc to BuildRequires
- Sync spec with downstream
- Allow building libbytesize without Python 2 support

Vratislav Podzimek (1):

- Add a HACKING.rst file

Thanks to all our contributors.

Vojtech Trefny, 2018-04-19

Libbytesize 1.2
---------------

New minor release of the libbytesize library. There are only small changes in
this release.


**Full list of changes**

Vratislav Podzimek (4):

- Do not lie about tag creation
- Do not require the glib-2.0 pkgconfig package
- Use only version as a tag of the last release

Thanks to all our contributors.

Vratislav Podzimek, 2017-09-29


Libbytesize 1.1
---------------

New minor release of the libbytesize library. There are only small changes in
this release and one important bug fix.

**Notable changes**

- Fixed parsing size strings with translated units (e.g. "10 Gio" in French).


**Full list of changes**

Vojtech Trefny (3):

- Use only one git tag for new releases
- Fix source and url in spec file
- Add NEWS.rst file

Vratislav Podzimek (4):

- Add two temporary test files to .gitignore
- Actually translate the units when expected
- Fix the shortlog target
- Sync spec with downstream

Thanks to all our contributors.

Vratislav Podzimek, 2017-09-21


Libbytesize 1.0
---------------

New major release of the libbytesize library. There are only small changes in
this release, mostly bug fixes. The version bump is intended as a statement of
"finishing" work on this library. The API is now stable and we don't plan to
change it or add new major features. Future changes will probably include only
bug fixes.

**Full list of changes**

Vojtech Trefny (1):

- Make more space for CI status image

Vratislav Podzimek (4):

- Properly support 64bit operands
- Remove extra 'is' in two docstrings
- Include limits.h to make sure ULONG_MAX is defined
- New version - 1.0

Thanks to all our contributors.

Vratislav Podzimek, 2017-09-14


Libbytesize 0.11
----------------

New minor release of the libbytesize library. Most changes in this release are
related to fixing new issues and bugs.

**Full list of changes**

Kai Lüke (1):

- Allow non-source directory builds

Vojtech Trefny (7):

- Do not try to run translation tests on CentOS/RHEL 7
- Fix library name in acinclude.m4
- Fix checking for available locales
- Check for requires in generated spec file, not in the template
- Remove "glibc-all-langpacks" from test dependencies
- Fix README file name
- Do not check for test dependencies for every test run

Vratislav Podzimek (4):

- Skip tests if they require unavailable locales
- Add a build status image to the README.md
- Reserve more space for the CI status
- New version - 0.11

Thanks to all our contributors.

Vratislav Podzimek, 2017-06-14
