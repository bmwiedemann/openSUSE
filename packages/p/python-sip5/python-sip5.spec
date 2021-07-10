#
# spec file for package python-sip
#
# Copyright (c) 2020 SUSE LLC
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-sip5
Version:        5.5.0
Release:        0
Summary:        A Python bindings generator for C/C++ libraries
License:        GPL-2.0-only OR GPL-3.0-only OR SUSE-SIP
Group:          Development/Libraries/Python
URL:            https://www.riverbankcomputing.com/software/sip
Source0:        https://files.pythonhosted.org/packages/source/s/sip/sip-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module toml}
BuildRequires:  %{python_module base >= 3.5.1}
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros

%python_subpackages

%description
SIP is a tool that makes it very easy to create Python bindings for C
and C++ libraries. It was originally developed to create PyQt, the
Python bindings for the Qt toolkit, but can be used to create bindings
for any C or C++ library.

%package devel
Summary:        A Python bindings generator for C/C++ libraries
Group:          Development/Libraries/Python
Requires:       c++_compiler
Requires:       python-base >= 3.5.1
Requires:       python-devel
Requires:       python-setuptools
Requires:       python-toml
Requires(post): update-alternatives
Requires(postun): update-alternatives
Conflicts:      python-sip-impl
Provides:       python-sip-devel = %{version}-%{release}
Provides:       python-sip-impl = %{version}-%{release}


%description devel
SIP is a tool that makes it very easy to create Python bindings for C
and C++ libraries. It was originally developed to create PyQt, the
Python bindings for the Qt toolkit, but can be used to create bindings
for any C or C++ library.

This package contains all the developer tools you need to create your
own sip bindings.

%package -n python-sip5-doc
Summary:        A Python bindings generator for C/C++ libraries -- common documentation
Group:          Development/Libraries/Python
Provides:       %{python_module sip5-doc = %{version}-%{release}}

%description -n python-sip5-doc
SIP is a tool that makes it very easy to create Python bindings for C
and C++ libraries. It was originally developed to create PyQt, the
Python bindings for the Qt toolkit, but can be used to create bindings
for any C or C++ library.

This package contains the documentation and example files.

%prep
%setup -q -n sip-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/sip-build
%python_clone -a %{buildroot}%{_bindir}/sip-distinfo
%python_clone -a %{buildroot}%{_bindir}/sip-install
%python_clone -a %{buildroot}%{_bindir}/sip-module
%python_clone -a %{buildroot}%{_bindir}/sip-sdist
%python_clone -a %{buildroot}%{_bindir}/sip-wheel
%python_clone -a %{buildroot}%{_bindir}/sip5
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%fdupes -s doc

%post devel
%python_install_alternative sip-build sip-distinfo sip-install sip-module sip-sdist sip-wheel sip5

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
%python_alternative %{_bindir}/sip5
%{python_sitearch}/sipbuild
%{python_sitearch}/sip-%{version}*-info

%files -n python-sip5-doc
%license LICENSE*
%doc doc/

%changelog
