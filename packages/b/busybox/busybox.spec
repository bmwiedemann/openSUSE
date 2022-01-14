#
# spec file for package busybox
#
# Copyright (c) 2022 SUSE LLC
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


Name:           busybox
Version:        1.35.0
Release:        0
Summary:        Minimalist variant of UNIX utilities linked in a single executable
License:        GPL-2.0-or-later
Group:          System/Base
URL:            https://www.busybox.net/
Source:         https://busybox.net/downloads/%{name}-%{version}.tar.bz2
Source1:        BusyBox.1
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
# other patches
Patch100:       busybox.install.patch
Provides:       useradd_or_adduser_dep
BuildRequires:  glibc-devel-static
BuildRequires:  pkgconfig(libselinux)
# for test suite
BuildRequires:  zip

%ifarch x86_64 aarch64 i586
%define build_ww3 1
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

%package static
Summary:        Static linked version of Busybox, a compact UNIX utility collection
Group:          System/Base

%description static
BusyBox combines tiny versions of many common UNIX utilities into a
single executable.

%package warewulf3
Summary:        Static version of Busybox - for building Warewulf3
Group:          System/Base

%description warewulf3
This version of busybox is only for building Warewulf3
https://github.com/warewulf/warewulf3

%package testsuite
Summary:        Testsuite of busybox
Group:          Development/Testing
Requires:       %{name} = %{version}
Requires:       zip

%description testsuite
Using this package you can test the busybox build on different kernels and glibc.
It needs to run with permission to the current directory, so either copy it away
as is or run as root:

cd /usr/share/busybox/testsuite
PATH=/usr/share/busybox:$PATH SKIP_KNOWN_BUGS=1 ./runtest

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch100 -p0
cp -a %{SOURCE1} docs/
find "(" -name CVS -o -name .cvsignore -o -name .svn -o -name .gitignore ")" \
	-exec rm -Rf {} +

%build
export KCONFIG_NOTIMESTAMP=KCONFIG_NOTIMESTAMP
export VERBOSE=-v
export BUILD_VERBOSE=2
export CFLAGS="%{optflags} -fno-strict-aliasing -I/usr/include/tirpc"
export CC="gcc"
export HOSTCC=gcc
cat %{SOURCE3} %{SOURCE2} > .config
make %{?_smp_mflags} -e oldconfig
make -e %{?_smp_mflags}
mv busybox busybox-static

%if 0%{?build_ww3}
make -e %{?_smp_mflags} clean
cat %{SOURCE7} %{SOURCE3} %{SOURCE2} > .config
make %{?_smp_mflags} -e oldconfig
make -e %{?_smp_mflags}
mv busybox busybox-warewulf3
make -e busybox.links %{?_smp_mflags}
mv busybox.links busybox-warewulf3.links
%endif

make -e %{?_smp_mflags} clean
cp -a %{SOURCE2} .config
make %{?_smp_mflags} -e oldconfig
#make -e %{?_smp_mflags}
make -e
make -e doc busybox.links %{?_smp_mflags}

%if 0%{?usrmerged}
for i in busybox.links %{?build_ww3:busybox-warewulf3.links}; do
    sed -i -e 's,^/\(s\?bin\)/,/usr/\1/,' $i
done
%endif

%install
install -d %{buildroot}/%{_bindir}
install -d %{buildroot}/%{_datadir}/busybox
install -m 0644 busybox.links %{buildroot}%{_datadir}/busybox
install applets/install.sh %{buildroot}%{_bindir}/busybox.install
install -m 0755 busybox %{buildroot}%{_bindir}
install -m 0755 busybox-static %{buildroot}%{_bindir}
install -d %{buildroot}%{_sysconfdir}
install -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/
install -d %{buildroot}%{_mandir}/man1
install -m 644 docs/BusyBox.1 %{buildroot}%{_mandir}/man1
%if 0%{?build_ww3}
install -m 0644 busybox-warewulf3.links %{buildroot}%{_datadir}/busybox
install -m 0755 busybox-warewulf3 %{buildroot}%{_bindir}
%endif
cp %{SOURCE2} %{buildroot}%{_datadir}/busybox/.config
ln -s %_bindir/busybox %{buildroot}%{_datadir}/busybox/busybox
cp -a testsuite %{buildroot}%{_datadir}/busybox/testsuite

%check
export KCONFIG_NOTIMESTAMP=KCONFIG_NOTIMESTAMP
export BUILD_VERBOSE=2
export CFLAGS="%{optflags} -fno-strict-aliasing -I/usr/include/tirpc"
export CC="gcc"
export HOSTCC=gcc
export SKIP_KNOWN_BUGS=1
export SKIP_INTERNET_TESTS=1
make -e %{?_smp_mflags} test

%files
%license LICENSE
%doc docs/mdev.txt
%config %{_sysconfdir}/man.conf
%doc %{_mandir}/man1/BusyBox.1.gz
%{_bindir}/busybox
%{_bindir}/busybox.install
%dir %{_datadir}/busybox
%{_datadir}/busybox/busybox.links

%files testsuite
%{_datadir}/busybox/busybox
%{_datadir}/busybox/.config
%{_datadir}/busybox/testsuite

%files static
%license LICENSE
%{_bindir}/busybox-static

%if 0%{?build_ww3}
%files warewulf3
%license LICENSE
%{_bindir}/busybox-warewulf3
%dir %{_datadir}/busybox
%{_datadir}/busybox/busybox-warewulf3.links
%endif

%changelog
