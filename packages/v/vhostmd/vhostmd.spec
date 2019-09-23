#
# spec file for package vhostmd
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


%define with_xen        0%{!?_without_xen:1}

# Xen is available only on x86_64
%ifnarch x86_64
%define with_xen        0
%endif

Name:           vhostmd
Version:        1.1
Release:        0
Summary:        Virtual Host Metrics Daemon (vhostmd)
License:        LGPL-2.1-or-later
Group:          System/Daemons
Url:            https://github.com/vhostmd/vhostmd
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        vhostmd-%{version}.tar.bz2
Patch0:         vhostmd-conf.patch
Patch1:         manpage.patch
Patch2:         value-newline.patch
Patch3:         libmetrics-link.patch
BuildRequires:  libtool
BuildRequires:  libvirt-devel
BuildRequires:  libxml2
BuildRequires:  libxml2-devel
BuildRequires:  pkg-config
BuildRequires:  systemd
%{?systemd_requires}
%if %{with_xen}
BuildRequires:  xen-devel
%endif
PreReq:         coreutils

%description
vhostmd provides a "metrics communication channel" between a host and
its hosted virtual machines, allowing limited introspection of host
resource usage from within virtual machines.

%package -n     vm-dump-metrics
Summary:        Virtual Host Metrics Daemon (vhostmd)
Group:          System/Monitoring

%description -n vm-dump-metrics
vhostmd provides a "metrics communication channel" between a host and
its hosted virtual machines, allowing limited introspection of host
resource usage from within virtual machines.

%package -n     libmetrics0
Summary:        Virtual Host Metrics Daemon (vhostmd)
Group:          System/Libraries

%description -n libmetrics0
vhostmd provides a "metrics communication channel" between a host and
its hosted virtual machines, allowing limited introspection of host
resource usage from within virtual machines.

%package -n     libmetrics-devel
Summary:        Virtual Host Metrics Daemon (vhostmd)
Group:          Development/Libraries/C and C++
Requires:       libmetrics0 = %{version}

%description -n libmetrics-devel
vhostmd provides a "metrics communication channel" between a host and
its hosted virtual machines, allowing limited introspection of host
resource usage from within virtual machines.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%if ! %{with_xen}
%define _disable_libxenstat --disable-libxenstat
%define _disable_xenctrl --disable-xenctrl
%endif

autoreconf -fi
%configure --without-xenstore \
     %{?_disable_libxenstat}  \
     %{?_disable_xenctrl}
make

%install
%make_install
rm -f %{buildroot}/%{_libdir}/*.la %{buildroot}/%{_libdir}/*.a
ln -s %{_sbindir}/service %{buildroot}/%{_sbindir}/rcvhostmd

%pre
%service_add_pre vhostmd.service

%post
%service_add_post vhostmd.service

%preun
%service_del_preun vhostmd.service

%postun
%service_del_postun vhostmd.service

%post   -n libmetrics0 -p /sbin/ldconfig
%postun -n libmetrics0 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%dir /etc/vhostmd
%dir %{_datadir}/vhostmd
%dir %{_datadir}/vhostmd/scripts
%dir %{_datadir}/doc/vhostmd
%{_sbindir}/vhostmd
%{_sbindir}/rcvhostmd
%{_datadir}/vhostmd/scripts/pagerate.pl
%config(noreplace) /etc/vhostmd/vhostmd.conf
%config /etc/vhostmd/vhostmd.dtd
%config /etc/vhostmd/metric.dtd
%{_unitdir}/vhostmd.service
%{_datadir}/doc/vhostmd/vhostmd.dtd
%{_datadir}/doc/vhostmd/metric.dtd
%{_datadir}/doc/vhostmd/vhostmd.xml
%{_datadir}/doc/vhostmd/mdisk.xml
%{_datadir}/doc/vhostmd/README
%{_datadir}/man/man8/vhostmd.8.gz

%files -n vm-dump-metrics
%defattr(-,root,root)
%{_sbindir}/vm-dump-metrics
%{_datadir}/man/man1/vm-dump-metrics.1.gz

%files -n libmetrics0
%defattr(-,root,root)
%{_libdir}/libmetrics.so.*

%files -n libmetrics-devel
%defattr(-,root,root)
%{_libdir}/libmetrics.so
%dir %{_includedir}/vhostmd
%{_includedir}/vhostmd/libmetrics.h

%changelog
