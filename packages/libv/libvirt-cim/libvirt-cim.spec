#
# spec file for package libvirt-cim (Version 0.5.14)
#
# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

%if 0%{?suse_version} > 1140 || 0%{?fedora_version} > 14
%define has_systemd 1
%else
%define has_systemd 0
%endif

Name:           libvirt-cim

Url:            http://libvirt.org
License:        LGPL-2.1+
Group:          System/Management
Version:        0.6.3+git92.a5a073c
Release:        0
Summary:        CMPI-based CIM provider implementing DMTF SVPC model
Source:         %{name}-%{version}.tar.gz
Source1:        libvirt-cim-rpmlintrc
Source2:        README.SUSE
Patch1:         0001-provider-reg.patch
Patch2:         0002-automake.patch
Patch3:         0003-fix-bashisms.patch
Patch4:         0004-memory-leaks.patch
Patch5:         0005-include-stdlib.h.patch
Patch6:         0006-drop-base_schema.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  e2fsprogs-devel
BuildRequires:  libcmpiutil-devel > 0.5.4
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  libvirt-devel >= 0.3.2
BuildRequires:  libxml2-devel
BuildRequires:  sblim-cmpi-devel
BuildRequires:  sblim-sfcb
%if 0%{?has_systemd}
BuildRequires:  pkgconfig(systemd)
%{?systemd_requires}
%endif
# the %pre/%post scripts are sfcb specific currently
Requires:       sblim-sfcb
Requires:       libxml2 >= 2.6.0
Requires:       cim-schema >= 2.17
Requires:       unzip
%if 0%{?suse_version} >= 1140
%if 0%{?has_systemd} == 0
Requires:       sysvinit-tools
%endif
%endif
Provides:       xen-cim-cmpi = 0.2.0
Obsoletes:      xen-cim-cmpi < 0.2.0

%description
Libvirt-cim is a CMPI CIM provider that implements the DMTF SVPC
virtualization model. The goal is to support most of the features
exported by libvirt itself, enabling management of multiple platforms
with a single provider.

%define REGISTRATION %{_datadir}/%{name}/*.registration
%define SCHEMA %{_datadir}/%{name}/*.mof
%define INTEROP_REG %{_datadir}/%{name}/{RegisteredProfile,ElementConformsToProfile,ReferencedProfile}.registration
%define INTEROP_MOF %{_datadir}/%{name}/{ComputerSystem,HostSystem,RegisteredProfile,DiskPool,MemoryPool,NetPool,ProcessorPool,VSMigrationService,ElementConformsToProfile,ReferencedProfile,AllocationCapabilities}.mof
%define CIMV2_REG %{_datadir}/%{name}/{HostedResourcePool,ElementCapabilities,HostedService,HostedDependency,ElementConformsToProfile,HostedAccessPoint}.registration
%define CIMV2_MOF %{_datadir}/%{name}/{HostedResourcePool,ElementCapabilities,HostedService,HostedDependency,RegisteredProfile,ComputerSystem,ElementConformsToProfile,HostedAccessPoint}.mof

%prep
%autosetup -p1
chmod -x src/* libxkutil/* schema/* README doc/* base_schema/README*
chmod +X src/* libxkutil/* schema/*

%build
autoreconf -i -f
%configure --disable-werror --disable-static
make %{?_smp_mflags} DOCS_DIR=%{_docdir}/%{name} HTML_DIR=%{_docdir}/%{name}

%install
%if 0%{?suse_version}
%make_install DOCS_DIR=%{_docdir}/%{name} HTML_DIR=%{_docdir}/%{name}
install -m 644 %{S:2} $RPM_BUILD_ROOT%{_docdir}/%{name}
%else
make install DESTDIR=$RPM_BUILD_ROOT DOCS_DIR=%{_docdir}/%{name}-%{version} HTML_DIR=%{_docdir}/%{name}-%{version}
install -m 644 %{S:2} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%endif
%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/*.{a,la}
%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/cmpi/*.{a,la}
%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/libxkutil.so
#%{__rm} -rf $RPM_BUILD_ROOT%{_docdir}/%{name}
#%{__rm} -f $RPM_BUILD_ROOT%{_datadir}/%{name}/install_base_schema.sh
#%{__rm} -f $RPM_BUILD_ROOT%{_datadir}/%{name}/cimv216-interop_mof
#%{__rm} -f $RPM_BUILD_ROOT%{_datadir}/%{name}/cimv216Experimental-MOFs.zip
#%{__rm} -f $RPM_BUILD_ROOT%{_datadir}/%{name}/fix_schema.patch
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/libvirt/cim

%pre
# unregister current providers on upgrade only
if [ $1 -eq 2 ]; then
%{_datadir}/%{name}/provider-register.sh -d -t sfcb \
	-n root/virt \
	-r %{REGISTRATION} -m %{SCHEMA} >/dev/null 2>&1 || true
fi

%post
/sbin/ldconfig
# Register libvirt-cim on the sfcb's providers list
%{_datadir}/%{name}/provider-register.sh -t sfcb \
        -n root/virt \
        -r %{REGISTRATION} -m %{SCHEMA} >/dev/null 2>&1 || true
# Register some of our providers under other namespaces too? ok.
%{_datadir}/%{name}/provider-register.sh -t sfcb \
        -n root/interop \
        -r %{INTEROP_REG} -m %{INTEROP_MOF} -v >/dev/null 2>&1 || true
%{_datadir}/%{name}/provider-register.sh -t sfcb \
        -n root/cimv2\
        -r %{CIMV2_REG} -m %{CIMV2_MOF} -v >/dev/null 2>&1 || true
# Restart the sfcb to update its providers list
if test -x /usr/sbin/sfcbd ; then
%if 0%{?has_systemd}
  systemctl try-restart sblim-sfcb.service >/dev/null 2>&1 || :
%else
  /etc/init.d/sfcb restart
%endif
fi

%preun
# unregister our providers only on uninstall
if [ $1 -eq 0 ]; then
%{_datadir}/%{name}/provider-register.sh -d -t sfcb \
	-n root/virt \
	-r %{REGISTRATION} -m %{SCHEMA} >/dev/null 2>&1 || true
fi

%postun
/sbin/ldconfig
# Restart the sfcb to update its providers list
if test -x /usr/sbin/sfcbd ; then
%if 0%{?has_systemd}
  systemctl try-restart sblim-sfcb.service >/dev/null 2>&1 || :
%else
  /etc/init.d/sfcb restart
%endif
fi

%files
%defattr(-, root, root)
%dir %{_datadir}/%{name}
%config(noreplace) %{_sysconfdir}/libvirt-cim.conf
%{_libdir}/lib*.so*
%{_libdir}/cmpi/lib*.so*
%{_datadir}/%{name}/*.sh
%{_datadir}/%{name}/*.mof
%{_datadir}/%{name}/*.registration
%dir %attr(0700, root, root) %{_sysconfdir}/libvirt
%dir %attr(0700, root, root) %{_sysconfdir}/libvirt/cim
%if 0%{?suse_version}
%doc %{_docdir}/%{name}
%doc COPYING README
%else
%doc %{_docdir}/%{name}-%{version}
%endif

%changelog
