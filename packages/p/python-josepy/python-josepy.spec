#
# spec file for package python-josepy
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
%define libname josepy
Name:           python-%{libname}
Version:        1.2.0
Release:        0
Summary:        JOSE protocol implementation in Python
License:        Apache-2.0
URL:            https://github.com/certbot/josepy
Source0:        https://files.pythonhosted.org/packages/source/j/%{libname}/%{libname}-%{version}.tar.gz
Source1:        https://files.pythonhosted.org/packages/source/j/%{libname}/%{libname}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
BuildRequires:  %{python_module coverage >= 4.0}
BuildRequires:  %{python_module cryptography >= 0.8}
BuildRequires:  %{python_module devel >= 2.7}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pyOpenSSL >= 0.13}
BuildRequires:  %{python_module pytest >= 2.8.0}
BuildRequires:  %{python_module setuptools >= 1.0}
BuildRequires:  %{python_module six >= 1.9.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cryptography >= 0.8
Requires:       python-pyOpenSSL >= 0.13
Requires:       python-six >= 1.9.0
Conflicts:      python-acme < 0.21.0
Obsoletes:      python-%{libname}-doc
BuildArch:      noarch
%python_subpackages

%description
JOSE protocol implementation in Python using cryptography.
It is used by the certbot project. Formerly Let's Encrypt project.

%prep
%setup -q -n %{libname}-%{version}
rm pytest.ini

%build
%python_build

%install
%python_install
# remove test-data
%python_expand rm -rf %{buildroot}%{$python_sitelib}/%{libname}/testdata
%python_expand rm -rf %{buildroot}%{$python_sitelib}/%{libname}/*_test.py*
%python_expand rm -rf %{buildroot}%{$python_sitelib}/%{libname}/**/*_test.py*
%python_expand rm -rf %{buildroot}%{$python_sitelib}/%{libname}/__pycache__/*_test*
# remove duplicates
%python_expand %fdupes %{buildroot}%{$python_sitelib}/%{libname}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} py.test-%{$python_bin_suffix} src/

%files %{python_files}
%license LICENSE.txt
%{python_sitelib}/%{libname}
%{python_sitelib}/%{libname}-%{version}*.egg-info
%pycache_only %{python_sitelib}/%{libname}/__pycache__
# following the certbot-packaging guide, "jws" should not be packaged
%exclude %{_bindir}/jws

%changelog
