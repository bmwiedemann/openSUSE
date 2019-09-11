#
# spec file for package ytalk
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           ytalk
Version:        3.3.0
Release:        0
Summary:        Multi-User replacement for Unix talk client
License:        MIT
Group:          Productivity/Networking/Talk/Clients
Url:            http://www.impul.se/ytalk/
Source:         %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ncurses-devel

%description
YTalk is, in essence, a multiuser chat program. It works almost exactly
like the UNIX talk program and even communicates with the same talk
daemons, but YTalk allows for multiple connections.



Authors:
--------
    Britt Yenne <yenne@austin.eds.com>
    Roger Espel Llima <roger.espel.llima@pobox.com>
    Jessica Peterson <angel@metawire.org>

%prep
%setup

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install

%files
%defattr(-,root,root)
%doc ChangeLog README*  
%config /etc/ytalkrc
/usr/bin/ytalk
%doc %{_mandir}/man1/*

%changelog
