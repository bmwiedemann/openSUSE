#
# spec file for package busybox
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%ifarch x86_64 aarch64 i586
%bcond_without  ww3
%else
%bcond_with     ww3
%endif
%bcond_without  static

Name:           busybox
Version:        1.37.0
Release:        0
Summary:        Minimalist variant of UNIX utilities linked in a single executable
License:        GPL-2.0-or-later
URL:            https://www.busybox.net/
Source:         https://busybox.net/downloads/%{name}-%{version}.tar.bz2
Source2:        busybox.config
# Make sure busybox-static.config stays in sync with busybox.config -
# exception: SELinux commands - these do not build statically.
Source3:        busybox.config.static
Source4:        man.conf
Source5:        https://busybox.net/downloads/%{name}-%{version}.tar.bz2.sig
Source6:        https://busybox.net/~vda/vda_pubkey.gpg#/%{name}.keyring
Source7:        busybox.config.static.warewulf3
Patch0:         cpio-long-opt.patch
Patch1:         sendmail-ignore-F-option.patch
Patch2:         testsuite-gnu-echo.patch
# # PATCH-FIX-UPSTREAM shell: avoid segfault on ${0::0/0~09J} (CVE-2022-48174) https://git.busybox.net/busybox/commit/?id=d417193cf
# Patch3:         ash-fix-segfault-d417193cf.patch
Patch4:         udhcp6-install-path.patch
Patch5:         tc-no-TCA_CBQ.patch
# PATCH-FIX-UPSTREAM - Borrowed from Fedora - https://src.fedoraproject.org/rpms/busybox/blob/rawhide/f/busybox-1.37.0-fix-conditional-for-sha1_process_block64_shaNI.patch
Patch6:         busybox-1.37.0-fix-conditional-for-sha1_process_block64_shaNI.patch
# https://gitlab.alpinelinux.org/alpine/aports/-/raw/3.21-stable/main/busybox/0015-ping-make-ping-work-without-root-privileges.patch?ref_type=heads
Patch7:         busybox-1.37.0-make-ping-work-without-root-privileges.patch
#PATCH-FIX-UPSTREAM -  hexdump: fix regression with -n4 -e '"%u"' bug introduced in busybox 1.37.0 that broke kernel builds.
Patch8:         busybox-1.37.0-fix-regression-n2.patch
#PATCH-FIX-UPSTREAM - Fixes for hexdump and tests on big endian (S390) systems
Patch9:         busybox-1.37.0-hexdump-fix-regression-for-uint16-on-big-endian-syst.patch
Patch10:        busybox-1.37.0-od-make-B-test-little-endian-only-add-variant-for-bi.patch
Patch11:        busybox-1.37.0-hexdump-add-tests-for-x-handle-little-big-endian-pro.patch
# PATCH-FIX-UPSTREAM - Fix adduser inside containers (boo#1247779)
Patch12:        0001-update_passwd-Avoid-selinux_preserve_fcontext-if-SEL.patch
# PATCH-FIX-UPSTREAM - Fix bsc#1241661 (CVE-2025-46394), from upstream commit f5e1bf966
Patch13:        0001-archival-libarchive-sanitize-filenames-on-output-pre.patch
# PATCH-FIX-UPSTREAM - Fix bsc#1253245 (CVE-2025-60876), submitted to mailing list
Patch14:        wget-don-t-allow-control-characters-in-url.patch
# PATCH-FIX-UPSTREAM - Fix bsc#1249237, from upstream commit 362159593
Patch15:        0001-nsenter-unshare-don-t-use-xvfork_parent_waits_and_ex.patch
# PATCH-FIX-UPSTREAM - Fix bsc#1258163 from upstream commit 3fb6b31c716669e12f75a2accd31bb7685b1a1cb
Patch16:        0001-tar-strip-unsafe-hardlink-components-GNU-tar-does-th.patch
# PATCH-FIX-UPSTREAM - The fix above introducesa problem rewriting symlink targets too
Patch17:        0002-tar-only-strip-unsafe-components-from-hardlinks-not-.patch

# other patches
Patch100:       busybox.install.patch
BuildRequires:  glibc-devel-static
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libselinux)
# for test suite
BuildRequires:  zip
Provides:       useradd_or_adduser_dep
#in SLE12 hostname is part of the net-tools package
%if %{?suse_version} && %{?suse_version} <= 1315
BuildRequires:  net-tools
%else
BuildRequires:  hostname
%endif

%description
BusyBox combines tiny versions of many common UNIX utilities into a
single executable. It provides minimalist replacements for utilities
usually found in fileutils, shellutils, findutils, textutils, grep,
gzip, tar, and more. BusyBox provides a fairly complete POSIX
environment for small or embedded systems. The utilities in BusyBox
generally have fewer options than their GNU cousins. The options that
are included provide the expected functionality and behave much like
their GNU counterparts.
BusyBox is for emergency and special use cases. Replacing the standard
tools in a system is not supported. Some tools don't work out of the
box but need special configuration, like udhcpc, the dhcp client.

