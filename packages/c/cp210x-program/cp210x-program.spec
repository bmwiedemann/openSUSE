#
# spec file for package cp210x-program
#
# Copyright (c) 2020, Martin Hauke <mardnh@gmx.de>
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


Name:           cp210x-program
Version:        0.3
Release:        0
Summary:        EEPROM tool for Silabs CP210x USB-Serial adapters
License:        LGPL-2.1-only
Group:          Hardware/Other
URL:            http://cp210x-program.sourceforge.net/
#Git-Clone:     https://github.com/VCTLabs/cp210x-program.git
Source:         https://github.com/VCTLabs/cp210x-program/archive/%{name}-0-3.tar.gz
# PATCH-FIX-UPSTREAM: documentation fixes
Patch0:         0001-docs-fix-example-of-reading-EEPROM.patch
# PATCH-FIX-UPSTREAM: python3 compatibility
Patch1:         https://github.com/VCTLabs/cp210x-program/pull/3.patch
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
BuildRequires:  python3-pyusb
Requires:       python3-pyusb
BuildArch:      noarch

%description
The CP210x is an USB-to-serial chip used in a lot of USB devices (similar to
FTDIs and PL2303). The CP210x has a EEPROM on the chip which can be programmed
with this tool via USB.

%prep
%setup -q -n %{name}-%{name}-0-3/
%patch0 -p1
%patch1 -p1

%build
%python3_build

%install
%python3_install
%fdupes %{buildroot}/%{python3_sitelib}

%check
./test.sh

%files
%license LICENSE
%doc README doc/cp210x.txt
%{_bindir}/cp210x-program
%{python3_sitelib}/cp210x*

%changelog
