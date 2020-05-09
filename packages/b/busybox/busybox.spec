#
# spec file for package busybox
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


Name:           busybox
Version:        1.31.1
Release:        0
Summary:        Minimalist variant of UNIX utilities linked in a single executable
License:        GPL-2.0-or-later
Group:          System/Base
URL:            http://www.busybox.net/
Source:         http://busybox.net/downloads/%{name}-%{version}.tar.bz2
Source1:        BusyBox.1
Source2:        busybox.config
Source3:        busybox-static.config
Source4:        man.conf
# Upstream patches
Patch0:         busybox-no-stime.patch
# other patches
Patch100:       busybox.install.patch
Provides:       useradd_or_adduser_dep
BuildRequires:  glibc-devel-static

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

%prep
%setup -q
%patch0 -p1
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
cp -a %{SOURCE3} .config
make %{?_smp_mflags} -e oldconfig
make -e %{?_smp_mflags}
mv busybox busybox-static
make -e %{?_smp_mflags} clean
cp -a %{SOURCE2} .config
make %{?_smp_mflags} -e oldconfig
make -e %{?_smp_mflags}
make -e doc busybox.links %{?_smp_mflags}

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

%files
%license LICENSE
%doc docs/mdev.txt
%config %{_sysconfdir}/man.conf
%doc %{_mandir}/man1/BusyBox.1.gz
%{_bindir}/busybox
%{_bindir}/busybox.install
%dir %{_datadir}/busybox
%{_datadir}/busybox/busybox.links

%files static
%license LICENSE
%{_bindir}/busybox-static

%changelog
