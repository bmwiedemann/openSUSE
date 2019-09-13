#
# spec file for package smproxy
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           smproxy
Version:        1.0.6
Release:        0
Summary:        X Session Manager Proxy
License:        MIT
Group:          System/X11/Utilities
Url:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(xmuu)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xt)
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
smproxy allows X applications that do not support X11R6 session
management to participate in an X11R6 session.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc ChangeLog COPYING README
%{_bindir}/smproxy
%{_mandir}/man1/smproxy.1%{?ext_man}

%changelog
