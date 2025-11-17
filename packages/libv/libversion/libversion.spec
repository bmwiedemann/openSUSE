#
# spec file for package libversion
#
# Copyright (c) Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define sover 1
Name:           libversion
Version:        3.0.4
Release:        0
Summary:        Version string comparison library
License:        MIT
URL:            https://github.com/repology/libversion
Source:         https://github.com/repology/libversion/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  cmake >= 3.12
BuildRequires:  pkgconfig

%description
Libversion is an advanced version string comparison library. It can
compare versions of software packages, including complex cases like
1.2-x.3~alpha4. Is is used by the Repology project.

%package -n %{name}%{sover}
Summary:        Version string comparison library

%description -n %{name}%{sover}
Libversion is an advanced version string comparison library. It can
compare versions of software packages, including complex cases like
1.2-x.3~alpha4. Is is used by the Repology project.

%package devel
Summary:        Development files for libversion
Requires:       %{name}%{sover} = %{version}

%description devel
Libversion is an advanced version string comparison library. It can
compare versions of software packages, including complex cases like
1.2-x.3~alpha4. Is is used by the Repology project.

This package contains the files needed to build with Libversion.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
find %{buildroot} -type f -name "*.a" -print -delete

%check
%ctest

%ldconfig_scriptlets -n %{name}%{sover}

%files
%license COPYING
%{_bindir}/version_compare
%{_bindir}/version_sort

%files -n %{name}%{sover}
%license COPYING
%{_libdir}/libversion.so.%{sover}
%{_libdir}/libversion.so.%{sover}.*

%files devel
%license COPYING
%{_includedir}/libversion
%{_libdir}/libversion.so
%{_libdir}/cmake/libversion
%{_libdir}/pkgconfig/libversion.pc

%changelog
