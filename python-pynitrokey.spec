#
# spec file for package python-pynitrokey
#
# Copyright (c) 2023 SUSE LLC
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

# only build for the default python on Tumbleweed
# and for the new python stack on SLES15/Leap15
%if 0%{suse_version} < 1699
%{?sle15_python_module_pythons}
%else
%define pythons python3
%endif

Name:           python-pynitrokey
Version:        0.4.36
Release:        0
Summary:        Python Library for Nitrokey devices
License:        MIT
URL:            https://github.com/Nitrokey/pynitrokey
Source:         https://files.pythonhosted.org/packages/source/p/pynitrokey/pynitrokey-%{version}.tar.gz
BuildRequires:  %{python_module flit}
BuildRequires:  %{python_module pip}
# https://github.com/Nitrokey/pynitrokey/blob/master/pyproject.toml
BuildRequires:  %{python_module certifi >= 14.5.14}
BuildRequires:  %{python_module click >= 8.0.0 with %python-click < 9}
BuildRequires:  %{python_module cffi}
# "cryptography >=3.4.4,<37"
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module deepmerge >= 1.1.0}
BuildRequires:  %{python_module ecdsa}
# "frozendict ~= 2.3.4"
BuildRequires:  %{python_module frozendict >= 2.3.4}
# "fido2 >=1.1.0,<2"
BuildRequires:  %{python_module fido2 >= 1.1.0 with %python-fido2 < 2}
BuildRequires:  %{python_module nkdfu}
#"python-dateutil ~= 2.7.0"
BuildRequires:  %{python_module python-dateutil >= 2.7.0}
BuildRequires:  %{python_module pyusb}
BuildRequires:  %{python_module requests}
# "spsdk >=1.7.0,<1.8.0"
BuildRequires:  %{python_module spsdk >= 1.7.0}
BuildRequires:  %{python_module tqdm}
# "urllib3 ~= 1.26.7"
BuildRequires:  %{python_module urllib3 >= 1.26.7}
BuildRequires:  %{python_module tlv8}
# "typing_extensions ~= 4.3.0"
BuildRequires:  %{python_module typing_extensions >= 4.3.0}
BuildRequires:  %{python_module pyserial}
# "protobuf >=3.17.3, < 4.0.0"
BuildRequires:  %{python_module protobuf >= 3.17.3}
BuildRequires:  intelhex
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test
BuildRequires:  %{python_module pytest}
# /SECTION
Requires:       intelhex
Requires:       python-certifi >= 14.5.14
Requires:       python-cffi
Requires:       (python-click >= 8.0.0 with python-click < 9)
Requires:       python-cryptography
Requires:       python-deepmerge >= 1.1.0
Requires:       python-ecdsa
Requires:       python-frozendict >= 2.3.4
Requires:       (python-fido2 >= 1.1.0 with python-fido2 < 2)
Requires:       python-nkdfu
Requires:       python-python-dateutil >= 2.7.0
Requires:       python-pyusb
Requires:       python-requests
Requires:       python-spsdk >= 1.7.0
Requires:       python-tqdm
Requires:       python-urllib3 >= 1.26.7
Requires:       python-tlv8
Requires:       python-typing_extensions >= 4.3.0
Requires:       python-pyserial
Requires:       python-protobuf >= 3.17.3
Requires(post): update-alternatives
Requires(postun): update-alternatives
# only build for x86_64, as some dependencies are not available
# for other architectures
ExclusiveArch:  x86_64
Provides:       nitropy = %{version}-%{release}
%python_subpackages

%description
# nitropy

A command line interface for the Nitrokey FIDO2, Nitrokey Start, Nitrokey 3 and NetHSM.

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
%setup -q -n pynitrokey-%{version}

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
%license LICENSE-MIT
%{python_sitelib}/pynitrokey/
%{python_sitelib}/pynitrokey-%{version}*-info
%python_alternative %{_bindir}/nitropy

%changelog
