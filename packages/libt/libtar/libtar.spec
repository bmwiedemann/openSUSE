#
# spec file for package libtar
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


Name:           libtar
Version:        1.2.20
Release:        0
Summary:        Tar file manipulation API
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            http://www.feep.net/libtar/
Source0:        libtar-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM adding missing headers
Patch1:         libtar-1.2.11-missing-protos.patch
# PATCH-FIX-UPSTREAM two crash avoiding fixes
Patch4:         libtar-1.2.11-mem-deref.patch
# PATCH-FIX-UPSTREAM fix resource leaks
Patch5:         libtar-1.2.20-fix-resource-leaks.patch
# PATCH-FIX-UPSTREAM do not strip on install
Patch6:         libtar-1.2.11-bz729009.patch
# PATCH-FIX-UPSTREAM do not use a static buffer as return value
Patch7:         libtar-1.2.20-no-static-buffer.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  libtool
BuildRequires:  zlib-devel

%description
libtar is a C library for manipulating POSIX tar files. It handles adding
and extracting files to/from a tar archive.

%package -n libtar1
Summary:        Shared library for libtar
Group:          System/Libraries

%description -n libtar1
libtar is a C library for manipulating POSIX tar files. It handles adding
and extracting files to/from a tar archive.

This package contains the shared library needed for libtar.

%package        devel
Summary:        Development files for libtar
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}-%{release}

%description    devel
libtar is a C library for manipulating POSIX tar files. It handles adding
and extracting files to/from a tar archive.

This package contains devel files for libtar.

%prep
%autosetup -p1

# set correct version for .so build
%define ltversion %(echo %{version} | tr '.' ':')
sed -i 's/-rpath $(libdir)/-rpath $(libdir) -version-number %{ltversion}/' \
  lib/Makefile.in

%build
autoreconf -fiv
%configure \
  --disable-static
%make_build

%install
%make_install
# Without this we get no debuginfo and stripping
chmod +x %{buildroot}%{_libdir}/libtar.so.%{version}

%fdupes %{buildroot}%{_mandir}
# we dont want to ship these
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libtar1 -p /sbin/ldconfig
%postun -n libtar1 -p /sbin/ldconfig

%files
%license COPYRIGHT
%doc TODO README ChangeLog*
%{_bindir}/%{name}

%files -n libtar1
%license COPYRIGHT
%{_libdir}/libtar.so.*

%files devel
%license COPYRIGHT
%{_includedir}/libtar.h
%{_includedir}/libtar_listhash.h
%{_libdir}/libtar.so
%{_mandir}/man3/*.3%{?ext_man}

%changelog
