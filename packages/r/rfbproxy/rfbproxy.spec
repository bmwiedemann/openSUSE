#
# spec file for package rfbproxy
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


Name:           rfbproxy
Version:        1.1.0
Release:        0
Summary:        Record or play back a VNC session
License:        GPL-2.0-or-later
Group:          System/X11/Utilities
URL:            http://cyberelk.net/tim/software/rfbproxy/
Source:         http://cyberelk.net/tim/data/rfbproxy/devel/%name-%version.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#Requires:     xforms

%description
rfbproxy is a simple proxy for VNC which allows recording of screen
updates, key presses and mouse events for later replay.

%prep
%setup

%build
%configure
make %{?_smp_mflags}
top_builddir=. top_srcdir=. tests/run-tests

%install
make DESTDIR=$RPM_BUILD_ROOT install

%files
%defattr(-,root,root,-)
%doc COPYING README TODO
/usr/bin/rfbproxy
%_mandir/man1/rfbproxy.1.gz

%changelog
