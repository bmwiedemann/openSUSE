#
# spec file for package hyprwire
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2025/26 Florian "sp1rit" <sp1rit@disroot.org>
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

%define sover 3

Name:           hyprwire
Version:        0.3.0
Release:        0
Summary:        A wire protocol for IPC
License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprwire
Source0:        https://github.com/hyprwm/hyprwire/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(hyprutils) >= 0.9.0
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(pugixml)

%description
Hyprwire is a wire protocol, and its eponymous implementation. This
is essentially a method for processes to talk to each other.

%package -n     lib%{name}%{sover}
Summary:        A wire protocol for IPC
Group:          System/Libraries

%description -n lib%{name}%{sover}
Hyprwire is a wire protocol, and its eponymous implementation. This
is essentially a method for processes to talk to each other.

%package devel
Summary:        Development files for hyprwire
Group:          Development/Libraries/Other
Requires:       lib%{name}%{sover} = %{version}
Requires:       %{name} = %{version}

%description devel
Hyprwire is a wire protocol, and its eponymous implementation. This
is essentially a method for processes to talk to each other.

This subpackage contains headers for hyprwire.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets -n lib%{name}%{sover}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}-scanner

%files devel
%license LICENSE
%doc README.md
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}-scanner/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/%{name}-scanner.pc

%files -n lib%{name}%{sover}
%license LICENSE
%{_libdir}/lib%{name}.so.*

%changelog
