#
# spec file for package libassuan
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


Name:           libassuan
Version:        2.5.4
Release:        0
Summary:        IPC library used by GnuPG version 2
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.gnupg.org/related_software/libassuan/index.en.html
Source0:        ftp://ftp.gnupg.org/gcrypt/libassuan/%{name}-%{version}.tar.bz2
Source1:        baselibs.conf
Source2:        ftp://ftp.gnupg.org/gcrypt/libassuan/%{name}-%{version}.tar.bz2.sig
# http://www.gnupg.org/signature_key.en.html
Source3:        libassuan.keyring
BuildRequires:  libgpg-error-devel >= 1.17
Requires:       %{install_info_prereq}

%description
Libassuan is the IPC library used by gpg2 (GnuPG version 2)

%package -n libassuan0
Summary:        IPC library used by GnuPG version 2
Group:          Development/Libraries/C and C++

%description -n libassuan0
Libassuan is the IPC library used by gpg2 (GnuPG version 2)

%package devel
Summary:        IPC library used by GnuPG version 2
Group:          Development/Libraries/C and C++
Requires:       libassuan0 = %{version}
Requires:       libgpg-error-devel

%description devel
Libassuan is the IPC library used by gpg2 (GnuPG version 2)

gpgme also uses libassuan to communicate with a libassuan-enabled GnuPG
v2 server, but it uses it's own copy of libassuan.

%prep
%setup -q

%build
# Compile with PIC, library is linked into shared libraries:
export CFLAGS="%{optflags} $(getconf LFS_CFLAGS)"
export LDFLAGS="-fPIC"
%configure
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
%make_build check

%post -n libassuan0 -p /sbin/ldconfig
%postun -n libassuan0 -p /sbin/ldconfig
%post devel
%install_info --info-dir=%{_infodir} %{_infodir}/assuan.info.gz

%postun devel
%install_info_delete --info-dir=%{_infodir} %{_infodir}/assuan.info.gz

%files -n libassuan0
%license COPYING
%doc AUTHORS ChangeLog NEWS README THANKS
%{_libdir}/libassuan.so.*

%files devel
%{_libdir}/pkgconfig/libassuan.pc
%{_infodir}/assuan*
%{_includedir}/*.h
%{_bindir}/*-config
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/*.m4
%{_libdir}/libassuan.so

%changelog
