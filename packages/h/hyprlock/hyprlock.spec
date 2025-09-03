#
# spec file for package hyprlock
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


%if 0%{?suse_version} >= 1550
  %define _pam_confdir %{_pam_vendordir}
  %define _config_norepl %nil
%else
  %define _pam_confdir %{_sysconfdir}
  %define _config_norepl %config(noreplace)
%endif

Name:           hyprlock
Version:        0.9.1
Release:        0
Summary:        Hyprland's screen locking utility
License:        BSD-3-Clause
URL:            https://wiki.hyprland.org/Hypr-Ecosystem/hyprlock/
Source0:        %{name}-%{version}.tar.xz
Source1:        hyprlock.conf
BuildRequires:  Mesa-devel
BuildRequires:  Mesa-libGLESv3-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hyprgraphics-devel
BuildRequires:  hyprland
BuildRequires:  hyprland-protocols-devel
BuildRequires:  hyprlang-devel
BuildRequires:  hyprutils-devel
BuildRequires:  hyprwayland-scanner
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(hyprlang) >= 0.4.2
BuildRequires:  pkgconfig(hyprutils)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libmagic)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(sdbus-c++)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xkbcommon)

%description
Hyprland's simple, yet multi-threaded and GPU-accelerated screen locking utility.

* uses the secure ext-session-lock protocol
* full support for fractional-scale
* fully GPU accelerated
* multi-threaded resource acquisition for no hitches

%prep
%autosetup -p1
# Both _pam_confdir paths provide a pam.d path
sed -i 's/pam.d//' CMakeLists.txt

%build
%cmake \
  -D CMAKE_INSTALL_SYSCONFDIR=%{_pam_confdir} \
  -D CMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install
install -Dm 0644 %{SOURCE1} %{buildroot}/%{_docdir}/%{name}/hyprlock.conf.example

%files
%license LICENSE
%doc README.md hyprlock.conf.example
%_config_norepl %{_pam_confdir}/hyprlock
%{_bindir}/hyprlock
%{_datadir}/hypr/hyprlock.conf

%changelog
