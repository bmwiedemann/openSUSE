#
# spec file for package jeos-firstboot
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


Name:           jeos-firstboot
Version:        0.0+git20200508.d0ccd48
Release:        0
Summary:        Simple text based JeOS first boot wizard
License:        MIT
Group:          Development/Tools/Other
URL:            https://github.com/openSUSE/jeos-firstboot
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  systemd-rpm-macros
Requires:       dialog
Requires:       live-langset-data
BuildArch:      noarch
%{?systemd_requires}

%description
Simple text based JeOS first boot wizard that can be used instead
of the line based one that is built into systemd.

%package rpiwifi
Summary:        jeos-firstboot module for WiFi configuration for RaspberryPi systems
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       wicked
Requires:       wireless-tools
Requires:       wpa_supplicant

%description rpiwifi
This module hooks into jeos-firstboot and allows the user to enter data to connect
his RaspberryPi system to a wireless network.

%prep
%setup -q

%build

%install
cp -a files/* %{buildroot}

%preun
%service_del_preun jeos-firstboot.service

%postun
%service_del_postun jeos-firstboot.service

%pre
%service_add_pre jeos-firstboot.service

%post
%service_add_post jeos-firstboot.service

%files
%doc README
%license LICENSE
%{_unitdir}/jeos-firstboot.service
%{_unitdir}/jeos-firstboot-snapshot.service
%dir %{_datadir}/defaults/
%{_datadir}/defaults/jeos-firstboot.conf
%dir %{_datadir}/jeos-firstboot
%{_sbindir}/jeos-firstboot
%{_sbindir}/jeos-firstboot-snapshot

%files rpiwifi
%{_datadir}/jeos-firstboot/raspberrywifi

%changelog
