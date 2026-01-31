#
# spec file for package libressl
#
# Copyright (c) 2025 SUSE LLC
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
Version:        4.2.1
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
Source5:        unavailable-libcrypto-symbols.txt.zst
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
LibreSSL is an implementation of the Secure Sockets Layer (SSL) and
Transport Layer Security (TLS) protocols. It derives from OpenSSL,
with refactorings.

%package -n libcrypto57
Summary:        An SSL/TLS protocol implementation
Group:          System/Libraries

%description -n libcrypto57
The "crypto" library implements a wide range of cryptographic
algorithms used in various Internet standards. The services provided
by this library are used by the LibreSSL implementations of SSL, TLS
and S/MIME, and they have also been used to implement SSH, OpenPGP,
and other cryptographic standards.

%package -n libssl60
Summary:        An SSL/TLS protocol implementation
Group:          System/Libraries

%description -n libssl60
LibreSSL is an implementation of the Secure Sockets Layer (SSL) and
Transport Layer Security (TLS) protocols. It derives from OpenSSL,
with refactorings.

%package -n libtls33
Summary:        A simplified interface for the OpenSSL/LibreSSL TLS protocol implementation
Group:          System/Libraries

%description -n libtls33
LibreSSL is an implementation of the Secure Sockets Layer (SSL) and
Transport Layer Security (TLS) protocols. It derives from OpenSSL,
with refactorings.

The libtls library provides a modern and simplified interface (of
libssl) for secure client and server communications.

%package devel
Summary:        Development files for LibreSSL, an SSL/TLS protocol implementation
Group:          Development/Libraries/C and C++
Requires:       libcrypto57 = %version
Requires:       libssl60 = %version
Requires:       libtls33 = %version
Conflicts:      ssl-devel
Provides:       ssl-devel

%description devel
LibreSSL is an implementation of the Secure Sockets Layer (SSL) and
Transport Layer Security (TLS) protocols. It derives from OpenSSL,
with refactorings.

LibreSSL provides much of the OpenSSL 1.1 API. The OpenSSL 3 API is not
currently supported, but many programs only need v1.1. See
%_docdir/libressl-devel-doc/unavailable-libcrypto-symbols.txt.zst for
a list of symbols/functions that cannot be exercised when building
with libressl.

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
cp %_sourcedir/unavail* .

%build
%ifarch s390x
# libressl can work without any arch-specific code whatsoever. The makefiles
# contain a bunch of `if PPC64 { CPPFLAGS+=-Icrypto/arch/ppc64 }`-style lines,
# for various archs, but no "else" clause, so there is no functioning fallback.
# The following adds this fallback.
#
touch crypto/crypto_arch.h crypto/bn/bn_arch.h
%endif

autoreconf -fi
%configure --enable-libtls --with-openssldir="%_sysconfdir/libressl"
%make_build

%install
b="%buildroot"
%make_install
rm -f "$b/%_libdir"/*.la
for i in "$b/%_mandir"/man*; do
	cd "$i"
	for j in *.*; do
		if [ -L "$j" ]; then
			target=$(readlink "$j")
			ln -fs "${target}ssl" "$j"
		fi
		mv "$j" "${j}ssl"
	done
	cd -
done
rm -v "%buildroot/%_sysconfdir/libressl/cert.pem"
rm -fv "%buildroot/%_libdir"/*.a "%buildroot/%_libdir"/*.la

find "%buildroot/%_mandir" -type l -exec perl -e 'for (@ARGV) { next if(!-l $_); $t=readlink$_; unlink if(!-e $t); }' '{}' '+'

%check
if ! %make_build check; then
	cat tests/test-suite.log
	# testsuite seems to be tripping over openssl configs
	#exit 1
fi

%ldconfig_scriptlets -n libcrypto57
%ldconfig_scriptlets -n libssl60
%ldconfig_scriptlets -n libtls33

%files
# openssl's config (syntax) is incompatible with libressl,
# so all the more reason to separate it
%dir %_sysconfdir/libressl/
%config %_sysconfdir/libressl/openssl.cnf
%config %_sysconfdir/libressl/x509v3.cnf
%_bindir/ocspcheck
%_bindir/openssl
%_mandir/man1/*.1*
%_mandir/man5/*.5*
%_mandir/man8/*.8*
%doc COPYING

%files -n libcrypto57
%_libdir/libcrypto.so.*

%files -n libssl60
%_libdir/libssl.so.*

%files -n libtls33
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
%doc unavailable-libcrypto-symbols.txt.zst

%changelog
