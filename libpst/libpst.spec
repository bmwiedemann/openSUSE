#
# spec file for package libpst
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2008 Bharath Acharya
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


Name:           libpst
Version:        0.6.71
Release:        0
Summary:        Library and utilities for reading Personal Storage Table files
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Email/Utilities
URL:            http://www.gnome.org/projects/evolution/
Source0:        http://www.five-ten-sg.com/libpst/packages/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  gd-devel
BuildRequires:  libgsf-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(zlib)

%description
The libpst utilities include readpst, which can convert email messages
to both mbox and MH mailbox formats, pst2ldif, which can convert the
contacts to .ldif format for import into LDAP databases, and pst2dii,
which can convert email messages to the DII load file format used by
Summation.

%package -n libpst4
Summary:        A library for reading Personal Storage Table files
Group:          System/Libraries

%description -n libpst4
libpst is a library that can decode the email messages stored in a
.pst (Personal Storage Table) file as created by Outlook.

%package devel
Summary:        Development files for libpst, a .pst file reader
Group:          Development/Libraries/C and C++
Requires:       libpst4 = %{version}

%description devel
libpst is a library that can decode the email messages stored in a
"PST" file as created by Outlook.

This subpackage contains the header files for developing
applications that want to make use of libpst.

%prep
%setup -q

%build
%configure \
        --disable-static \
        --enable-libpst-shared \
        --disable-python
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libpst4 -p /sbin/ldconfig
%postun -n libpst4 -p /sbin/ldconfig

%files
%doc %{_datadir}/doc/%{name}-%{version}
%{_mandir}/man?/*
%{_bindir}/lspst
%{_bindir}/nick2ldif
%{_bindir}/pst2ldif
%{_bindir}/readpst

%files -n libpst4
%{_libdir}/libpst.so.*

%files devel
%{_includedir}/libpst-4/
%{_libdir}/pkgconfig/libpst.pc
%{_libdir}/libpst.so

%changelog
