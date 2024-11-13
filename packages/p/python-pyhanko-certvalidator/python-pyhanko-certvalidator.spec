#
# spec file for package python-pyhanko-certvalidator
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-pyhanko-certvalidator
Version:        0.26.4
Release:        0
Summary:        Validates X509 certificates and paths
License:        MIT
URL:            https://github.com/MatthiasValvekens/certvalidator
Source:         https://github.com/MatthiasValvekens/certvalidator/archive/refs/tags/v%{version}.tar.gz#/pyhanko-certvalidator-%{version}.tar.gz
Patch0:         https://github.com/MatthiasValvekens/certvalidator/commit/5dd5ff95b7b104667eb4f39367eb4f4c00fcedd5.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 67.4}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module asn1crypto >= 1.5.1}
BuildRequires:  %{python_module aiohttp >= 3.8}
BuildRequires:  %{python_module cryptography >= 41.0.5}
BuildRequires:  %{python_module freezegun >= 1.1.0}
BuildRequires:  %{python_module oscrypto >= 1.1.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.31.0}
BuildRequires:  %{python_module uritools >= 3.0.1}
# /SECTION
BuildRequires:  fdupes
Requires:       python-asn1crypto >= 1.5.1
Requires:       python-cryptography >= 41.0.5
Requires:       python-oscrypto >= 1.1.0
Requires:       python-requests >= 2.31.0
Requires:       python-uritools >= 3.0.1
Suggests:       python-aiohttp >= 3.8
Suggests:       python-freezegun >= 1.1.0
Suggests:       python-aiohttp >= 3.8
BuildArch:      noarch
%python_subpackages

%description
Validates X.509 certificates and paths; forked from wbond/certvalidator

%prep
%autosetup -p1 -n certvalidator-%{version}

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
