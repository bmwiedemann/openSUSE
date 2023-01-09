#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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


%define base_name cloud-netconfig

%if "@BUILD_FLAVOR@" == ""
%define flavor_suffix %nil
%define csp_string None
ExclusiveArch:  do-not-build
%endif
%if "@BUILD_FLAVOR@" == "azure"
%define flavor_suffix -azure
%define csp_string Microsoft Azure
%endif
%if "@BUILD_FLAVOR@" == "ec2"
%define flavor_suffix -ec2
%define csp_string Amazon EC2
%endif
%if "@BUILD_FLAVOR@" == "gce"
%define flavor_suffix -gce
%define csp_string Google Compute Engine
%endif

%if ! %{defined _distconfdir}
%define _distconfdir %{_sysconfdir}
%define no_dist_conf 1
%endif

Name:           %{base_name}%{flavor_suffix}
Version:        1.7
Release:        0
License:        GPL-3.0-or-later
Summary:        Network configuration scripts for %{csp_string}
URL:            https://github.com/SUSE-Enceladus/cloud-netconfig
Group:          System/Management
Source0:        %{base_name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%if 0%{?suse_version} == 1110
BuildRequires:  sysconfig
Requires:       sysconfig
%define _udevrulesdir %{_sysconfdir}/udev/rules.d
%else
BuildRequires:  sysconfig-netconfig
Requires:       sysconfig-netconfig
%endif
BuildRequires:  pkgconfig(udev)
%if 0%{?sle_version} > 150100
BuildRequires:  NetworkManager
%endif
Requires:       curl
Requires:       udev
%if 0%{?sles_version} == 11
# RPM in SLES 11 does not support self conflict, use otherproviders()
# workaround
Provides:       cloud-netconfig
Conflicts:      otherproviders(cloud-netconfig)
%else
Provides:       cloud-netconfig
Conflicts:      cloud-netconfig
%endif
%{?systemd_requires}
%define _scriptdir %{_libexecdir}/cloud-netconfig
%if 0%{?suse_version} > 1550
%define _netconfigdir %{_libexecdir}/netconfig.d
%else
%define _netconfigdir %{_sysconfdir}/netconfig.d
%endif

%description -n %{base_name}%{flavor_suffix}
This package contains scripts for automatically configuring network interfaces
in %{csp_string} with full support for hotplug.

%if 0%{?sle_version} > 150100
%package -n %{base_name}-nm
Summary:        Network configuration scripts for %{csp_string}
Group:          System/Management
Requires:       NetworkManager
Requires:       cloud-netconfig

%description -n %{base_name}-nm
Dispatch script for NetworkManager that automatically runs cloud-netconfig.
%endif

%prep
%setup -q -n %{base_name}-%{version}

%build

%install
make install%{flavor_suffix} \
  DESTDIR=%{buildroot} \
  PREFIX=%{_usr} \
  SYSCONFDIR=%{_sysconfdir} \
  DISTCONFDIR=%{_distconfdir} \
  SCRIPTDIR=%{_scriptdir} \
  UDEVRULESDIR=%{_udevrulesdir} \
  UNITDIR=%{_unitdir} \
  NETCONFIGDIR=%{_netconfigdir}

# Disable persistent net generator from udev-persistent-ifnames as
# it does not work for xen interfaces. This will likely produce a warning.
%if 0%{?suse_version} >= 1315
mkdir -p %{buildroot}/%{_sysconfdir}/udev/rules.d
ln -s /dev/null %{buildroot}/%{_sysconfdir}/udev/rules.d/75-persistent-net-generator.rules
%endif

%if 0%{?sle_version} <= 150100
rm -r %{buildroot}/usr/lib/NetworkManager
%endif

%files -n %{base_name}%{flavor_suffix}
%defattr(-,root,root)
%{_scriptdir}
%if %{defined no_config}
%config(noreplace) %{_distconfdir}/default/cloud-netconfig
%else
%{_distconfdir}/default/cloud-netconfig
%endif
%{_netconfigdir}
%if 0%{?suse_version} >= 1315
%{_sysconfdir}/udev/rules.d
%endif
%{_udevrulesdir}/*
%{_unitdir}/*
%doc README.md
%license LICENSE

%if 0%{?sle_version} > 150100
%files -n %{base_name}-nm
/usr/lib/NetworkManager/dispatcher.d
%endif

%pre
%service_add_pre %{base_name}.service %{base_name}.timer

%post
%service_add_post %{base_name}.service %{base_name}.timer

%preun
%service_del_preun %{base_name}.service %{base_name}.timer

%postun
%service_del_postun %{base_name}.service %{base_name}.timer

%changelog
