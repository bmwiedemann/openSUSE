#
# spec file for package tls
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


Name:           tls
Version:        1.7.22
Release:        0
Summary:        Tcl Binding for the OpenSSL Library
License:        BSD-3-Clause
Group:          Development/Libraries/Tcl
URL:            https://core.tcl-lang.org/tcltls
Source0:        https://core.tcl-lang.org/tcltls/uv/tcltls-%{version}.tar.gz
Patch0:         https://salsa.debian.org/tcltk-team/tcltls/-/raw/master/debian/patches/hostname-tests.patch
Patch1:         https://salsa.debian.org/tcltk-team/tcltls/-/raw/master/debian/patches/cipher-tests.patch
Patch2:         https://salsa.debian.org/tcltk-team/tcltls/-/raw/master/debian/patches/certs-tests.patch
Patch3:         https://salsa.debian.org/tcltk-team/tcltls/-/raw/master/debian/patches/fall-through.patch
Patch4:         https://salsa.debian.org/tcltk-team/tcltls/-/raw/master/debian/patches/openssl3.patch
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(tcl)

%description
This Tcl extension provides a generic binding to OpenSSL, utilizing
the Tcl_StackChannel API for Tcl 8.2 and higher. The sockets behave
exactly the same as channels created using Tcl's built-in socket
command with additional options for controlling the SSL session.

%prep
%autosetup -n tcl%{name}-%{version} -p1

%build
%configure \
	--disable-rpath		\
	--enable-deterministic	\
	--with-ssl-dir=%{_prefix}
%make_build

%install
%make_install libdir=%{_libdir}/tcl

%check
%make_build test

%files
%license license.terms
%doc ChangeLog README.txt tls.htm
%{_libdir}/tcl

%changelog
