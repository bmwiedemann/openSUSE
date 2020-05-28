#
# spec file for package python-pypiserver
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_without python2
Name:           python-pypiserver
Version:        1.3.2
Release:        0
Summary:        Minimal PyPI server for uploading & downloading packages with pip/easy_install
License:        MIT
URL:            https://github.com/pypiserver
Source:         https://github.com/pypiserver/pypiserver/archive/v%{version}.tar.gz#/pypiserver-%{version}.tar.gz
BuildRequires:  %{python_module WebTest}
BuildRequires:  %{python_module passlib >= 1.6}
BuildRequires:  %{python_module pip >= 7}
BuildRequires:  %{python_module pytest >= 3.5}
BuildRequires:  %{python_module setuptools-git >= 0.3}
BuildRequires:  %{python_module setuptools_scm >= 1.15.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tox}
BuildRequires:  %{python_module twine}
BuildRequires:  %{python_module wheel >= 0.25.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-passlib >= 1.6
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%if %{with python2}
BuildRequires:  python-mock
%endif
%python_subpackages

%description
Minimal PyPI server for uploading & downloading packagesj with pip/easy_install

%prep
%setup -q -n pypiserver-%{version}
# we don't need the extensions for smoke testing
rm -f pytest.ini

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pypi-server
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_hash_algos:
# ERROR: No matching distribution found for a==1.0 (from centodeps)
# (see centodeps-setup.py)
%pytest tests -k "not (test_pipInstall_openOk or test_pipInstall_authedOk or test_hash_algos)"

%post
%python_install_alternative pypi-server

%postun
%python_uninstall_alternative pypi-server

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/*
%python_alternative %{_bindir}/pypi-server

%changelog
