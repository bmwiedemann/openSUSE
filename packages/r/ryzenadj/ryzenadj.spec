#
# spec file for package ryzenadj
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


Name:           ryzenadj
Version:        0.15.0
Release:        0
Summary:        Settings manager for mobile AMD Ryzen processors
License:        GPL-3.0-or-later
URL:            https://github.com/FlyGoat/RyzenAdj
Source0:        https://github.com/FlyGoat/RyzenAdj/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libpci)
ExclusiveArch:  %ix86 x86_64

%description
RyzenAdj is a settings manager for mobile AMD Ryzen processors.

%prep
%autosetup -p1 -n RyzenAdj-%{version}

%build
%cmake
%cmake_build

%install
install -D -m0755 build/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
