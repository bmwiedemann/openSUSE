#
# spec file for package gpgme
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define sover 45
Name:           gpgme
Version:        2.0.1
Release:        0
Summary:        Programmatic library interface to GnuPG
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Security
URL:            https://www.gnupg.org/related_software/gpgme/
Source:         https://www.gnupg.org/ftp/gcrypt/gpgme/gpgme-%{version}.tar.bz2
Source1:        https://www.gnupg.org/ftp/gcrypt/gpgme/gpgme-%{version}.tar.bz2.sig
Source2:        baselibs.conf
# https://www.gnupg.org/signature_key.html
Source3:        https://gnupg.org/signature_key.asc#/gpgme.keyring
# used to have a fixed timestamp
Source99:       gpgme.changes
# PATCH-FIX-UPSTREAM Treat empty DISPLAY variable as unset. [bsc#1252425, bsc#1231055] https://dev.gnupg.org/T7919
Patch1:         gpgme-Treat-empty-DISPLAY-variable-as-unset.patch
BuildRequires:  gpg2 >= 2.4.1
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gpg-error) >= 1.47
BuildRequires:  pkgconfig(libassuan) >= 2.4.2

%description
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG
easier for applications. It provides a high-level crypto API for
encryption, decryption, signing, signature verification, and key
management. It uses GnuPG as its back-end.

%package -n libgpgme%{sover}
Summary:        Programmatic library interface to GnuPG
Group:          System/Libraries
Requires:       gpg2

%description -n libgpgme%{sover}
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG
easier for applications. It provides a high-level crypto API for
encryption, decryption, signing, signature verification, and key
management. It uses GnuPG as its back-end.

%package devel
Summary:        Development files for GPGME, a C library for accessing GnuPG
Group:          Development/Libraries/C and C++
Requires:       libgpgme%{sover} = %{version}
Provides:       libgpgme-devel = %{version}
Obsoletes:      libgpgme-devel < %{version}

%description devel
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG
easier for applications. It provides a high-level crypto API for
encryption, decryption, signing, signature verification, and key
management.

This subpackage contains the headers needed for building applications
making use of libgpgme.

%prep
%autosetup -p1

%build
build_timestamp=$(date -u +%{Y}-%{m}-%{dT}%{H}:%{M}+0000 -r %{SOURCE99})
%configure \
	--disable-static \
	--disable-fd-passing \
	--enable-languages="${languages}" \
	--enable-languages=cl \
	--enable-build-timestamp="${build_timestamp}" \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
GPGME_DEBUG=2:mygpgme.log %make_build check || cat $(find -name mygpgme.log -type f)

%ldconfig_scriptlets -n libgpgme%{sover}

%files
%license COPYING COPYING.LESSER LICENSES
%{_bindir}/gnupg-key-manage
%{_bindir}/gpgme-json
%{_bindir}/gpgme-tool
%dir %{_datadir}/common-lisp
%dir %{_datadir}/common-lisp/source
%{_datadir}/common-lisp/source/gpgme
%{_infodir}/gpgme*
%{_mandir}/man1/*.1%{?ext_man}

%files -n libgpgme%{sover}
%license COPYING COPYING.LESSER LICENSES
%{_libdir}/libgpgme.so.%{sover}{,.*}

%files devel
%license COPYING COPYING.LESSER LICENSES
%{_libdir}/libgpgme.so
%{_bindir}/gpgme-config
%{_datadir}/aclocal/gpgme.m4
%{_includedir}/gpgme.h
%{_libdir}/pkgconfig/gpgme.pc
%{_libdir}/pkgconfig/gpgme-glib.pc

%changelog
