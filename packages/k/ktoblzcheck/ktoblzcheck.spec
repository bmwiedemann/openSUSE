#
# spec file for package ktoblzcheck
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ktoblzcheck
%define libsoname lib%{name}1
Summary:        A library to check account numbers and bank codes of German banks
License:        LGPL-2.1
Group:          Productivity/Office/Finance
Version:        1.48
Release:        0
Source:         http://downloads.sourceforge.net/project/%{name}/%{name}-%{version}.tar.gz
Url:            http://ktoblzcheck.sourceforge.net
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  python

%if 0%{?suse_version} > 121
BuildRequires:  automake
BuildRequires:  libtool
%endif

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


%package -n python-%{name}
Summary:        KtoBLZCheck python-bindings
Group:          Development/Libraries/Python
%py_requires
Requires:       %{libsoname} = %{version}
Requires:       %{name} = %{version}
Requires:       python >= 2.3

%description -n python-%{name}
This package contains the python-bindings for ktoblzcheck.


%prep
%setup -q
autoreconf -fi

%build
%{configure} \
    --enable-python \
    --with-pic

make %{?_smp_mflags}

%install
%makeinstall pythondir=%{py_sitedir}

%fdupes -s %{buildroot}

%__rm %{buildroot}%{_libdir}/*.la

%post -n %{libsoname} -p /sbin/ldconfig

%postun -n %{libsoname} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/ibandata.txt
%{_datadir}/%{name}/bundesbank.pl
%{_datadir}/%{name}/online_update.pl
%{_datadir}/%{name}/bankdata_*.txt

%files -n %{libsoname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%doc AUTHORS README COPYING ChangeLog NEWS
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}.h
%{_includedir}/iban.h

%files -n python-%{name}
%defattr(-,root,root)
%{py_sitedir}/*

%changelog
