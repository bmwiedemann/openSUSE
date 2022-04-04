#
# spec file for package xsm
#
# Copyright (c) 2022 SUSE LLC
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


%if 0%{?suse_version} < 1550
%define _distconfdir %{_prefix}%{_sysconfdir}
%endif
Name:           xsm
Version:        1.0.5
Release:        0
Summary:        X Session Manager
License:        MIT
Group:          System/X11/Utilities
URL:            https://xorg.freedesktop.org/
Source0:        https://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
Patch0:         n_UsrEtc.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xt) > 1.0.99
# default rsh command is ssh
Requires:       openssh
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6

%description
xsm is a session manager. A session is a group of applications, each
of which has a particular state. xsm allows you to create arbitrary
sessions - for example, you might have a "light" session, a "development"
session, or an "xterminal" session. Each session can have its own set of
applications. Within a session, you can perform a "checkpoint" to save
application state, or a "shutdown" to save state and exit the session. When
you log back in to the system, you can load a specific session, and you can
delete sessions you no longer want to keep.

%prep
%setup -q
%patch0 -p1

%build
autoreconf -fi
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc ChangeLog README
%dir %{_distconfdir}
%dir %{_distconfdir}/X11
%{_distconfdir}/X11/xsm/
%{_bindir}/xsm
%dir %{_datadir}/X11/app-defaults
%{_datadir}/X11/app-defaults/XSm
%{_mandir}/man1/xsm.1%{?ext_man}

%changelog
