#
# spec file
#
# Copyright (c) 2023 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


# there are more fancy ways to define a package name using magic
# macros but OBS and the bots that rely on parser information from
# OBS can't deal with all of them
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "single"
%global psuffix -single
%elif "%{flavor}" == "testsuite"
%global psuffix -testsuite
%else
%global psuffix %{nil}
%endif
Name:           coreutils%{?psuffix}
Version:        9.2
Release:        0
Summary:        GNU Core Utilities
License:        GPL-3.0-or-later
Group:          System/Base
URL:            https://www.gnu.org/software/coreutils/
Source0:        https://ftp.gnu.org/gnu/coreutils/coreutils-%{version}.tar.xz
Source1:        https://ftp.gnu.org/gnu/coreutils/coreutils-%{version}.tar.xz.sig
Source2:        https://savannah.gnu.org/project/release-gpgkeys.php?group=coreutils&download=1&file=./coreutils.keyring
Source3:        baselibs.conf
Patch1:         coreutils-remove_hostname_documentation.patch
Patch3:         coreutils-remove_kill_documentation.patch
Patch4:         coreutils-i18n.patch
Patch8:         coreutils-sysinfo.patch
Patch16:        coreutils-invalid-ids.patch
# OBS / RPMLINT require /usr/bin/timeout to be built with the -fpie option.
Patch100:       coreutils-build-timeout-as-pie.patch
# There is no network in the build root so make the test succeed
Patch112:       coreutils-getaddrinfo.patch
# Assorted fixes
Patch113:       coreutils-misc.patch
# Skip 2 valgrind'ed sort tests on ppc/ppc64 which would fail due to
# a glibc issue in mkstemp.
Patch300:       coreutils-skip-some-sort-tests-on-ppc.patch
Patch301:       coreutils-skip-gnulib-test-tls.patch
# tests: shorten extreme-expensive factor tests
Patch303:       coreutils-tests-shorten-extreme-factor-tests.patch
# Stop using Python 2.x
Patch304:       coreutils-use-python3.patch
Patch500:       coreutils-disable_tests.patch
Patch501:       coreutils-test_without_valgrind.patch
# Downstream patch to skip a test failing on OBS.
# tests: skip tests/rm/ext3-perf.sh temporarily as it hangs on OBS.
Patch810:       coreutils-skip-tests-rm-ext3-perf.patch
Patch900:       coreutils-tests-workaround-make-fdleak.patch
BuildRequires:  automake
BuildRequires:  gmp-devel
BuildRequires:  hostname
BuildRequires:  libacl-devel
BuildRequires:  libattr-devel
BuildRequires:  libcap-devel
BuildRequires:  libselinux-devel
BuildRequires:  makeinfo
BuildRequires:  perl
BuildRequires:  xz
%if 0%{?suse_version} > 1320
BuildRequires:  gcc-PIE
%endif
%if "%{name}" == "coreutils-testsuite"
BuildRequires:  acl
BuildRequires:  gdb
BuildRequires:  perl-Expect
BuildRequires:  python3
BuildRequires:  python3-pyinotify
BuildRequires:  strace
BuildRequires:  timezone
# Some tests need the 'bin' user.
BuildRequires:  user(bin)
%ifarch %{ix86} x86_64 ppc ppc64 s390x armv7l armv7hl
BuildRequires:  valgrind
%endif
%endif
%if "%{name}" == "coreutils" || "%{name}" == "coreutils-single"
Provides:       fileutils = %{version}
Provides:       mktemp = %{version}
Provides:       sh-utils = %{version}
Provides:       stat = %{version}
Provides:       textutils = %{version}
%if "%{name}" == "coreutils-single"
Conflicts:      coreutils
Provides:       coreutils = %{version}-%{release}
%endif
%endif

