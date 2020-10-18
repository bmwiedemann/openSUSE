#
# spec file for package pam_u2f
#
# Copyright (c) 2020 SUSE LLC
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


Name:           pam_u2f
Version:        1.1.0
Release:        0
Summary:        U2F authentication integration into PAM
License:        BSD-2-Clause
Group:          Productivity/Networking/Security
URL:            https://developers.yubico.com
Source0:        https://developers.yubico.com/pam-u2f/Releases/%{name}-%{version}.tar.gz
Source1:        https://developers.yubico.com/pam-u2f/Releases/%{name}-%{version}.tar.gz.sig
Source2:        baselib.conf
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libfido2)

%description
The PAM U2F module provides a way to integrate the Yubikey
(or other U2F-compliant authenticators) into the existing user
authentication infrastructure.

%prep
%setup -q

%build
%configure --with-pam-dir=/%{_lib}/security \
           --disable-static
make %{?_smp_mflags}

%install
%make_install %{?_smp_mflags}

find %{buildroot} -type f -name "*.la" -delete -print

%files
%license COPYING
%doc AUTHORS NEWS ChangeLog README
%{_bindir}/pamu2fcfg
%{_mandir}/man?/*
/%{_lib}/security/pam_u2f.so

%changelog
