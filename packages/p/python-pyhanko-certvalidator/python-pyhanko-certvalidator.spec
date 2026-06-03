#
# spec file for package python-pyhanko-certvalidator
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%{?sle15_python_module_pythons}
Name:           python-pyhanko-certvalidator
Version:        0.31.1
Release:        0
Summary:        Validates X509 certificates and paths
License:        MIT
URL:            https://github.com/MatthiasValvekens/pyHanko
Source:         https://files.pythonhosted.org/packages/source/p/pyhanko_certvalidator/pyhanko_certvalidator-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 80.8.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module asn1crypto >= 1.5.1}
BuildRequires:  %{python_module aiohttp >= 3.9}
BuildRequires:  %{python_module certifi >= 2023.5.7}
BuildRequires:  %{python_module cryptography >= 48.0.0}
BuildRequires:  %{python_module freezegun >= 1.1.0}
BuildRequires:  %{python_module oscrypto >= 1.1.0}
BuildRequires:  %{python_module pytest-aiohttp >= 1.0.4}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.31.0}
BuildRequires:  %{python_module uritools >= 3.0.1}
# /SECTION
BuildRequires:  fdupes
Requires:       python-asn1crypto >= 1.5.1
Requires:       python-cryptography >= 48.0.0
Requires:       python-oscrypto >= 1.1.0
Requires:       python-requests >= 2.31.0
Requires:       python-uritools >= 3.0.1
Suggests:       python-aiohttp >= 3.9
Suggests:       python-certifi >= 2023.5.7
Suggests:       python-freezegun >= 1.1.0
# Used to be shipped by pyHanko package
Conflicts:      python-pyHanko <= 0.34.1
BuildArch:      noarch
%python_subpackages

%description
Validates X.509 certificates and paths; forked from wbond/certvalidator

%prep
%autosetup -p1 -n pyhanko_certvalidator-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/pyhanko_certvalidator
%{python_sitelib}/pyhanko_certvalidator-%{version}.dist-info

%changelog
