#
# spec file for package deepin-wayland-protocols
#
# Copyright (c) 2023 SUSE LLC
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

Name:           deepin-wayland-protocols
Version:        1.6.0
Release:        0
Summary:        Deepin Wayland Protocols
License:        LGPL-2.1-or-later
Group:          Development/Tools/Building
URL:            https://github.com/linuxdeepin/deepin-wayland-protocols
Source0:        https://github.com/linuxdeepin/deepin-wayland-protocols/archive/refs/tags/%{version}-deepin.1.2.tar.gz
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(wayland-protocols)

%description
This project should be installing only the xml files of the non-standard wayland
protocols we use in Deepin.

%prep
%autosetup -p1 -n %{name}-%{version}-deepin.1.2

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license COPYING.LIB
%dir %{_libdir}/cmake/DeepinWaylandProtocols
%{_libdir}/cmake/DeepinWaylandProtocols/*.cmake
%{_datadir}/%{name}

%changelog

