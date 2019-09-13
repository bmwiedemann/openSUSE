#
# spec file for package network-autoconfig
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           network-autoconfig
Version:        1.0
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Requires:       wicked
Requires:       /bin/bash
BuildRequires:  systemd-rpm-macros
%{?systemd_requires}
Summary:        Find a connected eth interface and create an ifcfg for it
License:        MIT
Group:          System/Boot
Url:            http://gitorious.org/opensuse/network-autoconfig

Source0:        README
Source1:        network-autoconfig
Source2:        network-autoconfig.service

%description
All available Ethernet network interfaces will be cycled
until one is successfully configured.
This script should run at the first boot of a machine
that has several interfaces.

%prep
%setup -c -T
cp %{SOURCE0} .

%build

%install
# install it to a directory where autoyast will run it once
SBINDIR=%{buildroot}/%{_sbindir}
mkdir -p $SBINDIR
install %{SOURCE1} $SBINDIR
install -d %{buildroot}/%{_unitdir}
install %{SOURCE2} %{buildroot}/%{_unitdir}
install -d %{buildroot}/etc/systemd/system/network-pre.target.wants
ln -s %{_unitdir}/network-autoconfig.service %{buildroot}/etc/systemd/system/network-pre.target.wants

%pre
%service_add_pre network-autoconfig.service

%post
%service_add_post network-autoconfig.service

%preun
%service_del_preun network-autoconfig.service

%postun
%service_del_postun network-autoconfig.service

%files
%defattr(-,root,root)
%doc README
%{_unitdir}/network-autoconfig.service
/usr/sbin/network-autoconfig
/etc/systemd

%changelog
