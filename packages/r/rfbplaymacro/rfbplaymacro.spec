#
# spec file for package rfbplaymacro
#
# Copyright (c) 2025 SUSE LLC
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


Name:           rfbplaymacro
URL:            http://cyberelk.net/tim/rfbplaymacro/
License:        GPL-2.0-or-later
Group:          System/X11/Utilities
#Requires:     xforms
Version:        0.2.2
Release:        0
Summary:        Replays VNC macros
Source:         http://cyberelk.net/tim/data/rfbplaymacro/stable/%name-%version.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
rfbplaymacro replays VNC macros as created by rfbproxy to a VNC server.

%prep
%setup

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog NEWS README AUTHORS COPYING test.rfm
/usr/bin/rfbplaymacro

%changelog
