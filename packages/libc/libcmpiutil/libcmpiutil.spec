#
# spec file for package libcmpiutil
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


Name:           libcmpiutil
Version:        0.5.7+git3.cd438a8
Release:        0
Summary:        Library of utility functions for CMPI providers
License:        LGPL-2.1-or-later
URL:            http://libvirt.org/sources/CIM/
Group:          Development/Libraries/C and C++
Source:         %{name}-%{version}.tar.gz
Patch1:         0001-fix-ARM-build.patch
Patch2:         0002-drop-duplicate-definition-of-_FORTIFY_SOURCE.patch
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libtool
BuildRequires:  libxml2-devel
%if 0%{?fedora_version} || 0%{?centos_version} || 0%{?rhel_version} || 0%{?fedora} || 0%{?rhel}
BuildRequires:  pkgconfig
%else
%if 0%{?suse_version} < 920
BuildRequires:  pkgconfig
%else
BuildRequires:  pkg-config
%endif
%endif
BuildRequires:  sblim-cmpi-devel
# SLE11
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Libcmpiutil is a library of utility functions for CMPI providers.  The
goal is to reduce the amount of repetitive work done in most CMPI
providers by encapsulating common procedures with more "normal" APIs.
This extends from operations like getting typed instance properties to
standardizing method dispatch and argument checking.

%package -n libcmpiutil0
Summary:        Library of utility functions for CMPI providers
Group:          Development/Libraries/C and C++
Obsoletes:      libcmpiutil < %{version}-%{release}
Provides:       libcmpiutil

%description -n libcmpiutil0
Libcmpiutil is a library of utility functions for CMPI providers.  The
goal is to reduce the amount of repetitive work done in most CMPI
providers by encapsulating common procedures with more "normal" APIs.
This extends from operations like getting typed instance properties to
standardizing method dispatch and argument checking.

%package devel
Summary:        Library of utility functions for CMPI providers
Group:          Development/Libraries/C and C++
Requires:       libcmpiutil0 = %{version}-%{release}
Requires:       sblim-cmpi-devel

%description devel
Libcmpiutil is a library of utility functions for CMPI providers.  The
goal is to reduce the amount of repetitive work done in most CMPI
providers by encapsulating common procedures with more "normal" APIs.
This extends from operations like getting typed instance properties to
standardizing method dispatch and argument checking.

%prep
%setup -q
%ifarch %arm
%patch -P 1 -p1
%endif
%patch -P 2 -p1
chmod -x *.c *.y *.h *.l

%build
export CFLAGS="%{optflags} -fgnu89-inline"
rm -f aclocal.m4 configure Makefile.in
touch AUTHORS ChangeLog NEWS
autoupdate acinclude.m4 configure.ac Makefile.am
autoreconf -fi
%configure --enable-static=no
%if 0%{?make_build:1}
%make_build
%else
make %{?_smp_mflags}
%endif

%install
%makeinstall
rm -f %{buildroot}/%{_libdir}/*.{a,la}

%post   -n libcmpiutil0 -p /sbin/ldconfig
%postun -n libcmpiutil0 -p /sbin/ldconfig

%files -n libcmpiutil0
%defattr(-, root, root, -)
%doc doc/doxygen.conf doc/mainpage README COPYING
%{_libdir}/lib*.so.*

%files devel
%defattr(-, root, root, -)
%{_libdir}/lib*.so
%dir %{_includedir}/libcmpiutil
%{_includedir}/libcmpiutil/*.h
%{_libdir}/pkgconfig/libcmpiutil.pc
%doc doc/SubmittingPatches

%changelog
