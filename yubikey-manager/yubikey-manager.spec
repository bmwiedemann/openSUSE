#
# spec file for package yubikey-manager
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        3.1.0
Release:        0
Summary:        Python 3 library and command line tool for configuring a YubiKey
License:        BSD-2-Clause
Group:          Productivity/Security
URL:            https://developers.yubico.com/yubikey-manager/Releases
Source0:        https://developers.yubico.com/yubikey-manager/Releases/%{name}-%{version}.tar.gz
Source1:        https://developers.yubico.com/yubikey-manager/Releases/%{name}-%{version}.tar.gz.sig
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(ykpers-1)
Requires:       libykpers-1-1
Requires:       python3-click
Requires:       python3-cryptography
Requires:       python3-fido2
Requires:       python3-pyOpenSSL
Requires:       python3-pyscard
Requires:       python3-six
Requires:       python3-usb
Provides:       python3-yubikey-manager
BuildArch:      noarch

%description
Python 3 library and command line tool for configuring a YubiKey.
YubiKey Manager (ykman) is a command line tool for configuring a YubiKey over
all transports. It is capable of reading out device information as well as
configuring several aspects of a YubiKey, including enabling or disabling
connection transports an programming various types of credentials.

%prep
%setup -q

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
%fdupes %{buildroot}
install -Dm0644 man/ykman.1 %{buildroot}/usr/share/man/man1/ykman.1

%files
%license COPYING*
%doc NEWS*
%{_bindir}/ykman
%{python3_sitelib}
%{_mandir}/man1/*

%changelog
