#
# spec file for package logrotate
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           logrotate
Version:        3.15.0
Release:        0
Summary:        Cron service for rotating, compressing, mailing and removing system log files
License:        GPL-2.0-or-later
Group:          System/Base
Url:            https://github.com/%{name}/%{name}
Source0:        https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source10:       https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
# SUSE specific logrotate configurations
Source1:        logrotate.wtmp
Source2:        logrotate.default
Source100:      %{name}-rpmlintrc
Patch0:         logrotate-3.13.0-systemd_add_home_env.patch
BuildRequires:  acl
BuildRequires:  libacl-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(systemd) >= 197
Requires:       xz
%{?systemd_requires}

%description
The logrotate utility does automatic rotation, compression, mailing and removal
of log files. Logrotate can be set to handle a log file daily, weekly, monthly,
or when the log file reaches a certain size. Normally, logrotate runs as a
daily cron job.

It manages plain files only and is not involved in systemd's journal rotation.

%prep
%setup -q
%patch0 -p1

%build
%configure \
    --disable-silent-rules \
    --with-state-file-path=%{_localstatedir}/lib/misc/logrotate.status \
    --disable-werror
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check

%install
%make_install
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/wtmp
install -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.conf
install -D -m 0644 examples/%{name}.service %{buildroot}%{_unitdir}/%{name}.service
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
%license COPYING
%doc ChangeLog.md README.md
%{_sbindir}/logrotate
%{_sbindir}/rc%{name}
%{_mandir}/man8/logrotate.8*
%{_mandir}/man5/logrotate.conf.5*
%config %{_sysconfdir}/logrotate.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/wtmp
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.timer

%changelog
