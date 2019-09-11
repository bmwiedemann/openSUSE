#
# spec file for package squidview
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


Name:           squidview
Version:        0.86
Release:        0
Summary:        Interactive console program which monitors squid logs access
License:        GPL-2.0
Group:          Productivity/Networking/Web/Proxy
Url:            http://www.rillion.net/%{name}/index.html
Source:         http://www.rillion.net/%{name}/%{name}-%{version}.tar.gz
Patch0:         COPYING.patch
Patch1:         ltinfo-obs.patch
Patch2:         ac_new-autoconf.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ncurses-devel

%description
Squidview is an interactive console program which monitors
and displays squid logs in a nice fashion, and may then go
deeper with searching and reporting functions.

If you don't know what squid is or does this program is probably not for you.

To use squidview you must at least have read access to squid's
access.log file. You may need to see your administrator for this.
Squidview uses this text log file for all operations.
It does not generate its own database for tasks

%prep
%setup -q
%patch0
%patch1
%patch2
mv configure.in configure.ac
autoreconf -fiv

%build
%configure
make VERBOSE=1 %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
# Remove stuff that are docs
rm -fv %{buildroot}%{_datadir}/%{name}/BUGS %{buildroot}%{_datadir}/%{name}/example.log

%files
%defattr(-, root, root, 0755)
# Upstream Author doesn't want to be spammed!
# AUTHORS NEWS are empty
%doc BUGS ChangeLog COPYING example.log README
%dir %{_datadir}/squidview
%{_datadir}/squidview/*
%{_mandir}/man1/squidview*
%{_bindir}/squidview

%changelog
