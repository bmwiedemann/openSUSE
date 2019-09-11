#
# spec file for package xbanish
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           xbanish
Version:        1.6
Release:        0
Summary:        Program to hide the mouse cursor when typing
License:        BSD-3-Clause
Group:          System/X11/Utilities
URL:            https://github.com/jcs/xbanish
Source:         https://github.com/jcs/xbanish/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xt)

%description
xbanish hides the mouse cursor when you start typing, and shows it again when
the mouse cursor moves or a mouse button is pressed.  This is similar to
xterm's pointerMode setting, but xbanish works globally in the X11 session.

unclutter's -keystroke mode is supposed to do this, but it's broken[0].  I
looked into fixing it, but the unclutter source code is terrible, so I wrote
xbanish in a few hours.

The name comes from ratpoison's "banish" command that sends the cursor to the
corner of the screen.

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
%make_install PREFIX="%{_prefix}" MANDIR="%{_mandir}/man1"

%files
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
