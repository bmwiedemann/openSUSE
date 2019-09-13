#
# spec file for package libksba
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define soname 8
Name:           libksba
Version:        1.3.5
Release:        0
Summary:        A X.509 Library
License:        (LGPL-3.0+ or GPL-2.0+) and GPL-3.0+ and MIT
Group:          Development/Libraries/C and C++
Url:            http://www.gnupg.org/aegypten/
Source:         ftp://ftp.gnupg.org/gcrypt/libksba/%{name}-%{version}.tar.bz2
Source2:        ftp://ftp.gnupg.org/gcrypt/libksba/%{name}-%{version}.tar.bz2.sig
Source3:        libksba.keyring
Source4:        libksba.changes
BuildRequires:  libgpg-error-devel >= 1.8
# FIXME: use proper Requires(pre/post/preun/...)
PreReq:         %{install_info_prereq}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
Requires:       libgpg-error-devel
Requires:       libksba = %{version}
Provides:       libksba:%{_includedir}/ksba.h

%description devel
KSBA is a library to simplify the task of working with X.509
certificates, CMS data, and related data.

This package contains the needed files to compile and link against the
libksba.

%prep
%setup -q -n libksba-%{version}

%build
build_timestamp=$(date -u +%{Y}-%{m}-%{dT}%{H}:%{M}+0000 -r %{SOURCE4})
%configure \
	--disable-static \
	--with-pic \
	--enable-build-timestamp="${build_timestamp}"

make %{?_smp_mflags}

%check
make %{?_smp_mflags} check

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{name}%{soname} -p /sbin/ldconfig
%postun -n %{name}%{soname} -p /sbin/ldconfig

%files -n %{name}%{soname}
%defattr(-,root,root)
%license COPYING
%doc README AUTHORS ChangeLog NEWS THANKS TODO
%{_libdir}/libksba*.so.*

%post devel
%install_info --info-dir=%{_infodir} %{_infodir}/ksba.info.gz

%postun devel
%install_info_delete --info-dir=%{_infodir} %{_infodir}/ksba.info.gz

%files devel
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/libksba*.so
%{_includedir}/*
%{_infodir}/ksba*
%{_datadir}/aclocal/*

%changelog
