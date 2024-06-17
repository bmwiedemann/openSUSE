#
# spec file for package appres
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


Name:           appres
Version:        1.0.7
Release:        0
Summary:        Utility to list the resource database of an X application
License:        X11
Group:          System/X11/Utilities
URL:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
BuildRequires:  meson
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto) >= 7.0.17
BuildRequires:  pkgconfig(xt)
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The appres program prints the resources seen by an application (or
subhierarchy of an application) with the specified class and instance
names. It can be used to determine which resources a particular
program will load.

%prep
%setup -q

%build
%{meson}
%{meson_build}

%install
%{meson_install}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING
%{_bindir}/appres
%{_mandir}/man1/appres.1%{?ext_man}

%changelog
