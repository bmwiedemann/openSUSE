#
# spec file for package tls
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        2.0
Release:        0
Summary:        Tcl Binding for the OpenSSL Library
License:        BSD-3-Clause
Group:          Development/Libraries/Tcl
URL:            https://core.tcl-lang.org/tcltls
Source0:        https://core.tcl-lang.org/tcltls/uv/tcltls-%{version}-src.tar.gz
%define srcdir tcltls-20260121024900-5d3e3c3bf8
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(tcl)

%description
This Tcl extension provides a generic binding to OpenSSL, utilizing
the Tcl_StackChannel API for Tcl 8.2 and higher. The sockets behave
exactly the same as channels created using Tcl's built-in socket
command with additional options for controlling the SSL session.

%prep
%autosetup -n %srcdir -p1

%build
export TCL_PACKAGE_PATH=%tcl_archdir
%configure \
	--disable-rpath

%make_build

%install
%make_install libdir=%{_libdir}/tcl
# We don't do a devel package (yet)
rm %{buildroot}/usr/include/tls.h

%check
%make_build test

%files
%license license.terms
%doc ChangeLog README.txt doc/tls.html
%doc %{_mandir}/*/*
%{_libdir}/tcl

%changelog
