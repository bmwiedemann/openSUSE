#
# spec file for package python-pywbem
#
# Copyright (c) 2019 SUSE LLC
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

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-pywbem
Version:        0.17.2
Release:        0
Summary:        Python module for making CIM operation calls using the WBEM protocol
License:        LGPL-2.1-or-later
Group:          System/Management
URL:            https://pywbem.github.io/
Source0:        https://github.com/pywbem/pywbem/archive/%{version}.tar.gz#/pywbem-%{version}.tar.gz
BuildRequires:  %{python_module FormEncode}
BuildRequires:  %{python_module M2Crypto}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module httpretty}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module ply}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools} >= 38.4.1
BuildRequires:  %{python_module six} >= 0.12.0
BuildRequires:  %{python_module testfixtures}
BuildRequires:  %{python_module yamlloader}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# For xmllint
BuildRequires:  libxml2-tools
Requires:       python
Requires:       python-M2Crypto
Requires:       python-PyYAML
Requires:       python-pbr
Requires:       python-ply
Requires:       python-six
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%ifpython2
Provides:       pywbem = %{version}
%endif
%python_subpackages

%description
PyWBEM is a Python module for making CIM operation calls using the WBEM
protocol to query and update managed objects.

%prep
%setup -q -n pywbem-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%fdupes %{buildroot}
# don't clash with sblim-wbemcli
mv %{buildroot}%{_bindir}/wbemcli %{buildroot}%{_bindir}/pywbemcli
rm %{buildroot}%{_bindir}/*.bat
%python_clone -a %{buildroot}%{_bindir}/pywbemcli
%python_clone -a %{buildroot}%{_bindir}/wbemcli.py
%python_clone -a %{buildroot}%{_bindir}/mof_compiler

%check
# gh#pywbem/pywbem#2004 for -k
%{python_expand PYTHONPATH=$PYTHONPATH:%{buildroot}%{$python_sitelib} \
py.test-%{$python_bin_suffix} --ignore=_build.python2 --ignore=_build.python3 --ignore=_build.pypy3 -v \
    --cov pywbem --cov pywbem_mock  --cov-config coveragerc \
    -W default -W ignore::PendingDeprecationWarning -W ignore::ResourceWarning \
    -k 'not test_wbemcli' \
    tests/unittest tests/functiontest -s
}

%post
%python_install_alternative pywbemcli
%python_install_alternative wbemcli.py
%python_install_alternative mof_compiler

%postun
%python_uninstall_alternative pywbemcli
%python_uninstall_alternative wbemcli.py
%python_uninstall_alternative mof_compiler

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%python_alternative %{_bindir}/pywbemcli
%python_alternative %{_bindir}/wbemcli.py
%python_alternative %{_bindir}/mof_compiler
%{python_sitelib}/*

%changelog
