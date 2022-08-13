#
# spec file for package rinutils
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


Name:           rinutils
Version:        0.10.1
Release:        0
Summary:        Shlomi Fish's gnu11 C Library of Random headers
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/shlomif/rinutils/
Source:         https://github.com/shlomif/rinutils/releases/download/%{version}/rinutils-%{version}.tar.xz
BuildRequires:  cmake
# Only due to the PROJECT declaration in CMakeLists
BuildRequires:  gcc-c++
BuildRequires:  xz

%description
Shlomi Fish's gnu11 C Library of Random headers.

%package devel
Summary:        Shlomi Fish's gnu11 C Library of Random headers
Group:          Development/Libraries/C and C++
BuildArch:      noarch

%description devel
Shlomi Fish's gnu11 C Library of Random headers.

%prep
%autosetup -p1

%build
%cmake -DWITH_TEST_SUITE=OFF -DINSTALL_TO_DATADIR=ON
%cmake_build

%install
%cmake_install

%files devel
%license LICENSE
%doc README.asciidoc NEWS.asciidoc
%{_includedir}/rinutils/
%{_datadir}/pkgconfig/*.pc
%dir %{_datadir}/cmake/
%{_datadir}/cmake/Rinutils/

%changelog
