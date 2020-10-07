#
# spec file for package python-acme
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
%define libname acme
Name:           python-%{libname}
Version:        1.9.0
Release:        0
Summary:        Python library for the ACME protocol
License:        Apache-2.0
URL:            https://github.com/certbot/certbot
Source0:        https://files.pythonhosted.org/packages/source/a/%{libname}/%{libname}-%{version}.tar.gz
Source1:        https://files.pythonhosted.org/packages/source/a/%{libname}/%{libname}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
BuildRequires:  %{python_module cryptography >= 1.2.3}
BuildRequires:  %{python_module josepy >= 1.1.0}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pyOpenSSL >= 0.15.1}
BuildRequires:  %{python_module pyRFC3339}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module requests >= 2.6.0}
BuildRequires:  %{python_module requests-toolbelt >= 0.3.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.9.0}
BuildRequires:  %{python_module tox}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cryptography >= 1.2.3
Requires:       python-josepy >= 1.1.0
Requires:       python-pyOpenSSL >= 0.15.1
Requires:       python-pyRFC3339
Requires:       python-pytz
Requires:       python-requests >= 2.6.0
Requires:       python-requests-toolbelt >= 0.3.0
Requires:       python-six >= 1.9.0
%ifpython2
Requires:       python-mock
%endif
BuildArch:      noarch
%if %{?suse_version} < 1500
BuildRequires:  %{python_module devel}
%endif
%python_subpackages

%description
Python library implementing the Automatic Certificate Management Environment
(ACME) protocol. It is used by the certbot project. Formerly Let's Encrypt project.

%prep
%setup -q -n %{libname}-%{version}

%build
%python_build

%install
%python_install
# remove duplicates
%python_expand %fdupes %{buildroot}%{$python_sitelib}/%{libname}

%check
%pytest tests/

%files %{python_files}
%license LICENSE.txt
%{python_sitelib}/%{libname}
%{python_sitelib}/%{libname}-%{version}*.egg-info
%pycache_only %{python_sitelib}/%{libname}/__pycache__

%changelog
