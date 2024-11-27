#
# spec file for package autocutsel
#
# Copyright (c) 2024 SUSE LLC
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


Name:           autocutsel
URL:            https://www.nongnu.org/autocutsel/
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xt)
Version:        0.10.1
Release:        0
Summary:        Clipboard / Cutbuffer management helper
License:        GPL-2.0-or-later
Group:          System/X11/Utilities
Source:         https://github.com/sigmike/autocutsel/releases/download/%{version}/%{name}-%{version}.tar.gz
Source100:      autocutsel.1
Source101:      cutsel.1

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
%make_build

%install
%make_install
install -m 644 -D -t %{buildroot}%{_mandir}/man1 %{SOURCE100} %{SOURCE101}

%files
%license COPYING
%{_bindir}/cutsel
%{_bindir}/autocutsel
%{_mandir}/man1/*
%doc README

%changelog
