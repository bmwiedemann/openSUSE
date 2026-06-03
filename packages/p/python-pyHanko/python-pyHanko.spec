#
# spec file for package python-pyHanko
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
Name:           python-pyHanko
Version:        0.35.1
Release:        0
Summary:        Tools for stamping and signing PDF files
License:        MIT
URL:            https://github.com/MatthiasValvekens/pyHanko
Source:         https://files.pythonhosted.org/packages/source/p/pyhanko/pyhanko-%{version}.tar.gz
BuildRequires:  %{python_module FontTools >= 4.33.3}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module PyYAML >= 6.0}
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module asn1crypto >= 1.5.1}
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module certomancer}
BuildRequires:  %{python_module cryptography >= 43.0.3}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module lxml >= 5.4}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyhanko-certvalidator}
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
BuildRequires:  softhsm
Requires:       python-PyYAML >= 6.0
Requires:       python-asn1crypto >= 1.5.1
Requires:       python-cryptography >= 43.0.3
Requires:       python-lxml >= 5.4
Requires:       python-pyhanko-certvalidator
Requires:       python-requests >= 2.31
Requires:       python-tzlocal >= 4.3
Suggests:       python-xsdata >= 24.4
Suggests:       python-FontTools >= 4.33.3
Suggests:       python-uharfbuzz >= 0.25
Suggests:       python-qrcode >= 7.3.1
Suggests:       python-Pillow >= 7.2
Suggests:       python-python-barcode
Suggests:       python-python-pkcs11 >= 0.9
Suggests:       python-aiohttp
Suggests:       python-signxml >= 4.2
# Also provide lowercase name
Provides:       python-pyhanko = %{version}-%{release}
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
The lack of open-source CLI tooling to handle digitally signing and stamping PDF files was bothering me, so I went ahead and rolled my own.

%prep
%autosetup -p1 -n pyhanko-%{version}
# We need to run this before the tests, and we don't want to use uv
sed -i '/uv run /d' pyhanko_testing_commons/test_data/data/crypto/testing-ca-setup/pkcs11-setup-certomancer.sh

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# intial softhsm configuration
export SOFTHSM2_CONF=/tmp/softhsm.conf
mkdir softhsm_tokens
echo "directories.tokendir = $(pwd)/softhsm_tokens" > $SOFTHSM2_CONF
export CERTOMANCER_CONFIG_PATH="pyhanko_testing_commons/test_data/data/crypto/certomancer.yml"
export SOFTHSM2_MODULE_PATH=$(softhsm2-util --show-config default-pkcs11-lib)
export PKCS11_TEST_MODULE=$SOFTHSM2_MODULE_PATH
PYTHONPATH=%{buildroot}%{python3_sitelib} ./pyhanko_testing_commons/test_data/data/crypto/testing-ca-setup/pkcs11-setup-certomancer.sh
# Tests that are skipped or ignored require modules that are not shipped
donttest=""
if [ $(getconf LONG_BIT) -eq 32 ]; then
    donttest="not test_pades"
fi
%pytest --ignore tests/test_csc.py -k "$donttest"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/pyhanko
%{python_sitelib}/pyhanko-%{version}.dist-info

%changelog
