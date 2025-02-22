#
# spec file for package python-pyHanko
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


%{?sle15_python_module_pythons}
Name:           python-pyHanko
Version:        0.25.3
Release:        0
Summary:        Tools for stamping and signing PDF files
License:        MIT
URL:            https://github.com/MatthiasValvekens/pyHanko
Source:         https://github.com/MatthiasValvekens/pyHanko/archive/refs/tags/v%{version}.tar.gz#/pyhanko-%{version}.tar.gz
BuildRequires:  %{python_module FontTools}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module certomancer}
BuildRequires:  %{python_module defusedxml}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyhanko-certvalidator}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-barcode}
BuildRequires:  %{python_module qrcode}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module tzlocal}
BuildRequires:  %{python_module uharfbuzz}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-asn1crypto
Requires:       python-click
Requires:       python-cryptography
Requires:       python-pyhanko-certvalidator
Requires:       python-qrcode
Requires:       python-requests
Requires:       python-tzlocal
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
The lack of open-source CLI tooling to handle digitally signing and stamping PDF files was bothering me, so I went ahead and rolled my own.

%prep
%autosetup -p1 -n pyHanko-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/pyhanko

%check
# Tests that are skipped or ignored require modules that are not shipped
%pytest --ignore pyhanko_tests/test_csc.py --ignore pyhanko_tests/test_pkcs11.py -k 'not (test_pades or test_ts_fetch)'

%post
%python_install_alternative pyhanko

%postun
%python_uninstall_alternative pyhanko

%files %{python_files}
%python_alternative %{_bindir}/pyhanko
%{python_sitelib}/pyhanko
%{python_sitelib}/pyHanko-%{version}.dist-info

%changelog
