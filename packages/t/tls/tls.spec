#
# spec file for package tls
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


Name:           tls
Summary:        Tcl Binding for the OpenSSL Library
License:        BSD-3-Clause
Group:          Development/Libraries/Tcl
Version:        1.7.22
Release:        0
URL:            https://core.tcl-lang.org/tcltls
Source0:        https://core.tcl-lang.org/tcltls/uv/tcltls-%version.tar.gz
Source1:        %name-test-certs.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(tcl)

%description
This Tcl extension provides a generic binding to OpenSSL, utilizing
the Tcl_StackChannel API for Tcl 8.2 and higher. The sockets behave
exactly the same as channels created using Tcl's built-in socket
command with additional options for controlling the SSL session.

%prep
%setup -q -a 1 -n tcl%name-%version

%build
%configure \
	--enable-deterministic \
	--enable-ssl-fastpath
make %{?_smp_mflags}

%check
cat > known-failures <<EOF
ciphers-1.4
ciphers-1.3
tls-bug58-1.0
EOF
make test 2>&1 | tee testresults
grep FAILED testresults | grep -Fqvf known-failures && exit 1 ||:

%install
make install \
	DESTDIR=%buildroot \
	PKG_HEADERS= \
	libdir=%_libdir/tcl

%files
%defattr(-,root,root,-)
%doc ChangeLog README.txt license.terms tls.htm
%_libdir/tcl

%changelog
