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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
Name:           python-pywbem
Version:        1.8.1
Release:        0
Summary:        Python module for making CIM operation calls using the WBEM protocol
License:        LGPL-2.1-or-later
Group:          System/Management
URL:            https://pywbem.github.io/
Source0:        https://files.pythonhosted.org/packages/source/p/pywbem/pywbem-%{version}.tar.gz
BuildRequires:  %{python_module FormEncode >= 2.0.0}
BuildRequires:  %{python_module PyYAML >= 6.0.2}
BuildRequires:  %{python_module certifi >= 2024.07.04}
BuildRequires:  %{python_module idna >= 3.7}
BuildRequires:  %{python_module lxml >= 4.6.4}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module ply >= 3.10}
BuildRequires:  %{python_module pytest >= 6.2.5}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module requests >= 2.32.4}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module setuptools >= 70.0.0}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module testfixtures}
BuildRequires:  %{python_module urllib3 >= 1.26.5}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module yamlloader >= 0.5.5}
BuildRequires:  fdupes
BuildRequires:  libxml2-tools
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML >= 6.0.2
Requires:       python-certifi >= 2024.07.04
Requires:       python-idna >= 3.7
Requires:       python-ply >= 3.10
Requires:       python-requests >= 2.32.4
Requires:       python-urllib3 >= 2.5.0
Requires:       python-yamlloader >= 0.5.5
Recommends:     python-pywebmtools
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
BuildArch:      noarch
%python_subpackages

%description
PyWBEM is a Python module for making CIM operation calls using the WBEM
protocol to query and update managed objects.

%prep
%autosetup -p1 -n pywbem-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%fdupes %{buildroot}
rm %{buildroot}%{_bindir}/*.bat
%python_clone -a %{buildroot}%{_bindir}/mof_compiler

%check
%pytest -k "not (skipnothingbydefault ${$python_donttest})" tests/unittest tests/functiontest

%post
%python_install_alternative mof_compiler

%postun
%python_uninstall_alternative mof_compiler

%pre
%python_libalternatives_reset_alternative mof_compiler

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
