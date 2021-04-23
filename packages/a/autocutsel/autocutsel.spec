#
# spec file for package autocutsel
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


Name:           autocutsel
Url:            http://www.nongnu.org/autocutsel/
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xt)
Version:        0.10.0
Release:        0
Summary:        Clipboard / Cutbuffer management helper
License:        GPL-2.0+
Group:          System/X11/Utilities
Source:         https://github.com/sigmike/autocutsel/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
X servers use two schemes to copy text between applications. The first one
(old and deprecated) is the cutbuffer. The other scheme is the selection.
Recent desktop applications (GNOME, KDE, ...) use two selections: the
PRIMARY and the CLIPBOARD. The PRIMARY selection is used when you select
some text with the mouse. You usually paste it using the middle button. The
CLIPBOARD selection is used when you copy text by using, for example,
the Edit/Copy menu. You may paste it using the Edit/Paste menu.

Windows VNC clients keep the Windows clipboard synchronized with the
cutbuffer, but not with the selections. And since recent applications
don't use the cutbuffer, the server's CLIPBOARD is never synchronized
with Windows' one.

Autocutsel tracks changes in the server's cutbuffer and CLIPBOARD
selection. When the CLIPBOARD is changed, it updates the cutbuffer. When
the cutbuffer is changed, it owns the CLIPBOARD selection. The cutbuffer
and CLIPBOARD selection are always synchronized. Since the VNC client
synchronizes the Windows' clipboard and the server's cutbuffer, all
three "clipboards" are always kept synchronized.

%prep
%setup

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install

%files
%defattr(-,root,root)
%doc COPYING
/usr/bin/cutsel
/usr/bin/autocutsel
%doc README

%changelog
