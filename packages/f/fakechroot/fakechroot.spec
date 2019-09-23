#
# spec file for package fakechroot
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


Name:           fakechroot
Version:        2.19
Release:        0
Summary:        Preloadable library for a fake chroot environment
License:        LGPL-2.1-only AND LGPL-2.1-or-later AND GPL-2.0-or-later AND GPL-3.0-or-later
Group:          Development/Tools/Building
URL:            https://github.com/dex4er/fakechroot/wiki
Source0:        https://github.com/dex4er/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

%description
fakechroot runs a command in an environment where it is possible to use the
chroot(8) command without root privileges. This is useful for allowing users to
create own chrooted environments with the possibility to install other packages
without the need for root privileges.

fakechroot does this by replacing some libc library functions (chroot(2),
open(2), etc.) by ones that simulate the effect of being called with root
privileges.

These wrapper functions are in a shared library called libfakechroot.so, which
can be loaded through the LD_PRELOAD mechanism of the dynamic loader.

%prep
%autosetup

%build
%define _lto_cflags %{nil}
%configure --disable-static
%make_build

%check
make %{?_smp_mflags} check V=1

%install
%make_install

%files
%license COPYING LICENSE
%doc NEWS.md README.md THANKS.md
%doc scripts/restoremode.sh scripts/savemode.sh
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*
%{_bindir}/*
%{_sbindir}/*
%{_libdir}/%{name}
%{_mandir}/man?/*

%changelog
