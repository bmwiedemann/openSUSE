#
# spec file for package python-sip6
#
# Copyright (c) 2025 SUSE LLC and contributors
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
%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
Name:           python-sip6
Version:        6.14.0
Release:        0
Summary:        A Python bindings generator for C/C++ libraries
License:        BSD-2-Clause
Group:          Development/Libraries/Python
URL:            https://github.com/Python-SIP/sip
Source0:        https://github.com/Python-SIP/sip/archive/refs/tags/%{version}.tar.gz#/sip-%{version}-gh.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module packaging >= 24.2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module tomli if %python-base < 3.11}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if 0%{?suse_version} < 1600
BuildRequires:  %{python_module setuptools >= 75.8.1}
BuildRequires:  %{python_module setuptools_scm >= 7}
%else
BuildRequires:  %{python_module setuptools >= 77}
BuildRequires:  %{python_module setuptools_scm >= 8}
%endif
# SECTION test
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module testsuite}
BuildRequires:  c++_compiler
# /SECTION
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
Requires:       python-packaging >= 24.2
Requires:       python-setuptools >= 75.8.1
Requires:       (python-tomli if python-base < 3.11)
Conflicts:      python-sip-impl
# boo#1190441: remove erroneously created non-devel python3X-sip metapackages.
# In order not to remove SIPv4 and possible future packages, we have to explicitly
# name the only version which made it into Factory.
Obsoletes:      python-sip = 6.1.1
Provides:       python-sip-devel = %{version}-%{release}
Provides:       python-sip-impl = %{version}-%{release}
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif

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
# Make it work with setuptools < 77 and setuptools_scm < 8
%if 0%{?suse_version} < 1600
sed -i pyproject.toml \
    -e 's/version_file/write_to/' \
    -e 's/license = .*/license = { file = "LICENSE" }/' \
    -e '/license-files/d'
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
%python_group_libalternatives sip-build sip-distinfo sip-install sip-module sip-sdist sip-wheel
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v test

%pre devel
%python_libalternatives_reset_alternative sip-build

%post devel
%python_install_alternative sip-build sip-distinfo sip-install sip-module sip-sdist sip-wheel

%postun devel
%python_uninstall_alternative sip-build

%files %{python_files devel}
%license LICENSE
%python_alternative %{_bindir}/sip-build
%python_alternative %{_bindir}/sip-distinfo
%python_alternative %{_bindir}/sip-install
%python_alternative %{_bindir}/sip-module
%python_alternative %{_bindir}/sip-sdist
%python_alternative %{_bindir}/sip-wheel
%{python_sitelib}/sipbuild
%{python_sitelib}/sip-%{version}.dist-info

%changelog
