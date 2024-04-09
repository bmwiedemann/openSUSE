#
# spec file for package xorg-sgml-doctools
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


Name:           xorg-sgml-doctools
Version:        1.12.1
Release:        0
Summary:        Set of SGML entities and XML/CSS style sheets for building X.org documentation
License:        MIT
Group:          Development/Tools/Building
URL:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/doc/%{name}-%{version}.tar.xz
BuildRequires:  meson
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
# This was part of the xorg-x11-util-devel package up to version 7.6
Conflicts:      xorg-x11-util-devel <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This package provides a common set of SGML entities and XML/CSS style
sheets used in building/formatting the documentation provided in other
X.Org packages.

%prep
%setup -q

%build
%{meson}
%{meson_build}

%install
%{meson_install}

%files
%defattr(-,root,root)
%doc README.md
%license COPYING
%{_datadir}/sgml/X11/
%{_datadir}/pkgconfig/xorg-sgml-doctools.pc

%changelog
