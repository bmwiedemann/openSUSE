#
# spec file for package wsl-firstboot
#
# Copyright (c) 2025 SUSE LLC
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


Name:           wsl-firstboot
Version:        1.5.9+git20251110.c1fca4e
Release:        0
Summary:        Simple text based WSL first boot wizard
License:        MIT
Group:          Development/Tools/Other
URL:            https://github.com/openSUSE/wsl-firstboot
Source0:        %{name}-%{version}.tar.gz
Source99:       %{name}-rpmlintrc
Source100:      README.md
BuildRequires:  systemd-rpm-macros
# Provides cracklib-check used for password quality checking during user creation
Requires:       cracklib
Requires:       dialog
#Requires:       iproute2
Requires:       live-langset-data
Requires:       timezone
BuildArch:      noarch
%{?systemd_requires}

%description
Simple text based first boot wizard (adjusted for WSL) that can be used
instead of the line based one that is built into systemd.

%prep
%setup -q

%build

%install
cp -a files/* %{buildroot}

%pre
%service_add_pre wsl-firstboot.service
%service_add_pre wsl-firstboot-snapshot.service

%post
%service_add_post wsl-firstboot.service
%service_add_post wsl-firstboot-snapshot.service

%preun
%service_del_preun wsl-firstboot.service
%service_del_preun wsl-firstboot-snapshot.service


%postun
%service_del_postun wsl-firstboot.service
%service_del_postun wsl-firstboot-snapshot.service

%files
%doc README.md
%license LICENSE
%{_unitdir}/wsl-firstboot.service
%{_unitdir}/wsl-firstboot-snapshot.service
%dir %{_datadir}/defaults/
%{_datadir}/defaults/wsl-firstboot.conf
%dir %{_datadir}/wsl-firstboot/
%dir %{_datadir}/wsl-firstboot/modules/
%{_datadir}/wsl-firstboot/modules/{ssh_enroll,status_mail,otp,registration,switch,user}
%{_sbindir}/wsl-config
%{_sbindir}/wsl-firstboot
%{_sbindir}/wsl-firstboot-snapshot
%{_datadir}/wsl-firstboot/wsl-firstboot-dialogs
%{_datadir}/wsl-firstboot/wsl-firstboot-functions
%{_datadir}/wsl-firstboot/welcome-screen

%changelog
