#
# spec file for package xkbcomp
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           xkbcomp
Version:        1.4.2
Release:        0
Summary:        Utility to compile XKB keyboard description
License:        MIT
Group:          System/X11/Utilities
Url:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Source1:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2.sig
Source2:        %{name}.keyring
BuildRequires:  bison
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto) >= 7.0.17
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
make %{?_smp_mflags} V=1

%install
%make_install

%files
%defattr(-,root,root)
%doc ChangeLog COPYING README
%{_bindir}/xkbcomp
%{_mandir}/man1/xkbcomp.1%{?ext_man}

%files devel
%defattr(-,root,root)
%{_libdir}/pkgconfig/xkbcomp.pc

%changelog
