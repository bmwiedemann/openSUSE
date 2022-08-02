#
# spec file for package xtl
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


Name:           xtl
Version:        0.7.4
Release:        0
Summary:        The x template library
License:        BSD-3-Clause
Group:          Development/Languages/C and C++
URL:            https://github.com/xtensor-stack/xtl
Source0:        https://github.com/xtensor-stack/xtl/archive/refs/tags/%{version}/xtl-%{version}.tar.gz
#PATCH-FIX-OPENSUSE fix_cmake_install_directory.patch change install directories of cmake and pkgconfig files
Patch0:         fix_cmake_install_directory.patch
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkg-config
BuildRequires:  python3-breathe
BuildRequires:  cmake(nlohmann_json)

%description
Basic tools (containers, algorithms) used by other quantstack packages.

%prep
%autosetup

%build
%cmake
%cmake_build

#build documentation
cd %{_builddir}/%{name}-%{version}/docs
make html

%install
%cmake_install

#install documentation
mkdir -p %{buildroot}/%{_docdir}/%{name}
cp -r %{_builddir}/%{name}-%{version}/docs/build/html/* %{buildroot}/%{_docdir}/%{name}

%package        devel
Summary:        The x template library
Group:          Development/Languages/C and C++
Requires:       cmake(nlohmann_json)

%description    devel
Basic tools (containers, algorithms) used by other quantstack packages.

%files devel
%license LICENSE
%doc README.md
%{_includedir}/xtl/
%{_libdir}/cmake/xtl/
%{_libdir}/pkgconfig/xtl.pc

%package        doc
Summary:        Documentation for xtl
Group:          Documentation/HTML

%description    doc
Basic tools (containers, algorithms) used by other quantstack packages.

%files doc
%doc %{_docdir}/%{name}

%changelog
