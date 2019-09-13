# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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

# vim: set ts=4 sw=4 et:

Name:           nload
BuildRequires:  gcc-c++
BuildRequires:  ncurses-devel
BuildRequires:  automake
BuildRequires:  autoconf
Url:            http://www.roland-riegel.de/nload/
Version:        0.7.4
Release:        0
License:        GPL-2.0+
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Group:          Productivity/Networking/Diagnostic
Summary:        Monitors network traffic and bandwidth usage
Source:         http://www.roland-riegel.de/nload/nload-%{version}.tar.gz
Patch1:         form_h_paths.diff
Patch2:         GNU_address_update.diff

%description
nload is a console application which monitors network traffic and bandwidth
usage in real time. It visualizes the in- and outgoing traffic using two graphs
and provides additional info like total amount of transfered data and min/max
network usage.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
./run_autotools
%configure
make %{?_smp_flags}

%install
%makeinstall

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/%{name}
%doc %{_mandir}/man1/%{name}.1*

%changelog

