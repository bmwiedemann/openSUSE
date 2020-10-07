#
# spec file for package libvma
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
%define git_ver .0.0ed40128ffc0
%define lib_major 9

Name:           libvma
Summary:        A library for boosting TCP and UDP traffic (over RDMA hardware)
License:        GPL-2.0-only OR BSD-2-Clause
Group:          Development/Libraries/C and C++
Version:        9.1.2
Release:        0
Source0:        %{name}-%{version}%{git_ver}.tar.gz
Source1:        vma.service
URL:            https://github.com/Mellanox/libvma
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libibverbs-devel
BuildRequires:  librdmacm-devel
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libnl-3.0)
Requires:       libvma%{lib_major} = %{version}
ExclusiveArch:  x86_64 aarch64 ppc64le

%description
VMA library is a performance booster of TCP and UDP traffic
Part of Mellanox enhanced services
Allows application written over standard socket API
To run over Infiniband/Ethernet from userspace with full network stack bypass
and get better throughput, latency and packets/sec rate

%package       -n libvma%{lib_major}
Summary:        Libvma runtime libary
Group:          System/Libraries

%description -n libvma%{lib_major}
VMA library is a performance booster of TCP and UDP traffic
Part of Mellanox enhanced services
Allows application written over standard socket API
To run over Infiniband/Ethernet from userspace with full network stack bypass
and get better throughput, latency and packets/sec rate

%package        devel
Summary:        Header files and link required to develop with Libvma
Group:          Development/Libraries/C and C++
Requires:       libvma%{lib_major} = %{version}

%description devel
Headers and symbolink link required to compile and link with the Libvma library.

%prep
%setup -q -n  %{name}-%{version}%{git_ver}

%build
./autogen.sh
export CXXFLAGS="%optflags -Wno-address-of-packed-member"
%configure --docdir=%{_docdir}/%{name}
make %{?_smp_mflags} V=1

%install
make DESTDIR=%{buildroot} install
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}/etc/init.d/vma
rm -f %{buildroot}/etc/systemd/system/vma.service

install -D -m 755 tests/vma_perf_envelope/vma_perf_envelope.sh %{buildroot}/%{_datadir}/%{name}/vma_perf_envelope.sh
install -m 644 src/vma/vma_extra.h %{buildroot}/%{_includedir}/mellanox/vma_extra.h
install -m 644 src/vma/util/libvma.conf %{buildroot}/%{_sysconfdir}/
install -s -m 755 src/stats/vma_stats %{buildroot}/%{_bindir}/vma_stats
install -s -m 755 tools/daemon/vmad %{buildroot}/%{_sbindir}/vmad
install -D -m 644 %{S:1} %{buildroot}%{_unitdir}/vma.service

for service in vma; do ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc${service}; done

%post -n libvma%{lib_major} -p /sbin/ldconfig
%postun -n libvma%{lib_major} -p /sbin/ldconfig

%pre
%service_add_pre vma.service

%post
%service_add_post vma.service

%preun
%service_del_preun vma.service

%postun
%service_del_postun vma.service

%files
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/README.txt
%{_docdir}/%{name}/journal.txt
%{_docdir}/%{name}/VMA_VERSION
%config(noreplace) %{_sysconfdir}/libvma.conf
%config %{_sysconfdir}/security/limits.d/30-libvma-limits.conf
%{_sbindir}/vmad
%{_sbindir}/vma
%{_sbindir}/rcvma
%{_unitdir}/vma.service
%{_bindir}/vma_stats
%{_datadir}/%{name}/vma_perf_envelope.sh
%{_mandir}/man*/*
%license COPYING

%files -n libvma%{lib_major}
%{_libdir}/%{name}*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/mellanox
%{_libdir}/%{name}.so

%changelog
