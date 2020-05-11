#
# spec file for package coreutils
#
# Copyright (c) 2020 SUSE LLC
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


%bcond_with ringdisabled

# there are more fancy ways to define a package name using magic
# macros but OBS and the bots that rely on parser information from
# OBS can't deal with all of them
%define flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" != ""
%define name_suffix -%{flavor}
%if %{with ringdisabled}
ExclusiveArch:  do_not_build
%endif
%endif

Name:           coreutils%{?name_suffix}
Summary:        GNU Core Utilities
License:        GPL-3.0-or-later
Group:          System/Base
URL:            https://www.gnu.org/software/coreutils/
Version:        8.32
Release:        0

BuildRequires:  automake
BuildRequires:  gmp-devel
BuildRequires:  libacl-devel
BuildRequires:  libattr-devel
BuildRequires:  libcap-devel
BuildRequires:  libselinux-devel
BuildRequires:  makeinfo
BuildRequires:  perl
BuildRequires:  suse-module-tools
BuildRequires:  xz
%if %{suse_version} > 1320
BuildRequires:  gcc-PIE
%endif
%if "%{name}" == "coreutils-testsuite"
BuildRequires:  acl
BuildRequires:  gdb
BuildRequires:  perl-Expect
BuildRequires:  python
BuildRequires:  python3
BuildRequires:  python3-pyinotify
BuildRequires:  strace
BuildRequires:  timezone
# Some tests need the 'bin' user.
BuildRequires:  user(bin)
%ifarch %ix86 x86_64 ppc ppc64 s390x armv7l armv7hl
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

# this will create a cycle, broken up randomly - coreutils is just
# too core to have other prerequisites.
#PreReq:         permissions

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

#cgit-URL:	https://git.savannah.gnu.org/cgit/coreutils.git/
#Git-Clone:	git://git.sv.gnu.org/coreutils
%if "%{name}" == "coreutils"
# For upgrading the upstream version, increase the version number (above),
# then remove the old tarball and signature files and let OSC download
# those files of the new version:
#    osc rm coreutils-*.tar.xz coreutils-*.tar.xz.sig
#    osc service localrun download_files
#    osc addremove
# Then adjust the downstream patches (using quilt).
# Finally, add a changelog entry and commit:
#    osc vc
#    osc ci
Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
Source1:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        https://savannah.gnu.org/project/memberlist-gpgkeys.php?group=%{name}&download=1&file=./%{name}.keyring
%else
# In "coreutils-testsuite", we use the version controlled file from "coreutils".
# otherwise that file would be downloaded twice during the above mentioned
# upgrade procedure.
Source0:        coreutils-%{version}.tar.xz
Source1:        coreutils-%{version}.tar.xz.sig
Source2:        coreutils.keyring
%endif

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

%ifarch %ix86 x86_64 ppc ppc64
Patch301:       coreutils-skip-gnulib-test-tls.patch
%endif

# tests: shorten extreme-expensive factor tests
Patch303:       coreutils-tests-shorten-extreme-factor-tests.patch
# Stop using Python 2.x
Patch304:       coreutils-use-python3.patch
Patch500:       coreutils-disable_tests.patch
Patch501:       coreutils-test_without_valgrind.patch

# Upstream commits (squashed) after the release of coreutils-8.32:
#   [PATCH 1/2] ls: restore 8.31 behavior on removed directories
#   [PATCH 2/2] ls: improve removed-directory test
# Remove this patch with the next coreutils release.
Patch800:       coreutils-ls-restore-8.31-behavior-on-removed-dirs.patch

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
Provides:       coreutils:%{_infodir}/coreutils.info.gz
Supplements:    packageand(coreutils:patterns-base-documentation)
Supplements:    packageand(coreutils-single:patterns-base-documentation)
BuildArch:      noarch

%description doc
This package contains the documentation for the GNU Core Utilities.

# ================================================
%lang_package
%prep
%setup -q -n coreutils-%{version}
%patch4
%patch1
%patch3
%patch8
%patch16
#
%if %{suse_version} <= 1320
%patch100
%endif
%patch112
%patch113

%patch300

%ifarch %ix86 x86_64 ppc ppc64
%patch301
%endif

%patch303
%patch304
%patch500
%patch501

%patch800

# ================================================
%build
%if 0%{suse_version} >= 1200
AUTOPOINT=true autoreconf -fi
%endif
export CFLAGS="%optflags"
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

make -C po update-po

# Regenerate manpages
touch man/*.x

make all %{?_smp_mflags} V=1

# make sure that parse-datetime.{c,y} ends up in debuginfo (rh#1555079)
ln -v lib/parse-datetime.{c,y} .

# ================================================
%check
%if "%{name}" == "coreutils-testsuite"
  # Make our multi-byte test for sort executable
  chmod a+x tests/misc/sort-mb-tests.sh
  # Avoid parallel make, because otherwise some timeout based tests like
  # rm/ext3-perf may fail due to high CPU or IO load.
  make check-very-expensive \
    && install -d -m 755 %{buildroot}%{_docdir}/%{name} \
    && xz -c tests/test-suite.log \
         > %{buildroot}%{_docdir}/%{name}/test-suite.log.xz
%else
  # Run the shorter check otherwise.
  make check
%endif

# ================================================
%install
%if "%{name}" == "coreutils" || "%{name}" == "coreutils-single"
make install DESTDIR="%buildroot" pkglibexecdir=%{_libdir}/%{name}

#UsrMerge
install -d %{buildroot}/bin
for i in arch basename cat chgrp chmod chown cp date dd df echo \
  false ln ls mkdir mknod mktemp mv pwd rm rmdir sleep sort stat \
  stty sync touch true uname readlink md5sum
do
  ln -sf %{_bindir}/$i %{buildroot}/bin/$i
done
#EndUsrMerge
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

%defattr(-,root,root)
%license COPYING
%doc NEWS README THANKS
%{_bindir}/*
#UsrMerge
/bin/*
#EndUsrMerge
%{_libdir}/%{name}

%if "%{name}" == "coreutils"
%files lang -f coreutils.lang
%defattr(-,root,root)

%files doc
%doc %{_infodir}/coreutils.info*.gz
%doc %{_mandir}/man1/*.1.gz
%endif

%else

# test-suite
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/test-suite.log.xz

%endif

# ================================================

%changelog
