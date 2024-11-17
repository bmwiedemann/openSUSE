#
# spec file for package gnu-recutils
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


%define _lsover  1
%define _osover  0
Name:           gnu-recutils
Version:        1.9
Release:        0
Summary:        Text-based databases called recfiles
License:        GPL-3.0-or-later
Group:          Productivity/Databases/Tools
URL:            https://www.gnu.org/software/recutils
Source0:        https://ftp.gnu.org/gnu/recutils/recutils-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/recutils/recutils-%{version}.tar.gz.sig
Source2:        https://savannah.gnu.org/people/viewgpg.php?user_id=829#/%{name}.keyring
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bash)
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(libacl)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(uuid)

%description
A set of tools and libraries to access human-editable, text-based
databases.

The data is stored as a sequence of records, each record containing
an arbitrary number of named fields.

Despite its simplicity, recfiles can be used to store medium-sized
databases.

%package        devel
Summary:        Header files for %{name} libraries
Group:          Development/Languages/C and C++
Requires:       librec%{_lsover} = %{version}
Requires:       readrec%{_osover} = %{version}
Requires:       testrec%{_osover} = %{version}

%description    devel
This package contains files to develop for %{name} libraries

%package     -n librec%{_lsover}
Summary:        Text-based databases called recfiles
Group:          System/Libraries

%description -n librec%{_lsover}
A set of tools and libraries to access human-editable, text-based
databases.

The data is stored as a sequence of records, each record containing
an arbitrary number of named fields.

Despite its simplicity, recfiles can be used to store medium-sized
databases.

%package     -n readrec%{_osover}
Summary:        Text-based databases called recfiles
Group:          System/Libraries

%description -n readrec%{_osover}
A set of tools and libraries to access human-editable, text-based
databases.

The data is stored as a sequence of records, each record containing
an arbitrary number of named fields.

Despite its simplicity, recfiles can be used to store medium-sized
databases.

%package     -n testrec%{_osover}
Summary:        Text-based databases called recfiles
Group:          System/Libraries

%description -n testrec%{_osover}
A set of tools and libraries to access human-editable, text-based
databases.

The data is stored as a sequence of records, each record containing
an arbitrary number of named fields.

Despite its simplicity, recfiles can be used to store medium-sized
databases.

%lang_package

%prep
%setup -q -n recutils-%{version}

%build
export CFLAGS="%{optflags} -Wno-implicit-function-declaration -Wno-incompatible-pointer-types"
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang recutils %{name}.lang

%check
%make_build check

%post   -n librec%{_lsover} -p /sbin/ldconfig
%postun -n librec%{_lsover} -p /sbin/ldconfig
%post   -n readrec%{_osover} -p /sbin/ldconfig
%postun -n readrec%{_osover} -p /sbin/ldconfig
%post   -n testrec%{_osover} -p /sbin/ldconfig
%postun -n testrec%{_osover} -p /sbin/ldconfig

%files
%license COPYING
%doc NEWS README AUTHORS
%dir %{_datadir}/recutils
%dir %{_datadir}/recutils%{_sysconfdir}
%{_bindir}/*
%{_infodir}/*%{?ext_info}
%{_mandir}/man1/*.1%{?ext_man}
%{_datadir}/recutils%{_sysconfdir}/FSD.rec

%files devel
%license COPYING
%{_includedir}/rec.h
%{_libdir}/*.so

%files -n librec%{_lsover}
%license COPYING
%{_libdir}/librec.so.%{_lsover}*

%files -n readrec%{_osover}
%license COPYING
%{_libdir}/readrec.so.%{_osover}*

%files -n testrec%{_osover}
%license COPYING
%{_libdir}/testrec.so.%{_osover}*

%files lang -f %{name}.lang
%license COPYING

%changelog
