#
# spec file for package rfbproxy
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           rfbproxy
Version:        1.1.0
Release:        0
Summary:        Record or play back a VNC session
License:        GPL-2.0+
Group:          System/X11/Utilities
Url:            http://cyberelk.net/tim/software/rfbproxy/
Source:         http://cyberelk.net/tim/data/rfbproxy/devel/%name-%version.tar.bz2
#Patch:  patch.dif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#Requires:     xforms

%description
rfbproxy is a simple proxy for VNC which allows recording of screen
updates, key presses and mouse events for later replay.



Authors:
--------
    Tim Waugh <twaugh@redhat.com>

%prep
%setup
#%patch

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
