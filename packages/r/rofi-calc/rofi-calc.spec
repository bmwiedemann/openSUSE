#
# spec file for package rofi-calc
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           rofi-calc
Version:        2.5.0
Release:        0
Summary:        Calculator for rofi
License:        MIT
Group:          System/GUI/Other
URL:            https://github.com/svenstaro/rofi-calc
Source0:        https://github.com/svenstaro/rofi-calc/archive/v%{version}.tar.gz
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  rofi-wayland-devel >= 1.5
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.40
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(rofi) >= 1.5
Requires:       qalculate >= 2.0
Requires:       rofi-launcher >= 1.5

%description
A rofi plugin that uses libqalculate's qalc to parse natural language
input and provide results.

Since this uses libqalculate's qalc, natural language queries such as
"500 + 25%%" or "5000 EUR to USD" or "150 to hex" can be input.
It can also solve linear equations on the fly, like "60x + 30 = 50"
for instance.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%dir %{_libdir}/rofi
%{_libdir}/rofi/libcalc.so

%changelog
