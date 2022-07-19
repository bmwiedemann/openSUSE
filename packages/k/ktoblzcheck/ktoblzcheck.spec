#
# spec file for package ktoblzcheck
#
# Copyright (c) 2021 SUSE LLC
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


Name:           ktoblzcheck
%define libsoname lib%{name}1
Summary:        A library to check account numbers and bank codes of German banks
License:        LGPL-2.1-only
Group:          Productivity/Office/Finance
Version:        1.53
Release:        0
Source:         http://downloads.sourceforge.net/project/%{name}/%{name}-%{version}.tar.gz
URL:            http://ktoblzcheck.sourceforge.net
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  python3-devel

%description
KtoBLZCheck is a library to check account numbers and bank codes
of German banks. Both a library for other programs as well as a
short command-line tool is available. It is possible to check
pairs of account numbers and bank codes (BLZ) of German banks,
and to map bank codes (BLZ) to the clear-text name and location
of the bank.

%package devel
Summary:        KtoBLZCheck development files
Group:          Development/Libraries/C and C++
Requires:       %{libsoname} = %{version}
Provides:       %{libsoname}-devel = %{version}
Obsoletes:      %{libsoname}-devel < %{version}

%description devel
Libraries, includes etc to develop with ktoblzcheck library.

%package -n %{libsoname}
Summary:        Shared Libraries for ktoblzcheck
Group:          System/Libraries

%description -n %{libsoname}
This package contains shared Libraries for ktoblzcheck.

%package -n python3-%{name}
Summary:        KtoBLZCheck python-bindings
Group:          Development/Libraries/Python
Requires:       %{libsoname} = %{version}
Requires:       %{name} = %{version}
Obsoletes:      python-%{name} < %{version}

%description -n python3-%{name}
This package contains the python-bindings for ktoblzcheck.

%prep
%setup -q

%build
%cmake -DINSTALL_RAW_BANKDATA_FILE=1 -DENABLE_BANKDATA_DOWNLOAD=0
make %{?_smp_mflags}

%install
%cmake_install

%fdupes -s %{buildroot}

%post -n %{libsoname} -p /sbin/ldconfig

%postun -n %{libsoname} -p /sbin/ldconfig

%files
%doc AUTHORS ChangeLog NEWS README.md
%license COPYING
%{_bindir}/%{name}
%{_bindir}/ibanchk
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/ibanchk.1*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/ibandata.txt
%{_datadir}/%{name}/bankdata_*.txt
%{_datadir}/%{name}/blz_*.txt

%files -n %{libsoname}
%{_libdir}/*.so.*

%files devel
%doc AUTHORS ChangeLog NEWS README.md
%license COPYING
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}.h
%{_includedir}/iban.h
%{_libdir}/cmake/KtoBlzCheck

%files -n python3-%{name}
%{python3_sitearch}/*

%changelog
