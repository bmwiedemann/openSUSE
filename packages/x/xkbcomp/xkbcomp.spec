#
# spec file for package xkbcomp
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


Name:           xkbcomp
Version:        1.4.6
Release:        0
Summary:        Utility to compile XKB keyboard description
License:        MIT
Group:          System/X11/Utilities
URL:            https://xorg.freedesktop.org/
Source0:        https://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
BuildRequires:  bison
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto) >= 7.0.17
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6

%description
The xkbcomp keymap compiler converts a description of an XKB keymap
into one of several output formats.

%package devel
Summary:        Utility to compile XKB keyboard description -- Development Files
Group:          Development/Libraries/X11
Requires:       %{name} = %{version}

%description devel
The xkbcomp keymap compiler converts a description of an XKB keymap
into one of several output formats.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc ChangeLog README
%{_bindir}/xkbcomp
%{_mandir}/man1/xkbcomp.1%{?ext_man}

%files devel
%{_libdir}/pkgconfig/xkbcomp.pc

%changelog
