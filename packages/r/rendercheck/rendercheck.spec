#
# spec file for package rendercheck
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


Name:           rendercheck
Version:        1.6
Release:        0
Summary:        Program to test a Render extension implementation
License:        HPND
Group:          System/X11/Utilities
URL:            http://xorg.freedesktop.org/
Source0:        https://xorg.freedesktop.org/archive/individual/test/%{name}-%{version}.tar.xz
BuildRequires:  meson
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xrender)
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
rendercheck is a program to test a Render extension implementation
against separate calculations of expected output.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%files
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README
%{_bindir}/rendercheck
%{_mandir}/man1/rendercheck.1%{?ext_man}

%changelog
