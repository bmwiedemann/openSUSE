#
# spec file for package qos
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright 2013 Archie L. Cobbs.
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
    %define _fillupdir /var/adm/fillup-templates
%endif

%define systemdsvc  %{_usr}/lib/systemd/system
%define servicefile %{name}.service
%define netconfdir  %{_sysconfdir}/sysconfig/network
%define modprobe    /sbin/modprobe
%define tcutil      %{_sbindir}/tc
%define iputil      /bin/ip

Name:           qos
Version:        1.0.1
Release:        0
BuildArch:      noarch
Summary:        Simple traffic shaping utility for fighting bufferbloat
#Source0:            https://github.com/archiecobbs/qos/archive/1.0.1.tar.gz
License:        Apache-2.0
Group:          System/Management
Source0:        %{name}-%{version}.tar.gz
Source1:        %{servicefile}.in
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Url:            https://github.com/archiecobbs/qos
Requires:       iproute2
Requires(post):  %fillup_prereq
%systemd_requires

%description
The Problem: Bufferbloat (see http://en.wikipedia.org/wiki/Bufferbloat)

    - Your SSH session turns to molasses when your kid watches YouTube
    - Your wife complains that "the internet is slow"
    - You hate the stupid DSL modems supplied by the phone company
      with their giant packet queues that add unnecessary latency
    - You have your own Linux router that routes all your traffic
      or is the only machine you have connected to the Internet
      and know there must be a better way

The Solution: QoS

    QoS = "Quality of Service"

    You probably already know about it. Control and proritize traffic.

    This QoS is new and improved. Previous QoS setups only throttled
    traffic in the download direction. This one handles both directions
    using the (poorly documented) Linux ifb interface and tc(8) 'mirred'
    redirection.

%prep
%setup

%build
subst()
{
    sed -r \
        -e 's|@qosconfig@|%{netconfdir}/%{name}|g' \
        -e 's|@qosprog@|%{_bindir}/%{name}|g' \
        -e 's|@modprobe@|%{modprobe}|g' \
        -e 's|@iputil@|%{iputil}|g' \
        -e 's|@tcutil@|%{tcutil}|g'
}
subst < src/scripts/%{name}.sh > %{name}
subst < %{_sourcedir}/%{servicefile}.in > %{servicefile}

%install

# Install start/stop script (which is just the old SysV /etc/init.d file)
install -d %{buildroot}%{_bindir}
install  -m 0755 %{name} %{buildroot}%{_bindir}/

# Install systemd service file
install -d %{buildroot}%{systemdsvc}
install %{servicefile} %{buildroot}%{systemdsvc}/

# Install sysconfig template
install -d -m 0755 %{buildroot}%{_fillupdir}
install -m 0755 src/fillup/sysconfig.%{name} %{buildroot}%{_fillupdir}/

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service
%{fillup_only -n -d %{name} network}

%files
%attr(0644,root,root) %{systemdsvc}/%{servicefile}
%attr(0644,root,root) %{_fillupdir}/sysconfig.%{name}
%attr(0755,root,root) %{_bindir}/%{name}

%changelog
