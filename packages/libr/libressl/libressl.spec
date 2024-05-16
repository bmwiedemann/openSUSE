#
# spec file for package libressl
#
# Copyright (c) 2024 SUSE LLC
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

Name:           libressl
Version:        3.9.2
Release:        0
Summary:        An SSL/TLS protocol implementation
License:        OpenSSL
Group:          Development/Libraries/C and C++
URL:            https://www.libressl.org/
#Git-Clone:	https://github.com/libressl/portable
#See-Also:	https://github.com/libressl/openbsd
Source:         https://ftp.openbsd.org/pub/OpenBSD/LibreSSL/%name-%version.tar.gz
Source2:        https://ftp.openbsd.org/pub/OpenBSD/LibreSSL/%name-%version.tar.gz.asc
Source3:        %name.keyring
Source4:        baselibs.conf
Patch1:         des-fcrypt.diff
Patch2:         extra-symver.diff
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  fdupes
BuildRequires:  pkg-config
Provides:       ssl
Provides:       openssl(cli)
Conflicts:      openssl-1_1
Conflicts:      openssl-3

%description
LibreSSL is an open-source implementation of the Secure Sockets Layer
(SSL) and Transport Layer Security (TLS) protocols. It derives from
OpenSSL, with the aim of refactoring the OpenSSL code so as to
provide a more secure implementation.

%package -n libcrypto53
Summary:        An SSL/TLS protocol implementation
Group:          System/Libraries

%description -n libcrypto53
The "crypto" library implements a wide range of cryptographic
algorithms used in various Internet standards. The services provided
by this library are used by the LibreSSL implementations of SSL, TLS
and S/MIME, and they have also been used to implement SSH, OpenPGP,
and other cryptographic standards.

%package -n libssl56
Summary:        An SSL/TLS protocol implementation
Group:          System/Libraries

%description -n libssl56
LibreSSL is an open-source implementation of the Secure Sockets Layer
(SSL) and Transport Layer Security (TLS) protocols. It derives from
OpenSSL and intends to provide a more secure implementation.

%package -n libtls29
Summary:        A simplified interface for the OpenSSL/LibreSSL TLS protocol implementation
Group:          System/Libraries

%description -n libtls29
LibreSSL is an open-source implementation of the Secure Sockets Layer
(SSL) and Transport Layer Security (TLS) protocols. It derives from
OpenSSL and intends to provide a more secure implementation.

The libtls library provides a modern and simplified interface (of
libssl) for secure client and server communications.

%package devel
Summary:        Development files for LibreSSL, an SSL/TLS protocol implementation
Group:          Development/Libraries/C and C++
Requires:       libcrypto53 = %version
Requires:       libssl56 = %version
Requires:       libtls29 = %version
Conflicts:      ssl-devel
Provides:       ssl-devel

%description devel
LibreSSL is an open-source implementation of the Secure Sockets Layer
(SSL) and Transport Layer Security (TLS) protocols. It derives from
OpenSSL, with the aim of refactoring the OpenSSL code so as to
provide a more secure implementation.

This subpackage contains libraries and header files for developing
applications that want to make use of libressl.

%package devel-doc
Summary:        Documentation for the LibreSSL API
Group:          Documentation/Man
BuildArch:      noarch
Conflicts:      openssl-doc
Provides:       openssl-doc

%description devel-doc
LibreSSL is an open-source implementation of the Secure Sockets Layer
(SSL) and Transport Layer Security (TLS) protocols.

This subpackage contains the manpages to the LibreSSL API.

%prep
%autosetup -p1

%build
autoreconf -fi
# Some smart people broke disable-static
%configure --enable-libtls
%make_build

%install
b="%buildroot"
%make_install
rm -f "$b/%_libdir"/*.la
for i in "$b/%_mandir"/man*; do
	pushd "$i"
	for j in *.*; do
		if [ -L "$j" ]; then
			target=$(readlink "$j")
			ln -fs "${target}ssl" "$j"
		fi
		mv "$j" "${j}ssl"
	done
	popd
done
rm -f "%buildroot/%_sysconfdir/ssl/cert.pem"
rm -f "%buildroot/%_libdir"/*.a
rm -f "%buildroot/%_libdir"/*.la

%check
if ! %make_build check; then
	cat tests/test-suite.log
	exit 1
fi

%ldconfig_scriptlets -n libcrypto53
%ldconfig_scriptlets -n libssl56
%ldconfig_scriptlets -n libtls29

%files
%dir %_sysconfdir/ssl/
%config %_sysconfdir/ssl/openssl.cnf
%config %_sysconfdir/ssl/x509v3.cnf
%_bindir/ocspcheck
%_bindir/openssl
%_mandir/man1/*.1*
%_mandir/man5/*.5*
%_mandir/man8/*.8*
%doc COPYING

%files -n libcrypto53
%_libdir/libcrypto.so.*

%files -n libssl56
%_libdir/libssl.so.*

%files -n libtls29
%_libdir/libtls.so.*

%files devel
%_includedir/openssl/
%_includedir/tls.h
%_libdir/libcrypto.so
%_libdir/libssl.so
%_libdir/libtls.so
%_libdir/pkgconfig/*.pc

%files devel-doc
%_mandir/man3/*.*

%changelog
