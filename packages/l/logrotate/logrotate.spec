#
# spec file for package logrotate
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


%{!?_distconfdir: %global _distconfdir %{_prefix}%{_sysconfdir}}

Name:           logrotate
Version:        3.21.0
Release:        0
Summary:        Cron service for rotating, compressing, mailing and removing system log files
License:        GPL-2.0-or-later
Group:          System/Base
URL:            https://github.com/logrotate/logrotate
Source0:        https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
# SUSE specific logrotate configurations
Source1:        logrotate.wtmp
Source2:        logrotate.default
Source3:        logrotate.service
Source4:        logrotate-all
Source10:       https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source11:       logrotate.keyring
BuildRequires:  acl
BuildRequires:  automake
BuildRequires:  libacl-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(systemd) >= 197
Requires:       %{_bindir}/xz
%{?systemd_ordering}

%description
The logrotate utility does automatic rotation, compression, mailing and removal
of log files. Logrotate can be set to handle a log file daily, weekly, monthly,
or when the log file reaches a certain size. Normally, logrotate runs as a
daily cron job.

It manages plain files only and is not involved in systemd's journal rotation.

%prep
%autosetup -p1

%build
autoreconf -f -i
%configure \
    --disable-silent-rules \
    --with-state-file-path=%{_localstatedir}/lib/misc/logrotate.status \
    --disable-werror
%make_build

%check
%make_build check

%install
%make_install
mkdir -p %{buildroot}%{_distconfdir}/logrotate.d
install -m 644 %{SOURCE1} %{buildroot}%{_distconfdir}/logrotate.d/wtmp
install -m 644 %{SOURCE2} %{buildroot}%{_distconfdir}/logrotate.conf
install -D -m 644 %{SOURCE3} %{buildroot}%{_unitdir}/%{name}.service
install -D -m 755 %{SOURCE4} %{buildroot}%{_sbindir}/logrotate-all
install -D -m 0644 examples/%{name}.timer %{buildroot}%{_unitdir}/%{name}.timer
ln -s service %{buildroot}%{_sbindir}/rc%{name}

%pre
#only the timer can be enabled/disabled/masked !
%service_add_pre %{name}.service %{name}.timer

%post
%{remove_and_set MAX_DAYS_FOR_LOG_FILES}
# Move /var/lib/logrotate.status
if [ -f %{_localstatedir}/lib/logrotate.status -a ! -f %{_localstatedir}/lib/misc/logrotate.status ]; then
  mv %{_localstatedir}/lib/logrotate.status %{_localstatedir}/lib/misc/logrotate.status ||:
fi

%service_add_post %{name}.service %{name}.timer

%preun
%service_del_preun %{name}.service %{name}.timer

%postun
%service_del_postun %{name}.service %{name}.timer

%files
%if %{?suse_version} <= 1500
%dir %{_distconfdir}
%endif
%license COPYING
%doc ChangeLog.md README.md
%{_sbindir}/logrotate
%{_sbindir}/logrotate-all
%{_sbindir}/rc%{name}
%{_mandir}/man8/logrotate.8%{?ext_man}
%{_mandir}/man5/logrotate.conf.5%{?ext_man}
%{_distconfdir}/logrotate.conf
%{_distconfdir}/logrotate.d/wtmp
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.timer

%changelog
