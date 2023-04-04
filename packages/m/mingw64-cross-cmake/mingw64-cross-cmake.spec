#
# spec file for package mingw64-cross-cmake
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

Name:           mingw64-cross-cmake
Version:        1.0.0
Release:        0
Summary:        Cross build support for CMake
License:        BSD-3-Clause
Group:          Development/Tools/Building
URL:            https://www.cmake.org/
Source1:        macros.mingw64-cmake
Source2:        mingw64-cmake.prov
Source3:        mingw64_cmake.attr
BuildRequires:  mingw64-filesystem
Requires:       cmake >= 3.10
Requires:       mingw64-filesystem
BuildArch:      noarch
%_mingw64_package_header

%description
This package provides the required support files and macros
to create binary package for Windows with the CMake build system

%package -n mingw64-cross-ctest
Summary:        CTest support for cross CMake package
Requires:       mingw64-cross-cmake
Requires:       mingw64-cross-wine

%description -n mingw64-cross-ctest
This package provides the required package to running tests
with cross compiled binaries.

%prep

%build

%install
mkdir -p %{buildroot}%{_rpmmacrodir}
cp %{SOURCE1} %{buildroot}%{_rpmmacrodir}/macros.mingw64-cmake
mkdir -p %{buildroot}%{_bindir}
ln -s ../lib/mingw64-scripts %{buildroot}%{_bindir}/mingw64-cmake

# cmake support
install -m 0755 %{SOURCE2} %{buildroot}%{_rpmconfigdir}
mkdir -p %{buildroot}%{_fileattrsdir}
install -m 0644 %{SOURCE3} %{buildroot}%{_fileattrsdir}

%files
%defattr(-,root,root)
%{_rpmmacrodir}
%{_bindir}/mingw64-cmake
%{_rpmconfigdir}/mingw64-cmake.prov
%{_fileattrsdir}/mingw64_cmake.attr

%files -n mingw64-cross-ctest
%defattr(-,root,root)

%changelog
