#
# spec file for package libisds
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


%define libname %{name}5
Name:           libisds
Version:        0.11.2
Release:        0
Summary:        Library for accessing the Czech Data Boxes
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://xpisar.wz.cz/libisds/
Source0:        http://xpisar.wz.cz/%{name}/dist/%{name}-%{version}.tar.xz
Source1:        http://xpisar.wz.cz/%{name}/dist/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  gpg2
BuildRequires:  libgcrypt-devel
BuildRequires:  libgpgme-devel
BuildRequires:  pkgconfig
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(expat) >= 2.0.0
BuildRequires:  pkgconfig(gnutls) >= 2.12.0
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libxml-2.0)
Requires:       gpg2

%description
This is a library for accessing ISDS (Informační systém datových schránek /
Data Box Information System) SOAP services as defined in Czech ISDS Act
(300/2008 Coll.) and implied documents.

%package -n %{libname}
Summary:        Library for accessing the Czech Data Boxes
Group:          System/Libraries

%description -n %{libname}
This is a library for accessing ISDS (Informační systém datových schránek /
Data Box Information System) SOAP services as defined in Czech ISDS Act
(300/2008 Coll.) and implied documents.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/C and C++
Requires:       %{libname} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
%configure \
  --disable-fatalwarnings \
  --disable-static \
  --enable-test \
  --with-docbook-xsl-stylesheets=%{_datadir}/xml/docbook/stylesheet/nwalsh/current/ \
  --with-libcurl \
  --disable-openssl-backend
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}
mv doc specification
rm -rf client/.deps
rm -f specification/Makefile*
rm -f specification/*.3

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname} -f %{name}.lang
%license COPYING
%doc README AUTHORS NEWS TODO
%{_libdir}/*.so.*

%files devel
%{_includedir}/isds.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/*.3%{?ext_man}
%doc client specification

%changelog
