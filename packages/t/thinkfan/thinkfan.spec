#
# spec file for package thinkfan
#
# Copyright (c) 2021 SUSE LLC
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


%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           thinkfan
Version:        1.3.0
Release:        0
Summary:        A minimalist fan control program
License:        GPL-3.0-only
Group:          Productivity/Other
URL:            https://github.com/vmatare/thinkfan/
Source0:        %{name}-%{version}.tar.bz2
Source1:        thinkfan-sysconfig
Patch1:         thinkfan-systemd.patch
Patch2:         harden_thinkfan-sleep.service.patch
Patch3:         harden_thinkfan-wakeup.service.patch
Patch4:         harden_thinkfan.service.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libatasmart-devel
BuildRequires:  yaml-cpp-devel
BuildRequires:  pkgconfig(systemd)

%description
A simple fan control program. Read temperatures, check them against configured
limits and switch to appropriate (also pre-configured) fan level.
Requires a working thinkpad_acpi or any other hwmon driver
that enables temperature reading and fan control from userspace.

Don't forget to set the desired temperature values in %{_sysconfdir}/thinkfan.conf

%prep
%setup -q
%autopatch -p1

%build
%cmake -DUSE_ATASMART:BOOL=ON -DCMAKE_BUILD_TYPE:STRING=Release
%make_build CFLAGS="%{optflags}"

%install
%cmake_install
rm -rf %{buildroot}%{_datadir}/doc/%{name}

mkdir -p %{buildroot}/%{_sysconfdir}
install -D -m0644 %{SOURCE1} %{buildroot}%{_fillupdir}/sysconfig.%{name}
rm -rf %{buildroot}%{_sysconfdir}/systemd/system/thinkfan.service.d

cp examples/%{name}.yaml %{buildroot}/%{_sysconfdir}/%{name}.yaml

mkdir -p %{buildroot}/%{_unitdir}
cp -v rcscripts/systemd/*.service %{buildroot}/%{_unitdir}/
sed -i "s|%{_prefix}/local/sbin|%{_sbindir}|g" %{buildroot}/%{_unitdir}/*

mkdir -p %{buildroot}%{_sysconfdir}/modprobe.d
echo "options thinkpad_acpi fan_control=1" > %{buildroot}%{_sysconfdir}/modprobe.d/50-thinkfan.conf

%pre
%service_add_pre %{name}.service
%service_add_pre %{name}-sleep.service
%service_add_pre %{name}-wakeup.service

%post
%service_add_post %{name}.service
%service_add_post %{name}-sleep.service
%service_add_post %{name}-wakeup.service
%{fillup_only %{name}}

%preun
%service_del_preun %{name}.service
%service_del_preun %{name}-sleep.service
%service_del_preun %{name}-wakeup.service

%postun
%service_del_postun %{name}.service
%service_del_postun %{name}-sleep.service
%service_del_postun %{name}-wakeup.service

%files
%license COPYING
%doc README.md examples/*
%dir %{_sysconfdir}/modprobe.d
%{_sbindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.yaml
%config(noreplace) %{_sysconfdir}/modprobe.d/50-thinkfan.conf
%{_fillupdir}/sysconfig.%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man5/thinkfan.conf.5%{?ext_man}
%{_mandir}/man5/thinkfan.conf.legacy.5%{?ext_man}
%{_unitdir}/*.service

%changelog
