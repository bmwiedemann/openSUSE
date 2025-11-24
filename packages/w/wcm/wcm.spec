#
# spec file for package wcm
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


%define major_ver 0.10
%define minor_ver 0
Name:           wcm
Version:        %{major_ver}.%{minor_ver}
Release:        0
Summary:        Wayfire Config Manager
License:        MIT
URL:            https://wayfire.org/
Source0:        https://github.com/WayfireWM/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/WayfireWM/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz.sha256sum
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  wlroots-devel >= 0.19.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(wayfire)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wf-config) >= %{major_ver}
BuildRequires:  pkgconfig(wf-shell) >= %{major_ver}
BuildRequires:  pkgconfig(xkbregistry)
Requires:       wayfire >= %{major_ver}
Requires:       wdisplays >= %{major_ver}

%description
Wayfire Config Manager https://wayfire.org/.

%prep
echo "`grep %{name}-%{version}.tar.xz %{SOURCE1} | grep -Eo '^[0-9a-f]+'`  %{SOURCE0}" | sha256sum -c
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%fdupes %{buildroot}/%{_datadir}

%check
%meson_test

%files
%license LICENSE
%{_bindir}/%{name}
%dir %{_datadir}/wcm/
%{_datadir}/wcm/icons
%{_datadir}/icons/wcm.svg
%{_datadir}/applications/*.desktop

%changelog
