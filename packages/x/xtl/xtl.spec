#
# spec file for package xtl
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%{?sle15_python_module_pythons}
Name:           xtl
Version:        0.8.1
Release:        0
Summary:        The x template library
License:        BSD-3-Clause
Group:          Development/Languages/C and C++
URL:            https://github.com/xtensor-stack/xtl
Source0:        https://github.com/xtensor-stack/xtl/archive/refs/tags/%{version}/xtl-%{version}.tar.gz
BuildRequires:  %{python_module breathe}
BuildRequires:  %{python_module sphinx_rtd_theme}
BuildRequires:  cmake >= 3.5
BuildRequires:  doctest-devel
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkg-config
BuildRequires:  cmake(nlohmann_json)

%description
Basic tools (containers, algorithms) used by other quantstack packages.

%package        devel
Summary:        The x template library
Group:          Development/Languages/C and C++
Requires:       cmake(nlohmann_json)
BuildArch:      noarch

%description    devel
Basic tools (containers, algorithms) used by other quantstack packages.

%package        doc
Summary:        Documentation for xtl
Group:          Documentation/HTML
BuildArch:      noarch

%description    doc
Basic tools (containers, algorithms) used by other quantstack packages.

%prep
%autosetup

%build
%cmake \
  -DBUILD_TESTS:BOOL=ON \
  -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build

#build documentation
cd %{_builddir}/%{name}-%{version}/docs
make html

%install
%cmake_install

#install documentation
mkdir -p %{buildroot}/%{_docdir}/%{name}
cp -r %{_builddir}/%{name}-%{version}/docs/build/html/* %{buildroot}/%{_docdir}/%{name}

%fdupes -s %{buildroot}/%{_docdir}
%fdupes %{buildroot}/%{_prefix}

%check
%ctest

%files devel
%license LICENSE
%doc README.md
%{_includedir}/xtl/
%{_datadir}/cmake/xtl/
%{_datadir}/pkgconfig/xtl.pc

%files doc
%doc %{_docdir}/%{name}

%changelog
