#
# spec file for package fontobene-qt5
#
# Copyright (c) 2021 SUSE LLC
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


Name:           fontobene-qt5
Version:        0.2.0
Release:        0
Summary:        FontoBene parser for Qt5 (header-only)
License:        Apache-2.0 OR MIT
URL:            https://github.com/fontobene/fontobene-qt5
Source0:        https://github.com/fontobene/fontobene-qt5/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)

%description
A header-only library to parse FontoBene stroke fonts with C++/Qt5.

%package devel
Summary:        FontoBene parser for Qt5 (header-only)

%description devel
A header-only library to parse FontoBene stroke fonts with C++/Qt5.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
install -Dm0755 fontobene-qt5.pc.example %{buildroot}%{_libdir}/pkgconfig/%{name}.pc

%files devel
%license LICENSE-APACHE LICENSE-MIT
%doc CHANGELOG.md README.md
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc

%changelog
