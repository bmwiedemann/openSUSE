#
# spec file for package killerd
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           killerd
Version:        1.1
Release:        0
Summary:        Daemon for automatic killing of login shells
License:        GPL-2.0+
Group:          System/Daemons
Url:            http://mj.ucw.cz/linux.shtml
Source:         ftp://atrey.karlin.mff.cuni.cz/pub/local/mj/linux/%{name}-%{version}.tar.gz
Source1:        killerd.service
Patch0:         %{name}-%{version}-makefile.diff
BuildRequires:  systemd-rpm-macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{?systemd_requires}

%description
KillerD is a simple daemon for automatic killing of login shells with
idle time exceeding given limits, runaway processes and other system
hogs. Almost everything can be easily configured.

%prep
%setup -q
%patch0

%build
make CFLAGS="%{optflags}" CC="cc" %{?_smp_mflags}

%install
mkdir -p %{buildroot}/%{_sbindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}/%{_sysconfdir}
make install SBINDIR=%{buildroot}/%{_sbindir} CONFIGDIR=%{buildroot}/%{_sysconfdir}
install -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
ln -sf service %{buildroot}/%{_sbindir}/rckillerd

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%defattr(-,root,root)
%doc ChangeLog
%config %{_sysconfdir}/killerd.conf
%{_unitdir}/%{name}.service
%{_sbindir}/rckillerd
%{_sbindir}/killerd

%changelog
