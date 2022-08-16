#
# spec file for package python-requests-wsgi-adapter
#
# Copyright (c) 2022 SUSE LLC
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


%define commit 7b33ce210c17bd9707e4b26c2f0ed307424f90b9
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-requests-wsgi-adapter
Version:        0.4.1
Release:        0
Summary:        WSGI Transport Adapter for Requests
License:        BSD-3-Clause
URL:            https://github.com/seanbrant/requests-wsgi-adapter
# no tests in PyPI sdist, no tags on GitHub
Source:         https://github.com/seanbrant/requests-wsgi-adapter/archive/%{commit}.tar.gz#/requests-wsgi-adapter-%{version}.tar.gz
BuildRequires:  %{python_module requests >= 1.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests >= 1.0
BuildArch:      noarch
%python_subpackages

%description
WSGI Transport Adapter for Requests

%prep
%setup -q -n requests-wsgi-adapter-%{commit}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v tests.py

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/wsgiadapter.py*
%pycache_only %{python_sitelib}/__pycache__/wsgiadapter*.pyc
%{python_sitelib}/requests_wsgi_adapter-%{version}*-info

%changelog
