#
# spec file for package slurp
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


Name:           slurp
Version:        1.4.0
Release:        0
Summary:        Wayland region selector
License:        MIT
Group:          System/GUI/Other
URL:            https://github.com/emersion/slurp
Source:         https://github.com/emersion/slurp/archive/v%{version}.tar.gz
BuildRequires:  meson >= 0.48.0
BuildRequires:  pkgconfig
BuildRequires:  scdoc
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.14
BuildRequires:  pkgconfig(xkbcommon)

%description
Tool to select a region in a Wayland compositor.
Meant to be used with a tool called grim.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -I/usr/include/wayland"
%meson
%meson_build

%install
%meson_install

%files
%{_bindir}/slurp
%{_mandir}/man1/slurp.1%{?ext_man}

%changelog