%package static
Summary:        Static linked version of Busybox, a compact UNIX utility collection

%description static
BusyBox combines tiny versions of many common UNIX utilities into a
single executable.

%package warewulf3
Summary:        Static version of Busybox - for building Warewulf3

%description warewulf3
This version of busybox is only for building Warewulf3
https://github.com/warewulf/warewulf3

%package testsuite
Summary:        Testsuite of busybox
Requires:       %{name} = %{version}
Requires:       zip

%description testsuite
Using this package you can test the busybox build on different kernels and glibc.
It needs to run with permission to the current directory, so either copy it away
as is or run as root:

cd %{_datadir}/busybox/testsuite
PATH=%{_datadir}/busybox:$PATH SKIP_KNOWN_BUGS=1 ./runtest

%prep
#SLE12 needs an empty line after autosetup for it to expand properly (bsc#1205420)
%autosetup -p1

find "(" -name CVS -o -name .cvsignore -o -name .svn -o -name .gitignore ")" \
	-exec rm -Rf {} +

%build
export KCONFIG_NOTIMESTAMP=KCONFIG_NOTIMESTAMP
export KBUILD_VERBOSE=1
export CFLAGS="%{optflags} -fPIC -fno-strict-aliasing -I/usr/include/tirpc"
export CC="gcc"
export HOSTCC=gcc
# Keep debug info, we take care of stripping ourselves
export SKIP_STRIP=y
%if %{with static}
cat %{SOURCE3} %{SOURCE2} > .config
%make_build -e oldconfig
%make_build -e
mv busybox busybox-static
%endif

%if 0%{with ww3}
%make_build -e clean
cat %{SOURCE7} %{SOURCE3} %{SOURCE2} > .config
%make_build -e oldconfig
%make_build -e
mv busybox busybox-warewulf3
%make_build -e busybox.links
mv busybox.links busybox-warewulf3.links
%endif

%make_build -e clean
cp -a %{SOURCE2} .config
%make_build -e oldconfig
#make -e %{?_smp_mflags}
%make_build -e
%make_build -e doc busybox.links

%if 0%{?suse_version} >= 1550
for i in busybox.links %{?with_ww3:busybox-warewulf3.links}; do
    sed -i -e 's,^/\(s\?bin\)/,%{_prefix}/\1/,' $i
done
%endif

%install
install -d %{buildroot}/%{_bindir}
install -d %{buildroot}/%{_datadir}/busybox
install -m 0644 busybox.links %{buildroot}%{_datadir}/busybox
install applets/install.sh %{buildroot}%{_bindir}/busybox.install
install -m 0755 busybox %{buildroot}%{_bindir}
%if %{with static}
install -m 0755 busybox-static %{buildroot}%{_bindir}
%endif
install -d %{buildroot}%{_sysconfdir}
install -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/
install -d %{buildroot}%{_mandir}/man1
install -m 644 docs/busybox.1 %{buildroot}%{_mandir}/man1
%if %{with ww3}
install -m 0644 busybox-warewulf3.links %{buildroot}%{_datadir}/busybox
install -m 0755 busybox-warewulf3 %{buildroot}%{_bindir}
%endif
cp %{SOURCE2} %{buildroot}%{_datadir}/busybox/.config
ln -s %{_bindir}/busybox %{buildroot}%{_datadir}/busybox/busybox
cp -a testsuite %{buildroot}%{_datadir}/busybox/testsuite

%check
export KCONFIG_NOTIMESTAMP=KCONFIG_NOTIMESTAMP
export KBUILD_VERBOSE=1
export CFLAGS="%{optflags} -fPIC -fno-strict-aliasing -I/usr/include/tirpc"
export CC="gcc"
export HOSTCC=gcc
export SKIP_KNOWN_BUGS=1
export SKIP_INTERNET_TESTS=1
%make_build -e test

%files
%license LICENSE
%doc docs/mdev.txt
%config %{_sysconfdir}/man.conf
%{_mandir}/man1/busybox.1%{?ext_man}
%{_bindir}/busybox
%{_bindir}/busybox.install
%dir %{_datadir}/busybox
%{_datadir}/busybox/busybox.links

%files testsuite
%{_datadir}/busybox/busybox
%{_datadir}/busybox/.config
%{_datadir}/busybox/testsuite

%if %{with static}
%files static
%license LICENSE
%{_bindir}/busybox-static
%endif

%if %{with ww3}
%files warewulf3
%license LICENSE
%{_bindir}/busybox-warewulf3
%dir %{_datadir}/busybox
%{_datadir}/busybox/busybox-warewulf3.links
%endif

%changelog
