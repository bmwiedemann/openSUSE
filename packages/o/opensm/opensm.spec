#
# spec file for package opensm
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


%define         git_ver .0.24d2f346ad8e
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%define lib_osm_major 9
%define lib_osmcomp_major 5
%define lib_osmvendor_major 5

Name:           opensm
Summary:        Infiniband Subnet Manager
License:        BSD-2-Clause OR GPL-2.0-only
Group:          Productivity/Networking/System
Version:        3.3.22
Release:        0
Source:         opensm-%{version}%{git_ver}.tar.gz
Source1:        conf.sysconfig
Source2:        %{name}.launch
Source3:        opensm.service
Source4:        baselibs.conf
Patch1:         opensm-remove-date-time.patch
Url:            https://github.com/linux-rdma/opensm
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  libibumad-devel
BuildRequires:  libtool
BuildRequires:  systemd-rpm-macros
PreReq:         %fillup_prereq
Requires:       logrotate
%{?systemd_requires}

%description
OpenSM provides an implementation for an InfiniBand Subnet Manager and
Administration. Such a software entity is required to run for in order
to initialize the InfiniBand hardware (at least one per each InfiniBand
subnet).

%package -n libopensm%{lib_osm_major}
Summary:        Opensm runtime library
Group:          System/Libraries
Obsoletes:      opensm-libs3

%description -n libopensm%{lib_osm_major}
This package contains one of the opensm runtime libraries.

%package -n libosmcomp%{lib_osmcomp_major}
Summary:        Opensm runtime library
Group:          System/Libraries
Obsoletes:      opensm-libs3

%description -n libosmcomp%{lib_osmcomp_major}
This package contains one of the opensm runtime libraries.

%package -n libosmvendor%{lib_osmvendor_major}
Summary:        Opensm runtime library
Group:          System/Libraries
Obsoletes:      opensm-libs3

%description -n libosmvendor%{lib_osmvendor_major}
This package contains one of the opensm runtime libraries.

%package        devel
Summary:        Development files for OpenSM
Group:          Development/Libraries/C and C++
Requires:       libibumad-devel
Requires:       libopensm%{lib_osm_major} = %{version}
Requires:       libosmcomp%{lib_osmcomp_major} = %{version}
Requires:       libosmvendor%{lib_osmvendor_major} = %{version}

%description devel
Symlinks for the dynamic libraries and header files for OpenSM.

%prep
%setup -q -n  %{name}-%{version}%{git_ver}
%patch1

cp %{S:1} %{S:2} %{S:3} .
FAKE_BUILDDATE=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%b %%e %%Y')
FAKE_BUILDTIME=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%H:%%M:%%S')
sed -i -e "s/__DATE__/\"$FAKE_BUILDDATE\"/" -e "s/__TIME__/\"$FAKE_BUILDTIME\"/" opensm/osm_console.c

%build
autoreconf -fi
%configure --disable-static
make %{?_smp_mflags} V=1

%install
export NO_BRP_STALE_LINK_ERROR=yes
make DESTDIR=%{buildroot} install
install -D -m 644 scripts/opensm.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/opensm

# get rid of the included init script because we use a systemd unit file instead
rm -rf %{buildroot}%_sysconfdir/init.d/
install -Dm 644 %{SOURCE3} %{buildroot}%_unitdir/%{name}.service
install -D %{SOURCE2}  %{buildroot}%{_libexecdir}/opensm-launch
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rc%{name}

# install the sysconfig configuration file
install -m 644 -D conf.sysconfig %{buildroot}%{_fillupdir}/sysconfig.%name

# and make a compat link
ln -s %_sysconfdir/sysconfig/opensm %{buildroot}/%_sysconfdir/opensm.conf
sed -i -e 's$-L/usr/src/packages/BUILD/%{name}-%{version}/complib$$g' %{buildroot}%{_libdir}/libosmvendor.la

#we don't package static libraries anymore.
rm -f %{buildroot}%_libdir/lib{opensm,osmcomp,osmvendor}.la

%pre
%service_add_pre opensm.service

%post
%{fillup_only}
%service_add_post opensm.service

%preun
%service_del_preun opensm.service

%postun
%service_del_postun opensm.service

%post   -n libopensm%{lib_osm_major} -p /sbin/ldconfig
%postun -n libopensm%{lib_osm_major} -p /sbin/ldconfig
%post   -n libosmcomp%{lib_osmcomp_major} -p /sbin/ldconfig
%postun -n libosmcomp%{lib_osmcomp_major} -p /sbin/ldconfig
%post   -n libosmvendor%{lib_osmvendor_major} -p /sbin/ldconfig
%postun -n libosmvendor%{lib_osmvendor_major} -p /sbin/ldconfig

%files
%defattr(-, root, root)
%_sysconfdir/opensm.conf
%doc COPYING
%_unitdir/opensm.service
%config %_sysconfdir/logrotate.d/opensm
%_sbindir/*
%{_libexecdir}/opensm-launch
%_mandir/man5/torus-2QoS.conf.5.gz
%_mandir/man8/torus-2QoS.8.gz
%_mandir/man8/opensm.8.gz
%_mandir/man8/osmtest.8.gz
%{_fillupdir}/sysconfig.%name

%files -n libopensm%{lib_osm_major}
%defattr(-, root, root)
%_libdir/libopensm.so.%{lib_osm_major}*

%files -n libosmcomp%{lib_osmcomp_major}
%defattr(-,root,root)
%_libdir/libosmcomp.so.%{lib_osmcomp_major}*

%files -n libosmvendor%{lib_osmvendor_major}
%defattr(-,root,root)
%_libdir/libosmvendor.so.%{lib_osmvendor_major}*

%files devel
%defattr(-,root,root)
%_includedir/infiniband/complib/
%_includedir/infiniband/iba/
%_includedir/infiniband/opensm/
%_includedir/infiniband/vendor/
%_libdir/libopensm.so
%_libdir/libosmcomp.so
%_libdir/libosmvendor.so

%changelog
