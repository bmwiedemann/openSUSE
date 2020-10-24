#
# spec file for package ndctl
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2015 Intel Corporation
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


%define lname libndctl6
%define dname libndctl-devel
Name:           ndctl
Version:        70.1
Release:        0
Summary:        Manage "libnvdimm" subsystem devices (Non-volatile Memory)
License:        GPL-2.0-only
Group:          Hardware/Other
URL:            https://github.com/pmem/ndctl
Source0:        https://github.com/pmem/ndctl/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch9:         %{name}-namespace-skip-zero-namespaces-when-processing.patch
Patch13:        %{name}-namespace-Suppress-ENXIO-when-processing-all-n.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  keyutils-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  xmlto
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(json)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libkmod)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(uuid)
ExclusiveArch:  x86_64 ppc64le
%{?systemd_requires}
# required for documentation
#if 0%{?suse_version} >= 1330
%if %{defined rubygem(asciidoctor)}
BuildRequires:  rubygem(asciidoctor)
%else
BuildRequires:  asciidoc
BuildRequires:  libxslt-tools
%endif

%description
Utility library for managing the "libnvdimm" subsystem, used for
platform NVDIMM resources like those defined by the ACPI 6.0 NFIT
(NVDIMM Firmware Interface Table).

%package -n %{dname}
Summary:        Development files for libndctl
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}-%{release}

%description -n %{dname}
Utility library for managing the "libnvdimm" subsystem, which defines
a kernel device model and control message interface for platform
NVDIMM resources like those defined by the ACPI 6.0 NFIT (NVDIMM
Firmware Interface Table).

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n %{lname}
Summary:        Management library for "libnvdimm" subsystem devices (Non-volatile Memory)
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n %{lname}
Utility library for managing the "libnvdimm" subsystem, which defines
a kernel device model and control message interface for platform
NVDIMM resources like those defined by the ACPI 6.0 NFIT (NVDIMM
Firmware Interface Table).

%prep
%setup -q
%autopatch -p1

%build
%if 0%{?suse_version} > 1500
export CFLAGS="%optflags -fcommon"
%endif
echo "%{version}" > version
./autogen.sh
CONF_FLAGS="--disable-static"
%if ! %{defined rubygem(asciidoctor)}
CONF_FLAGS="$CONF_FLAGS --disable-asciidoctor"
%endif
%configure $CONF_FLAGS
make %{?_smp_mflags}

%install
%if 0%{?suse_version} > 1500
export CFLAGS="%optflags -fcommon"
%endif
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
mkdir -p %{buildroot}%{_sbindir}
ln -sf service %{buildroot}%{_sbindir}/rcndctl-monitor

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig
%pre
%service_add_pre ndctl-monitor.service

%post
%service_add_post ndctl-monitor.service

%preun
%service_del_preun ndctl-monitor.service

%postun
%service_del_postun ndctl-monitor.service

%files
%doc licenses/BSD-MIT licenses/CC0
%{_bindir}/ndctl
%{_bindir}/daxctl
%{_sbindir}/rcndctl-monitor
%{_mandir}/man1/*
%dir %{_sysconfdir}/ndctl
%dir %{_sysconfdir}/ndctl/keys
%{_sysconfdir}/ndctl/keys/keys.readme
%config %{_sysconfdir}/ndctl/monitor.conf
%dir %{_sysconfdir}/modprobe.d
%config %{_sysconfdir}/modprobe.d/nvdimm-security.conf
%{_unitdir}/ndctl-monitor.service
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions/
%{_datadir}/bash-completion/completions/ndctl
%dir %{_datadir}/daxctl
%{_datadir}/daxctl/daxctl.conf

%files -n %{lname}
%doc README.md
%license COPYING
%doc licenses/BSD-MIT licenses/CC0
%{_libdir}/libndctl.so.*
%{_libdir}/libdaxctl.so.*

%files -n %{dname}
%license COPYING
%{_includedir}/ndctl/
%{_libdir}/libndctl.so
%{_libdir}/pkgconfig/libndctl.pc
%{_includedir}/daxctl/
%{_libdir}/libdaxctl.so
%{_libdir}/pkgconfig/libdaxctl.pc

%changelog
