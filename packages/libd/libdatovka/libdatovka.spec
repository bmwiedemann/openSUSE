#
# spec file for package libdatovka
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


%define libname %{name}6
Name:           libdatovka
Version:        0.6.2
Release:        0
Summary:        Library for accessing the Czech Data Boxes
License:        GPL-3.0-or-later
Group:          System/Libraries
URL:            https://www.datovka.cz/cs/pages/libdatovka.html
Source0:        https://secure.nic.cz/files/datove_schranky/%{name}/%{name}-%{version}.tar.xz
Source1:        https://secure.nic.cz/files/datove_schranky/%{name}/%{name}-%{version}.tar.xz.sha256
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  libcurl-devel
BuildRequires:  libexpat-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libgpgme-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-tools

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
	--disable-static \
	--with-docbook-xsl-stylesheets=/usr/share/xml/docbook/stylesheet/nwalsh/current
make %{?_smp_mflags}

%install
%make_install
%find_lang %{name}
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -f %{name}.lang

%files -n %{libname}
%license COPYING
%doc AUTHORS
%{_libdir}/*.so.*

%files devel
%doc client
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/isds.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/*.3.gz

%changelog
