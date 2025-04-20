#
# spec file for package framework-ectool
#
# Copyright (c) 2025 SUSE LLC
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

%define pkg_name ectool
Name:           framework-ectool
Version:        1+git20240623.0ac6155
Release:        0
Summary:        ectool for the Framework laptop
License:        MIT
URL:            https://gitlab.howett.net/DHowett/ectool
Provides:       ectool
Conflicts:      ectool
Source:         %{pkg_name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libusb)
BuildRequires:  pkgconfig(libftdi1)

%description
ectool for the Framework laptop. It allows setting the fan speed
or battery charge limits.

%prep
%autosetup -p1 -n %{pkg_name}-%{version}

%build
%cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_INSTALL_PREFIX=/usr \
%{nil}

%cmake_build

%check

%install
install -Dm755 build/src/ectool %{buildroot}%{_bindir}/ectool
ln -s %{_bindir}/ectool %{buildroot}%{_bindir}/framework-ectool

%files
%doc README.md
%license LICENSE
%{_bindir}/ectool
%{_bindir}/framework-ectool

%changelog
