#
# spec file for package pam_yubico
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

%{!?_pam_moduledir: %define _pam_moduledir /%{_lib}/security}

Name:           pam_yubico
Version:        2.27
Release:        0
Summary:        Yubico Pluggable Authentication Module (PAM)
License:        BSD-2-Clause
Group:          Productivity/Networking/Security
URL:            https://developers.yubico.com/yubico-pam/
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

The Yubico PAM module provides an easy way to integrate the YubiKey into your
existing user authentication infrastructure. PAM is used by GNU/Linux, Solaris
and Mac OS X for user authentication, and by other specialized applications
such as NCSA MyProxy.

%prep
%setup -q

%build
%configure --bindir=%{_bindir} --with-pam-dir=%{_pam_moduledir} --disable-static --disable-silent-rules
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%files
%license COPYING*
%doc README AUTHORS NEWS doc/*
%{_bindir}/ykpamcfg
%{_pam_moduledir}/pam_yubico.so
%{_mandir}/man1/ykpamcfg.1*
%{_mandir}/man8/pam_yubico.8*

%changelog
