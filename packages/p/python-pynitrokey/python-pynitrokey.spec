#
# spec file for package python-pynitrokey
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
Name:           python-pynitrokey
Version:        0.10.0
Release:        0
Summary:        Python Library for Nitrokey devices
License:        Apache-2.0 OR MIT
URL:            https://github.com/Nitrokey/pynitrokey
Source:         https://files.pythonhosted.org/packages/source/p/pynitrokey/pynitrokey-%{version}.tar.gz
Source1:        LICENSE-MIT
Source2:        LICENSE-APACHE
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
#
BuildRequires:  %{python_module cffi}
BuildRequires:  %{python_module click >= 8.2 with %python-click < 9}
BuildRequires:  %{python_module cryptography >= 43 with %python-cryptography < 46}
BuildRequires:  %{python_module fido2 >= 2 with %python-fido2 < 3}
# https://github.com/Nitrokey/pynitrokey/issues/601
BuildRequires:  %{python_module hidapi >= 0.14.0.post1 with %python-hidapi < 0.14.0.post4}
BuildRequires:  %{python_module nethsm >= 1.4.0 with %python-nethsm < 2}
BuildRequires:  %{python_module nitrokey >= 0.4.0 with %python-nitrokey < 0.5}
BuildRequires:  %{python_module nkdfu}
BuildRequires:  %{python_module pyusb}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module semver}
BuildRequires:  %{python_module tlv8}
BuildRequires:  %{python_module tqdm}
BuildRequires:  intelhex
# SECTION test
BuildRequires:  %{python_module pytest}
# /SECTION
Requires:       intelhex
Requires:       python-cffi
Requires:       python-click >= 8.2
Requires:       python-nkdfu
Requires:       python-pyusb
Requires:       python-requests
Requires:       python-semver
Requires:       python-tlv8
Requires:       python-tqdm
Requires:       (python-cryptography >= 43 with python-cryptography < 46)
Requires:       (python-fido2 >= 2 with python-fido2 < 3)
Requires:       (python-hidapi >= 0.14.0.post1 with python-hidapi < 0.14.0.post4)
Requires:       (python-nethsm >= 1.4.0 with python-nethsm < 2)
Requires:       (python-nitrokey >= 0.4.0 with python-nitrokey < 0.5)
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
Provides:       nitropy = %{version}-%{release}
%python_subpackages

%description
# nitropy

A command line interface for the Nitrokey FIDO2, Nitrokey Start, Nitrokey 3 and
NetHSM.

## Quickstart

```
$ nitropy --help
```

## Documentation

The user documentation for the `nitropy` CLI is available on [docs.nitrokey.com](https://docs.nitrokey.com/software/nitropy/index.html). See also the product documentation for more information on the available commands:
- [Nitrokey 3](https://docs.nitrokey.com/nitrokey3/index.html)
- [Nitrokey FIDO2](https://docs.nitrokey.com/fido2/index.html)
- [Nitrokey Start](https://docs.nitrokey.com/start/index.html)
- [NetHSM](https://docs.nitrokey.com/nethsm/index.html)

%prep
%autosetup -p1 -n pynitrokey-%{version}

cp %SOURCE1 .
cp %SOURCE2 .

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/nitropy
# make scripts in start executable
%python_expand find %{buildroot}%{$python_sitelib}/pynitrokey/start/ -type f -name "*.py" -exec sed -i '1 i\#!/usr/bin/python%{$python_version}' {} +
%python_expand find %{buildroot}%{$python_sitelib}/pynitrokey/start/ -type f -name "*.py" -exec chmod 755 {} +
# remove shebangs
%python_expand find %{buildroot}%{$python_sitelib} -iname "*.py" -exec sed -i '1{/env python/d;}' {} +
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
echo "Disabled pytest"

%post
%python_install_alternative nitropy

%postun
%python_uninstall_alternative nitropy

%files %{python_files}
%doc README.md
%license LICENSE-MIT LICENSE-APACHE
%{python_sitelib}/pynitrokey/
%{python_sitelib}/pynitrokey-%{version}*-info
%exclude %{python_sitelib}/pynitrokey/nk_headers/*.h
%python_alternative %{_bindir}/nitropy

%changelog
