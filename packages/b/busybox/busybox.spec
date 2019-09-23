#
# spec file for package busybox
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        1.30.1
Release:        0
Summary:        The Swiss Army Knife of Embedded Linux
License:        GPL-2.0-or-later
Group:          System/Base
Url:            http://www.busybox.net/
Source:         http://busybox.net/downloads/%{name}-%{version}.tar.bz2
Source1:        BusyBox.1
Source2:        busybox.config
Source3:        busybox-static.config
Source4:        busybox-container.config
# other patches
Patch:          busybox.install.patch
Provides:       useradd_or_adduser_dep
BuildRequires:  glibc-devel-static
BuildRequires:  libtirpc-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
BusyBox combines tiny versions of many common UNIX utilities into a
small single executable. It provides minimalist replacements for most
of the utilities usually found in fileutils, shellutils, findutils,
textutils, grep, gzip, tar, and more. BusyBox provides a fairly
complete POSIX environment for any small or embedded system. The
utilities in BusyBox generally have fewer options than their
full-featured GNU cousins. The options that are included provide the
expected functionality and behave very much like their GNU
counterparts.

%package static
Summary:        Static linked Swiss Army Knife of Embedded Linux
Group:          System/Base

%description static
The static linked BusyBox combines tiny versions of many common UNIX utilities into a
small single executable. It provides minimalist replacements for most
of the utilities usually found in fileutils, shellutils, findutils,
textutils, grep, gzip, tar, and more. BusyBox provides a fairly
complete POSIX environment for any small or embedded system. The
utilities in BusyBox generally have fewer options than their
full-featured GNU cousins. The options that are included provide the
expected functionality and behave very much like their GNU
counterparts.

%package container
Summary:        Swiss Army Knife of Embedded Linux configured for container
Group:          System/Base
Provides:       useradd_or_adduser_dep

%description container
This is a very small BusyBox version which contains only the tools which
makes sense in a container.
BusyBox combines tiny versions of many common UNIX utilities into a
small single executable. It provides minimalist replacements for most
of the utilities usually found in fileutils, shellutils, findutils,
textutils, grep, gzip, tar, and more. BusyBox provides a fairly
complete POSIX environment for any small or embedded system. The
utilities in BusyBox generally have fewer options than their
full-featured GNU cousins. The options that are included provide the
expected functionality and behave very much like their GNU
counterparts.


%prep
%setup -q
%patch -p0
cp -a %{SOURCE1} docs/
find -name CVS | xargs rm -rf
find -name .cvsignore | xargs rm -rf
find -name .svn | xargs rm -rf
find -name .gitignore | xargs rm -rf

%build
export KCONFIG_NOTIMESTAMP=KCONFIG_NOTIMESTAMP
export VERBOSE=-v
export BUILD_VERBOSE=2
export CFLAGS="%{optflags} -fno-strict-aliasing -I/usr/include/tirpc"
export CC="gcc"
export HOSTCC=gcc
cp -a %{SOURCE4} .config
make %{?_smp_mflags} -e oldconfig
make -e %{?_smp_mflags}
mv busybox busybox-container
make busybox.links
mv busybox.links busybox-container.links
sed -e 's|busybox.links|busybox-container.links|g' -e 's|/usr/bin/busybox|/usr/bin/busybox-container|g' applets/install.sh > busybox-container.install
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
install -m 0644 busybox-container.links %{buildroot}%{_datadir}/busybox
install applets/install.sh %{buildroot}%{_bindir}/busybox.install
install busybox-container.install %{buildroot}%{_bindir}/busybox-container.install
install -m 0755 busybox %{buildroot}/%{_bindir}
install -m 0755 busybox-static %{buildroot}/%{_bindir}
install -m 0755 busybox-container %{buildroot}/%{_bindir}
install -d %{buildroot}%{_mandir}/man1
install -m 644 docs/BusyBox.1 %{buildroot}%{_mandir}/man1

%files
%defattr(-,root,root)
%license LICENSE
%doc docs/mdev.txt
%doc %{_mandir}/man1/BusyBox.1.gz
%{_bindir}/busybox
%{_bindir}/busybox.install
%dir %{_datadir}/busybox
%{_datadir}/busybox/busybox.links

%files static
%defattr(-,root,root)
%license LICENSE
%{_bindir}/busybox-static

%files container
%defattr(-,root,root)
%license LICENSE
%{_bindir}/busybox-container
%{_bindir}/busybox-container.install
%{_datadir}/busybox/busybox-container.links

%changelog
