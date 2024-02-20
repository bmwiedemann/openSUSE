#
# spec file for package python-pyaes
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


Name:           python-pyaes
Version:        1.6.1
Release:        0
Summary:        Pure-Python Implementation of the AES block-cipher
License:        MIT
URL:            https://github.com/ricmoo/pyaes/
Source:         https://files.pythonhosted.org/packages/source/p/pyaes/pyaes-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pycryptodome}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pycryptodome
BuildArch:      noarch
%python_subpackages

%description
A pure-Python implementation of the AES (FIPS-197) block-cipher algorithm
and common modes of operation (CBC, CFB, CTR, ECB, OFB) with no dependencies
beyond standard Python libraries. See README.md for API reference and details.

%prep
%setup -q -n pyaes-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand for test in tests/*.py; do PYTHONPATH=%{buildroot}%{$python_sitelib} $python $test; done | tee output.log
if grep -q passed=False output.log; then
  false
fi

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/pyaes
%{python_sitelib}/pyaes-%{version}.dist-info

%changelog
