#
# spec file for package logdigest
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


Name:           logdigest
Version:        0.2.4
Release:        0
Summary:        Mail Digests of System Log Files to the System Administrator
License:        GPL-2.0-or-later
Group:          System/Monitoring
URL:            http://sourceforge.net/projects/logdigest
Source:         http://dfn.dl.sourceforge.net/sourceforge/logdigest/logdigest-%{version}.tar.bz2
Source1:        logdigest-all-ignores-autogeneration
Source2:        logdigest.service
Source3:        logdigest.timer
Source4:        logdigest-all-ignores-autogeneration.service
Source5:        logdigest-all-ignores-autogeneration.timer
BuildRequires:  automake
Requires:       logtail
Requires(post): /bin/chmod
Requires(post): /bin/touch
# procinfo is needed when EXTENDED_STATS=yes
Recommends:     procinfo
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Logdigest, run by daily as a systemd timer, greps through system log files
(/var/log/messages, /var/log/mail, etc.) to find "interesting" content.

Lines matching the regular expressions in /etc/logdigest/ignore are simply
ignored. More expressions can be added to %{_sysconfdir}/logdigest/ignore.local.
See /etc/logdigest/config for some general settings.

The results are mailed to the sysadmin daily.

%package -n logtail
Summary:        Helper application to analyze logfiles
Group:          System/Monitoring

%description -n logtail
Print log file lines that have not been read

%prep
%setup -q -n logdigest-%{version}

%build
export CFLAGS="%{optflags}"
aclocal
autoconf
automake --add-missing
./configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir} --with-tmpdir=%{_localstatedir}/lib/logdigest
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}

mkdir -p %{buildroot}%{_datadir}/logdigest
cp -p %{SOURCE1} %{buildroot}%{_datadir}/logdigest/
mv %{buildroot}%{_sysconfdir}/cron.daily/logdigest %{buildroot}%{_datadir}/logdigest/logdigest
install -D -m 0644 %{SOURCE2} %{buildroot}/%{_unitdir}/%{name}.service
install -D -m 0644 %{SOURCE3} %{buildroot}/%{_unitdir}/%{name}.timer
install -D -m 0644 %{SOURCE4} %{buildroot}/%{_unitdir}/%{name}-all-ignores-autogeneration.service
install -D -m 0644 %{SOURCE5} %{buildroot}/%{_unitdir}/%{name}-all-ignores-autogeneration.timer

%pre
%service_add_pre %{name}.service %{name}.timer
%service_add_pre %{name}-all-ignores-autogeneration.service %{name}-all-ignores-autogeneration.timer

%post
%service_add_post %{name}.service %{name}.timer
%service_add_post %{name}-all-ignores-autogeneration.service %{name}-all-ignores-autogeneration.timer

# add .local conf files if they are not there
cd etc/logdigest
for i in alarming ignore; do
        test -e $i.local || { touch $i.local; chmod 600 $i.local; }
done
#
%{_datadir}/logdigest/logdigest-all-ignores-autogeneration

%preun
%service_del_preun %{name}.service %{name}.timer
%service_del_preun %{name}-all-ignores-autogeneration.service %{name}-all-ignores-autogeneration.timer

# update?
if [ ${FIRST_ARG:-0} -gt 1 ]; then
	exit 0
fi

# remove .local conf files if empty
cd etc/logdigest
for i in alarming ignore; do
	test -s $i.local || rm -f $i.local
done

%postun
%service_del_postun %{name}.service %{name}.timer
%service_del_postun %{name}-all-ignores-autogeneration.service %{name}-all-ignores-autogeneration.timer

%files
%defattr(-,root,root)
%license COPYING
%doc README AUTHORS ChangeLog TODO VERSION
%dir %{_sysconfdir}/logdigest
%config(noreplace) %{_sysconfdir}/logdigest/*
%{_localstatedir}/lib/logdigest
%dir %{_datadir}/logdigest
%attr(755,root,root) %{_datadir}/logdigest/logdigest
%attr(755,root,root) %{_datadir}/logdigest/logdigest-all-ignores-autogeneration
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.timer
%{_unitdir}/%{name}-all-ignores-autogeneration.service
%{_unitdir}/%{name}-all-ignores-autogeneration.timer

%files -n logtail
%defattr(-,root,root)
%{_bindir}/logtail

%changelog
