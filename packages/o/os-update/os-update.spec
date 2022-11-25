#
# spec file for package os-update
#
# Copyright (c) 2022 SUSE LLC
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


%if ! %{defined _distconfdir}
  %define _distconfdir %{_sysconfdir}
%endif

Name:           os-update
Version:        1.5
Release:        0
Summary:        Updates the system regular to stay current and safe
License:        GPL-2.0-or-later
URL:            https://github.com/thkukuk/os-update
Source:         https://github.com/thkukuk/os-update/releases/download/v%{version}/os-update-%{version}.tar.xz
Source99:       os-update-rpmlintrc
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(systemd)
Requires:       zypper-needs-restarting
Recommends:     rebootmgr
Recommends:     systemd-status-mail
BuildArch:      noarch

%description
Service to keep an OS update to date and secure. It is run by a
systemd.timer daily and can inform rebootmgrd that the update
requires a reboot.

%package -n systemd-status-mail
Summary:        Send a mail if a systemd.timer fails and/or succeeds
Requires:       (/usr/sbin/sendmail or mailx)
Suggests:       mailx

%description -n systemd-status-mail
systemd-mail-status is called by systemd-status-mail@.service if the
service is configured for the OnFailure and/or OnSuccess case of a
systemd unit. It sends an email to a configureable address with the name
of the service, the hostname and the output of
"systemctl status --full <service>".

%prep
%setup -q

%build
%configure --enable-vendordir=%{_distconfdir}
%make_build

%install
%make_install
install -m 644 -D etc/default/systemd-status-mail %{buildroot}%{_distconfdir}/default/systemd-status-mail

%pre
%service_add_pre os-update.timer

%post
%service_add_post os-update.timer

%preun
%service_del_preun os-update.timer

%postun
%service_del_postun os-update.timer

%files
%license COPYING
%doc README.md
%{_distconfdir}/os-update.conf
%{_libexecdir}/os-update
%{_prefix}/lib/systemd/system/os-update.service
%{_prefix}/lib/systemd/system/os-update.timer
%{_mandir}/man8/os-update.8%{?ext_man}

%files -n systemd-status-mail
%license COPYING
%{_distconfdir}/default/systemd-status-mail
%{_libexecdir}/systemd-status-mail
%{_prefix}/lib/systemd/system/systemd-status-mail@.service
%{_mandir}/man8/systemd-status-mail.8%{?ext_man}
%dir %{_datadir}/systemd-status-mail
%{_datadir}/systemd-status-mail/status-mail.conf

%changelog
