#
# spec file for package os-update
#
# Copyright (c) 2024 SUSE LLC
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
Version:        1.21+git.20241206
Release:        0
Summary:        Updates the system regularly to stay current and safe
License:        GPL-2.0-or-later
URL:            https://github.com/openSUSE/os-update
Source:         os-update-%{version}.tar.xz
Source99:       os-update-rpmlintrc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  go-md2man
BuildRequires:  pkgconfig
BuildRequires:  sysuser-shadow
BuildRequires:  sysuser-tools
BuildRequires:  pkgconfig(systemd)
Requires:       lsof
Recommends:     rebootmgr
Recommends:     systemd-status-mail
BuildArch:      noarch
%if 0%{?suse_version} >= 1500
Requires:       zypper-needs-restarting
%endif
%if 0%{?suse_version} >= 1600
Requires:       zypp-boot-plugin >= 0.0.4
%endif

%description
Service to keep an OS update to date and secure. It is run by a
systemd.timer daily and can inform rebootmgrd that the update
requires a reboot.

%package -n systemd-status-mail
Summary:        Send a mail if a systemd.timer fails and/or succeeds
%sysusers_requires
%if 0%{?suse_version} >= 1500
Requires:       (/usr/sbin/sendmail or mailx)
Suggests:       mailx
%else
Requires:       mailx
%endif

%description -n systemd-status-mail
systemd-mail-status is called by systemd-status-mail@.service if the
service is configured for the OnFailure and/or OnSuccess case of a
systemd unit. It sends an email to a configureable address with the name
of the service, the hostname and the output of
"systemctl status --full <service>".

%prep
%setup -q

%build
./autogen.sh
%configure
%if 0%{?suse_version} < 1500
  %define make_build %{__make} -O %{?_smp_mflags}
%endif
%make_build
%sysusers_generate_pre systemd/systemd-status-mail.conf systemd-status-mail systemd-status-mail.conf

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

%pre -n systemd-status-mail -f systemd-status-mail.pre

%files
%license COPYING
%doc README.md
%dir %{_datadir}/os-update
%{_datadir}/os-update/os-update.conf
%{_libexecdir}/os-update
%{_prefix}/lib/systemd/system/os-update.service
%{_prefix}/lib/systemd/system/os-update.timer
%{_mandir}/man8/os-update.8%{?ext_man}

%files -n systemd-status-mail
%license COPYING
%if 0%{?suse_version} < 1550
%config(noreplace) %{_sysconfdir}/default/systemd-status-mail
%else
%{_distconfdir}/default/systemd-status-mail
%endif
%{_libexecdir}/systemd-status-mail
%{_prefix}/lib/systemd/system/systemd-status-mail@.service
%{_prefix}/lib/systemd/system-generators/status-mail-generator.sh
%{_mandir}/man8/systemd-status-mail.8%{?ext_man}
%dir %{_datadir}/systemd-status-mail
%{_datadir}/systemd-status-mail/status-mail.conf
%{_sysusersdir}/systemd-status-mail.conf

%changelog
