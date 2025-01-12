#
# spec file for package python-sip6
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


%{?sle15_python_module_pythons}
Name:           python-sip6
Version:        6.9.1
Release:        0
Summary:        A Python bindings generator for C/C++ libraries
License:        BSD-2-Clause AND BSD-3-Clause
Group:          Development/Libraries/Python
URL:            https://github.com/Python-SIP/sip
Source0:        https://github.com/Python-SIP/sip/archive/refs/tags/%{version}.tar.gz#/sip-%{version}-gh.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 69.5}
# Technically >= 8, but we make it compatible in prep.
BuildRequires:  %{python_module setuptools_scm >= 7}
BuildRequires:  %{python_module tomli if %python-base < 3.11}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test
BuildRequires:  %{python_module testsuite}
BuildRequires:  %{python_module devel}
BuildRequires:  c++_compiler
# /SECTION
BuildArch:      noarch

%python_subpackages

%description
SIP is a collection of tools that makes it very easy to create Python
bindings for C and C++ libraries. It was originally developed in 1998
to create PyQt, the Python bindings for the Qt toolkit, but can be used
to create bindings for any C or C++ library. For example it is also used
to generate wxPython, the Python bindings for wxWidgets.

%package devel
Summary:        A Python bindings generator for C/C++ libraries
Group:          Development/Libraries/Python
Requires:       c++_compiler
Requires:       python-base >= 3.9
Requires:       python-packaging
Requires:       python-setuptools >= 69.5
Requires:       (python-tomli if python-base < 3.11)
Requires(post): update-alternatives
Requires(postun): update-alternatives
Conflicts:      python-sip-impl
# boo#1190441: remove erroneously created non-devel python3X-sip metapackages.
# In order not to remove SIPv4 and possible future packages, we have to explicitly
# name the only version which made it into Factory.
Obsoletes:      python-sip = 6.1.1
Provides:       python-sip-devel = %{version}-%{release}
Provides:       python-sip-impl = %{version}-%{release}

%description devel
SIP is a collection of tools that makes it very easy to create Python
bindings for C and C++ libraries. It was originally developed in 1998
to create PyQt, the Python bindings for the Qt toolkit, but can be used
to create bindings for any C or C++ library. For example it is also used
to generate wxPython, the Python bindings for wxWidgets.

This package contains all the developer tools you need to create your
own sip bindings.

%prep
%autosetup -p1 -n sip-%{version}
# Make it work with setuptools_scm < 8
%if 0%{suse_version} < 1600
sed -i s/version_file/write_to/ pyproject.toml
%endif

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/sip-build
%python_clone -a %{buildroot}%{_bindir}/sip-distinfo
%python_clone -a %{buildroot}%{_bindir}/sip-install
%python_clone -a %{buildroot}%{_bindir}/sip-module
%python_clone -a %{buildroot}%{_bindir}/sip-sdist
%python_clone -a %{buildroot}%{_bindir}/sip-wheel
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v test

%post devel
%python_install_alternative sip-build sip-distinfo sip-install sip-module sip-sdist sip-wheel

%postun devel
%python_uninstall_alternative sip-build

%files %{python_files devel}
%license LICENSE*
%python_alternative %{_bindir}/sip-build
%python_alternative %{_bindir}/sip-distinfo
%python_alternative %{_bindir}/sip-install
%python_alternative %{_bindir}/sip-module
%python_alternative %{_bindir}/sip-sdist
%python_alternative %{_bindir}/sip-wheel
%{python_sitelib}/sipbuild
%{python_sitelib}/sip-%{version}.dist-info

%changelog
