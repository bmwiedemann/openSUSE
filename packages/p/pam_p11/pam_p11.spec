#
# spec file for package pam_p11
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


Name:           pam_p11
Version:        0.3.0
Release:        0
Summary:        PAM Authentication Module for Using Cryptographic Tokens
License:        LGPL-2.1-or-later
Group:          Hardware/Other
URL:            https://github.com/OpenSC/pam_p11
Source0:        https://github.com/OpenSC/pam_p11/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
# PATCH-FIX-UPSTREAM -- Fix build with LTO, picked from upstream
Patch0:         pam_p11-0.3.0-lto-type-mismatch.patch
BuildRequires:  libp11-devel
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel

%description
Pam_p11 is a pluggable authentication module (pam) package for using
cryptographic tokens, such as smart cards and usb crypto tokens, for
authentication.

Pam_p11 has limited functionality since it simply compares public
keys to sign some random data and verifies the signature with the
public key. This works fine for small installations but may have
security implications, see README.SUSE.

%prep
%setup -q
%patch0 -p1

%build
%configure\
	--libdir=/%{_lib} \
	--disable-static \
	--docdir=%{_docdir}/%{name}

make %{?_smp_mflags}

%install
%make_install
# remove .la files
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name} %{name}.mo

%files -f %{name}.mo
%license COPYING
%doc README.md NEWS
/%{_lib}/security/*.so

%changelog
