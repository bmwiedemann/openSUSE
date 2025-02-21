#
# spec file for package libassuan
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define soversion 9
Name:           libassuan
Version:        3.0.2
Release:        0
Summary:        IPC library used by GnuPG version 2
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.gnupg.org/related_software/libassuan/index.en.html
Source0:        https://www.gnupg.org/ftp/gcrypt/libassuan/%{name}-%{version}.tar.bz2
Source1:        baselibs.conf
Source2:        https://www.gnupg.org/ftp/gcrypt/libassuan/%{name}-%{version}.tar.bz2.sig
# https://www.gnupg.org/signature_key.html
Source3:        https://gnupg.org/signature_key.asc#/%{name}.keyring
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gpg-error) >= 1.17

%description
Libassuan is the IPC library used by gpg2 (GnuPG version 2)

%package -n libassuan%{soversion}
Summary:        IPC library used by GnuPG version 2
Group:          Development/Libraries/C and C++

%description -n libassuan%{soversion}
Libassuan is the IPC library used by gpg2 (GnuPG version 2)

%package devel
Summary:        IPC library used by GnuPG version 2
Group:          Development/Libraries/C and C++
Requires:       libassuan%{soversion} = %{version}

%description devel
Libassuan is the IPC library used by gpg2 (GnuPG version 2)

gpgme also uses libassuan to communicate with a libassuan-enabled GnuPG
v2 server, but it uses it's own copy of libassuan.

%prep
%autosetup -p1

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

%ldconfig_scriptlets -n libassuan%{soversion}

%files -n libassuan%{soversion}
%license COPYING COPYING.LIB
%doc AUTHORS ChangeLog NEWS README THANKS
%{_libdir}/libassuan.so.%{soversion}
%{_libdir}/libassuan.so.%{soversion}.*

%files devel
%license COPYING COPYING.LIB
%{_libdir}/pkgconfig/libassuan.pc
%{_infodir}/assuan*
%{_includedir}/*.h
%{_bindir}/*-config
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/*.m4
%{_libdir}/libassuan.so

%changelog
