#
# spec file for package labwc-menu-generator
#
# Copyright (c) 2026 SUSE LLC and contributors
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

Name:           labwc-menu-generator
Version:        0.2.2
Release:        0
Summary:        Generate a full Labwc/Openbox menu
License:        GPL-2.0-or-later
URL:            https://github.com/labwc/labwc-menu-generator
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  meson
BuildRequires:  scdoc
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
Suggests:       labwc
Suggests:       openbox

%description
A simple, lightweight, easily configurable C program that generates a full 
Labwc/Openbox XML-menu based on the information present in .desktop application files.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%doc README.md contrib/example-dynamic-root-menu.sh contrib/update-menu.sh
%{_bindir}/%{name}
%{_mandir}/man?/%{name}.?%{?ext_man}

%changelog
