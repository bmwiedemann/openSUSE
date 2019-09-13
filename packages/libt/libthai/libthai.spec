#
# spec file for package libthai
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


Name:           libthai
Version:        0.1.27
Release:        0
Summary:        Thai Language Support Routines
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Url:            http://linux.thai.net/plone/TLWG/libthai/
Source:         https://linux.thai.net/pub/thailinux/software/libthai/%{name}-%{version}.tar.xz
Source99:       baselibs.conf
BuildRequires:  libdatrie-devel
BuildRequires:  pkgconfig

%description
LibThai is a set of Thai language support routines to aid
incorporation of Thai language support into applications. It includes
important Thai-specific functions, such as word breaking, input and
output methods, and basic character and string support.

%package -n libthai0
Summary:        Thai Language Support Routines
# SLPP applied since version 0.1.15.
# libthai needs the data to run, but the data is not parallel-installable,
# hence the >= instead of =. We just hope the data format will stay the same in
# the future.
Group:          System/Libraries
Requires:       libthai-data >= %{version}
Provides:       libthai = %{version}
Obsoletes:      libthai < %{version}

%description -n libthai0
LibThai is a set of Thai language support routines to aid
incorporation of Thai language support into applications. It includes
important Thai-specific functions, such as word breaking, input and
output methods, and basic character and string support.

%package data
Summary:        Data files for the Thai language support library
Group:          System/Libraries

%description data
LibThai is a set of Thai language support routines to aid
incorporation of Thai language support into applications. It includes
important Thai-specific functions, such as word breaking, input and
output methods, and basic character and string support.

This package contains the data files for libthai.

%package devel
Summary:        Development files for the Thai language support library
Group:          Development/Languages/C and C++
Requires:       libthai0 = %{version}

%description devel
LibThai is a set of Thai language support routines to aid
incorporation of Thai language support into applications. It includes
important Thai-specific functions, such as word breaking, input and
output methods, and basic character and string support.

This package contains headers and libraries required for developing
software using libthai.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libthai0 -p /sbin/ldconfig
%postun -n libthai0 -p /sbin/ldconfig

%files -n libthai0
%{_libdir}/libthai.so.*

%files data
%{_datadir}/libthai/

%files devel
%{_includedir}/thai/
%{_libdir}/libthai.so
%{_libdir}/pkgconfig/*.pc

%changelog