# ================================================
%description
These are the GNU core utilities.  This package is the union of
the GNU fileutils, sh-utils, and textutils packages.

  [ arch b2sum base32 base64 basename basenc cat chcon chgrp chmod chown chroot
  cksum comm cp csplit cut date dd df dir dircolors dirname du echo env expand
  expr factor false fmt fold groups head hostid id install join
  link ln logname ls md5sum mkdir mkfifo mknod mktemp mv nice nl nohup
  nproc numfmt od paste pathchk pinky pr printenv printf ptx pwd readlink
  realpath rm rmdir runcon seq sha1sum sha224sum sha256sum sha384sum sha512sum
  shred shuf sleep sort split stat stdbuf stty sum sync tac tail tee test
  timeout touch tr true truncate tsort tty uname unexpand uniq unlink
  uptime users vdir wc who whoami yes

%package doc
Summary:        Documentation for the GNU Core Utilities
Group:          Documentation/Man
Supplements:    (coreutils and patterns-base-documentation)
Supplements:    (coreutils-single and patterns-base-documentation)
Provides:       coreutils:%{_infodir}/coreutils.info.gz
BuildArch:      noarch

%description doc
This package contains the documentation for the GNU Core Utilities.

# ================================================
%lang_package

%prep
%setup -q -n coreutils-%{version}
%patch4 -p1
%patch1
%patch3
%patch8
%patch16
#
%if 0%{?suse_version} <= 1320
%patch100
%endif
%patch112
%patch113

%patch300

%ifarch %{ix86} x86_64 ppc ppc64
%patch301
%endif

%patch303
%patch304
%patch500
%patch501

%patch810
%patch900

# ================================================
%build
%if 0%{?suse_version} >= 1200
AUTOPOINT=true autoreconf -fi
%endif
export CFLAGS="%{optflags}"
%configure --libexecdir=%{_libdir} \
           --enable-install-program=arch \
	   --enable-no-install-program=kill \
%if "%{name}" == "coreutils-single"
           --enable-single-binary \
           --without-openssl \
           --without-gmp \
%endif
           DEFAULT_POSIX2_VERSION=200112 \
           alternative=199209

%make_build -C po update-po

# Regenerate manpages
touch man/*.x

%make_build all

# make sure that parse-datetime.{c,y} ends up in debuginfo (rh#1555079)
ln -v lib/parse-datetime.{c,y} .

# ================================================
%check
%if "%{name}" == "coreutils-testsuite"
  # Make our multi-byte test for sort executable
  chmod a+x tests/misc/sort-mb-tests.sh
  # Avoid parallel make, because otherwise some timeout based tests like
  # rm/ext3-perf may fail due to high CPU or IO load.
  %make_build -j1 check-very-expensive VERBOSE=yes \
    && install -d -m 755 %{buildroot}%{_docdir}/%{name} \
    && xz -c tests/test-suite.log \
         > %{buildroot}%{_docdir}/%{name}/test-suite.log.xz
%else
  # Run the shorter check otherwise.
  %make_build check VERBOSE=yes
%endif

# ================================================
%install
%if "%{name}" == "coreutils" || "%{name}" == "coreutils-single"
make install DESTDIR=%{buildroot} pkglibexecdir=%{_libdir}/%{name}

echo '.so man1/test.1' > %{buildroot}/%{_mandir}/man1/\[.1
%if "%{name}" == "coreutils"
%find_lang coreutils
# add LC_TIME directories to lang package
awk '/LC_TIME/ {a=$2; gsub(/\/[^\/]+\.mo/,"", a); print "%%dir", a} {print}' < coreutils.lang > tmp
mv tmp coreutils.lang
%else
rm -rf %{buildroot}%{_mandir}
rm -rf %{buildroot}%{_infodir}
rm -rf %{buildroot}%{_datadir}/locale
> coreutils.lang
%endif
%endif

# ================================================
%post
%if "%{name}" == "coreutils" || "%{name}" == "coreutils-single"
%{?regenerate_initrd_post}
%endif

# ================================================
%posttrans
%if "%{name}" == "coreutils" || "%{name}" == "coreutils-single"
%{?regenerate_initrd_posttrans}
%endif

# ================================================
%files
%if "%{name}" == "coreutils" || "%{name}" == "coreutils-single"

%license COPYING
%doc NEWS README THANKS
%{_bindir}/*
%{_libdir}/%{name}

%if "%{name}" == "coreutils"
%files lang -f coreutils.lang

%files doc
%{_infodir}/coreutils.info*.gz
%{_mandir}/man1/*.1%{?ext_man}
%endif

%else

# test-suite
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/test-suite.log.xz

%endif

# ================================================

%changelog
