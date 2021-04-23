#
# spec file for package pam_yubico
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           pam_yubico
Version:        2.26
Release:        0
Summary:        Yubico Pluggable Authentication Module (PAM)
License:        BSD-2-Clause
Group:          Productivity/Networking/Security
Url:            https://developers.yubico.com/yubico-pam/
Source:         https://developers.yubico.com/yubico-pam/Releases/pam_yubico-%{version}.tar.gz
Source1:        https://developers.yubico.com/yubico-pam/Releases/pam_yubico-%{version}.tar.gz.sig
Source2:        baselib.conf
BuildRequires:  libykclient-devel >= 2.15
BuildRequires:  libyubikey-devel
BuildRequires:  openldap2-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ykpers-1) >= 1.11

%description

This module allows you to use the Yubikey device to authenticate to the PAM system.

%prep
%setup -q

%build
%configure --bindir=%{_bindir} --with-pam-dir=/%{_lib}/security --disable-static --disable-silent-rules
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%files
%license COPYING*
%doc README AUTHORS NEWS doc/*
%{_bindir}/ykpamcfg
/%{_lib}/security/pam_yubico.so
%{_mandir}/man1/ykpamcfg.1*
%{_mandir}/man8/pam_yubico.8*

%changelog
