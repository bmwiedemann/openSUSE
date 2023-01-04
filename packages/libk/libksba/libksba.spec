#
# spec file for package libksba
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


%define soname 8
Name:           libksba
Version:        1.6.3
Release:        0
Summary:        A X.509 Library
License:        (GPL-2.0-or-later OR LGPL-3.0-or-later) AND GPL-3.0-or-later AND MIT
Group:          Development/Libraries/C and C++
URL:            https://www.gnupg.org
Source:         https://gnupg.org/ftp/gcrypt/libksba/%{name}-%{version}.tar.bz2
Source2:        https://gnupg.org/ftp/gcrypt/libksba/%{name}-%{version}.tar.bz2.sig
# https://www.gnupg.org/signature_key.html
Source3:        %{name}.keyring
Source4:        libksba.changes
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gpg-error) >= 1.8

%description
KSBA is a library to simplify the task of working with X.509
certificates, CMS data, and related data.

%package -n %{name}%{soname}
Summary:        A X.509 Library
Group:          Development/Libraries/C and C++
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n %{name}%{soname}
KSBA is a library to simplify the task of working with X.509
certificates, CMS data, and related data.

%package devel
Summary:        A X.509 Library
Group:          Development/Libraries/C and C++
Requires:       libksba%{soname} = %{version}
Provides:       libksba:%{_includedir}/ksba.h

%description devel
KSBA is a library to simplify the task of working with X.509
certificates, CMS data, and related data.

This package contains the needed files to compile and link against the
libksba.

%prep
%autosetup -p1

%build
build_timestamp=$(date -u +%{Y}-%{m}-%{dT}%{H}:%{M}+0000 -r %{SOURCE4})
%configure \
	--disable-static \
	--with-pic \
	--enable-build-timestamp="${build_timestamp}"

%make_build

%check
%make_build check

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{name}%{soname} -p /sbin/ldconfig
%postun -n %{name}%{soname} -p /sbin/ldconfig

%files -n %{name}%{soname}
%license COPYING*
%doc README AUTHORS ChangeLog NEWS THANKS TODO
%{_libdir}/libksba*.so.*

%files devel
%license COPYING*
%{_bindir}/ksba-config
%{_libdir}/libksba*.so
%{_libdir}/pkgconfig/ksba.pc
%{_includedir}/ksba.h
%{_datadir}/aclocal/ksba.m4
%{_infodir}/ksba.info%{?ext_info}

%changelog
