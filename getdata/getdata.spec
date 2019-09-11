#
# spec file for package getdata
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2011,2012 Christian Trippe <ctrippe@opensuse.org>
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


Name:           getdata
Version:        0.10.0
Release:        0
Summary:        Library for reading and writing dirfile data
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Url:            http://getdata.sourceforge.net/
Source:         %{name}-%{version}.tar.xz
BuildRequires:  bzip2
%if 0%{?is_opensuse}
BuildRequires:  flac
BuildRequires:  flac-devel
%endif
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  libbz2-devel
BuildRequires:  libtool
BuildRequires:  perl
%if 0%{?suse_version} > 1320
BuildRequires:  perl-ExtUtils-MakeMaker
%else
BuildRequires:  perl-Module-Build
%endif
BuildRequires:  pkg-config
BuildRequires:  python-devel
BuildRequires:  python-numpy-devel
BuildRequires:  xz
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
Recommends:     %{name}-doc
Recommends:     bzip2
%if 0%{?is_opensuse}
Recommends:     flac
%endif
Recommends:     gzip
Recommends:     xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The GetData Project is the reference implementation of the Dirfile Standards, a
filesystem-based database format for time-ordered binary data. The Dirfile
database format is designed to provide a fast, simple format for storing and
reading data.

%package devel
Summary:        Headers required when building programs against GetData
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}
Requires:       gcc-c++
Requires:       gcc-fortran
Requires:       libgetdata++7 = %{version}
Requires:       pkgconfig

%description devel
Headers required when building a program against the GetData library.
Includes C++ and FORTRAN (77 & 95) bindings.

%package doc
Summary:        Documentation for GetData
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description doc
Documentation and manuals for the GetData library.

%package -n libgetdata8
Summary:        C library for reading and writing dirfile data
Group:          System/Libraries

%description -n libgetdata8
Library for the C bindings for GetData.

%post -n libgetdata8 -p /sbin/ldconfig

%postun -n libgetdata8 -p /sbin/ldconfig

%package -n libgetdata++7
Summary:        C++ library for reading and writing dirfile data
Group:          System/Libraries

%description -n libgetdata++7
Library for C++-bindings for GetData.

%post -n libgetdata++7 -p /sbin/ldconfig

%postun -n libgetdata++7 -p /sbin/ldconfig

%package -n libf95getdata7
Summary:        Fortran95 library for reading and writing dirfile data
Group:          System/Libraries

%description -n libf95getdata7
The GetData library for Fortran95 programs.

%post -n libf95getdata7 -p /sbin/ldconfig

%postun -n libf95getdata7 -p /sbin/ldconfig

%package -n libfgetdata6
Summary:        Fortran library for reading and writing dirfile data
Group:          System/Libraries

%description -n libfgetdata6
The GetData library for Fortran programs.

%post -n libfgetdata6 -p /sbin/ldconfig

%postun -n libfgetdata6 -p /sbin/ldconfig

%package -n perl-getdata
Summary:        GetData bindings for the Perl language
Group:          Development/Libraries/Perl
Requires:       %{name} = %{version}
%{perl_requires}

%description -n perl-getdata
Bindings to the GetData library for the Perl language.

%package -n python-getdata
Summary:        GetData bindings for the Python language
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}
Requires:       python-base = %py_ver
Requires:       python-numpy

%description -n python-getdata
Bindings to the GetData library for the Python lanuguage.
Uses (and requires) the numpy Python library for large numeric arrays.


%prep
%setup -q

%build
%configure --disable-static --enable-modules --with-perl-dir=vendor
make %{?_smp_mflags}

%check
make check

%install
%make_install
# Remove .la files.
rm -f %{buildroot}/%{_libdir}/lib*.la
rm -f %{buildroot}/%{python_sitearch}/*.la
# Remove simple docs
rm -f  %{buildroot}/%{_datadir}/doc/%{name}/*

%files
%defattr(-,root,root,-)
%doc COPYING AUTHORS
%{_bindir}/dirfile2ascii
%{_bindir}/checkdirfile
%{_libdir}/getdata
%{_mandir}/man1/checkdirfile.1.gz
%{_mandir}/man1/dirfile2ascii.1.gz

%files doc
%defattr(-,root,root,-)
%{_mandir}/man5/*
%doc README NEWS TODO ChangeLog

%files -n libgetdata8
%defattr(-,root,root,-)
%{_libdir}/libgetdata.so.*

%files -n libgetdata++7
%defattr(-,root,root,-)
%{_libdir}/libgetdata++.so.*

%files -n python-getdata
%defattr(-,root,root,-)
%{python_sitearch}/*.so

%files -n libfgetdata6
%defattr(-,root,root,-)
%{_libdir}/libfgetdata.so.*

%files -n libf95getdata7
%defattr(-,root,root,-)
%{_libdir}/libf95getdata.so.*

%files -n perl-getdata
%defattr(-,root,root,-)
%perl_vendorarch/GetData.pm
%dir %perl_vendorarch/auto
%dir %perl_vendorarch/auto/GetData
%perl_vendorarch/auto/GetData/GetData.so

%files devel
%defattr(-,root,root,-)
%doc doc/README.cxx doc/README.f77 doc/unclean_database_recovery.txt doc/README.python
%{_libdir}/libgetdata.so
%{_libdir}/libf*getdata.so
%{_libdir}/libgetdata++.so
%{_includedir}/*
%{_mandir}/man3/*
%{_libdir}/pkgconfig/getdata.pc

%changelog
