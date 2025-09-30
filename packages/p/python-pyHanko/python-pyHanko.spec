#
# spec file for package python-pyHanko
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Version:        0.31.0
Release:        0
Summary:        Tools for stamping and signing PDF files
License:        MIT
URL:            https://github.com/MatthiasValvekens/pyHanko
Source:         https://github.com/MatthiasValvekens/pyHanko/archive/refs/tags/v%{version}.tar.gz#/pyhanko-%{version}.tar.gz
BuildRequires:  %{python_module FontTools >= 4.33.3}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module PyYAML >= 6.0}
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module asn1crypto >= 1.5.1}
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module certomancer}
BuildRequires:  %{python_module click >= 8.1.3}
BuildRequires:  %{python_module cryptography >= 43.0.3}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module lxml >= 5.4}
BuildRequires:  %{python_module oscrypto >= 1.1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module platformdirs >= 4.3.8}
BuildRequires:  %{python_module pytest-aiohttp}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-barcode}
BuildRequires:  %{python_module python-pkcs11}
BuildRequires:  %{python_module qrcode}
BuildRequires:  %{python_module requests >= 2.31}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module signxml >= 4.2}
BuildRequires:  %{python_module tzlocal >= 4.3}
BuildRequires:  %{python_module uharfbuzz >= 0.25}
BuildRequires:  %{python_module uritools >= 3.0.1}
BuildRequires:  %{python_module xsdata >= 24.4}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML >= 6.0
Requires:       python-asn1crypto >= 1.5.1
Requires:       python-click >= 8.1.3
Requires:       python-cryptography >= 43.0.3
Requires:       python-lxml >= 5.4
Requires:       python-oscrypto >= 1.1
Requires:       python-platformdirs >= 4.3.8
Requires:       python-requests >= 2.31
Requires:       python-tzlocal >= 4.3
Requires:       python-uritools >= 3.0.1
Suggests:       python-FontTools >= 4.33.3
Suggests:       python-uharfbuzz >= 0.25
Suggests:       python-qrcode >= 7.3.1
Suggests:       python-Pillow >= 7.2
Suggests:       python-python-barcode
Suggests:       python-python-pkcs11 >= 0.9
Suggests:       python-aiohttp
Suggests:       python-xsdata >= 24.4
Suggests:       python-signxml >= 4.2
Obsoletes:      python-pyhanko-certvalidator < %{version}
Provides:       python-pyhanko-certvalidator = %{version}
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
The lack of open-source CLI tooling to handle digitally signing and stamping PDF files was bothering me, so I went ahead and rolled my own.

%prep
%autosetup -p1 -n pyHanko-%{version}

%build
for pkg in pkgs/* ; do
pushd $pkg
# Hardcoded versions
sed -i 's/0.0.0.dev1/%{version}/' pyproject.toml
%pyproject_wheel
popd
done

%install
for pkg in pkgs/* ; do
pushd $pkg
%pyproject_install
popd
done
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/pyhanko

%check
export PYTHONPATH=$(pwd)/internal/common-test-utils/src
pushd pkgs/pyhanko-certvalidator
%pytest
popd
pushd pkgs/pyhanko-cli
%pytest
popd
pushd pkgs/pyhanko
# Tests that are skipped or ignored require modules that are not shipped
%pytest --ignore tests/test_csc.py -k 'not (test_pades or test_ts_fetch or test_simple_text_stamp_on_page_with_leaky_graphics_state)'
popd

%post
%python_install_alternative pyhanko

%postun
%python_uninstall_alternative pyhanko

%files %{python_files}
%doc pkgs/pyhanko/README.md
%license pkgs/pyhanko/LICENSE
%python_alternative %{_bindir}/pyhanko
%{python_sitelib}/pyhanko
%{python_sitelib}/pyhanko_certvalidator
%{python_sitelib}/pyhanko-%{version}.dist-info
%{python_sitelib}/pyhanko_certvalidator-%{version}.dist-info
%{python_sitelib}/pyhanko_cli-%{version}.dist-info

%changelog
