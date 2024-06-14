#
# spec file for package booth
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


%bcond_with html_man

%bcond_with glue

%global uname hacluster
%global gname haclient

%global test_path   	%{_datadir}/booth/tests

%define _libexecdir %{_libdir}
%define _fwdefdir %{_prefix}/lib/firewalld/services

Name:           booth
Version:        1.2+git0.322fea0
Release:        0
Summary:        Ticket Manager for Multi-site Clusters
License:        GPL-2.0-or-later
Group:          Productivity/Clustering/HA
URL:            https://github.com/ClusterLabs/booth
Source:         %{name}-%{version}.tar.bz2
Source1:        %{name}-rpmlintrc
Patch1:         harden_booth-arbitrator.service.patch
BuildRequires:  asciidoc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  firewall-macros
BuildRequires:  libgcrypt-devel
%if 0%{?with_glue}
BuildRequires:  cluster-glue-devel
%else
# logging provider
BuildRequires:  pkgconfig(libqb)
# nametag provider
BuildRequires:  pkgconfig(libsystemd)
%endif
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pacemaker)
BuildRequires:  pkgconfig(zlib)
Requires:       pacemaker-ticket-support >= 2.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Booth manages tickets which authorize cluster sites located in
geographically dispersed locations to run resources. It
facilitates support of geographically distributed clustering in
Pacemaker.

%package test
Summary:        Test scripts for Booth
Group:          Productivity/Clustering/HA
Requires:       booth
Requires:       python3

%description test
This package contains automated tests for Booth,
the Cluster Ticket Manager for Pacemaker.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
autoreconf -fvi
%configure \
    --with-initddir=%{_initddir} \
    --docdir=%{_docdir}/%{name} \
    %{!?with_html_man:--without-html_man} \
    %{!?with_glue:--without-glue}
make %{?_smp_mflags}

%install
%make_install

ln -s boothd.8 %{buildroot}/%{_mandir}/man8/booth.8

# systemd
mkdir -p %{buildroot}/%{_unitdir}
cp -a conf/booth@.service %{buildroot}/%{_unitdir}/booth@.service
cp -a conf/booth-arbitrator.service %{buildroot}/%{_unitdir}/booth-arbitrator.service
ln -s service %{buildroot}%{_sbindir}/rcbooth-arbitrator

#install test-parts
mkdir -p %{buildroot}/%{test_path}/conf
cp -a test %{buildroot}/%{test_path}/
cp -a conf/booth.conf.example %{buildroot}/%{test_path}/conf/
chmod +x %{buildroot}/%{test_path}/test/booth_path
chmod +x %{buildroot}/%{test_path}/test/live_test.sh

mkdir -p %{buildroot}/%{test_path}/src/
ln -s %{_sbindir}/boothd %{buildroot}/%{test_path}/src/
rm -f %{buildroot}/%{test_path}/test/*.pyc

%if 0%{?suse_version}
#Firewalld rule
mkdir -p $RPM_BUILD_ROOT/%{_fwdefdir}
install -m 644 contrib/geo-cluster.firewalld.xml $RPM_BUILD_ROOT/%{_fwdefdir}/booth.xml
%endif

%pre
%service_add_pre booth-arbitrator.service

%post
#Reload firewalld if already installed
if [ -e /usr/sbin/firewalld ]; then
    %firewalld_reload
fi
%service_add_post booth-arbitrator.service

%preun
%service_del_preun booth-arbitrator.service

%postun
%service_del_postun booth-arbitrator.service

%files
%defattr(-,root,root,-)
%{_sbindir}/booth
%{_sbindir}/boothd
%{_sbindir}/booth-keygen
%{_sbindir}/geostore
%{_mandir}/man8/booth.8%{ext_man}
%{_mandir}/man8/boothd.8%{ext_man}
%{_mandir}/man8/booth-keygen.8%{ext_man}
%{_mandir}/man8/geostore.8%{ext_man}
%dir %{_prefix}/lib/ocf
%dir %{_prefix}/lib/ocf/resource.d
%dir %{_prefix}/lib/ocf/resource.d/pacemaker
%dir %{_prefix}/lib/ocf/resource.d/booth
%dir %{_prefix}/lib/ocf/lib
%dir %{_prefix}/lib/ocf/lib/booth
%dir %attr (755, %{uname}, %{gname}) %{_sysconfdir}/booth
%{_sbindir}/rcbooth-arbitrator
%{_prefix}/lib/ocf/resource.d/pacemaker/booth-site
%{_prefix}/lib/ocf/lib/booth/geo_attr.sh
%{_prefix}/lib/ocf/resource.d/booth/geostore
%config %attr (644, %{uname}, %{gname}) %{_sysconfdir}/booth/booth.conf.example
%if 0%{?suse_version}
%dir %{_prefix}/lib/firewalld
%dir %{_fwdefdir}
%{_fwdefdir}/booth.xml
%endif
%{_unitdir}/booth@.service
%{_unitdir}/booth-arbitrator.service
%exclude %{_initddir}/booth-arbitrator
%dir %{_datadir}/booth
%{_datadir}/booth/service-runnable
%doc AUTHORS README COPYING
%doc README.upgrade-from-v0.1
/usr/share/pkgconfig/booth.pc

%dir %attr (750, %{uname}, %{gname}) %{_var}/lib/booth/
%dir %attr (750, %{uname}, %{gname}) %{_var}/lib/booth/cores

%files test
%defattr(-,root,root)
/usr/share/doc/packages/booth/README-testing
%{test_path}
%dir %{_prefix}/lib/ocf
%dir %{_prefix}/lib/ocf/resource.d
%dir %{_prefix}/lib/ocf/resource.d/booth
%{_prefix}/lib/ocf/resource.d/booth/sharedrsc

%changelog
