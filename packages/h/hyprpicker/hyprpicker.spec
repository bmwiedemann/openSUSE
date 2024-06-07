#
# spec file for package hyprpicker
#
# Copyright (c) 2023 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           hyprpicker
Version:        0.3.0
Release:        0
Summary:        A wlroots-compatible Wayland color picker
License:        BSD-3-Clause
Url:            https://github.com/hyprwm/hyprpicker
Source:         %{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  Mesa-libGLESv3-devel
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(libjpeg)
buildRequires:  pkgconfig(xkbcommon)

%description
A wlroots-compatible Wayland color picker with magnifying lens. It
supports a few different output forms, e.g. RGB, CMYK, HSL, HSV.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man?/%{name}.?%{?ext_man}

%changelog
