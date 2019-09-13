#
# spec file for package xmh
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


Name:           xmh
Version:        1.0.3
Release:        0
Summary:        Graphical user interface to send and read mail with MH
License:        MIT
Group:          System/X11/Utilities
Url:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xbitmaps) >= 1.1.0
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xt)
Requires:       nmh
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The xmh program provides a graphical user interface to the
MH Message Handling System. To actually do things with your
mail, it makes calls to the MH package.

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
%{_bindir}/xmh
%dir %{_datadir}/X11/app-defaults
%{_datadir}/X11/app-defaults/Xmh
%{_mandir}/man1/xmh.1%{?ext_man}

%changelog
