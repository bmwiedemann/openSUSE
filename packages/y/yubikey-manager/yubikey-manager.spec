#
# spec file for package yubikey-manager
#
# Copyright (c) 2022 SUSE LLC
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


Name:           yubikey-manager
Version:        4.0.9
Release:        0
Summary:        Python 3 library and command line tool for configuring a YubiKey
License:        BSD-2-Clause
Group:          Productivity/Security
URL:            https://developers.yubico.com/yubikey-manager/Releases
Source0:        https://developers.yubico.com/yubikey-manager/Releases/%{name}-%{version}.tar.gz
Source1:        https://developers.yubico.com/yubikey-manager/Releases/%{name}-%{version}.tar.gz.sig
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python3-click
BuildRequires:  python3-cryptography >= 3.0
BuildRequires:  python3-fido2 >= 0.9
BuildRequires:  python3-pip
BuildRequires:  python3-pyscard
BuildRequires:  python3-setuptools
# TEST DEPENDENCIES
BuildRequires:  python3-pyOpenSSL
BuildRequires:  python3-makefun >= 1.9.5
BuildRequires:  python3-pytest
%if 0%{?suse_version} <= 1540
# dataclasses is required for tests if python < 3.7
BuildRequires:  python3-dataclasses >= 0.8
Requires:       python3-dataclasses >= 0.8
%endif
Requires:       python3-click
Requires:       python3-cryptography
Requires:       python3-fido2 >= 0.9
Requires:       python3-pyscard
Recommends:     python3-pyOpenSSL
Provides:       python3-yubikey-manager
BuildArch:      noarch

%description
Python 3 library and command line tool for configuring a YubiKey.
YubiKey Manager (ykman) is a command line tool for configuring a YubiKey over
all transports. It is capable of reading out device information as well as
configuring several aspects of a YubiKey, including enabling or disabling
connection transports an programming various types of credentials.

%prep
%autosetup -p1

%build
%python3_build

%install
%python3_install
%fdupes %{buildroot}
install -Dpm0644 man/ykman.1 %{buildroot}%{_mandir}/man1/ykman.1

%check
python3 -m pytest

%files
%license COPYING*
%doc NEWS*
%{_bindir}/ykman
%{python3_sitelib}/ykman
%{python3_sitelib}/yubikey_manager-*.egg-info
%{python3_sitelib}/yubikit
%{_mandir}/man1/*

%changelog
