#
# spec file for package python-solo-python
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-solo-python
Version:        0.0.27
Release:        0
Summary:        Library for SoloKeys
License:        Apache-2.0 OR MIT
URL:            https://github.com/solokeys/solo-python
Source:         https://files.pythonhosted.org/packages/source/s/solo-python/solo-python-%{version}.tar.gz
BuildRequires:  python3-click >= 7.0
BuildRequires:  python3-cryptography
BuildRequires:  python3-ecdsa
BuildRequires:  python3-fido2
BuildRequires:  python3-pyserial
BuildRequires:  python3-pyusb
BuildRequires:  python3-requests
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-poetry-core
BuildRequires:  python3-flit
BuildRequires:  intelhex
Requires:       python3-click >= 7.0
Requires:       python3-cryptography
Requires:       python3-ecdsa
Requires:       python3-fido2
Requires:       python3-pyserial
Requires:       python3-pyusb
Requires:       python3-requests
Requires:       intelhex
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%description
Python tool and library for SoloKeys

For help, run `solo --help` after installation. The tool has a
hierarchy of commands and subcommands.

Example:

```bash
solo ls  # lists all Solo keys connected to your machine
solo version  # outputs version of installed `solo` library and tool

solo key wink  # blinks the LED
solo key verify  # checks whether your Solo is genuine
solo key rng hexbytes  # outputs some random hex bytes generated on your key
solo key version  # outputs the version of the firmware on your key
```

- update your `solo` tool if necessary via `pip3 install --upgrade solo-python`
- plug in your key, keeping the button pressed until the LED flashes yellow
- run `solo key update`

%prep
%autosetup -p1 -n solo-python-%{version}

%build
python3 -mpip wheel --no-deps --disable-pip-version-check \
    --use-pep517 --no-build-isolation --progress-bar off --verbose . -w build/

%install
python3 -mpip install --root %{buildroot} --disable-pip-version-check \
    --no-compile --no-warn-script-location --no-deps --progress-bar off \
    build/*.whl
%fdupes %{buildroot}%{python3_sitelib}

%check
# tests are not available

%files
%{_bindir}/solo
%{python3_sitelib}/solo*

%changelog
