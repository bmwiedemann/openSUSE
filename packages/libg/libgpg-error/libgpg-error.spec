#
# spec file for package libgpg-error
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           libgpg-error
Version:        1.50
Release:        0
Summary:        Library That Defines Common Error Values for All GnuPG Components
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.gnupg.org/software/libgpg-error/
Source0:        https://gnupg.org/ftp/gcrypt/libgpg-error/%{name}-%{version}.tar.bz2
Source1:        https://gnupg.org/ftp/gcrypt/libgpg-error/%{name}-%{version}.tar.bz2.sig
# http://www.gnupg.org/signature_key.en.html
Source2:        https://gnupg.org/signature_key.asc#/%{name}.keyring
Source3:        baselibs.conf
#PATCH-FIX-OPENSUSE Do not pull revision info from GIT when autoconf is run
Patch0:         libgpg-error-nobetasuffix.patch
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
This is a library that defines common error values for all GnuPG
components.  Among these are GPG, GPGSM, GPGME, GPG-Agent, libgcrypt,
pinentry, SmartCard Daemon, and possibly more in the future.

%package -n libgpg-error0
Summary:        Library That Defines Common Error Values for All GnuPG Components
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Provides:       libgpg-error = %{version}
Obsoletes:      libgpg-error < %{version}

%description -n libgpg-error0
This is a library that defines common error values for all GnuPG
components.  Among these are GPG, GPGSM, GPGME, GPG-Agent, libgcrypt,
pinentry, SmartCard Daemon, and possibly more in the future.

%package devel
Summary:        Development package for libgpg-error
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libgpg-error0 = %{version}
Requires(post): info
Requires(preun): info

%description devel
Files needed for software development using libgpg-error.

%prep
%autosetup -p1

autoreconf -fiv

%build
%configure --disable-static \
	   --enable-install-gpg-error-config
%make_build

%install
%make_install
rm %{buildroot}%{_libdir}/libgpg-error.la
# Drop the lisp stuff, it depends on ASDF and CFFI
# which needs to be packaged first
rm -r %{buildroot}%{_datadir}/common-lisp
%find_lang %{name}

%check
%make_build check

%post -n libgpg-error0 -p /sbin/ldconfig
%postun -n libgpg-error0 -p /sbin/ldconfig

%post devel
%install_info --info-dir=%{_infodir} %{_infodir}/gpgrt.info.gz

%preun devel
%install_info_delete --info-dir=%{_infodir} %{_infodir}/gpgrt.info.gz

%files -n libgpg-error0 -f %{name}.lang
%license COPYING.LIB COPYING
%doc README NEWS ChangeLog AUTHORS ABOUT-NLS
%{_libdir}/libgpg-error*.so.*

%files devel
%{_bindir}/*
%{_libdir}/libgpg-error*.so
%{_libdir}/pkgconfig/gpg-error.pc
%{_includedir}/*
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/gpg-error.m4
%{_datadir}/aclocal/gpgrt.m4
%dir %{_datadir}/libgpg-error
%{_datadir}/libgpg-error/errorref.txt
%{_infodir}/gpgrt.info%{?ext_info}
%{_mandir}/man1/gpg-error-config.*
%{_mandir}/man1/gpgrt-config.*

%changelog
