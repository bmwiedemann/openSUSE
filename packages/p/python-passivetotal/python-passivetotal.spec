#
# spec file for package python-passivetotal
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
%bcond_without test
Name:           python-passivetotal
Version:        1.0.31
Release:        0
Summary:        Client for the PassiveTotal REST API
License:        GPL-2.0-only
Group:          Development/Languages/Python
Url:            https://passivetotal.readthedocs.org
Source:         https://files.pythonhosted.org/packages/source/p/passivetotal/passivetotal-%{version}.tar.gz
Source1:        https://github.com/passivetotal/python_api/raw/c2d0c8f4ea3dde4caec01f5401fb6f105f8a2447/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module ez_setup}
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module requests}
%endif
BuildRequires:  fdupes
Requires:       python-ez_setup
Requires:       python-future
Requires:       python-python-dateutil
Requires:       python-requests
BuildArch:      noarch

%python_subpackages

%description
Passivetotal provides a Python client library implementation into RiskIQ API
services. The library currently provides support for the following services:

- Passive DNS queries and filters
- WHOIS queries (search and details)
- SSL Certificates (search and details)
- Account configuration
- Site actions (tagging, classifying, etc.)

%prep
%setup -q -n passivetotal-%{version}
sed -i '1s/^#!.*//' passivetotal/*.py passivetotal/*/*.py
cp %{S:1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%python3_only %{_bindir}/pt-info
%python3_only %{_bindir}/pt-config
%python3_only %{_bindir}/pt-client
%{python_sitelib}/*

%changelog
