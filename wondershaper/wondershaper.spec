#
# spec file for package wondershaper
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           wondershaper
Version:        1.1a
Release:        0
Summary:        A network QoS (Quality of Service) script
License:        GPL-2.0-or-later
Group:          Productivity/Networking/System
Url:            http://lartc.org/wondershaper/

Source0:        wondershaper-1.1a.tar.bz2
Source1:        sysconfig.wondershaper
Source2:        rcwondershaper
Source3:        wondershaper.service
Patch0:         %{name}-%{version}.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
BuildRequires:  systemd-rpm-macros
Requires:       iproute2
Requires(post): %fillup_prereq
%{?systemd_ordering}

%description
Many cablemodem and ADSL users experience horrifying latency while
uploading or downloading. They also notice that uploading hampers
downloading greatly. The wondershaper neatly addresses these issues,
allowing users of a router with a wondershaper to continue using SSH
over a loaded link happily.

%prep
%setup 
cp %{S:1} %{S:2} .
%patch0 -p1

%build

%install
mv wshaper wshaper.cbq
install -m 755 -d %{buildroot}/usr/sbin
install -m 755 -d %{buildroot}/%{_fillupdir}
install -d %{buildroot}/%{_datadir}/%{name}/scripts
install -m 755 %{SOURCE2} %{buildroot}/%{_datadir}/%{name}/scripts
install -d %{buildroot}/%{_unitdir}
install -m 644 %{SOURCE3} %{buildroot}/%{_unitdir}
install -d %{buildroot}/
install -m 750 wshaper.* %{buildroot}/usr/sbin/
install -m 644 sysconfig.wondershaper %{buildroot}/%{_fillupdir}/
ln -sf service %{buildroot}/usr/sbin/rcwondershaper

%pre
%service_add_pre wondershaper.service

%post
%service_add_post wondershaper.service
%{fillup_only}

%preun
%service_del_preun wondershaper.service

%postun
%service_del_postun wondershaper.service

%files
%defattr(-, root, root)
%doc COPYING ChangeLog README TODO VERSION
%{_datadir}/%{name}
%{_unitdir}
%{_sbindir}/*
%{_fillupdir}/*

%changelog
