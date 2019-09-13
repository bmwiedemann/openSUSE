#
# spec file for package apr
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


%define         aprver 1
%define         libname lib%{name}%{aprver}
%define         installbuilddir %{_libdir}/apr-%{aprver}/build
%define         includedir %{_includedir}/apr-%{aprver}
Name:           apr
Version:        1.7.0
Release:        0
Summary:        Apache Portable Runtime (APR) Library
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://apr.apache.org/
Source0:        https://www.apache.org/dist/apr/apr-%{version}.tar.bz2
Source1:        https://www.apache.org/dist/apr/apr-%{version}.tar.bz2.asc
Source2:        %{name}.keyring
Patch5:         apr-visibility.patch
Patch9:         apr-proc-mutex-map-anon.patch
# prevent random failures of the testsuite (sendfile test)
Patch10:        apr-test-sendfile-timeout.patch
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  lksctp-tools-devel
# for the testsuite
BuildRequires:  netcfg
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
APR is Apache's Portable Runtime Library, designed to be a support
library that provides a predictable and consistent interface to
underlying platform-specific implementations.

%package -n %{libname}
Summary:        Apache Portable Runtime (APR) Library
Group:          System/Libraries

%description -n %{libname}
APR is Apache's Portable Runtime Library, designed to be a support
library that provides a predictable and consistent interface to
underlying platform-specific implementations.

The range of platform-spanning functionality provided by APR
includes: Memory allocation and memory pool functionality, atomic
operations, dynamic library handling, file I/O, command-argument
parsing, locking, hash tables and arrays, mmap functionality, network
sockets and protocols, threads, process and mutex functionality,
shared memory functionality, time routines, as well as user and group
ID services.

%package devel
Summary:        Development files for the Apache Portable Runtime (APR) library
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Provides:       %{libname}-devel = %{version}
Obsoletes:      %{libname}-devel < %{version}-%{release}

%description devel
APR is Apache's Portable Runtime Library, designed to be a support
library that provides a predictable and consistent interface to
underlying platform-specific implementations.

This subpackage contains header files for developing applications
that want to make use of APR.

%prep
%setup -q
%patch5 -p1
%patch9 -p1
%patch10 -p1

# Do not put date to doxy content
sed -i \
	-e '4 iHTML_TIMESTAMP=NO' \
	docs/doxygen.conf

%build
autoreconf -fiv
%configure \
	--enable-other-child \
	--with-installbuilddir=%{installbuilddir} \
	--includedir=%{includedir} \
%ifarch %{ix86}
	--enable-nonportable-atomics=yes \
%endif
	--with-devrandom=/dev/urandom \
	--disable-static \
	--enable-posix-shm \
	--with-sendfile
make %{?_smp_mflags} CFLAGS="%{optflags} -DREADDIR_IS_THREAD_SAFE -fvisibility=hidden -fPIC"
make dox %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install %{?_smp_mflags}
# Move docs to more convenient location
mv docs/dox/html html
# Unpackaged files:
rm -f %{buildroot}/%{_libdir}/apr.exp
rm -f %{buildroot}%{_libdir}/libapr-%{aprver}.la

# Trim exported dependecies
sed -ri '/^LIBS=/{s,-l(uuid|crypt) ,,g;s/  */ /g}' \
      %{buildroot}%{_bindir}/apr-%{aprver}-config
sed -ri '/^Libs/{s,-l(uuid|crypt) ,,g}' \
      %{buildroot}%{_libdir}/pkgconfig/apr-%{aprver}.pc

%fdupes %{buildroot}

%check
%if ! 0%{?qemu_user_space_build}
%ifarch ppc ppc64 ppc64le
make check -j1 || { echo "ignore PowerPC transient test failures"; exit 0; }
%else
make check -j1
%endif
%endif

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root,-)
%doc CHANGES
%if 0%{?suse_version} > 1315
%license LICENSE
%else
%doc LICENSE
%endif
%doc NOTICE
%{_libdir}/libapr-%{aprver}.so.*
# Do NOT move to devel as this is utilized by Tomcat
%{_libdir}/libapr-%{aprver}.so

%files devel
%defattr(-,root,root,-)
%doc docs/APRDesign.html
%doc docs/canonical_filenames.html
%doc docs/incomplete_types
%doc docs/non_apr_programs
%doc html
%doc emacs-mode
%{includedir}
%{_bindir}/apr-%{aprver}-config
%{_libdir}/pkgconfig/apr-%{aprver}.pc
%{_libdir}/apr-%{aprver}

%changelog
