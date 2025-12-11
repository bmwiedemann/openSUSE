#
# spec file for package python-zope.proxy
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2013 LISA GmbH, Bingen, Germany.
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

%{?sle15_python_module_pythons}
Name:           python-zope.proxy%{psuffix}
Version:        7.1
Release:        0
Summary:        Generic Transparent Proxies
License:        ZPL-2.1
URL:            https://github.com/zopefoundation/zope.proxy
Source:         https://files.pythonhosted.org/packages/source/z/zope.proxy/zope_proxy-%{version}.tar.gz
BuildRequires:  %{python_module devel >= 3.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-zope.interface
%if %{with test}
BuildRequires:  %{python_module zope.proxy = %{version}}
BuildRequires:  %{python_module zope.security >= 7.3}
BuildRequires:  %{python_module zope.testrunner}
%endif
Conflicts:      python-zope-proxy < %{version}
%python_subpackages

%description
Proxies are special objects which serve as mostly-transparent wrappers around
another object, intervening in the apparent behavior of the wrapped object only
when necessary to apply the policy (e.g., access checking, location brokering,
etc.) for which the proxy is responsible.

%package        devel
Summary:        Generic Transparent Proxies
Requires:       %{name} = %{version}
Provides:       python-zope-proxy = %{version}
Obsoletes:      python-zope-proxy < %{version}

%description    devel
This package contains the files needed for binding the %{name} C module.

%prep
%autosetup -p1 -n zope_proxy-%{version}
rm -rf zope.proxy.egg-info

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%{python_expand rm %{buildroot}%{$python_sitearch}/zope/proxy/_zope_proxy_proxy.c
  %fdupes %{buildroot}%{$python_sitearch}
}
%endif

%if %{with test}
%check
%python_expand PYTHONPATH=src %{_bindir}/zope-testrunner-%{$python_bin_suffix} -vvv --test-path src
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE.txt
%doc COPYRIGHT.txt CHANGES.rst README.rst
%exclude %{python_sitearch}/zope/proxy/proxy.h
%dir %{python_sitearch}/zope
%{python_sitearch}/zope/proxy
%{python_sitearch}/zope[_.]proxy-%{version}.dist-info

%files %{python_files devel}
%dir %{python_sysconfig_path include}/zope[_.]proxy
%{python_sysconfig_path include}/zope[_.]proxy/*
%dir %{python_sitearch}/zope
%{python_sitearch}/zope/proxy/proxy.h
%endif

%changelog
