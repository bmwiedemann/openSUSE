#
# spec file for package python-josepy
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


%define libname josepy
%{?sle15_python_module_pythons}
Name:           python-%{libname}
Version:        1.15.0
Release:        0
Summary:        JOSE protocol implementation in Python
License:        Apache-2.0
URL:            https://github.com/certbot/josepy
Source0:        https://files.pythonhosted.org/packages/source/j/%{libname}/%{libname}-%{version}.tar.gz
Source2:        %{name}.keyring
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module coverage >= 4.0}
BuildRequires:  %{python_module cryptography >= 1.5}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry >= 1.0.8}
BuildRequires:  %{python_module pyOpenSSL >= 0.13}
BuildRequires:  %{python_module pytest >= 2.8.0}
BuildRequires:  %{python_module setuptools >= 1.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cryptography >= 1.5
Requires:       python-pyOpenSSL >= 0.13
Conflicts:      python-acme < 0.21.0
Obsoletes:      python-%{libname}-doc
BuildArch:      noarch
%python_subpackages

%description
JOSE protocol implementation in Python using cryptography.
It is used by the certbot project. Formerly Let's Encrypt project.

%prep
%autosetup -p1 -n %{libname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
# remove test-data
%python_expand rm -rf %{buildroot}%{$python_sitelib}/%{libname}/testdata
%python_expand rm -rf %{buildroot}%{$python_sitelib}/%{libname}/*_test.py*
%python_expand rm -rf %{buildroot}%{$python_sitelib}/%{libname}/**/*_test.py*
%python_expand rm -rf %{buildroot}%{$python_sitelib}/%{libname}/__pycache__/*_test*
# remove duplicates
%python_expand %fdupes %{buildroot}%{$python_sitelib}/%{libname}
# remove docfiles
%python_expand rm -rf %{buildroot}%{$python_sitelib}/CHANGELOG.rst
%python_expand rm -rf %{buildroot}%{$python_sitelib}/CONTRIBUTING.md

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%doc CHANGELOG.rst CONTRIBUTING.md
%{python_sitelib}/%{libname}
%{python_sitelib}/%{libname}-%{version}.dist-info
%pycache_only %{python_sitelib}/%{libname}/__pycache__
# following the certbot-packaging guide, "jws" should not be packaged
%exclude %{_bindir}/jws

%changelog
