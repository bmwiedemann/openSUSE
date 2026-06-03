#
# spec file for package python-pyhanko-cli
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


Name:           python-pyhanko-cli
Version:        0.4.0
Release:        0
Summary:        CLI tools for stamping and signing PDF files
License:        MIT
URL:            https://github.com/MatthiasValvekens/pyHanko
Source:         https://files.pythonhosted.org/packages/source/p/pyhanko-cli/pyhanko_cli-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 80.8.0}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module FontTools >= 4.33.3}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module asn1crypto >= 1.5.1}
BuildRequires:  %{python_module certifi >= 2023.5.7}
BuildRequires:  %{python_module certomancer}
BuildRequires:  %{python_module click >= 8.1.3}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module platformdirs >= 4.3.8}
BuildRequires:  %{python_module pyhanko >= 0.35.0}
BuildRequires:  %{python_module pyhanko-certvalidator >= 0.31.0}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-barcode}
BuildRequires:  %{python_module python-pkcs11}
BuildRequires:  %{python_module qrcode}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module signxml >= 4.2}
BuildRequires:  %{python_module tzlocal >= 4.3}
BuildRequires:  %{python_module uharfbuzz >= 0.25}
BuildRequires:  %{python_module xsdata >= 24.4}
# /SECTION
BuildRequires:  fdupes
Requires:       python-asn1crypto >= 1.5.1
Requires:       python-certifi >= 2023.5.7
Requires:       python-click >= 8.1.3
Requires:       python-platformdirs >= 4.3.8
Requires:       python-pyhanko >= 0.35.0
Requires:       python-pyhanko-certvalidator >= 0.31.0
Requires:       python-tzlocal >= 4.3
# Used to be shipped by pyHanko package
Conflicts:      python-pyHanko <= 0.34.1
BuildArch:      noarch
%python_subpackages

%description
CLI tools for stamping and signing PDF files

%prep
%autosetup -p1 -n pyhanko_cli-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pyhanko
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative pyhanko

%postun
%python_uninstall_alternative pyhanko

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/pyhanko
%{python_sitelib}/pyhanko/__main__.py
%dir %{python_sitelib}/pyhanko/__pycache__
%pycache_only %{python_sitelib}/pyhanko/__pycache__/__main__.*.pyc
%{python_sitelib}/pyhanko/cli
%{python_sitelib}/pyhanko_cli-%{version}.dist-info

%changelog
