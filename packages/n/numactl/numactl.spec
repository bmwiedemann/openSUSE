#
# spec file for package numactl
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


Name:           numactl
Version:        2.0.12
Release:        0
Summary:        NUMA Policy Control
License:        GPL-2.0-only
Group:          System/Management
Url:            https://github.com/numactl/numactl/releases
Source0:        %{name}-%{version}.tar.gz
Source2:        baselibs.conf
# PATCH-MISSING-TAG -- See http://wiki.opensuse.org/openSUSE:Packaging_Patches_guidelines
Patch0:         revert_date_in_numastat.patch
# PATCH-MISSING-TAG -- See http://wiki.opensuse.org/openSUSE:Packaging_Patches_guidelines
Patch1:         0001-Fixed-segfault-when-no-node-could-be-found-in-sysfs-.patch
Patch2:         numactl-clearcache-pie.patch
%if 0%{?suse_version} > 1110
BuildRequires:  autoconf >= 2.64
BuildRequires:  automake
BuildRequires:  libtool
%endif
Requires:       perl
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExcludeArch:    %arm

%description
Control NUMA policy for individual processes. Offer libnuma for
individual NUMA policy in applications.

%package -n libnuma1
Summary:        NUMA Policy Control
License:        LGPL-2.1-or-later
Group:          Development/Languages/C and C++

%description -n libnuma1
Control NUMA policy for individual processes. Offer libnuma for
individual NUMA policy in applications.

%package -n libnuma-devel
Summary:        NUMA Policy Control
License:        GPL-2.0-only
Group:          Development/Languages/C and C++
Requires:       libnuma1 = %{version}

%description -n libnuma-devel
Control NUMA policy for individual processes. Offer libnuma for
individual NUMA policy in applications.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%define _lto_cflags %{nil}
%if 0%{?suse_version} > 1110
autoreconf -fiv
%endif
%configure \
  --disable-static
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%make_install
rm  %{buildroot}%{_mandir}/man2/move_pages.2*
rm -f %{buildroot}/%{_libdir}/lib*a

%post -n libnuma1 -p /sbin/ldconfig

%postun -n libnuma1 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man8/*

%files -n libnuma1
%defattr(-,root,root)
%{_libdir}/lib*so.*

%files -n libnuma-devel
%defattr(-,root,root)
%{_mandir}/man3/*
%{_includedir}/*
%{_libdir}/lib*so
%{_libdir}/pkgconfig/numa.pc

%changelog
