#
# spec file for package mpir
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           mpir
%define lname	libmpir23
%define lnamexx	libmpirxx8
Version:        3.0.0
Release:        0
Summary:        Multiprecision integer library derived from GMP
License:        LGPL-3.0-or-later
Group:          Productivity/Scientific/Math
Url:            http://mpir.org/

#Git-Clone:	git://github.com/wbhart/mpir
#Git-Web:	https://github.com/wbhart/mpir
Source:         http://mpir.org/%name-%version.tar.bz2
Patch1:         gmp-noexec.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  m4
BuildRequires:  yasm >= 1.3

%description
MPIR is a library for arbitrary precision arithmetic, operating on signed
integers, rational numbers, and floating point numbers. It has a rich set of
functions, and the functions have a regular interface.

%package -n %lname
Summary:        Multiprecision integer library derived from GMP
Group:          System/Libraries

%description -n %lname
MPIR is a library for arbitrary precision arithmetic, operating on signed
integers, rational numbers, and floating point numbers. It has a rich set of
functions, and the functions have a regular interface.

%package -n %lnamexx
Summary:        Multiprecision integer library derived from GMP
Group:          System/Libraries

%description -n %lnamexx
MPIR is a library for arbitrary precision arithmetic, operating on signed
integers, rational numbers, and floating point numbers. It has a rich set of
functions, and the functions have a regular interface.

%package -n libmpir-devel
Summary:        Multiprecision integer library derived from GMP
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       %lnamexx = %version
Requires:       libstdc++-devel
PreReq:         %install_info_prereq

%description -n libmpir-devel
MPIR is an open source multiprecision integer library derived from version
4.2.1 of the GMP.

MPIR is a library for arbitrary precision arithmetic, operating on signed
integers, rational numbers, and floating point numbers. It has a rich set of
functions, and the functions have a regular interface.

This subpackage contains libraries and header files for developing
applications that want to make use of libmpir.

%prep
%setup -qn mpir-3.0.0
%patch -P 1 -p1

%build
# Update configure scripts to modern versions.
autoreconf -fi
export CFLAGS="%optflags -fexceptions"
export CXXFLAGS="%optflags -fexceptions"
# SLES11 %%configure contains --target=, but this is wrong to use.
# Override with empty value to calm the scripts flagging uses of --target.
%ifarch ppc64le
export ABI=mode64
export MPN_PATH=generic
%endif
%ifarch %arm
export MPN_PATH=generic
%endif
%configure --target="" --disable-static --with-yasm=%{_bindir}/yasm  \
	--disable-mpfr --enable-cxx --enable-fat
make %{?_smp_mflags}

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%check
make check %{?_smp_mflags}

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig
%post   -n %lnamexx -p /sbin/ldconfig
%postun -n %lnamexx -p /sbin/ldconfig

%post -n libmpir-devel
%install_info --info-dir=%_infodir %_infodir/%name.info.gz
%install_info --info-dir=%_infodir %_infodir/%name.info-1.gz
%install_info --info-dir=%_infodir %_infodir/%name.info-2.gz

%preun -n libmpir-devel
%install_info_delete --info-dir=%_infodir %_infodir/%name.info.gz
%install_info_delete --info-dir=%_infodir %_infodir/%name.info-1.gz
%install_info_delete --info-dir=%_infodir %_infodir/%name.info-2.gz

%files -n %lname
%defattr(-, root, root)
%_libdir/libmpir.so.*

%files -n %lnamexx
%defattr(-, root, root)
%_libdir/libmpirxx.so.*

%files -n libmpir-devel
%defattr(-, root, root)
%doc README
%license COPYING
%_includedir/*.h
%_libdir/libmpir.so
%_libdir/libmpirxx.so
%_infodir/mpir.info*.gz

%changelog
