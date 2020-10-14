#
# spec file for package libfabric
#
# Copyright (c) 2020 SUSE LLC
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
%define git_ver .0.6c51de3d7817

Name:           libfabric
Version:        1.11.1
Release:        0
Summary:        User-space RDMA Fabric Interfaces
License:        GPL-2.0-only OR BSD-2-Clause
Group:          Development/Libraries/C and C++
Source:         %{name}-%{version}%{git_ver}.tar.bz2
Source1:        baselibs.conf
Patch0:         libfabric-libtool.patch
URL:            http://www.github.com/ofiwg/libfabric
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libibverbs-devel
BuildRequires:  libnl3-devel
%ifarch x86_64
BuildRequires:  libpsm2-devel
%endif
%ifarch x86_64 %{ix86}
BuildRequires:  infinipath-psm-devel
%endif
BuildRequires:  fdupes
BuildRequires:  librdmacm-devel
BuildRequires:  libtool
BuildRequires:  pkg-config
%define lib_major 1

%description
libfabric provides a user-space API to access high-performance fabric
services, such as RDMA. This package only contains the fi_info binary.

%package       -n libfabric%{lib_major}
Summary:        User-space RDMA fabric interfaces
Group:          System/Libraries

%description -n libfabric%{lib_major}
libfabric provides a user-space API to access high-performance fabric
services, such as RDMA. This package contains the runtime library.


%package        devel
Summary:        Development files for the libfabric library
Group:          Development/Libraries/C and C++
Requires:       libfabric%{lib_major} = %{version}

%description    devel
libfabric provides a user-space API to access high-performance fabric
services, such as RDMA. This package contains the development files.

%prep
%setup -q -n  %{name}-%{version}%{git_ver}
%patch0 -p1

%build
%define _lto_cflags %{nil}
rm -f config/libtool.m4
autoreconf -fi
# defaults: with-dlopen and without-valgrind can be over-rode:
%configure %{?_without_dlopen} %{?_with_valgrind} \
	--enable-sockets --enable-verbs --enable-usnic \
%ifarch x86_64 %{ix86}
    --enable-psm \
%endif
%ifarch x86_64
    --enable-psm2 \
%endif
    --disable-static
make %{?_smp_mflags}

%install
%make_install

# remove unpackaged files from the buildroot
rm -f %{buildroot}%{_libdir}/*.la
%fdupes %{buildroot}/%{_prefix}

%post -n libfabric%{lib_major} -p /sbin/ldconfig
%postun -n libfabric%{lib_major} -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
%doc NEWS.md
%license COPYING

%files -n libfabric%{lib_major}
%defattr(-,root,root,-)
%{_libdir}/%{name}.so.%{lib_major}*
%doc AUTHORS README
%license COPYING

%files devel
%defattr(-,root,root)
%{_libdir}/%{name}.so
%dir %{_includedir}/rdma
%{_includedir}/rdma/fabric.h
%{_includedir}/rdma/fi_atomic.h
%{_includedir}/rdma/fi_cm.h
%{_includedir}/rdma/fi_collective.h
%{_includedir}/rdma/fi_domain.h
%{_includedir}/rdma/fi_eq.h
%{_includedir}/rdma/fi_rma.h
%{_includedir}/rdma/fi_endpoint.h
%{_includedir}/rdma/fi_errno.h
%{_includedir}/rdma/fi_tagged.h
%{_includedir}/rdma/fi_trigger.h
%{_includedir}/rdma/fi_ext_usnic.h
%{_mandir}/man3/*
%{_mandir}/man7/*

%{_libdir}/pkgconfig/%{name}.pc

%changelog
