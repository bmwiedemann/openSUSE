#
# spec file for package ndctl
#
# Copyright (c) 2024 SUSE LINUX GmbH, Nuernberg, Germany.
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

%if 0%{?suse_version} < 1550 && 0%{?sle_version} <= 150300
# systemd-rpm-macros is wrong in 15.3 and below
%define _modprobedir /lib/modprobe.d
%endif
%global modprobe_d_files nvdimm-security.conf

%define lname libndctl6
%define dname libndctl-devel
Name:           ndctl
Version:        79
Release:        0
Summary:        Manage "libnvdimm" subsystem devices (Non-volatile Memory)
License:        GPL-2.0-only
Group:          Hardware/Other
URL:            https://github.com/pmem/ndctl
Source0:        https://github.com/pmem/ndctl/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        ndctl-rpmlintrc
Patch0:         harden_ndctl-monitor.service.patch
BuildRequires:  keyutils-devel
BuildRequires:  libiniparser-devel
BuildRequires:  libtool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  xmlto
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(json)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libkmod)
BuildRequires:  pkgconfig(libtraceevent)
BuildRequires:  pkgconfig(libtracefs)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(uuid)
ExclusiveArch:  x86_64 aarch64 ppc64le
%{?systemd_requires}
# required for documentation
%if 0%{?suse_version} >= 1330
BuildRequires:  rubygem(asciidoctor)
%define asciidoc -Dasciidoctor=enabled
%else
BuildRequires:  asciidoc
BuildRequires:  libxslt-tools
%define asciidoc -Dasciidoctor=disabled
%endif

%description
Utility library for managing the "libnvdimm" subsystem, used for
platform NVDIMM resources like those defined by the ACPI 6.0 NFIT
(NVDIMM Firmware Interface Table).

%package -n %{dname}
Summary:        Development files for libndctl
License:        LGPL-2.1-only
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
License:        LGPL-2.1-only
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
%meson %{?asciidoc} -Dversion-tag=%{version} -Dmodprobedatadir=%{_modprobedir}
%meson_build

%install
%if 0%{?suse_version} > 1500
export CFLAGS="%optflags -fcommon"
%endif
%meson_install
find %{buildroot} -type f -name "*.la" -delete -print
mkdir -p %{buildroot}%{_sbindir}
ln -sf service %{buildroot}%{_sbindir}/rcndctl-monitor
# libdaxctl.h has moved breaking users of libdaxctl, provide a compatibility symlink
ln -s ../daxctl/libdaxctl.h %{buildroot}%{_includedir}/ndctl

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%pre
%service_add_pre ndctl-monitor.service
# Avoid restoring outdated stuff in posttrans
for _f in %{?modprobe_d_files}; do
    [ ! -f "/etc/modprobe.d/${_f}.rpmsave" ] || \
        mv -f "/etc/modprobe.d/${_f}.rpmsave" "/etc/modprobe.d/${_f}.rpmsave.old" || :
done
if [ -f %{_sysconfdir}/ndctl/monitor.conf ] ; then
  if ! [ -f %{_sysconfdir}/ndctl.conf.d/monitor.conf ] ; then
    cp -a %{_sysconfdir}/ndctl/monitor.conf /var/run/ndctl-monitor.conf-migration
  fi
fi

%post
%service_add_post ndctl-monitor.service
if [ -f /var/run/ndctl-monitor.conf-migration ] ; then
  config_found=false
  while read line ; do
    [ -n "$line" ] || continue
    case "$line" in
      \#*) continue ;;
    esac
    config_found=true
    break
  done < /var/run/ndctl-monitor.conf-migration
  if $config_found ; then
    echo "[monitor]" > %{_sysconfdir}/ndctl.conf.d/monitor.conf
    cat /var/run/ndctl-monitor.conf-migration >> %{_sysconfdir}/ndctl.conf.d/monitor.conf
  fi
  rm /var/run/ndctl-monitor.conf-migration
fi

%preun
%service_del_preun ndctl-monitor.service cxl-monitor.service

%postun
%service_del_postun ndctl-monitor.service cxl-monitor.service

%posttrans
# Migration of modprobe.conf files to _modprobedir
for _f in %{?modprobe_d_files}; do
    [ ! -f "/etc/modprobe.d/${_f}.rpmsave" ] || \
        mv -fv "/etc/modprobe.d/${_f}.rpmsave" "/etc/modprobe.d/${_f}" || :
done

%files
%license COPYING LICENSES/*/*
%doc README.md CONTRIBUTING.md
%{_bindir}/cxl
%{_bindir}/daxctl
%{_bindir}/ndctl
%{_sbindir}/rcndctl-monitor
%{_unitdir}/daxdev-reconfigure@.service
%{_udevrulesdir}/90-daxctl-device.rules
%{_mandir}/man1/*
%dir %{_sysconfdir}/daxctl.conf.d
%config(noreplace) %{_sysconfdir}/daxctl.conf.d/daxctl.example.conf
%dir %{_sysconfdir}/ndctl
%dir %{_sysconfdir}/ndctl.conf.d
%dir %{_sysconfdir}/ndctl/keys
%{_sysconfdir}/ndctl/keys/keys.readme
%config(noreplace) %{_sysconfdir}/ndctl.conf.d/monitor.conf
%config(noreplace) %{_sysconfdir}/ndctl.conf.d/ndctl.conf
%dir %{_modprobedir}
%{_modprobedir}/nvdimm-security.conf
%{_unitdir}/cxl-monitor.service
%{_unitdir}/ndctl-monitor.service
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions/
%{_datadir}/bash-completion/completions/cxl
%{_datadir}/bash-completion/completions/daxctl
%{_datadir}/bash-completion/completions/ndctl
%dir %{_datadir}/daxctl
%{_datadir}/daxctl/daxctl.conf

%files -n %{lname}
%license COPYING LICENSES/*/*
%doc README.md CONTRIBUTING.md
%{_libdir}/libcxl.so.*
%{_libdir}/libdaxctl.so.*
%{_libdir}/libndctl.so.*

%files -n %{dname}
%license COPYING LICENSES/*/*
%doc README.md CONTRIBUTING.md
%{_includedir}/cxl/
%{_libdir}/libcxl.so
%{_libdir}/pkgconfig/libcxl.pc
%{_includedir}/daxctl/
%{_libdir}/libdaxctl.so
%{_libdir}/pkgconfig/libdaxctl.pc
%{_includedir}/ndctl/
%{_libdir}/libndctl.so
%{_libdir}/pkgconfig/libndctl.pc
%{_mandir}/man3/*

%changelog
