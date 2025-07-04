#
# spec file for package libfabric
#
# Copyright (c) 2025 SUSE LLC
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
%define git_ver .0.cf173800a

%ifarch aarch64 %power64 x86_64 s390x
%if 0%{?suse_version} > 1530
%define with_ucx 1
%endif
%define with_efa 1
%endif

Name:           libfabric
Version:        2.1.0
Release:        0
Summary:        User-space RDMA Fabric Interfaces
License:        BSD-2-Clause OR GPL-2.0-only
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
BuildRequires:  libnuma-devel
BuildRequires:  libpsm2-devel
%endif
BuildRequires:  fdupes
BuildRequires:  librdmacm-devel
BuildRequires:  libtool
%if 0%{?with_ucx}
BuildRequires:  libucm-devel
BuildRequires:  libucp-devel
 # 1.10 Needed for UCS_MEMORY_TYPE_UNKNOWN
BuildRequires:  libucs-devel >= 1.10
BuildRequires:  libuct-devel
%endif
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
%autosetup -p0 -n  %{name}-%{version}%{git_ver}

%build
export CFLAGS=-Wno-incompatible-pointer-types
rm -f config/libtool.m4
autoreconf -fi
# defaults: with-dlopen and without-valgrind can be over-rode:
%configure %{?_without_dlopen} %{?_with_valgrind} \
	--enable-sockets --enable-verbs --enable-usnic \
%if 0%{?with_efa}
        --enable-efa \
%endif
%if 0%{?with_ucx}
        --enable-ucx \
%endif
%ifarch x86_64
    --enable-psm2 \
    --enable-psm3 \
%endif
    --disable-static
%make_build

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
%{_includedir}/rdma/fi_endpoint.h
%{_includedir}/rdma/fi_eq.h
%{_includedir}/rdma/fi_errno.h
%{_includedir}/rdma/fi_ext.h
%{_includedir}/rdma/fi_profile.h
%{_includedir}/rdma/fi_rma.h
%{_includedir}/rdma/fi_tagged.h
%{_includedir}/rdma/fi_trigger.h
%dir %{_includedir}/rdma/providers
%{_includedir}/rdma/providers/fi_log.h
%{_includedir}/rdma/providers/fi_peer.h
%{_includedir}/rdma/providers/fi_prov.h
%{_includedir}/rdma/fi_ext_usnic.h
%ifarch x86_64
%{_includedir}/rdma/fi_ext_psm2.h
%endif
%if 0%{?with_efa}
%{_includedir}/rdma/fi_ext_efa.h
%endif
%{_mandir}/man3/*
%{_mandir}/man7/*

%{_libdir}/pkgconfig/%{name}.pc

%changelog
