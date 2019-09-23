#
# spec file for package libpng12
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


#
%define major   1
%define minor   2
%define micro   59
%define branch  %{major}%{minor}
%define libname libpng%{branch}-0

Name:           libpng12
Url:            http://www.libpng.org/pub/png/libpng.html
Version:        %{major}.%{minor}.%{micro}
Release:        0
Summary:        Library for the Portable Network Graphics Format (PNG)
License:        Zlib
Group:          Development/Libraries/C and C++
Source:         http://downloads.sourceforge.net/project/libpng/%{name}/%{version}/libpng-%{version}.tar.xz
Source2:        baselibs.conf
Patch0:         libpng-1.2.51-CVE-2013-7353.patch
Patch1:         libpng-1.2.51-CVE-2013-7354.patch
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%define debug_package_requires %{libname} = %{version}-%{release}

%package -n %{libname}

Summary:        Library for the Portable Network Graphics Format (PNG)
# bug437293
Group:          System/Libraries
%ifarch ppc64
Obsoletes:      libpng-64bit
%endif
#
Obsoletes:      libpng < %{version}
Provides:       libpng = %{version}-%{release}

%package devel
Summary:        Development tools for applications which will use libpng
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       glibc-devel
Requires:       pkg-config
Requires:       zlib-devel
Recommends:     libpng%{branch}-compat-devel
# bug437293
%ifarch ppc64
Obsoletes:      libpng-devel-64bit
%endif
#

%package compat-devel
Summary:        Development tools for applications which will use libpng
Group:          Development/Libraries/C and C++
Requires:       libpng%{branch}-devel = %{version}
Provides:       libpng-devel = %{version}
Obsoletes:      libpng-devel < 1.2.43
Conflicts:      otherproviders(libpng-devel)

%description
libpng is the official reference library for the Portable Network
Graphics format (PNG).

%description -n %{libname}
libpng is the official reference library for the Portable Network
Graphics format (PNG).

%description devel
The libpng%{branch}-devel package includes the header files, libraries,
configuration files and development tools necessary for compiling and
linking programs which will manipulate PNG files using libpng%{branch}.

libpng is the official reference library for the Portable Network
Graphics (PNG) format.

%description compat-devel
The libpng%{branch}-compat-devel package contains unversioned symlinks 
to the header files, libraries, configuration files and development 
tools necessary for compiling and linking programs that don't care 
about libpng version.

%prep
%setup -n libpng-%{version}
%patch0 
%patch1

%build
# PNG_SAFE_LIMITS_SUPPORTED: http://www.openwall.com/lists/oss-security/2015/01/10/1
export CFLAGS="%optflags -O3 -DPNG_SAFE_LIMITS_SUPPORTED -DPNG_SKIP_SETJMP_CHECK $(getconf LFS_CFLAGS)"
export LDFLAGS="-Wl,-z,relro,-z,now"

%configure \
              --disable-static \
              --with-libpng-compat=no
make %{?_smp_mflags}

%check
make -j1 check

%install
make install DESTDIR=$RPM_BUILD_ROOT 
rm $RPM_BUILD_ROOT/%{_libdir}/libpng*.la

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libpng%{branch}.so.*

%files devel
%defattr(-,root,root)
%{_bindir}/libpng%{branch}-config
%{_includedir}/libpng%{branch}
%{_libdir}/libpng%{branch}.so
%{_libdir}/pkgconfig/libpng%{branch}.pc
%doc CHANGES README TODO ANNOUNCE LICENSE libpng-*.txt

%files compat-devel
%defattr(-,root,root)
%{_bindir}/libpng-config
%{_includedir}/*.h
%{_libdir}/libpng.so
%{_libdir}/pkgconfig/libpng.pc
%doc %{_mandir}/man3/libpng.3.gz
%doc %{_mandir}/man3/libpngpf.3.gz
%doc %{_mandir}/man5/png.5.gz

%changelog
