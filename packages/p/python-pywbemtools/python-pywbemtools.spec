#
# spec file for package python-pywbemtools
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-pywbemtools
Version:        0.7.3
Release:        0
Summary:        Python client tools to work with WBEM Servers using the PyWBEM API
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/pywbem/pywbemtools
# The PyPI archive does not contain the tests
Source:         https://github.com/pywbem/pywbemtools/archive/%{version}.tar.gz#/pywbemtools-0.7.3-gh.tar.gz
# PATCH-FIX-UPSTREAM pywbemtools-pr755-replace-pydicti-nocasedict.patch -- replace pydicti by nocasedict gh#pywbem/pywbemtools#755
Patch1:         pywbemtools-pr755-replace-pydicti-nocasedict.patch
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML >= 5.1
Requires:       python-asciitree >= 0.3.3
Requires:       python-click
Requires:       python-click-repl >= 0.1.6
Requires:       python-click-spinner >= 0.1.8
Requires:       python-mock >= 3.0.0
Requires:       python-nocasedict >= 1.0.1
Requires:       python-nocaselist >= 1.0.3
Requires:       python-packaging >= 17.0
Requires:       python-prompt_toolkit
Requires:       python-pywbem >= 1.1.1
Requires:       python-six >= 1.14.0
Requires:       python-tabulate >= 0.8.2
Requires:       python-yamlloader >= 0.5.5
BuildArch:      noarch
%if !%{with test}
BuildRequires:  %{python_module setuptools}
%else
BuildRequires:  %{python_module pytest}
# tests require entrypoint in standard path
BuildRequires:  %{python_module pywbemtools = %{version}}
%endif
%python_subpackages

%description
Pywbemtools is a collection of command line tools that communicate with WBEM
servers. The tools are written in pure Python and support Python 2 and Python
3.

At this point, pywbemtools includes a single command line tool named
pywbemcli that uses the python-pywbem package to issue operations to a
WBEM server using the CIM/WBEM standards defined by the DMTF to perform
system management tasks.

%prep
%autosetup -p1 -n pywbemtools-%{version}

%if !%{with test}
%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pywbemcli
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%else
%check
%pytest -v -x tests/unit
%endif

%if !%{with test}
%post
%python_install_alternative pywbemcli

%postun
%python_uninstall_alternative pywbemcli

%files %{python_files}
%python_alternative %{_bindir}/pywbemcli
%{python_sitelib}/pywbemtools
%{python_sitelib}/pywbemtools-%{version}*info
%endif

%changelog
