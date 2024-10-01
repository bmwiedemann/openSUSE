#
# spec file for package hyprpicker
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


Name:           hyprpicker
Version:        0.4.1
Release:        0
Summary:        A wlroots-compatible Wayland color picker
License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprpicker
Source:         %{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  pkgconfig(hyprutils) >= 0.2.0
BuildRequires:  pkgconfig(hyprwayland-scanner) >= 0.4.2
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xkbcommon)

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
