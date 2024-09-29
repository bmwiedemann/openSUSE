#
# spec file for package python-pywbem
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


# cythonized pywbem produces yacc parser errors
%bcond_with cythonize
Name:           python-pywbem
Version:        1.7.2
Release:        0
Summary:        Python module for making CIM operation calls using the WBEM protocol
License:        LGPL-2.1-or-later
Group:          System/Management
URL:            https://pywbem.github.io/
Source0:        https://github.com/pywbem/pywbem/archive/%{version}.tar.gz#/pywbem-%{version}.tar.gz
# PATCH-FIX-UPSTREAM Based on gh#pywbem/pywbem#3217
Patch0:         support-new-testfixtures.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 38.4.1}
BuildRequires:  %{python_module wheel}
%if %{with cythonize}
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
%endif
BuildRequires:  %{python_module FormEncode >= 2.0.0}
BuildRequires:  %{python_module PyYAML > 5.3.1}
BuildRequires:  %{python_module certifi >= 2019.11.28}
BuildRequires:  %{python_module httpretty}
BuildRequires:  %{python_module lxml >= 4.6.4}
BuildRequires:  %{python_module ply >= 3.10}
BuildRequires:  %{python_module pytest >= 6.2.5}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module requests >= 2.25.0}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module six >= 1.16.0}
BuildRequires:  %{python_module testfixtures}
BuildRequires:  %{python_module urllib3 >= 1.26.5}
BuildRequires:  %{python_module yamlloader >= 0.5.5}
BuildRequires:  fdupes
BuildRequires:  libxml2-tools
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML >= 5.3.1
Requires:       python-certifi >= 2019.11.28
Requires:       python-ply >= 3.10
Requires:       python-requests >= 2.25.0
Requires:       python-six >= 1.16.0
Requires:       python-urllib3 >= 1.26.5
Requires:       python-yamlloader >= 0.5.5
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-pywebmtools
%if ! %{with cythonize}
BuildArch:      noarch
%endif
%python_subpackages

%description
PyWBEM is a Python module for making CIM operation calls using the WBEM
protocol to query and update managed objects.

%prep
%autosetup -p1 -n pywbem-%{version}

%build
%pyproject_wheel %{?_with_cythonize:--config-settings "--build-option=--cythonized" .}

%install
%pyproject_install
%fdupes %{buildroot}
rm %{buildroot}%{_bindir}/*.bat
%python_clone -a %{buildroot}%{_bindir}/mof_compiler

%check
%if %{with cythonize}
%pytest_arch -k "not (skipnothingbydefault ${$python_donttest})" tests/unittest tests/functiontest
%else
%pytest -k "not (skipnothingbydefault ${$python_donttest})" tests/unittest tests/functiontest
%endif

%post
%python_install_alternative mof_compiler

%postun
%python_uninstall_alternative mof_compiler

%files %{python_files}
%doc README.md
%license LICENSE.txt
%python_alternative %{_bindir}/mof_compiler
%if %{with cythonize}
%{python_sitearch}/pywbem
%{python_sitearch}/pywbem_mock
%{python_sitearch}/pywbem-%{version}.dist-info
%else
%{python_sitelib}/pywbem
%{python_sitelib}/pywbem_mock
%{python_sitelib}/pywbem-%{version}.dist-info
%endif

%changelog
