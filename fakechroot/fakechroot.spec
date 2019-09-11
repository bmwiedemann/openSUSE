#
# spec file for package fakechroot
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           fakechroot
Version:        2.19
Release:        0
Summary:        Gives a fake chroot environment
License:        LGPL-2.1
Group:          Development/Tools/Building
Url:            https://github.com/dex4er/fakechroot/wiki
Source0:        https://github.com/dex4er/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

%description
fakechroot runs a command in an environment where it is possible to use the
chroot(8) command without root privileges. This is useful for allowing users to
create own chrooted environments with the possibility to install other packages
without the need for root privileges.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check

%install
%make_install

%files
%doc COPYING LICENSE NEWS.md README.md THANKS.md
%doc scripts/restoremode.sh scripts/savemode.sh
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*
%{_bindir}/*
%{_sbindir}/*
%{_libdir}/%{name}
%{_mandir}/man?/*

%changelog
