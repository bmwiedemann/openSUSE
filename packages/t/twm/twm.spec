#
# spec file for package twm
#
# Copyright (c) 2020 SUSE LLC
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


Name:           twm
Version:        1.0.11
Release:        0
Summary:        Tab Window Manager for the X Window System
License:        HPND
Group:          System/X11/Utilities
URL:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
Source1:        twm.desktop
Patch1:         twm-suse.diff
BuildRequires:  bison
BuildRequires:  pkg-config
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto) >= 7.0.17
BuildRequires:  pkgconfig(xt)
# This was part of the xorg-x11 package up to version 7.6
Provides:       windowmanager
Conflicts:      xorg-x11 <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
twm is a window manager for the X Window System. It provides
titlebars, shaped windows, several forms of icon management,
user-defined macro functions, click-to-type and pointer-driven
keyboard focus, and user-specified key and pointer button bindings.

%prep
%setup -q
%patch1 -p1

%build
%configure
make %{?_smp_mflags}

%install
%make_install
install -m0644 -D %{SOURCE1} %{buildroot}%{_datadir}/xsessions/twm.desktop
%suse_update_desktop_file %{buildroot}%{_datadir}/xsessions/twm.desktop

%files
%defattr(-,root,root)
%doc ChangeLog COPYING README.md
%{_bindir}/twm
%{_datadir}/X11/twm/
%{_datadir}/xsessions/twm.desktop
%{_mandir}/man1/twm.1%{?ext_man}

%changelog
