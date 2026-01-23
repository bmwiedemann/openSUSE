#
# spec file for package libpkgmanifest
#
# Copyright (c) 2025 Red Hat, Inc.
# Copyright (c) 2026 Neal Gompa.
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


%global libsoversion 0
%global libname %{name}%{libsoversion}
%global devname %{name}-devel

%bcond_without docs
%bcond_without python
%bcond_without tests

Name:           libpkgmanifest
Version:        0.5.9
Release:        0
Summary:        Library for working with RPM manifests
License:        LGPL-2.1-or-later
URL:            https://github.com/rpm-software-management/libpkgmanifest
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.13
BuildRequires:  gcc-c++ >= 10.1
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(yaml-cpp) >= 0.7.0

%if %{with tests}
BuildRequires:  pkgconfig(gmock)
BuildRequires:  pkgconfig(gtest)
%endif

%if %{with python}
BuildRequires:  python3-devel
BuildRequires:  swig >= 4.2.0
%endif

%if %{with docs}
# requests requires ca-certs to work properly
BuildRequires:  ca-certificates
BuildRequires:  ca-certificates-mozilla
BuildRequires:  doxygen
#BuildRequires:  python3dist(sphinx) >= 4.1.2
BuildRequires:  python3-Sphinx >= 4.1.2
#BuildRequires:  python3dist(breathe)
BuildRequires:  python3-breathe
#BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3-sphinx_rtd_theme
%endif

%description
This library provides functionality for parsing and serializing
RPM package manifest files.

It is primarily designed for use by package managers like DNF,
which populate information into manifest files. However, it can
also be used directly to interact with manifest objects in custom
applications.

# -----------------------------------------------------------------

%package -n %{libname}
Summary:        Library for working with RPM manifests

%description -n %{libname}
This library provides functionality for parsing and serializing
RPM package manifest files.

%ldconfig_scriptlets -n %{libname}

%files -n %{libname}
%{_libdir}/%{name}.so.%{libsoversion}
%license LICENSE
%doc README.md

# -----------------------------------------------------------------

%package -n %{devname}
Summary:        Development files for %{name}
Requires:       %{libname}%{?_isa} = %{version}-%{release}

%description -n %{devname}
Development files for %{name}.

%files -n %{devname}
%{_includedir}/%{name}/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%doc docs/design

# -----------------------------------------------------------------

%if %{with python}
%package -n python3-%{name}
Summary:        Python 3 bindings for the %{name} library
Requires:       %{libname}%{?_isa} = %{version}-%{release}

%description -n python3-%{name}
Python 3 bindings for the %{name} library.

%files -n python3-%{name}
%{python3_sitearch}/%{name}
%{python3_sitearch}/%{name}-*.dist-info/
%endif

# -----------------------------------------------------------------

%prep
%autosetup -p1

# Drop Werror to fix bindings build on 32-bit arches
sed -e "s/-Werror//" -i CMakeLists.txt

%build
%cmake \
    -DWITH_DOCS=%{?with_docs:ON}%{!?with_docs:OFF} \
    -DWITH_PYTHON=%{?with_python:ON}%{!?with_python:OFF} \
    -DWITH_TESTS=%{?with_tests:ON}%{!?with_tests:OFF} \
    -DWITH_CODE_COVERAGE=OFF \

%cmake_build

%install
%cmake_install

%check
%if %{with tests}
    %ctest
%endif

%changelog
